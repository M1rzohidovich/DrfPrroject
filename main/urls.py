from django.urls import path

from main.views import AnnouncementListAPIView,DeleteAnnouncement, AnnouncementCreateAPIView,\
 AnnouncementUpdateDeleteAPIView, GetDistricts, GetRegions, GetBlog, BlogCreate, BlogUpdateDelete


urlpatterns = [
    path('announcement-list', AnnouncementListAPIView.as_view(), name='announcement_list'),
    path('announcement', AnnouncementCreateAPIView.as_view(), name='announcement'),
    path('announcement-upd/<int:pk>', AnnouncementUpdateDeleteAPIView.as_view(), name='announcement_update_delete'),
    path('get-districts', GetDistricts.as_view(), name='get-districts'),
    path('get-regions', GetRegions.as_view(), name='get-regions'),
    path('blogs', GetBlog.as_view(), name='blogs'),
    path('blog-create', BlogCreate.as_view(), name='blog-create'),
    path('blog-upd/<int:pk>', BlogUpdateDelete.as_view(), name='blog_update_delete'),
    path('delete-announcement/<int:pk>', DeleteAnnouncement.as_view(), name='delete_announcement')
    
    

]