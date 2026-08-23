from django.db import models
from django.utils.text import slugify

class Timestamped(models.Model):
    created_at=models.DateTimeField(auto_now_add=True); updated_at=models.DateTimeField(auto_now=True)
    class Meta: abstract=True
class Publishable(Timestamped):
    title=models.CharField(max_length=180); slug=models.SlugField(unique=True, blank=True); is_published=models.BooleanField(default=True); display_order=models.PositiveIntegerField(default=0)
    def save(self,*args,**kwargs):
        if not self.slug: self.slug=slugify(self.title)
        super().save(*args,**kwargs)
    class Meta: abstract=True
class SiteSettings(Timestamped):
    company_name=models.CharField(max_length=120, default='sidhivinayaksoftwork'); tagline=models.CharField(max_length=180, blank=True); email=models.EmailField(default='sidhivinayaksoftwork@gmail.com'); phone=models.CharField(max_length=40, default='9755550213'); meta_description=models.TextField(blank=True)
    def __str__(self): return self.company_name
class Service(Publishable):
    summary=models.TextField(); description=models.TextField(blank=True); icon=models.CharField(max_length=20, blank=True); benefits=models.JSONField(default=list, blank=True); technologies=models.JSONField(default=list, blank=True)
class Industry(Publishable): summary=models.TextField(); icon=models.CharField(max_length=20, blank=True)
class Technology(Publishable): category=models.CharField(max_length=40); description=models.TextField(blank=True); website_url=models.URLField(blank=True); logo=models.ImageField(upload_to='technologies/', blank=True)
class Project(Publishable):
    category=models.CharField(max_length=80); industry=models.ForeignKey(Industry,null=True,blank=True,on_delete=models.SET_NULL); summary=models.TextField(); client=models.CharField(max_length=120, blank=True); challenge=models.TextField(blank=True); solution=models.TextField(blank=True); results=models.TextField(blank=True); cover_image=models.ImageField(upload_to='projects/', blank=True); technologies=models.ManyToManyField(Technology, blank=True)
class ProjectImage(Timestamped): project=models.ForeignKey(Project,on_delete=models.CASCADE,related_name='images'); image=models.ImageField(upload_to='projects/gallery/'); alt_text=models.CharField(max_length=160, blank=True); display_order=models.PositiveIntegerField(default=0)
class CaseStudy(Publishable): project=models.OneToOneField(Project,null=True,blank=True,on_delete=models.SET_NULL); problem=models.TextField(); strategy=models.TextField(blank=True); implementation=models.TextField(blank=True); results=models.TextField(blank=True); metrics=models.JSONField(default=list, blank=True); hero_image=models.ImageField(upload_to='case-studies/', blank=True)
class Testimonial(Publishable): quote=models.TextField(); person_name=models.CharField(max_length=120); company=models.CharField(max_length=120, blank=True); designation=models.CharField(max_length=120, blank=True)
class TeamMember(Publishable): role=models.CharField(max_length=120); bio=models.TextField(blank=True); image=models.ImageField(upload_to='team/', blank=True); linkedin_url=models.URLField(blank=True)
class BlogCategory(Timestamped):
    name=models.CharField(max_length=80,unique=True)
    slug=models.SlugField(unique=True,blank=True)
    def save(self,*a,**k):
        self.slug=self.slug or slugify(self.name)
        super().save(*a,**k)
class BlogTag(Timestamped):
    name=models.CharField(max_length=60,unique=True)
    slug=models.SlugField(unique=True,blank=True)
    def save(self,*a,**k):
        self.slug=self.slug or slugify(self.name)
        super().save(*a,**k)
class BlogPost(Publishable): category=models.ForeignKey(BlogCategory,null=True,blank=True,on_delete=models.SET_NULL); tags=models.ManyToManyField(BlogTag,blank=True); excerpt=models.TextField(); body=models.TextField(); author=models.ForeignKey(TeamMember,null=True,blank=True,on_delete=models.SET_NULL); featured_image=models.ImageField(upload_to='blog/',blank=True); meta_description=models.TextField(blank=True); published_at=models.DateTimeField(null=True,blank=True)
class Job(Publishable): category=models.CharField(max_length=80); location=models.CharField(max_length=100); employment_type=models.CharField(max_length=80); experience=models.CharField(max_length=100); description=models.TextField(); skills=models.JSONField(default=list,blank=True)
class JobApplication(Timestamped): job=models.ForeignKey(Job,on_delete=models.PROTECT); candidate_name=models.CharField(max_length=120); email=models.EmailField(); phone=models.CharField(max_length=40,blank=True); resume=models.FileField(upload_to='applications/resumes/'); cover_letter=models.TextField(blank=True); portfolio_url=models.URLField(blank=True); linkedin_url=models.URLField(blank=True); status=models.CharField(max_length=30,default='new')
class ContactInquiry(Timestamped): name=models.CharField(max_length=120); email=models.EmailField(); phone=models.CharField(max_length=40,blank=True); company=models.CharField(max_length=120,blank=True); service=models.CharField(max_length=120,blank=True); budget=models.CharField(max_length=80,blank=True); message=models.TextField(); is_read=models.BooleanField(default=False)
