from rest_framework.routers import DefaultRouter
from .views import *
router=DefaultRouter()
for prefix, view in [('services',ServiceViewSet),('industries',IndustryViewSet),('technologies',TechnologyViewSet),('projects',ProjectViewSet),('case-studies',CaseStudyViewSet),('testimonials',TestimonialViewSet),('team',TeamViewSet),('blog',BlogViewSet),('careers',CareerViewSet),('applications',ApplicationViewSet),('contact',ContactViewSet),('site-settings',SiteSettingsViewSet)]: router.register(prefix,view)
urlpatterns=router.urls

