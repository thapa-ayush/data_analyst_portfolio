#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from portfolio.models import About

print("=" * 60)
print("CHECKING ABOUT SECTION")
print("=" * 60)

about = About.objects.first()

if about:
    print("\n✅ About entry EXISTS\n")
    print(f"Name: {about.name}")
    print(f"Title: {about.title}")
    print(f"Profile Image: {about.profile_image}")
    print(f"Hero Heading: {about.hero_heading}")
    print(f"Hero Tagline: {about.hero_tagline}")
    print(f"Hero Description: {about.hero_description[:50]}..." if about.hero_description else "Hero Description: (empty)")
    print(f"Hero CTA Primary: {about.hero_cta_primary}")
    print(f"Hero CTA Secondary: {about.hero_cta_secondary}")
    print(f"Show Profile Picture: {about.show_profile_picture}")
    print("\n" + "=" * 60)
    print("✅ ALL FIELDS AVAILABLE")
    print("=" * 60)
    print("\nTO CUSTOMIZE:")
    print("1. Go to: http://127.0.0.1:8000/admin/")
    print("2. Login with your superuser credentials")
    print("3. Click on 'About Section' under PORTFOLIO")
    print("4. Scroll to 'Media' section to UPLOAD PROFILE PICTURE")
    print("5. Scroll to 'Hero Section Customization' to EDIT HERO TEXT")
    print("6. Click SAVE at the bottom")
    print("\nFIELDS YOU CAN CUSTOMIZE:")
    print("  - Profile Image (upload your photo)")
    print("  - Hero Tagline (short subtitle)")
    print("  - Hero Heading (main title)")
    print("  - Hero Description (long text)")
    print("  - Hero CTA Primary (button text)")
    print("  - Hero CTA Secondary (button text)")
    print("  - Show Profile Picture (toggle)")
else:
    print("\n❌ NO ABOUT ENTRY FOUND")
    print("\nCreating default About entry...")
    about = About.objects.create(
        name="Your Name",
        title="Data Analyst",
        bio="Your professional bio",
        email="your.email@example.com",
        hero_heading="Transforming Data Into Strategic Insights",
        hero_tagline="Data Analyst",
        hero_description="Your professional description",
        hero_cta_primary="View My Work",
        hero_cta_secondary="Get In Touch",
        show_profile_picture=True,
        footer_tagline="Turning data into insights"
    )
    print(f"✅ Created About entry with ID: {about.id}")
    print("\nNow go to admin and customize it!")

print("\n")
