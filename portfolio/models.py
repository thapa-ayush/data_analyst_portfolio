from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from datetime import datetime, timedelta


class About(models.Model):
    """Model for portfolio owner's about section"""
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    bio = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=200, blank=True)
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    
    # Hero Section Customization Fields
    hero_heading = models.CharField(
        max_length=300,
        default='Transforming Data Into Strategic Insights',
        help_text='Main heading text for hero section'
    )
    hero_tagline = models.CharField(
        max_length=200,
        blank=True,
        help_text='Short tagline above the main heading'
    )
    hero_description = models.TextField(
        blank=True,
        help_text='Full description text in hero section (appears with profile picture)'
    )
    hero_cta_primary = models.CharField(
        max_length=100,
        default='View My Work',
        help_text='Primary call-to-action button text'
    )
    hero_cta_secondary = models.CharField(
        max_length=100,
        default='Get In Touch',
        help_text='Secondary call-to-action button text'
    )
    show_profile_picture = models.BooleanField(
        default=True,
        help_text='Display profile picture in hero section'
    )
    
    # Footer Customization Fields
    footer_tagline = models.CharField(
        max_length=200,
        blank=True,
        default='Turning data into insights',
        help_text='Footer tagline or motto'
    )
    footer_show_social_links = models.BooleanField(
        default=True,
        help_text='Display social media links in footer'
    )
    footer_show_resume_link = models.BooleanField(
        default=True,
        help_text='Display resume download link in footer'
    )
    footer_copyright_text = models.CharField(
        max_length=300,
        blank=True,
        help_text='Custom copyright text (leave blank for auto-generated)'
    )
    
    # Homepage Stats Customization Fields
    stat_projects = models.IntegerField(
        default=None,
        null=True,
        blank=True,
        help_text='Custom count for projects stat (leave blank to auto-count from database)'
    )
    stat_skills = models.IntegerField(
        default=None,
        null=True,
        blank=True,
        help_text='Custom count for skills stat (leave blank to auto-count from database)'
    )
    stat_certifications = models.IntegerField(
        default=None,
        null=True,
        blank=True,
        help_text='Custom count for certifications stat (leave blank to auto-count from database)'
    )
    stat_experience = models.IntegerField(
        default=None,
        null=True,
        blank=True,
        help_text='Custom count for years of experience (leave blank to auto-count from database)'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "About Section"
        verbose_name_plural = "About Section"

    def __str__(self):
        return self.name


class Skill(models.Model):
    """Model for professional skills"""
    CATEGORY_CHOICES = [
        ('technical', 'Technical'),
        ('tools', 'Tools & Software'),
        ('analytics', 'Analytics'),
        ('soft', 'Soft Skills'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='technical'
    )
    proficiency = models.IntegerField(
        default=50,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Proficiency level (0-100)"
    )
    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Icon class or emoji"
    )
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Project(models.Model):
    """Model for portfolio projects"""
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('in_progress', 'In Progress'),
        ('archived', 'Archived'),
    ]
    
    CATEGORY_CHOICES = [
        ('data_analysis', 'Data Analysis'),
        ('dashboard', 'Dashboard'),
        ('data_visualization', 'Data Visualization'),
        ('machine_learning', 'Machine Learning'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    detailed_description = models.TextField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    technologies = models.CharField(
        max_length=500,
        help_text="Comma-separated technologies"
    )
    project_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='completed'
    )
    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
        default='data_analysis'
    )
    key_achievements = models.TextField(
        blank=True,
        help_text="Bullet points separated by newlines"
    )
    order = models.IntegerField(default=0)
    date_completed = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-featured', 'order', '-date_completed']

    def __str__(self):
        return self.title

    def get_technologies_list(self):
        """Returns a list of technologies by splitting comma-separated string"""
        return [tech.strip() for tech in self.technologies.split(',')]
    
    def get_achievements_list(self):
        """Returns a list of achievements by splitting by newlines"""
        return [achievement.strip() for achievement in self.key_achievements.split('\n') if achievement.strip()]


class Certificate(models.Model):
    """Model for professional certifications"""
    certificate_name = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200)
    issue_date = models.DateField()
    expiry_date = models.DateField(blank=True, null=True)
    credential_id = models.CharField(max_length=200, blank=True)
    credential_url = models.URLField(blank=True)
    certificate_image = models.ImageField(upload_to='certificates/', blank=True, null=True)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-issue_date']

    def __str__(self):
        return f"{self.certificate_name} - {self.issuing_organization}"
    
    @property
    def is_expired(self):
        """Check if certificate has expired"""
        if self.expiry_date is None:
            return False
        return self.expiry_date < datetime.now().date()
    
    @property
    def days_until_expiry(self):
        """Calculate days until expiry"""
        if self.expiry_date is None:
            return None
        days = (self.expiry_date - datetime.now().date()).days
        return max(0, days)


class Experience(models.Model):
    """Model for work experience"""
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    current = models.BooleanField(default=False)
    description = models.TextField()
    achievements = models.TextField(
        blank=True,
        help_text="Bullet points separated by newlines"
    )
    company_logo = models.ImageField(upload_to='companies/', blank=True, null=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-start_date']
        verbose_name_plural = "Experiences"

    def __str__(self):
        return f"{self.position} at {self.company}"

    def get_achievements_list(self):
        """Returns a list of achievements by splitting by newlines"""
        return [achievement.strip() for achievement in self.achievements.split('\n') if achievement.strip()]


class Education(models.Model):
    """Model for education background"""
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    current = models.BooleanField(default=False)
    grade = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    institution_logo = models.ImageField(upload_to='institutions/', blank=True, null=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-start_date']
        verbose_name_plural = "Education"

    def __str__(self):
        return f"{self.degree} - {self.institution}"


class ContactMessage(models.Model):
    """Model for contact form messages"""
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=300)
    message = models.TextField()
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
