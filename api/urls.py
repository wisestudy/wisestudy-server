from django.urls import path, include
from .category import views as category_views  # 카테고리
from .user import views as user_views  # 유저
from .study import views as study_views  # 스터디
from .study_member import views as study_member_views  # 스터디원
from .activity_picture import views as activity_picture_views  # 활동사진
from .schedule import views as schedule_views  # 일정

urlpatterns = [
    path('users', user_views.UserList.as_view()),
    path('users/<int:pk>', user_views.UserDetail.as_view()),
    path('categorys', category_views.CategoryList.as_view()),
    path('categorys/<int:pk>', category_views.CategoryDetail.as_view()),
    path('studys/', study_views.StudyList.as_view()),
    path('studys/<int:pk>', study_views.StudyDetail.as_view()),
    path('study_members/', study_member_views.StudyMemberList.as_view()),
    path('schedules/', schedule_views.ScheduleList.as_view()),
    path('schedules/<int:pk>', schedule_views.ScheduleDetail.as_view()),
    path('aps/', activity_picture_views.APList.as_view()),
    path('aps/<int:pk>', activity_picture_views.APDetail.as_view()),
]