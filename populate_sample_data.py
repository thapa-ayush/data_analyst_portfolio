"""
Script to populate the portfolio database with sample data.
Run this script using: python manage.py shell < populate_sample_data.py
Or alternatively: python manage.py shell and then paste the code
"""

import os
import django
from datetime import datetime, timedelta

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from portfolio.models import About, Skill, Project, Certificate, Experience, Education

# Clear existing data (optional - comment out to preserve existing data)
print("Clearing existing data...")
About.objects.all().delete()
Skill.objects.all().delete()
Project.objects.all().delete()
Certificate.objects.all().delete()
Experience.objects.all().delete()
Education.objects.all().delete()

# Create About Section
print("Creating About section...")
about = About.objects.create(
    name="Alex Johnson",
    title="Senior Data Analyst",
    bio="Passionate data analyst with 5+ years of experience turning complex datasets into actionable insights. Specialized in Python, SQL, and data visualization to drive data-driven decision making. I love uncovering hidden patterns in data and translating them into strategic business recommendations.",
    email="alex.johnson@example.com",
    phone="+1 (555) 123-4567",
    location="San Francisco, CA",
    linkedin_url="https://linkedin.com/in/alexjohnson",
    github_url="https://github.com/alexjohnson",
    twitter_url="https://twitter.com/alexjohnson"
)
print(f"✓ Created: {about}")

# Create Skills - Technical
print("\nCreating Skills...")
technical_skills = [
    ("Python", "technical", 95, "🐍"),
    ("SQL", "technical", 92, "🗄️"),
    ("R", "technical", 85, "📊"),
    ("JavaScript", "technical", 78, "💻"),
]

for name, category, proficiency, icon in technical_skills:
    skill = Skill.objects.create(
        name=name,
        category=category,
        proficiency=proficiency,
        icon=icon
    )
    print(f"✓ Created: {skill}")

# Tools & Software
tools_skills = [
    ("Tableau", "tools", 90, "📈"),
    ("Power BI", "tools", 88, "📊"),
    ("Excel", "tools", 95, "📑"),
    ("Jupyter", "tools", 92, "📓"),
]

for name, category, proficiency, icon in tools_skills:
    skill = Skill.objects.create(
        name=name,
        category=category,
        proficiency=proficiency,
        icon=icon
    )
    print(f"✓ Created: {skill}")

# Analytics
analytics_skills = [
    ("Statistical Analysis", "analytics", 90, "📉"),
    ("Machine Learning", "analytics", 82, "🤖"),
    ("Data Mining", "analytics", 88, "⛏️"),
    ("A/B Testing", "analytics", 85, "🧪"),
]

for name, category, proficiency, icon in analytics_skills:
    skill = Skill.objects.create(
        name=name,
        category=category,
        proficiency=proficiency,
        icon=icon
    )
    print(f"✓ Created: {skill}")

# Soft Skills
soft_skills = [
    ("Communication", "soft", 93, "💬"),
    ("Problem Solving", "soft", 90, "🧩"),
    ("Team Collaboration", "soft", 88, "🤝"),
]

for name, category, proficiency, icon in soft_skills:
    skill = Skill.objects.create(
        name=name,
        category=category,
        proficiency=proficiency,
        icon=icon
    )
    print(f"✓ Created: {skill}")

# Create Projects (3 featured + 2 regular)
print("\nCreating Projects...")
projects_data = [
    {
        "title": "E-Commerce Sales Analytics Dashboard",
        "description": "Built an interactive dashboard analyzing $10M+ in annual sales data, identifying key trends and customer segments that increased retention by 28%.",
        "detailed_description": "This comprehensive dashboard integrates data from multiple sources including transaction logs, customer databases, and market data. Using Tableau and Python-based ETL pipelines, I created visualizations that enabled the business to identify high-value customer segments and optimize marketing spend allocation.",
        "technologies": "Python, Pandas, NumPy, Tableau, SQL, PostgreSQL",
        "project_url": "https://example.com/projects/ecommerce-dashboard",
        "github_url": "https://github.com/alexjohnson/ecommerce-dashboard",
        "featured": True,
        "date_completed": datetime(2023, 6, 15).date(),
        "order": 1
    },
    {
        "title": "Customer Churn Prediction Model",
        "description": "Developed ML model predicting customer churn with 87% accuracy, enabling proactive retention strategies and saving $2.5M annually.",
        "detailed_description": "Implemented an ensemble machine learning model using XGBoost and scikit-learn that predicts customer churn with high precision. Feature engineering included customer lifecycle analysis, RFM segmentation, and behavioral clustering.",
        "technologies": "Python, Scikit-learn, XGBoost, Pandas, Plotly",
        "project_url": "https://example.com/projects/churn-prediction",
        "github_url": "https://github.com/alexjohnson/churn-prediction",
        "featured": True,
        "date_completed": datetime(2023, 4, 20).date(),
        "order": 2
    },
    {
        "title": "Marketing Campaign Performance Analysis",
        "description": "Analyzed multi-channel marketing campaigns, optimizing spend allocation and increasing ROI by 34% through data-driven insights.",
        "detailed_description": "Conducted comprehensive analysis across email, social media, and paid search campaigns. Using attribution modeling and cohort analysis, identified the most effective marketing channels and customer acquisition strategies.",
        "technologies": "R, ggplot2, SQL, Google Analytics, Tableau",
        "project_url": "https://example.com/projects/marketing-analysis",
        "github_url": "https://github.com/alexjohnson/marketing-analysis",
        "featured": True,
        "date_completed": datetime(2023, 3, 10).date(),
        "order": 3
    },
    {
        "title": "Supply Chain Optimization",
        "description": "Optimized inventory management reducing costs by 22% through predictive analytics and demand forecasting models.",
        "detailed_description": "Implemented time series forecasting models (ARIMA, Prophet) to predict demand and optimize inventory levels across distribution centers.",
        "technologies": "Python, Time Series, Power BI, SQL",
        "project_url": "",
        "github_url": "https://github.com/alexjohnson/supply-chain",
        "featured": False,
        "date_completed": datetime(2023, 2, 28).date(),
        "order": 4
    },
    {
        "title": "Financial Data ETL Pipeline",
        "description": "Automated data pipeline processing 1M+ daily transactions with 99.9% reliability using Apache Airflow and AWS.",
        "detailed_description": "Built scalable ETL infrastructure to handle massive financial data volumes, implementing error handling, data validation, and automated monitoring.",
        "technologies": "Python, Apache Airflow, PostgreSQL, AWS S3, AWS Lambda",
        "project_url": "",
        "github_url": "https://github.com/alexjohnson/financial-etl",
        "featured": False,
        "date_completed": datetime(2023, 1, 15).date(),
        "order": 5
    },
]

for project_data in projects_data:
    project = Project.objects.create(**project_data)
    print(f"✓ Created: {project} (Featured: {project.featured})")

# Create Certificates
print("\nCreating Certificates...")
certificates_data = [
    {
        "title": "Google Data Analytics Professional Certificate",
        "issuing_organization": "Google",
        "issue_date": datetime(2023, 6, 15).date(),
        "expiry_date": None,
        "credential_id": "GOOGLE-DA-12345",
        "credential_url": "https://coursera.org/verify/professional-cert/GOOGLE-DA-12345",
        "description": "Comprehensive data analytics certification covering SQL, spreadsheets, data visualization, and dashboarding.",
        "order": 1
    },
    {
        "title": "AWS Certified Data Analytics - Specialty",
        "issuing_organization": "Amazon Web Services",
        "issue_date": datetime(2023, 9, 20).date(),
        "expiry_date": datetime(2025, 9, 20).date(),
        "credential_id": "AWS-DAS-98765",
        "credential_url": "https://aws.amazon.com/certification/certified-data-analytics-specialty/",
        "description": "AWS Data Analytics certification demonstrating expertise in designing and maintaining analytics solutions on AWS.",
        "order": 2
    },
    {
        "title": "Tableau Desktop Specialist",
        "issuing_organization": "Tableau",
        "issue_date": datetime(2022, 11, 10).date(),
        "expiry_date": datetime(2024, 11, 10).date(),
        "credential_id": "TABLEAU-SPEC-54321",
        "credential_url": "https://www.tableau.com/learn/certification",
        "description": "Tableau Desktop specialization covering data visualization and dashboard creation.",
        "order": 3
    },
    {
        "title": "Machine Learning Specialization",
        "issuing_organization": "Stanford University (Coursera)",
        "issue_date": datetime(2023, 3, 22).date(),
        "expiry_date": None,
        "credential_id": "STANFORD-ML-11111",
        "credential_url": "https://coursera.org/verify/specialization/STANFORD-ML-11111",
        "description": "Machine Learning specialization covering supervised learning, unsupervised learning, and neural networks.",
        "order": 4
    },
]

for cert_data in certificates_data:
    cert = Certificate.objects.create(**cert_data)
    print(f"✓ Created: {cert}")

# Create Experiences
print("\nCreating Experiences...")
experiences_data = [
    {
        "company": "TechCorp Analytics",
        "position": "Senior Data Analyst",
        "location": "San Francisco, CA",
        "start_date": datetime(2021, 3, 1).date(),
        "end_date": None,
        "current": True,
        "description": "Lead data analytics initiatives across the organization, managing a team of junior analysts and implementing advanced analytics solutions.",
        "achievements": "Implemented real-time dashboard reducing report generation time by 80%\nDeveloped predictive models that saved $2.5M in operational costs\nMentored 3 junior analysts on best practices in data analysis\nPresented insights to C-level executives resulting in strategic business decisions",
        "order": 1
    },
    {
        "company": "DataDriven Solutions",
        "position": "Data Analyst",
        "location": "San Jose, CA",
        "start_date": datetime(2019, 6, 1).date(),
        "end_date": datetime(2021, 2, 28).date(),
        "current": False,
        "description": "Analyzed business data and created visualizations to support decision-making across multiple departments.",
        "achievements": "Built 15+ dashboards used by executive team for quarterly planning\nIdentified and resolved data quality issues affecting 20% of reports\nAutomated manual reporting processes saving 40 hours per month\nCollaborated with IT team to optimize database query performance",
        "order": 2
    },
    {
        "company": "Finance Analytics Inc",
        "position": "Junior Data Analyst",
        "location": "Los Angeles, CA",
        "start_date": datetime(2018, 1, 15).date(),
        "end_date": datetime(2019, 5, 31).date(),
        "current": False,
        "description": "Supported the analytics team in data collection, cleaning, and basic analysis for financial reporting.",
        "achievements": "Learned SQL and Python fundamentals while supporting data pipeline maintenance\nAssisted in creation of monthly financial reports for stakeholder review\nPerformed exploratory data analysis on customer transaction data",
        "order": 3
    },
]

for exp_data in experiences_data:
    exp = Experience.objects.create(**exp_data)
    print(f"✓ Created: {exp}")

# Create Education
print("\nCreating Education...")
education_data = [
    {
        "institution": "University of California, Berkeley",
        "degree": "Master of Science",
        "field_of_study": "Data Science",
        "start_date": datetime(2016, 8, 15).date(),
        "end_date": datetime(2018, 5, 31).date(),
        "current": False,
        "grade": "A",
        "description": "Specialized in machine learning, statistical modeling, and data engineering. Capstone project focused on predictive analytics for e-commerce.",
        "order": 1
    },
    {
        "institution": "Stanford University",
        "degree": "Bachelor of Science",
        "field_of_study": "Statistics",
        "start_date": datetime(2012, 8, 20).date(),
        "end_date": datetime(2016, 5, 15).date(),
        "current": False,
        "grade": "3.8",
        "description": "Strong foundation in probability, statistical methods, and mathematical modeling. Active in statistics club and research projects.",
        "order": 2
    },
]

for edu_data in education_data:
    edu = Education.objects.create(**edu_data)
    print(f"✓ Created: {edu}")

print("\n" + "="*50)
print("✓ Sample data population completed successfully!")
print("="*50)
print("\nYou can now:")
print("1. Run: python manage.py runserver")
print("2. Visit: http://127.0.0.1:8000/ to see your portfolio")
print("3. Visit: http://127.0.0.1:8000/admin/ to manage content")
