from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.permissons import DirectorPermission
from .models import Announcement, District, Region, Blog
from .serializers import AnnouncementSerializer, DistrictSerializers, RegionSerializers, BlogSerializers


class AnnouncementListAPIView(APIView):
    authentication_classes = []
    
    def get(self, request):
        try:
            ann = Announcement.objectts.all()
            announcement_list = AnnouncementSerializer(ann, many=True).data
        except:
            announcement_list = None
        return Response(announcement_list)


class AnnouncementCreateAPIView(APIView):
    authentication_classes = (JWTAuthentication,)

    def get(self, request):
        try:
            ann = Announcement.objects.filter(owner=request.user)
            announcement_list = AnnouncementSerializer(ann, many=True).data
        except:
            announcement_list = None
        return Response(announcement_list)

    def post(self, request):
        try:
            request.data['owner'] = request.user.id
            ann = AnnouncementSerializer(data=request.data)
            ann.is_valid(raise_exception=True)
            ann.save()
            data = ann.data
        except Exception as e:
            data = {
                'error': f'{e}'
            }
        return Response(data)


class AnnouncementUpdateDeleteAPIView(APIView):
    authentication_classes = (JWTAuthentication,)

    def put(self, request, pk): 
        try:
            announcement = Announcement.objects.get(pk=pk)
            ann = AnnouncementSerializer(data=request.data, instance=announcement)
            ann.is_valid(raise_exception=True)
            ann.save()
            data = ann.data
        except Exception as e:
            data = {
                'error': f'{e}'
            }
            return Response(data)

        
class GetDistricts(APIView):

    def get(self, request):
        region_id = request.GET['region_id']
        districts = District.objects.filter(region_id=region_id)
        serializer = DistrictSerializers(districts, many=True)

        return Response(serializer.data) 


class GetRegions(APIView):

    def get(self, request):
        regions = Region.objects.all()
        serializer = RegionSerializers(regions, many=True)

        return Response(serializer.data)


class GetBlog(APIView):
     
     def get(self, request):
        blog = Blog.objects.all()
        serializer = BlogSerializers(blog, many=True)

        return Response(serializer.data)

    
class BlogCreate(APIView):
    permission_classes = (DirectorPermission,)

    def post(self, request):
        blog = BlogSerializers(data=request.data)
        blog.is_valid(raise_exception=True)
        blog.save()

        return Response(blog.data)


class BlogUpdateDelete(APIView):
    permission_classes = (DirectorPermission,)

    def put(self, request, pk):
        blog = Blog.objects.get(pk=pk)
        if "title" in request.data.keys():
            blog.title=request.data['title']
        if "description" in request.data.keys():
            blog.description=request.data['description']
        if "img" in request.data.keys():
            blog.img=request.data['img']
        if "expiration_date" in request.data.keys():
            blog.expiration_date=request.data['expiration_date']

        serializer = BlogSerializers(blog)
        return Response(serializer.data)

    def delete(self, request, pk):
        blog = Blog.objects.get(pk=pk)
        blog.delete()
        return Response(stat=204)


class DeleteAnnouncement(APIView):
    authentication_classes = (JWTAuthentication,)

    def delete(self, request, pk):
      delete_announcement = Announcement.objects.get(Q(pk=pk), Q(owner=request.user))
      delete_announcement.delete()

      return Response(status=204)        


