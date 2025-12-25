from django.contrib import admin
from django.utils.html import format_html
from django.db import models
from datetime import date
from .models import About, Skill, Project, Certificate, Experience, Education, ContactMessage


class CustomModelForm(admin.ModelAdmin):
    """Custom model admin with textarea for rich editing"""
    formfield_overrides = {
        models.TextField: {'widget': admin.widgets.AdminTextareaWidget(
            attrs={
                'rows': 10,
                'style': 'font-family: monospace; width: 100%;'
            }
        )},
    }


# ==================== ABOUT ADMIN ====================
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    """Admin for About section - clean and simple interface"""
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'title', 'location', 'email', 'phone'),
        }),
        ('Biography', {
            'fields': ('bio',),
        }),
        ('Media', {
            'fields': ('profile_image', 'resume'),
        }),
        ('Social Media', {
            'fields': ('linkedin_url', 'github_url', 'twitter_url'),
        }),
        ('Hero Section Customization', {
            'fields': (
                'hero_tagline',
                'hero_heading',
                'hero_description',
                'hero_cta_primary',
                'hero_cta_secondary',
                'show_profile_picture',
                'availability_status',
                'availability_text',
            ),
        }),
        ('Homepage Stats Customization', {
            'fields': (
                'stat_projects',
                'stat_skills',
                'stat_certifications',
                'stat_experience',
            ),
            'description': 'Customize the numbers displayed on homepage. Leave blank to auto-count from database.'
        }),
        ('Footer Customization', {
            'fields': (
                'footer_tagline',
                'footer_show_social_links',
                'footer_show_resume_link',
                'footer_copyright_text',
            ),
        }),
        ('System', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    
    readonly_fields = ('created_at', 'updated_at')
    
    def has_add_permission(self, request):
        """Prevent adding new About entries"""
        return not About.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        """Prevent deleting the About entry"""
        return False
    
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        """Redirect to the first (only) About entry"""
        if object_id is None and About.objects.exists():
            return super().changeform_view(
                request, 
                About.objects.first().id, 
                form_url=form_url, 
                extra_context=extra_context
            )
        return super().changeform_view(request, object_id, form_url, extra_context)


# ==================== SKILL ADMIN ====================
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """Enhanced admin for Skills with proficiency visualization"""
    
    list_display = ('name', 'category_colored', 'proficiency_bar', 'proficiency', 'icon_preview', 'order')
    list_editable = ('order',)
    list_filter = ('category', 'proficiency')
    search_fields = ('name', 'icon')
    ordering = ('order', 'name')
    
    fieldsets = (
        ('Skill Information', {
            'fields': ('name', 'category'),
            'description': 'Name and category of the skill'
        }),
        ('Icon Settings', {
            'fields': ('icon', 'custom_svg'),
            'description': 'Select a predefined icon from the dropdown, or choose "Custom SVG" and paste your SVG code below'
        }),
        ('Proficiency', {
            'fields': ('proficiency',),
            'description': 'Skill level from 0 (beginner) to 100 (expert)'
        }),
        ('Display Settings', {
            'fields': ('order',),
            'description': 'Lower numbers appear first'
        }),
    )
    
    actions = ['delete_selected']
    
    class Media:
        css = {
            'all': []
        }
        js = []
    
    def has_delete_permission(self, request, obj=None):
        """Allow deleting skills"""
        return True
    
    def category_colored(self, obj):
        """Display category with color coding"""
        colors = {
            'technical': '#0A84FF',
            'tools': '#00D9FF',
            'analytics': '#FF6B35',
            'soft': '#7C3AED',
        }
        color = colors.get(obj.category, '#E8ECF4')
        return format_html(
            '<span style="background-color: {}; color: white; padding: 3px 8px; '
            'border-radius: 4px; font-weight: bold;">{}</span>',
            color,
            obj.get_category_display()
        )
    category_colored.short_description = 'Category'
    
    def proficiency_bar(self, obj):
        """Display proficiency as visual bar"""
        bar_width = obj.proficiency
        bar_color = '#0A84FF' if obj.proficiency >= 70 else '#FF6B35'
        return format_html(
            '<div style="width: 150px; background: #333; border-radius: 4px; overflow: hidden;">'
            '<div style="width: {}px; background: {}; height: 20px; '
            'display: flex; align-items: center; justify-content: center; color: white; font-size: 12px;">'
            '{}%</div></div>',
            bar_width * 1.5,
            bar_color,
            obj.proficiency
        )
    proficiency_bar.short_description = 'Proficiency'
    
    def icon_preview(self, obj):
        """Display icon preview"""
        svg = obj.get_icon_svg()
        if svg:
            return format_html(
                '<div style="width: 24px; height: 24px; color: #0A84FF;">{}</div>',
                svg
            )
        return '-'
    icon_preview.short_description = 'Icon'


# ==================== PROJECT ADMIN ====================
@admin.register(Project)
class ProjectAdmin(CustomModelForm):
    """Enhanced admin for Projects with featured status and tech tags"""
    
    list_display = ('title', 'featured_badge', 'tech_preview', 'date_completed', 'order', 'has_links')
    list_editable = ('order',)
    list_filter = ('featured', 'status', 'category', 'date_completed')
    search_fields = ('title', 'description', 'technologies')
    date_hierarchy = 'date_completed'
    
    fieldsets = (
        ('Project Overview', {
            'fields': ('title', 'description', 'category', 'status', 'date_completed'),
        }),
        ('Project Image', {
            'fields': ('image',),
            'description': 'Upload an image for your project'
        }),
        ('Detailed Information', {
            'fields': ('detailed_description',),
            'classes': ('collapse',),
            'description': 'Full project description. You can use HTML tags for formatting:<br><strong>Examples:</strong><br>&lt;p&gt;Paragraph&lt;/p&gt;<br>&lt;strong&gt;Bold Text&lt;/strong&gt;<br>&lt;em&gt;Italic Text&lt;/em&gt;<br>&lt;h3&gt;Subheading&lt;/h3&gt;<br>&lt;ul&gt;&lt;li&gt;List item&lt;/li&gt;&lt;/ul&gt;<br>&lt;img src="URL" alt="description" style="max-width:100%;"&gt;'
        }),
        ('Technologies & Achievements', {
            'fields': ('technologies', 'key_achievements'),
            'description': 'Technologies: comma-separated list (Python, Pandas, SQL, Tableau). Achievements: separate each with new line'
        }),
        ('Project Links', {
            'fields': ('project_url', 'github_url'),
        }),
        ('Display Settings', {
            'fields': ('featured', 'order'),
            'description': 'Featured projects appear on homepage'
        }),
    )
    
    actions = ['mark_featured', 'unmark_featured', 'duplicate_project', 'delete_selected']
    
    def has_delete_permission(self, request, obj=None):
        """Allow deleting projects"""
        return True
    
    def featured_badge(self, obj):
        """Display featured status with star"""
        if obj.featured:
            return format_html('⭐ Featured')
        return '—'
    featured_badge.short_description = 'Status'
    
    def tech_preview(self, obj):
        """Show first 3 technologies"""
        techs = obj.get_technologies_list()[:3]
        badges = ' '.join([
            format_html('<span style="background: #0A84FF; color: white; '
                       'padding: 2px 6px; border-radius: 3px; margin-right: 4px; '
                       'font-size: 11px;">{}</span>', tech)
            for tech in techs
        ])
        return format_html(badges)
    tech_preview.short_description = 'Technologies'
    
    def has_links(self, obj):
        """Show if project has links"""
        icons = ''
        if obj.project_url:
            icons += '🔗 '
        if obj.github_url:
            icons += '💻'
        return format_html(icons if icons else '—')
    has_links.short_description = 'Links'
    
    def mark_featured(self, request, queryset):
        count = queryset.update(featured=True)
        self.message_user(request, f'{count} project(s) marked as featured.')
    mark_featured.short_description = 'Mark selected as featured'
    
    def unmark_featured(self, request, queryset):
        count = queryset.update(featured=False)
        self.message_user(request, f'{count} project(s) unmarked as featured.')
    unmark_featured.short_description = 'Unmark selected as featured'
    
    def duplicate_project(self, request, queryset):
        for project in queryset:
            project.pk = None
            project.title = f"{project.title} (Copy)"
            project.save()
        self.message_user(request, f'{queryset.count()} project(s) duplicated.')
    duplicate_project.short_description = 'Duplicate selected projects'


# ==================== CERTIFICATE ADMIN ====================
@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    """Enhanced admin for Certificates with expiry status"""
    
    list_display = ('certificate_name', 'issuing_organization', 'issue_date', 'expiry_status', 'order', 'credential_link')
    list_editable = ('order',)
    list_filter = ('issuing_organization', 'issue_date', 'expiry_date')
    search_fields = ('certificate_name', 'issuing_organization', 'credential_id')
    
    fieldsets = (
        ('Certificate Details', {
            'fields': ('certificate_name', 'issuing_organization', 'certificate_image'),
        }),
        ('Dates', {
            'fields': ('issue_date', 'expiry_date'),
            'description': 'Leave expiry date blank for certifications that don\'t expire'
        }),
        ('Credentials', {
            'fields': ('credential_id', 'credential_url'),
            'description': 'ID and URL for credential verification'
        }),
        ('Additional Info', {
            'fields': ('description',),
            'classes': ('collapse',),
        }),
        ('Display Settings', {
            'fields': ('order',),
        }),
    )
    
    actions = ['duplicate_certificate', 'delete_selected']
    
    def has_delete_permission(self, request, obj=None):
        """Allow deleting certificates"""
        return True
    
    def expiry_status(self, obj):
        """Show if certificate is expired"""
        if obj.expiry_date is None:
            return format_html('∞ No expiry')
        elif obj.expiry_date < date.today():
            return format_html('<span style="color: #FF6B35; font-weight: bold;">🚫 Expired</span>')
        else:
            days_left = (obj.expiry_date - date.today()).days
            if days_left < 90:
                return format_html('<span style="color: #FFB84D;">⏰ {} days left</span>', days_left)
            return format_html('✓ Valid')
    expiry_status.short_description = 'Status'
    
    def credential_link(self, obj):
        """Show if credential URL exists"""
        if obj.credential_url:
            return format_html('<a href="{}" target="_blank">🔗 Verify</a>', obj.credential_url)
        return '—'
    credential_link.short_description = 'Verification'
    
    def duplicate_certificate(self, request, queryset):
        for cert in queryset:
            cert.pk = None
            cert.certificate_name = f"{cert.certificate_name} (Copy)"
            cert.save()
        self.message_user(request, f'{queryset.count()} certificate(s) duplicated.')
    duplicate_certificate.short_description = 'Duplicate selected certificates'


# ==================== EXPERIENCE ADMIN ====================
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    """Enhanced admin for Work Experience with timeline"""
    
    list_display = ('position', 'company', 'location', 'date_range', 'current_badge', 'order')
    list_editable = ('order',)
    list_filter = ('current', 'company', 'start_date')
    search_fields = ('position', 'company', 'description', 'achievements')
    
    fieldsets = (
        ('Position Details', {
            'fields': ('position', 'company', 'location', 'company_logo'),
        }),
        ('Employment Duration', {
            'fields': ('start_date', 'end_date', 'current'),
            'description': 'If currently employed, leave end_date blank and check "Current"'
        }),
        ('Description & Achievements', {
            'fields': ('description', 'achievements'),
            'description': 'Achievements: separate each point with a new line'
        }),
        ('Display Settings', {
            'fields': ('order',),
        }),
    )
    
    actions = ['mark_current', 'mark_past', 'delete_selected']
    
    def has_delete_permission(self, request, obj=None):
        """Allow deleting experiences"""
        return True
    
    def date_range(self, obj):
        """Display date range in human-readable format"""
        start = obj.start_date.strftime('%b %Y')
        if obj.current:
            end = 'Present'
        else:
            end = obj.end_date.strftime('%b %Y') if obj.end_date else '?'
        return f'{start} - {end}'
    date_range.short_description = 'Duration'
    
    def current_badge(self, obj):
        """Show if currently employed"""
        if obj.current:
            return format_html('<span style="background: #0A84FF; color: white; '
                              'padding: 3px 8px; border-radius: 4px; font-weight: bold;">Current</span>')
        return '—'
    current_badge.short_description = 'Status'
    
    def mark_current(self, request, queryset):
        queryset.update(current=True, end_date=None)
        self.message_user(request, f'{queryset.count()} experience(s) marked as current.')
    mark_current.short_description = 'Mark as currently employed'
    
    def mark_past(self, request, queryset):
        queryset.update(current=False)
        self.message_user(request, f'{queryset.count()} experience(s) marked as past.')
    mark_past.short_description = 'Mark as past employment'


# ==================== EDUCATION ADMIN ====================
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    """Enhanced admin for Education with degree info"""
    
    list_display = ('degree', 'institution', 'field_of_study', 'date_range', 'current_badge', 'grade_display', 'order')
    list_editable = ('order',)
    list_filter = ('current', 'institution', 'start_date', 'degree')
    search_fields = ('degree', 'institution', 'field_of_study')
    
    fieldsets = (
        ('Education Details', {
            'fields': ('institution', 'degree', 'field_of_study', 'institution_logo'),
        }),
        ('Study Duration', {
            'fields': ('start_date', 'end_date', 'current'),
            'description': 'If currently studying, leave end_date blank and check "Current"'
        }),
        ('Academic Info', {
            'fields': ('grade', 'description'),
            'description': 'Grade (GPA, honors, etc.) and additional notes'
        }),
        ('Display Settings', {
            'fields': ('order',),
        }),
    )
    
    actions = ['mark_current', 'mark_completed', 'delete_selected']
    
    def has_delete_permission(self, request, obj=None):
        """Allow deleting education entries"""
        return True
    
    def date_range(self, obj):
        """Display date range in human-readable format"""
        start = obj.start_date.strftime('%b %Y')
        if obj.current:
            end = 'Present'
        else:
            end = obj.end_date.strftime('%b %Y') if obj.end_date else '?'
        return f'{start} - {end}'
    date_range.short_description = 'Duration'
    
    def current_badge(self, obj):
        """Show if currently studying"""
        if obj.current:
            return format_html('<span style="background: #0A84FF; color: white; '
                              'padding: 3px 8px; border-radius: 4px; font-weight: bold;">Current</span>')
        return '—'
    current_badge.short_description = 'Status'
    
    def grade_display(self, obj):
        """Display grade or —"""
        return obj.grade if obj.grade else '—'
    grade_display.short_description = 'Grade'
    
    def mark_current(self, request, queryset):
        queryset.update(current=True, end_date=None)
        self.message_user(request, f'{queryset.count()} education entry/ies marked as current.')
    mark_current.short_description = 'Mark as currently studying'
    
    def mark_completed(self, request, queryset):
        queryset.update(current=False)
        self.message_user(request, f'{queryset.count()} education entry/ies marked as completed.')
    mark_completed.short_description = 'Mark as completed'


# ==================== CONTACT MESSAGE ADMIN ====================
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """Enhanced admin for Contact Messages with read status"""
    
    list_display = ('name', 'email', 'subject', 'read_badge', 'created_at')
    list_editable = ()
    list_filter = ('read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Message Details', {
            'fields': ('name', 'email', 'subject'),
        }),
        ('Message Content', {
            'fields': ('message',),
        }),
        ('Status', {
            'fields': ('read', 'created_at'),
        }),
    )
    
    actions = ['mark_as_read', 'mark_as_unread', 'delete_selected']
    
    def has_add_permission(self, request):
        """Prevent manually adding messages - only form submissions"""
        return False
    
    def has_delete_permission(self, request, obj=None):
        """Allow deleting contact messages"""
        return True
    
    def read_badge(self, obj):
        """Display read/unread status"""
        if obj.read:
            return format_html('✓ Read')
        else:
            return format_html('<span style="background: #00D9FF; color: #050816; '
                              'padding: 3px 8px; border-radius: 4px; font-weight: bold;">📧 Unread</span>')
    read_badge.short_description = 'Status'
    
    def mark_as_read(self, request, queryset):
        count = queryset.update(read=True)
        self.message_user(request, f'{count} message(s) marked as read.')
    mark_as_read.short_description = 'Mark selected as read'
    
    def mark_as_unread(self, request, queryset):
        count = queryset.update(read=False)
        self.message_user(request, f'{count} message(s) marked as unread.')
    mark_as_unread.short_description = 'Mark selected as unread'
