from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from ...user.models import User
from ...study.models import Study
from ..models import StudyMember

from rest_framework.response import Response
from rest_framework.views import APIView

from django.core.cache import cache

from lib.user_data import jwt_get_payload

import json

class StudyMemberConfirm(APIView):
    @swagger_auto_schema(
        tags=['studies'],
        operation_description=
        """
        스터디 가입 신청 넣은 인원 승인 api
        ---
            request_body
                - user_id : 스터디 가입 신청한 유저 id
        """,
    )
    ## study 가입 신청 멤버 승인
    def post(self, request, *args, **kwargs):
        print("안들어오누")
        user_payload = jwt_get_payload(request)
        study_id = self.kwargs['studies_id']

        if self.user_is_manager(user_id=user_payload['user_id'], studies_id=study_id):
            str_study_id = self.str_study_id(study_id)

            user_id = str(request.POST.get('user_id'))
            user_id = request.data.get('user_id')
            print(f'------------------{user_id} ------------------')
            self.apply_member_delete_redis(str_study_id, user_id)

            if len(StudyMember.objects.filter(study_id=study_id, user_id=user_id)) > 0:
                return Response(data=["이미 들어있다"])

            user = get_object_or_404(User, pk=user_id)
            print(f"+++++++ {user} +++++++")
            study = get_object_or_404(Study, pk=study_id)
            study.study_members_count += 1
            study.save()

            new_study_member = StudyMember(study=study, user=user, is_manager=False)
            new_study_member.save()

            return Response(data=[])
        else:
            return Response(data=['관리자가 아닙니다'])

    @swagger_auto_schema(
        tags=['studies'],
        operation_description=
        """
        스터디 가입 신청 인원 거절 
        ---
            request_body
                - user_id : 스터디 가입 신청한 유저 id
        """,
    )
    ## study 가입 신청 멤버 반려
    def delete(self, request, *args, **kwargs):
        print("delete 들어온다")
        user_payload = jwt_get_payload(request)
        study_id = self.kwargs['studies_id']

        if self.user_is_manager(user_id=user_payload['user_id'], studies_id=study_id):
            str_study_id = self.str_study_id(study_id)

            user_id = request.POST.get('user_id')
            print(user_id)
            # study_apply_dict = self.apply_member_delete_redis(str_study_id, user_id)
            # return Response(data=study_apply_dict)
            self.apply_member_delete_redis(str_study_id, user_id)
            return Response(data=[])

        else:
            return Response(data=['관리자가 아닙니다'])

    ## 가입 승인 또는 반려 된 인원 redis에서 제거
    def apply_member_delete_redis(self, study_id, user_id):
        study_apply_lists = cache.get(study_id)
        delete_index = 0
        for i, study_apply_list in enumerate(study_apply_lists):
            if hasattr(study_apply_list, 'user_id') is not None and study_apply_list['user_id'] == user_id:
                delete_index = i
                break

        if len(study_apply_lists) > 0:
            study_apply_lists.pop(delete_index)
            cache.set(study_id, study_apply_lists)

        return study_apply_lists

    def str_study_id(self, study_id):
        return 'study:' + str(study_id)

    def user_is_manager(self, studies_id, user_id):
        print(user_id)
        is_manager = get_object_or_404(StudyMember, study=studies_id, user=user_id)
        print(is_manager)
        if hasattr(is_manager, 'is_manager') is not None and getattr(is_manager, 'is_manager') is True:
            print("매니저 ok")
            return True
        else:
            print("매너지 X")
            return False
