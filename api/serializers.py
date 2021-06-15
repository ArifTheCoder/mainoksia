from .models import Company, Week, Image
from rest_framework import serializers


class CompanySerializer(serializers.ModelSerializer):

    logo_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Company
        fields = ('pk',
                  'name',
                  'webshop_link',
                  'logo_url',)

    def get_image_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.logo.url)


class ImageSerializer(serializers.ModelSerializer):

    image_url = serializers.SerializerMethodField('get_image_url')
    week_number = serializers.IntegerField(source='week.week_number')
    company_id = serializers.CharField(source='week.company.pk')

    class Meta:
        model = Image
        fields = (
                  'company_id',
                  'image_url',
                  'week_number',
                  'parent_link',
                  'is_default',)

    def get_image_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image.url)
