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
    
    # Availability Status
    availability_status = models.BooleanField(
        default=True,
        help_text='Toggle availability status on/off'
    )
    availability_text = models.CharField(
        max_length=100,
        default='Available for projects',
        help_text='Custom availability status text (e.g., "Available for projects", "Currently busy", "Open to opportunities")'
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
    
    # Predefined icon choices - common data analytics and tech icons
    ICON_CHOICES = [
        ('', '-- Select Icon --'),
        # Programming & Technical
        ('python', 'Python'),
        ('sql', 'SQL'),
        ('r-lang', 'R Language'),
        ('javascript', 'JavaScript'),
        ('html', 'HTML'),
        ('css', 'CSS'),
        ('git', 'Git'),
        ('terminal', 'Terminal/CLI'),
        ('code', 'Code/Programming'),
        ('database', 'Database'),
        ('api', 'API'),
        # Data & Analytics Tools
        ('excel', 'Excel'),
        ('tableau', 'Tableau'),
        ('powerbi', 'Power BI'),
        ('jupyter', 'Jupyter'),
        ('pandas', 'Pandas'),
        ('numpy', 'NumPy'),
        ('spark', 'Apache Spark'),
        ('hadoop', 'Hadoop'),
        # Analytics & Visualization
        ('chart-bar', 'Bar Chart'),
        ('chart-line', 'Line Chart'),
        ('chart-pie', 'Pie Chart'),
        ('analytics', 'Analytics'),
        ('dashboard', 'Dashboard'),
        ('report', 'Report'),
        ('statistics', 'Statistics'),
        # Machine Learning & AI
        ('brain', 'AI/Brain'),
        ('neural-network', 'Neural Network'),
        ('robot', 'Machine Learning'),
        ('target', 'Prediction/Target'),
        # Soft Skills
        ('users', 'Team/Collaboration'),
        ('communication', 'Communication'),
        ('lightbulb', 'Problem Solving'),
        ('clock', 'Time Management'),
        ('presentation', 'Presentation'),
        ('leadership', 'Leadership'),
        ('creative', 'Creativity'),
        ('detail', 'Attention to Detail'),
        ('learning', 'Fast Learner'),
        # Cloud & Infrastructure
        ('cloud', 'Cloud'),
        ('aws', 'AWS'),
        ('azure', 'Azure'),
        ('gcp', 'Google Cloud'),
        ('server', 'Server'),
        # General
        ('star', 'Star'),
        ('check', 'Checkmark'),
        ('bolt', 'Lightning Bolt'),
        ('cog', 'Settings/Cog'),
        ('custom', 'Custom SVG'),
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
        choices=ICON_CHOICES,
        default='',
        help_text="Select a predefined icon"
    )
    custom_svg = models.TextField(
        blank=True,
        help_text="Paste custom SVG code here (only used when icon is set to 'Custom SVG')"
    )
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_icon_svg(self):
        """Return SVG markup for the selected icon"""
        # If custom SVG is provided and icon is set to custom
        if self.icon == 'custom' and self.custom_svg:
            return self.custom_svg
        
        # SVG icons mapping
        icons = {
            'python': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M14.25.18l.9.2.73.26.59.3.45.32.34.34.25.34.16.33.1.3.04.26.02.2-.01.13V8.5l-.05.63-.13.55-.21.46-.26.38-.3.31-.33.25-.35.19-.35.14-.33.1-.3.07-.26.04-.21.02H8.77l-.69.05-.59.14-.5.22-.41.27-.33.32-.27.35-.2.36-.15.37-.1.35-.07.32-.04.27-.02.21v3.06H3.17l-.21-.03-.28-.07-.32-.12-.35-.18-.36-.26-.36-.36-.35-.46-.32-.59-.28-.73-.21-.88-.14-1.05-.05-1.23.06-1.22.16-1.04.24-.87.32-.71.36-.57.4-.44.42-.33.42-.24.4-.16.36-.1.32-.05.24-.01h.16l.06.01h8.16v-.83H6.18l-.01-2.75-.02-.37.05-.34.11-.31.17-.28.25-.26.31-.23.38-.2.44-.18.51-.15.58-.12.64-.1.71-.06.77-.04.84-.02 1.27.05zm-6.3 1.98l-.23.33-.08.41.08.41.23.34.33.22.41.09.41-.09.33-.22.23-.34.08-.41-.08-.41-.23-.33-.33-.22-.41-.09-.41.09zm13.09 3.95l.28.06.32.12.35.18.36.27.36.35.35.47.32.59.28.73.21.88.14 1.04.05 1.23-.06 1.23-.16 1.04-.24.86-.32.71-.36.57-.4.45-.42.33-.42.24-.4.16-.36.09-.32.05-.24.02-.16-.01h-8.22v.82h5.84l.01 2.76.02.36-.05.34-.11.31-.17.29-.25.25-.31.24-.38.2-.44.17-.51.15-.58.13-.64.09-.71.07-.77.04-.84.01-1.27-.04-1.07-.14-.9-.2-.73-.25-.59-.3-.45-.33-.34-.34-.25-.34-.16-.33-.1-.3-.04-.25-.02-.2.01-.13v-5.34l.05-.64.13-.54.21-.46.26-.38.3-.32.33-.24.35-.2.35-.14.33-.1.3-.06.26-.04.21-.02.13-.01h5.84l.69-.05.59-.14.5-.21.41-.28.33-.32.27-.35.2-.36.15-.36.1-.35.07-.32.04-.28.02-.21V6.07h2.09l.14.01zm-6.47 14.25l-.23.33-.08.41.08.41.23.33.33.23.41.08.41-.08.33-.23.23-.33.08-.41-.08-.41-.23-.33-.33-.23-.41-.08-.41.08z"/></svg>',
            'sql': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 3C7.58 3 4 4.79 4 7v10c0 2.21 3.58 4 8 4s8-1.79 8-4V7c0-2.21-3.58-4-8-4zm0 2c3.87 0 6 1.5 6 2s-2.13 2-6 2-6-1.5-6-2 2.13-2 6-2zm6 12c0 .5-2.13 2-6 2s-6-1.5-6-2v-2.23c1.61.78 3.72 1.23 6 1.23s4.39-.45 6-1.23V17zm0-4c0 .5-2.13 2-6 2s-6-1.5-6-2v-2.23c1.61.78 3.72 1.23 6 1.23s4.39-.45 6-1.23V13zm0-4c0 .5-2.13 2-6 2s-6-1.5-6-2V6.77c1.61.78 3.72 1.23 6 1.23s4.39-.45 6-1.23V9z"/></svg>',
            'r-lang': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 15h-2v-6h2v6zm0-8h-2V7h2v2zm5 8h-2l-2-3v3h-2v-6h2l2 3v-3h2v6z"/></svg>',
            'javascript': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M3 3h18v18H3V3zm16.525 13.707c-.131-.821-.666-1.511-2.252-2.155-.552-.259-1.165-.438-1.349-.854-.068-.248-.078-.382-.034-.529.113-.484.687-.629 1.137-.495.293.09.563.315.732.676.775-.507.775-.507 1.316-.844-.203-.314-.304-.451-.439-.586-.473-.528-1.103-.798-2.126-.775l-.528.067c-.507.124-.991.395-1.283.754-.855.968-.608 2.655.427 3.354 1.023.765 2.521.933 2.712 1.653.18.878-.652 1.159-1.475 1.058-.607-.136-.945-.439-1.316-1.002l-1.372.788c.157.359.337.517.607.832 1.305 1.316 4.568 1.249 5.153-.754.021-.067.18-.528.056-1.237l.034.049zm-6.737-5.434h-1.686c0 1.453-.007 2.898-.007 4.354 0 .924.047 1.772-.104 2.033-.247.517-.886.451-1.175.359-.297-.146-.448-.349-.623-.641-.047-.078-.082-.146-.095-.146l-1.368.844c.229.473.563.879.994 1.137.641.383 1.502.507 2.404.305.588-.17 1.095-.519 1.358-1.059.384-.697.302-1.553.299-2.509.008-1.541 0-3.083 0-4.635l.003-.042z"/></svg>',
            'html': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M1.5 0h21l-1.91 21.563L11.977 24l-8.564-2.438L1.5 0zm7.031 9.75l-.232-2.718 10.059.003.23-2.622L5.412 4.41l.698 8.01h9.126l-.326 3.426-2.91.804-2.955-.81-.188-2.11H6.248l.33 4.171L12 19.351l5.379-1.443.744-8.157H8.531z"/></svg>',
            'css': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M1.5 0h21l-1.91 21.563L11.977 24l-8.565-2.438L1.5 0zm17.09 4.413L5.41 4.41l.213 2.622 10.125.002-.255 2.716h-6.64l.24 2.573h6.182l-.366 3.523-2.91.804-2.956-.81-.188-2.11h-2.61l.29 3.855L12 19.288l5.373-1.53L18.59 4.414z"/></svg>',
            'git': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M23.546 10.93L13.067.452c-.604-.603-1.582-.603-2.188 0L8.708 2.627l2.76 2.76c.645-.215 1.379-.07 1.889.441.516.515.658 1.258.438 1.9l2.658 2.66c.645-.223 1.387-.078 1.9.435.721.72.721 1.884 0 2.604-.719.719-1.881.719-2.6 0-.539-.541-.674-1.337-.404-1.996L12.86 8.955v6.525c.176.086.342.203.488.348.713.721.713 1.883 0 2.6-.719.721-1.889.721-2.609 0-.719-.719-.719-1.879 0-2.598.182-.18.387-.316.605-.406V8.835c-.217-.091-.424-.222-.6-.401-.545-.545-.676-1.342-.396-2.009L7.636 3.7.45 10.881c-.6.605-.6 1.584 0 2.189l10.48 10.477c.604.604 1.582.604 2.186 0l10.43-10.43c.605-.603.605-1.582 0-2.187"/></svg>',
            'terminal': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 14H4V8h16v10zM7 17l4-4-4-4 1.4-1.4L13.8 13l-5.4 5.4L7 17zm6 0h4v-2h-4v2z"/></svg>',
            'code': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M9.4 16.6L4.8 12l4.6-4.6L8 6l-6 6 6 6 1.4-1.4zm5.2 0l4.6-4.6-4.6-4.6L16 6l6 6-6 6-1.4-1.4z"/></svg>',
            'database': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 3C7.58 3 4 4.79 4 7v10c0 2.21 3.58 4 8 4s8-1.79 8-4V7c0-2.21-3.58-4-8-4zm0 2c3.87 0 6 1.5 6 2s-2.13 2-6 2-6-1.5-6-2 2.13-2 6-2zm6 12c0 .5-2.13 2-6 2s-6-1.5-6-2v-2.23c1.61.78 3.72 1.23 6 1.23s4.39-.45 6-1.23V17zm0-4c0 .5-2.13 2-6 2s-6-1.5-6-2v-2.23c1.61.78 3.72 1.23 6 1.23s4.39-.45 6-1.23V13zm0-4c0 .5-2.13 2-6 2s-6-1.5-6-2V6.77c1.61.78 3.72 1.23 6 1.23s4.39-.45 6-1.23V9z"/></svg>',
            'api': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M7 7H5v10h2V7zm4 0H9v10h2V7zm2 0v10h2V7h-2zm6 0h-2v10h2V7z"/></svg>',
            'excel': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M21.17 3H7.83A1.83 1.83 0 006 4.83v.34H2.83A1.83 1.83 0 001 7v10a1.83 1.83 0 001.83 1.83H6v.34A1.83 1.83 0 007.83 21h13.34A1.83 1.83 0 0023 19.17V4.83A1.83 1.83 0 0021.17 3zM3 16.67V7.33h3v9.34H3zm4-2.84V7.17L8.5 9.5 10 7.17v6.66L8.5 11.5 7 13.83zm14 5.34H8V17h1v-1h2v1h2v-1h2v1h2v-1h2v2H8v.17h13v.83zm0-3.34h-2v-2h2v2zm0-3h-2v-2h2v2zm0-3h-2V7h2v2.83z"/></svg>',
            'tableau': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M11.654 5.327v2.02h-2.02v1.307h2.02v2.02h1.308v-2.02h2.018V7.347h-2.018v-2.02h-1.308zm-4.27 3.49v1.636H5.02v1.06h2.364v1.636h1.06v-1.636h2.365v-1.06H8.444V8.817h-1.06zm9.28 0v1.636h-2.365v1.06h2.365v1.636h1.06v-1.636h2.364v-1.06h-2.364V8.817h-1.06zM11.654 12.49v2.018h-2.02v1.308h2.02v2.02h1.308v-2.02h2.018v-1.308h-2.018v-2.018h-1.308zm-7.634.817v1.636H1.654v1.06H4.02v1.636h1.06v-1.636h2.364v-1.06H5.08v-1.636h-1.06zm15.27 0v1.636h-2.364v1.06h2.364v1.636h1.06v-1.636H22.714v-1.06H20.35v-1.636h-1.06z"/></svg>',
            'powerbi': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M10 12v8a2 2 0 002 2h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2zm2 0h8v8h-8v-8zM8 2a2 2 0 00-2 2v16a2 2 0 002 2h.5v-2H8V4h5v6h2V4a2 2 0 00-2-2H8zM4 6a2 2 0 00-2 2v12a2 2 0 002 2h.5v-2H4V8h1.5V6H4z"/></svg>',
            'jupyter': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.372 0 0 5.372 0 12s5.372 12 12 12 12-5.372 12-12S18.628 0 12 0zm-.5 3.5a1.5 1.5 0 110 3 1.5 1.5 0 010-3zM7 6a1 1 0 110 2 1 1 0 010-2zm10 0a1 1 0 110 2 1 1 0 010-2zm-5 2c3.314 0 6 2.686 6 6s-2.686 6-6 6-6-2.686-6-6 2.686-6 6-6zm-5.5 9.5a1.5 1.5 0 110 3 1.5 1.5 0 010-3zm11 0a1.5 1.5 0 110 3 1.5 1.5 0 010-3z"/></svg>',
            'pandas': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M16.922 0h2.623v18.104h-2.623zm-4.126 12.94h2.623v2.57h-2.623zm0-7.037h2.623v5.446h-2.623zm0 11.197h2.623v5.446h-2.623zM4.456 5.896h2.622V24H4.456zm4.213 2.559h2.623v2.57H8.67zm0 4.151h2.623v5.447H8.67zm0-11.16h2.623v5.446H8.67z"/></svg>',
            'numpy': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M10.315 4.876L6.098 2.227l-4.285 2.46v4.97l4.118 2.371V7.168l4.384-2.292zm-.577 6.465l-4.152 2.379v4.97l4.152-2.379v-4.97zm.958-.571l4.285 2.46v4.97l-4.285-2.46v-4.97zm4.861-2.834l-4.285-2.46-4.285 2.46 4.285 2.46 4.285-2.46zm.576 3.405v4.97l4.118 2.371V13.82l-4.118-2.479zm4.694-5.465l-4.285 2.46 4.285 2.46 4.285-2.46-4.285-2.46z"/></svg>',
            'spark': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 0L1.5 6v12L12 24l10.5-6V6L12 0zm0 2.5l7.5 4.3v8.4L12 19.5l-7.5-4.3V6.8L12 2.5zm0 3.5L7.5 9v6l4.5 2.6 4.5-2.6V9L12 6z"/></svg>',
            'hadoop': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 15h-2v-6h2v6zm0-8h-2V7h2v2zm5 8h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg>',
            'chart-bar': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M5 9.2h3V19H5V9.2zM10.6 5h2.8v14h-2.8V5zm5.6 8H19v6h-2.8v-6z"/></svg>',
            'chart-line': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M3.5 18.5l6-6 4 4L22 6.92 20.59 5.5l-7.09 8.58-4-4L2 18.5h1.5z"/></svg>',
            'chart-pie': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M11 2v20c-5.07-.5-9-4.79-9-10s3.93-9.5 9-10zm2.03 0v8.99H22c-.47-4.74-4.24-8.52-8.97-8.99zm0 11.01V22c4.74-.47 8.5-4.25 8.97-8.99h-8.97z"/></svg>',
            'analytics': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z"/></svg>',
            'dashboard': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M3 13h8V3H3v10zm0 8h8v-6H3v6zm10 0h8V11h-8v10zm0-18v6h8V3h-8z"/></svg>',
            'report': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/></svg>',
            'statistics': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M16 6l2.29 2.29-4.88 4.88-4-4L2 16.59 3.41 18l6-6 4 4 6.3-6.29L22 12V6z"/></svg>',
            'brain': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a9 9 0 00-9 9c0 4.17 2.84 7.67 6.69 8.69L12 22l2.31-2.31C18.16 18.67 21 15.17 21 11a9 9 0 00-9-9zm0 16c-3.87 0-7-3.13-7-7s3.13-7 7-7 7 3.13 7 7-3.13 7-7 7z"/><path d="M12 6c-2.76 0-5 2.24-5 5s2.24 5 5 5 5-2.24 5-5-2.24-5-5-5zm0 8c-1.66 0-3-1.34-3-3s1.34-3 3-3 3 1.34 3 3-1.34 3-3 3z"/></svg>',
            'neural-network': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>',
            'robot': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a2 2 0 012 2c0 .74-.4 1.39-1 1.73V7h1a7 7 0 017 7h1a1 1 0 011 1v3a1 1 0 01-1 1h-1v1a2 2 0 01-2 2H6a2 2 0 01-2-2v-1H3a1 1 0 01-1-1v-3a1 1 0 011-1h1a7 7 0 017-7h1V5.73c-.6-.34-1-.99-1-1.73a2 2 0 012-2M7.5 13A2.5 2.5 0 005 15.5 2.5 2.5 0 007.5 18a2.5 2.5 0 002.5-2.5A2.5 2.5 0 007.5 13m9 0a2.5 2.5 0 00-2.5 2.5 2.5 2.5 0 002.5 2.5 2.5 2.5 0 002.5-2.5 2.5 2.5 0 00-2.5-2.5z"/></svg>',
            'target': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm0-14c-3.31 0-6 2.69-6 6s2.69 6 6 6 6-2.69 6-6-2.69-6-6-6zm0 10c-2.21 0-4-1.79-4-4s1.79-4 4-4 4 1.79 4 4-1.79 4-4 4zm0-6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"/></svg>',
            'users': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5C6.34 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"/></svg>',
            'communication': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M20 2H4c-1.1 0-1.99.9-1.99 2L2 22l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm-2 12H6v-2h12v2zm0-3H6V9h12v2zm0-3H6V6h12v2z"/></svg>',
            'lightbulb': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M9 21c0 .5.4 1 1 1h4c.6 0 1-.5 1-1v-1H9v1zm3-19C8.1 2 5 5.1 5 9c0 2.4 1.2 4.5 3 5.7V17c0 .5.4 1 1 1h6c.6 0 1-.5 1-1v-2.3c1.8-1.3 3-3.4 3-5.7 0-3.9-3.1-7-7-7z"/></svg>',
            'clock': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm.5-13H11v6l5.25 3.15.75-1.23-4.5-2.67z"/></svg>',
            'presentation': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V5h14v14zM7 10h2v7H7zm4-3h2v10h-2zm4 6h2v4h-2z"/></svg>',
            'leadership': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>',
            'creative': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 22C6.49 22 2 17.51 2 12S6.49 2 12 2s10 4.04 10 9c0 3.31-2.69 6-6 6h-1.77c-.28 0-.5.22-.5.5 0 .12.05.23.13.33.41.47.64 1.06.64 1.67A2.5 2.5 0 0112 22zm0-18c-4.41 0-8 3.59-8 8s3.59 8 8 8c.28 0 .5-.22.5-.5a.54.54 0 00-.14-.35c-.41-.46-.63-1.05-.63-1.65a2.5 2.5 0 012.5-2.5H16c2.21 0 4-1.79 4-4 0-3.86-3.59-7-8-7z"/><circle cx="6.5" cy="11.5" r="1.5"/><circle cx="9.5" cy="7.5" r="1.5"/><circle cx="14.5" cy="7.5" r="1.5"/><circle cx="17.5" cy="11.5" r="1.5"/></svg>',
            'detail': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 4.5C7 4.5 2.73 7.61 1 12c1.73 4.39 6 7.5 11 7.5s9.27-3.11 11-7.5c-1.73-4.39-6-7.5-11-7.5zM12 17c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z"/></svg>',
            'learning': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 3L1 9l11 6 9-4.91V17h2V9M5 13.18v4L12 21l7-3.82v-4L12 17l-7-3.82z"/></svg>',
            'cloud': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96z"/></svg>',
            'aws': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M6.763 10.036c0 .296.032.535.088.71.064.176.144.368.256.576.04.063.056.127.056.183 0 .08-.048.16-.152.24l-.503.335a.383.383 0 01-.208.072c-.08 0-.16-.04-.239-.112a2.47 2.47 0 01-.287-.375 6.18 6.18 0 01-.248-.471c-.622.734-1.405 1.101-2.347 1.101-.67 0-1.205-.191-1.596-.574-.391-.384-.59-.894-.59-1.533 0-.678.239-1.23.726-1.644.487-.415 1.133-.623 1.955-.623.272 0 .551.024.846.064.296.04.6.104.918.176v-.583c0-.607-.127-1.03-.375-1.277-.255-.248-.686-.367-1.3-.367-.28 0-.568.031-.863.103-.295.072-.583.16-.862.272a2.287 2.287 0 01-.28.104.488.488 0 01-.127.023c-.112 0-.168-.08-.168-.247v-.391c0-.128.016-.224.056-.28a.597.597 0 01.224-.167c.279-.144.614-.264 1.005-.36a4.84 4.84 0 011.246-.151c.95 0 1.644.216 2.091.647.439.43.662 1.085.662 1.963v2.586zm-3.24 1.214c.263 0 .534-.048.822-.144.287-.096.543-.271.758-.51.128-.152.224-.32.272-.512.047-.191.08-.423.08-.694v-.335a6.66 6.66 0 00-.735-.136 6.02 6.02 0 00-.75-.048c-.535 0-.926.104-1.19.32-.263.215-.39.518-.39.917 0 .375.095.655.295.846.191.2.47.296.838.296zm6.41.862c-.144 0-.24-.024-.304-.08-.064-.048-.12-.16-.168-.311L7.586 5.55a1.398 1.398 0 01-.072-.32c0-.128.064-.2.191-.2h.783c.151 0 .255.025.31.08.065.048.113.16.16.312l1.342 5.284 1.245-5.284c.04-.16.088-.264.151-.312a.549.549 0 01.32-.08h.638c.152 0 .256.025.32.08.063.048.12.16.151.312l1.261 5.348 1.381-5.348c.048-.16.104-.264.16-.312a.52.52 0 01.311-.08h.743c.127 0 .2.065.2.2 0 .04-.009.08-.017.128a1.137 1.137 0 01-.056.2l-1.923 6.17c-.048.16-.104.263-.168.311a.51.51 0 01-.303.08h-.687c-.151 0-.255-.024-.32-.08-.063-.056-.119-.16-.15-.32l-1.238-5.148-1.23 5.14c-.04.16-.087.264-.15.32-.065.056-.177.08-.32.08zm10.256.215c-.415 0-.83-.048-1.229-.143-.399-.096-.71-.2-.918-.32-.128-.071-.215-.151-.247-.223a.563.563 0 01-.048-.224v-.407c0-.167.064-.247.183-.247.048 0 .096.008.144.024.048.016.12.048.2.08.271.12.566.215.878.279.319.064.63.096.95.096.502 0 .894-.088 1.165-.264a.86.86 0 00.415-.758.777.777 0 00-.215-.559c-.144-.151-.416-.287-.807-.415l-1.157-.36c-.583-.183-1.014-.454-1.277-.813a1.902 1.902 0 01-.4-1.158c0-.335.073-.63.216-.886.144-.255.335-.479.575-.654.24-.184.51-.32.83-.415.32-.096.655-.136 1.006-.136.175 0 .359.008.535.032.183.024.35.056.518.088.16.04.312.08.455.127.144.048.256.096.336.144a.69.69 0 01.24.2.43.43 0 01.071.263v.375c0 .168-.064.256-.184.256a.83.83 0 01-.303-.096 3.652 3.652 0 00-1.532-.311c-.455 0-.815.071-1.062.223-.248.152-.375.383-.375.71 0 .224.08.416.24.567.159.152.454.304.877.44l1.134.358c.574.184.99.44 1.237.767.247.327.367.702.367 1.117 0 .343-.072.655-.207.926-.144.272-.336.511-.583.703-.248.2-.543.343-.886.447-.36.111-.734.167-1.142.167z"/></svg>',
            'azure': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M5.483 21.3H24L14.025 4.013l-3.038 8.347 5.836 6.938L5.483 21.3zM13.175 2.7L6.458 12.525.025 18.34 13.175 2.7z"/></svg>',
            'gcp': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12.19 2.38a9.344 9.344 0 00-9.234 6.893c.053-.02-.055.013 0 0-3.875 2.551-3.922 8.11-.247 10.941l.006-.007-.007.03a6.717 6.717 0 004.077 1.356h5.173l.03.03h5.192c6.687.053 9.376-8.605 3.835-12.35a9.365 9.365 0 00-8.825-6.893zm.143 2.396a6.968 6.968 0 017.484 7.13 6.96 6.96 0 01-1.593 4.45 4.262 4.262 0 00-3.315-1.59h-.075l-.126-.005h-6.726a2.285 2.285 0 01-.118-4.568l.118-.002h3.794l.003-.004a2.285 2.285 0 10-1.142-4.402 6.948 6.948 0 011.696-.009z"/></svg>',
            'server': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M4 1h16c1.1 0 2 .9 2 2v4c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V3c0-1.1.9-2 2-2zm0 8h16c1.1 0 2 .9 2 2v4c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2v-4c0-1.1.9-2 2-2zm0 8h16c1.1 0 2 .9 2 2v4c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2v-4c0-1.1.9-2 2-2zM9 5H7v2h2V5zm0 8H7v2h2v-2zm0 8H7v2h2v-2z"/></svg>',
            'star': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>',
            'check': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>',
            'bolt': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M11 21h-1l1-7H7.5c-.58 0-.57-.32-.38-.66.19-.34.05-.08.07-.12C8.48 10.94 10.42 7.54 13 3h1l-1 7h3.5c.49 0 .56.33.47.51l-.07.15C12.96 17.55 11 21 11 21z"/></svg>',
            'cog': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M19.14 12.94c.04-.31.06-.63.06-.94 0-.31-.02-.63-.06-.94l2.03-1.58c.18-.14.23-.41.12-.61l-1.92-3.32c-.12-.22-.37-.29-.59-.22l-2.39.96c-.5-.38-1.03-.7-1.62-.94l-.36-2.54c-.04-.24-.24-.41-.48-.41h-3.84c-.24 0-.43.17-.47.41l-.36 2.54c-.59.24-1.13.57-1.62.94l-2.39-.96c-.22-.08-.47 0-.59.22L2.74 8.87c-.12.21-.08.47.12.61l2.03 1.58c-.04.31-.06.63-.06.94s.02.63.06.94l-2.03 1.58c-.18.14-.23.41-.12.61l1.92 3.32c.12.22.37.29.59.22l2.39-.96c.5.38 1.03.7 1.62.94l.36 2.54c.05.24.24.41.48.41h3.84c.24 0 .44-.17.47-.41l.36-2.54c.59-.24 1.13-.56 1.62-.94l2.39.96c.22.08.47 0 .59-.22l1.92-3.32c.12-.22.07-.47-.12-.61l-2.01-1.58zM12 15.6c-1.98 0-3.6-1.62-3.6-3.6s1.62-3.6 3.6-3.6 3.6 1.62 3.6 3.6-1.62 3.6-3.6 3.6z"/></svg>',
        }
        
        return icons.get(self.icon, '')

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
    detailed_description = models.TextField(
        blank=True,
        help_text="Detailed project description. Support for HTML and images. You can include HTML tags for formatting."
    )
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


class ProjectImage(models.Model):
    """Model for multiple images per project"""
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to='projects/gallery/')
    caption = models.CharField(max_length=200, blank=True, help_text="Optional caption for the image")
    order = models.IntegerField(default=0, help_text="Display order (lower numbers appear first)")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = "Project Image"
        verbose_name_plural = "Project Images"

    def __str__(self):
        return f"{self.project.title} - Image {self.order}"


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
    
    # Flexible date fields - only year is required if any date info is provided
    start_year = models.IntegerField(blank=True, null=True, help_text="e.g., 2020")
    start_month = models.IntegerField(blank=True, null=True, help_text="1-12 (optional)")
    end_year = models.IntegerField(blank=True, null=True, help_text="e.g., 2024")
    end_month = models.IntegerField(blank=True, null=True, help_text="1-12 (optional)")
    
    current = models.BooleanField(default=False)
    grade = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    institution_logo = models.ImageField(upload_to='institutions/', blank=True, null=True)
    certificate_image = models.ImageField(
        upload_to='education_certificates/', 
        blank=True, 
        null=True,
        help_text="Upload certificate/diploma image (optional)"
    )
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-end_year', '-start_year']
        verbose_name_plural = "Education"

    def __str__(self):
        return f"{self.degree} - {self.institution}"
    
    def get_start_display(self):
        """Format start date for display"""
        if not self.start_year:
            return None
        if self.start_month:
            from datetime import date
            month_name = date(2000, self.start_month, 1).strftime('%b')
            return f"{month_name} {self.start_year}"
        return str(self.start_year)
    
    def get_end_display(self):
        """Format end date for display"""
        if self.current:
            return "Present"
        if not self.end_year:
            return None
        if self.end_month:
            from datetime import date
            month_name = date(2000, self.end_month, 1).strftime('%b')
            return f"{month_name} {self.end_year}"
        return str(self.end_year)
    
    def get_date_range(self):
        """Get formatted date range string"""
        start = self.get_start_display()
        end = self.get_end_display()
        
        if start and end:
            return f"{start} - {end}"
        elif start:
            return f"Started {start}"
        elif end:
            return f"Completed {end}"
        return ""


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
