#!/usr/bin/env python
"""
Script to initialize About section if it doesn't exist
Run: python manage.py shell < setup_about.py
"""
from portfolio.models import About

# Check if About already exists
if About.objects.exists():
    print("✅ About section already exists!")
    about = About.objects.first()
    print(f"   Name: {about.name}")
    print(f"   Email: {about.email}")
else:
    # Create initial About entry with all fields
    about = About.objects.create(
        name="Your Name",
        title="Data Analyst",
        bio="Passionate data analyst transforming complex datasets into actionable insights. Specialized in Python, SQL, and data visualization.",
        email="your.email@example.com",
        phone="+1 (555) 123-4567",
        location="Your City, Country",
        hero_heading="Transforming Data Into Strategic Insights",
        hero_tagline="Data Analyst",
        hero_description="With 5+ years of experience, I transform complex datasets into compelling stories that drive business decisions. Specialized in Python, SQL, Tableau, and Power BI.",
        hero_cta_primary="View My Work",
        hero_cta_secondary="Get In Touch",
        show_profile_picture=True,
        linkedin_url="https://linkedin.com/in/yourprofile",
        github_url="https://github.com/yourprofile",
        twitter_url="https://twitter.com/yourprofile"
    )
    print("✅ About section created successfully!")
    print(f"   ID: {about.id}")
    print(f"   Name: {about.name}")
    print(f"   All hero fields are now editable in the admin panel!")

print("\n✅ Setup complete! Go to /admin/portfolio/about/ to edit.")
