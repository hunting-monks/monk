from rest_framework import serializers
from company.models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'name',
            'businessDescription',
            'area',
            'email',
            'phone',
            'address',
            'address2',
            'zipcode',
            'city',
            'province',
            'state')
