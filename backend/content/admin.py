from django.contrib import admin
from .models import *
admin.site.site_header='sidhivinayaksoftwork CMS'; admin.site.site_title='sidhivinayaksoftwork Admin'; admin.site.index_title='Content studio'
@admin.register(Service,Industry,Technology,Project,CaseStudy,Testimonial,TeamMember,BlogPost,Job)
class ContentAdmin(admin.ModelAdmin):
    list_display=('title','is_published','display_order','updated_at'); list_filter=('is_published',); search_fields=('title',); prepopulated_fields={'slug':('title',)}; ordering=('display_order','-updated_at')
@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin): list_display=('project','alt_text','display_order'); search_fields=('project__title','alt_text')
@admin.register(BlogCategory,BlogTag)
class TaxonomyAdmin(admin.ModelAdmin): list_display=('name','slug'); search_fields=('name',); prepopulated_fields={'slug':('name',)}
@admin.register(JobApplication)
class ApplicationAdmin(admin.ModelAdmin): list_display=('candidate_name','job','email','status','created_at'); list_filter=('status',); search_fields=('candidate_name','email'); readonly_fields=('created_at','updated_at')
@admin.register(ContactInquiry)
class ContactAdmin(admin.ModelAdmin): list_display=('name','email','service','is_read','created_at'); list_filter=('is_read','service'); search_fields=('name','email','company'); readonly_fields=('created_at','updated_at')
@admin.register(SiteSettings)
class SettingsAdmin(admin.ModelAdmin): list_display=('company_name','email','updated_at')

