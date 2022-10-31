from rest_framework import serializers

from main.models import Announcement, District, Blog, Region


class AnnouncementSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Announcement.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.region = validated_data.get('region', instance.region)
        instance.district = validated_data.get('district', instance.district)
        instance.address = validated_data.get('address', instance.address)
        instance.remaining_information = validated_data.get('remaining_information', instance.remaining_information)
        instance.description = validated_data.get('description', instance.discription)
        instance.type = validated_data.get('type', instance.type)
        instance.view = validated_data.get('view', instance.view)
        instance.condition = validated_data.get('condition', instance.condition)
        instance.img1 = validated_data.get('img1', instance.img1)
        instance.img2 = validated_data.get('img2', instance.img2)
        instance.img3 = validated_data.get('img3', instance.img3)
        instance.img4 = validated_data.get('img4', instance.img4)
        instance.img5 = validated_data.get('img5', instance.img5)
        instance.price = validated_data.get('price', instance.price)
        instance.save()

        return instance

    class Meta:
        model = Announcement
        fields = '__all__'


class DistrictSerializers(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'


class RegionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class BlogSerializers(serializers.ModelSerializer):

    def create(self, validated_data):
        return Blog.objects.create(**validated_data)

    class Meta:
        model = Blog
        fields = '__all__'