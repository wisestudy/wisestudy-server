from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from ...study_member.serializers.study_member_sz import StudyMemberSerializer
from ...study_member.serializers.study_member_delete_sz import StudyMemberDeleteSerializer
from ...study_member.models import StudyMember

from ...study.models import Study

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from lib.user_data import jwt_get_payload


##-- 스터디맴버 디테일--
class Study_StudyMemberDetail(APIView):
    @swagger_auto_schema(
        responses={200: StudyMemberSerializer()},
        tags=['StudyMember'],
        operation_description=
        """
        특정 id를 가진 회원 조회 API
        ---
        """,
    )
    def get(self, request, *args, **kwargs):
        study_member = get_object_or_404(StudyMember, study_member_id=self.kwargs['study_members_id'],
                                         study=self.kwargs['studies_id'])
        serializer = StudyMemberSerializer(study_member)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        responses={200: StudyMemberSerializer()},
        tags=['StudyMember'],
        operation_description=
        """
        특정 id를 가진 회원 수정 API
        ---
            수정 가능한 필드 :
                - is_manager : 운영진인지 아닌지 구분

        """,
    )
    def put(self, request, *args, **kwargs):
        study_member = get_object_or_404(StudyMember, study_member_id=self.kwargs['study_members_id'],
                                         study=self.kwargs['studies_id'])

        serializer = StudyMemberSerializer(study_member, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    @swagger_auto_schema(
        responses={200: StudyMemberDeleteSerializer()},
        tags=['StudyMember'],
        operation_description=
        """
        특정 id를 가진 회원 삭제 API - 관리자가 아니면 삭제 불가능
        ---
            Header : x-jwt-token
        """,
    )
    def delete(self, request, *args, **kwargs):
        user_payload = jwt_get_payload(request)

        if self.user_is_manager(user_id=user_payload['user_id'], studies_id=self.kwargs['studies_id']):
            study_member = get_object_or_404(StudyMember, study_member_id=self.kwargs['study_members_id'],
                                             study=self.kwargs['studies_id'])
            serializer = StudyMemberDeleteSerializer(study_member)
            study_member.delete()

            study = get_object_or_404(Study, pk=self.kwargs['studies_id'])
            study.study_members_count -= 1
            study.save()

            return Response(data=serializer.data)
        else:
            return Response(data=['관리자가 아닙니다'])

    def user_is_manager(self, studies_id, user_id):
        is_manager = get_object_or_404(StudyMember, study=studies_id, user=user_id)
        if hasattr(is_manager, 'is_manager') is not None and getattr(is_manager, 'is_manager') is True:
            return True
        else:
            return False