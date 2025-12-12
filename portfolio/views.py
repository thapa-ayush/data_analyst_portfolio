from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime, timedelta
from .models import About, Skill, Project, Certificate, Experience, Education, ContactMessage


def get_base_context(request):
    """
    Helper function to get common context data for all views
    """
    about = About.objects.first()
    return {
        'about': about,
    }


def home(request):
    """
    Home page view - displays hero section, stats, featured projects, and skills preview
    """
    about = About.objects.first()
    skills = Skill.objects.all()[:6]  # Top 6 skills
    
    # Show featured projects first, then fill with recent projects if not enough featured
    featured_projects = Project.objects.filter(featured=True).order_by('-date_completed')[:3]
    
    if featured_projects.count() < 3:
        # If not enough featured projects, add recent projects to fill
        remaining_needed = 3 - featured_projects.count()
        recent_projects = Project.objects.exclude(featured=True).order_by('-date_completed')[:remaining_needed]
        projects = list(featured_projects) + list(recent_projects)
    else:
        projects = featured_projects
    
    # Calculate stats - use custom values if set, otherwise count from database
    total_projects = about.stat_projects if about and about.stat_projects else Project.objects.count()
    total_skills = about.stat_skills if about and about.stat_skills else Skill.objects.count()
    total_certificates = about.stat_certifications if about and about.stat_certifications else Certificate.objects.count()
    total_experience = about.stat_experience if about and about.stat_experience else Experience.objects.count()

    context = get_base_context(request)
    context.update({
        'skills': skills,
        'projects': projects,
        'total_projects': total_projects,
        'total_skills': total_skills,
        'total_certificates': total_certificates,
        'total_experience': total_experience,
    })

    return render(request, 'portfolio/home.html', context)


def about_page(request):
    """
    About page view - displays biographical information, experience timeline, and education
    """
    from django.utils import timezone
    
    about = About.objects.first()
    experiences = Experience.objects.all().order_by('-start_date')
    education = Education.objects.all().order_by('-start_date')
    skills = Skill.objects.all()
    certificates = Certificate.objects.order_by('-issue_date')[:4]
    
    # Show featured projects first, then fill with recent projects if not enough featured
    featured_projects = Project.objects.filter(featured=True).order_by('-date_completed')[:6]
    
    if featured_projects.count() < 6:
        # If not enough featured projects, add recent projects to fill
        remaining_needed = 6 - featured_projects.count()
        recent_projects = Project.objects.exclude(featured=True).order_by('-date_completed')[:remaining_needed]
        projects = list(featured_projects) + list(recent_projects)
    else:
        projects = featured_projects

    context = get_base_context(request)
    context.update({
        'experiences': experiences,
        'education': education,
        'skills': skills,
        'certificates': certificates,
        'projects': projects,
        'now': timezone.now().date(),
    })

    return render(request, 'portfolio/about.html', context)


def skills_page(request):
    """
    Skills page view - displays all skills with category filtering
    """
    skills = Skill.objects.all().order_by('category', '-proficiency')

    context = get_base_context(request)
    context.update({
        'skills': skills,
    })

    return render(request, 'portfolio/skills.html', context)


def projects_page(request):
    """
    Projects page view - displays all projects with filtering and sorting
    """
    # Get filter and sort parameters from GET request
    filter_param = request.GET.get('filter', 'all')
    sort_param = request.GET.get('sort', 'recent')

    # Apply filter
    if filter_param == 'featured':
        projects = Project.objects.filter(featured=True)
    else:
        projects = Project.objects.all()

    # Apply sorting
    if sort_param == 'alphabetical':
        projects = projects.order_by('title')
    else:  # default to recent
        projects = projects.order_by('-date_completed')

    context = get_base_context(request)
    context.update({
        'projects': projects,
        'filter_param': filter_param,
        'sort_param': sort_param,
    })

    return render(request, 'portfolio/projects.html', context)


def project_detail(request, pk):
    """
    Project detail page view - displays detailed information about a specific project
    """
    project = get_object_or_404(Project, pk=pk)
    
    # Get related projects (same category, different project)
    related_projects = Project.objects.filter(
        category=project.category
    ).exclude(pk=pk)[:3]

    context = get_base_context(request)
    context.update({
        'project': project,
        'related_projects': related_projects,
    })

    return render(request, 'portfolio/project_detail.html', context)


def certificates_page(request):
    """
    Certificates page view - displays all certifications with sorting
    """
    certificates = Certificate.objects.all().order_by('-issue_date')
    
    # Calculate certificate stats
    total_certificates = certificates.count()
    active_certificates = 0
    expiring_soon = 0
    
    today = datetime.now().date()
    
    for cert in certificates:
        if cert.expiry_date:
            if cert.expiry_date >= today:
                active_certificates += 1
                days_until = (cert.expiry_date - today).days
                if days_until <= 30:
                    expiring_soon += 1
            # Add days_until_expiry attribute for template
            if cert.expiry_date >= today:
                cert.days_until_expiry = (cert.expiry_date - today).days
            else:
                cert.days_until_expiry = 0
                cert.is_expired = True
        else:
            active_certificates += 1

    context = get_base_context(request)
    context.update({
        'certificates': certificates,
        'total_certificates': total_certificates,
        'active_certificates': active_certificates,
        'expiring_soon': expiring_soon,
    })

    return render(request, 'portfolio/certificates.html', context)


@require_http_methods(["GET", "POST"])
def contact_page(request):
    """
    Contact page view - displays contact form and handles form submission
    """
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        subject = request.POST.get('subject', '').strip()
        message_text = request.POST.get('message', '').strip()

        # Validate required fields
        if not all([name, email, subject, message_text]):
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return render(request, 'portfolio/contact.html', 
                            get_base_context(request), status=400)
            messages.error(request, 'Please fill in all required fields.')
            return redirect('contact')

        # Validate email format
        if '@' not in email or '.' not in email:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return render(request, 'portfolio/contact.html', 
                            get_base_context(request), status=400)
            messages.error(request, 'Please enter a valid email address.')
            return redirect('contact')

        # Create ContactMessage object
        try:
            ContactMessage.objects.create(
                name=name,
                email=email,
                phone=phone,
                subject=subject,
                message=message_text
            )
            
            # Send email notification
            try:
                email_subject = f"New Contact Form Message: {subject}"
                email_body = f"""
You have received a new message from your portfolio contact form:

Name: {name}
Email: {email}
Phone: {phone if phone else 'Not provided'}
Subject: {subject}

Message:
{message_text}

---
This is an automated email. Do not reply to this address.
"""
                send_mail(
                    subject=email_subject,
                    message=email_body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=True,  # Don't fail if email can't be sent
                )
            except Exception as e:
                print(f"Error sending email: {e}")
                # Continue anyway - message is saved in database
            
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return render(request, 'portfolio/contact.html', 
                            get_base_context(request))
            messages.success(request, 'Thank you for your message! I will get back to you soon.')
            return redirect('contact')
        except Exception as e:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return render(request, 'portfolio/contact.html', 
                            get_base_context(request), status=500)
            messages.error(request, 'There was an error sending your message. Please try again.')
            return redirect('contact')

    context = get_base_context(request)
    return render(request, 'portfolio/contact.html', context)
