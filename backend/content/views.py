from rest_framework import viewsets, filters
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .models import *
from .serializers import *
class PublicViewSet(viewsets.ModelViewSet):
    http_method_names=['get','post','head','options']; filter_backends=[filters.SearchFilter,filters.OrderingFilter]; ordering='display_order'
    def get_queryset(self): return self.queryset.filter(is_published=True)
class ServiceViewSet(PublicViewSet): queryset=Service.objects.all(); serializer_class=ServiceSerializer; search_fields=['title','summary']
class IndustryViewSet(PublicViewSet): queryset=Industry.objects.all(); serializer_class=IndustrySerializer
class TechnologyViewSet(PublicViewSet): queryset=Technology.objects.all(); serializer_class=TechnologySerializer; search_fields=['title','category']
class ProjectViewSet(PublicViewSet): queryset=Project.objects.prefetch_related('technologies'); serializer_class=ProjectSerializer; search_fields=['title','category','summary']
class CaseStudyViewSet(PublicViewSet): queryset=CaseStudy.objects.all(); serializer_class=CaseStudySerializer
class TestimonialViewSet(PublicViewSet): queryset=Testimonial.objects.all(); serializer_class=TestimonialSerializer
class TeamViewSet(PublicViewSet): queryset=TeamMember.objects.all(); serializer_class=TeamSerializer
class BlogViewSet(PublicViewSet): queryset=BlogPost.objects.all(); serializer_class=BlogSerializer; search_fields=['title','excerpt','body']
class CareerViewSet(PublicViewSet): queryset=Job.objects.all(); serializer_class=JobSerializer; search_fields=['title','category','location']
class ApplicationViewSet(viewsets.ModelViewSet): queryset=JobApplication.objects.all(); serializer_class=ApplicationSerializer; parser_classes=[MultiPartParser,FormParser,JSONParser]; http_method_names=['post','options']
class ContactViewSet(viewsets.ModelViewSet): queryset=ContactInquiry.objects.all(); serializer_class=ContactSerializer; http_method_names=['post','options']
class SiteSettingsViewSet(viewsets.ReadOnlyModelViewSet): queryset=SiteSettings.objects.all(); serializer_class=SiteSettingsSerializer

