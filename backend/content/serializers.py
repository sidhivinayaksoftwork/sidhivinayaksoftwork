from rest_framework import serializers
from .models import *
class SimpleSerializer(serializers.ModelSerializer):
    class Meta: model=Service; fields='__all__'
class ServiceSerializer(SimpleSerializer):
    class Meta: model=Service; fields='__all__'
class IndustrySerializer(serializers.ModelSerializer):
    class Meta: model=Industry; fields='__all__'
class TechnologySerializer(serializers.ModelSerializer):
    class Meta: model=Technology; fields='__all__'
class ProjectSerializer(serializers.ModelSerializer):
    technology_names=serializers.SerializerMethodField()
    class Meta: model=Project; fields='__all__'; extra_kwargs={'technologies':{'required':False}}
    def get_technology_names(self,obj): return list(obj.technologies.values_list('title',flat=True))
class CaseStudySerializer(serializers.ModelSerializer):
    class Meta: model=CaseStudy; fields='__all__'
class TestimonialSerializer(serializers.ModelSerializer):
    class Meta: model=Testimonial; fields='__all__'
class TeamSerializer(serializers.ModelSerializer):
    class Meta: model=TeamMember; fields='__all__'
class BlogSerializer(serializers.ModelSerializer):
    class Meta: model=BlogPost; fields='__all__'
class JobSerializer(serializers.ModelSerializer):
    class Meta: model=Job; fields='__all__'
class ApplicationSerializer(serializers.ModelSerializer):
    class Meta: model=JobApplication; fields='__all__'; read_only_fields=['status']
    def validate_resume(self,value):
        if value.size > 5*1024*1024: raise serializers.ValidationError('Resume must be 5MB or smaller.')
        if not value.name.lower().endswith(('.pdf','.doc','.docx')): raise serializers.ValidationError('Upload a PDF or Word document.')
        return value
class ContactSerializer(serializers.ModelSerializer):
    class Meta: model=ContactInquiry; fields=['name','email','phone','company','service','budget','message']
class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta: model=SiteSettings; fields='__all__'

