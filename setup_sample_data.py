#!/usr/bin/env python
"""
Script to populate sample projects and skills
Run: python manage.py shell < setup_sample_data.py
"""
from portfolio.models import Project, Skill

# Create sample skills
skills_data = [
    {"name": "Python", "category": "technical", "proficiency": 95, "icon": "🐍", "order": 1},
    {"name": "SQL", "category": "technical", "proficiency": 92, "icon": "🗄️", "order": 2},
    {"name": "Tableau", "category": "tools", "proficiency": 90, "icon": "📊", "order": 3},
    {"name": "Power BI", "category": "tools", "proficiency": 88, "icon": "📈", "order": 4},
    {"name": "Statistical Analysis", "category": "analytics", "proficiency": 90, "icon": "📉", "order": 5},
    {"name": "Communication", "category": "soft", "proficiency": 93, "icon": "💬", "order": 6},
]

# Create sample projects
projects_data = [
    {
        "title": "E-Commerce Sales Dashboard",
        "description": "Built an interactive dashboard analyzing $10M+ in annual sales data, identifying key trends and customer segments that increased retention by 28%.",
        "technologies": "Python, Pandas, Tableau, SQL",
        "featured": True,
        "status": "completed",
    },
    {
        "title": "Customer Churn Prediction",
        "description": "Developed ML model predicting customer churn with 87% accuracy, enabling proactive retention strategies and saving $2.5M annually.",
        "technologies": "Python, Scikit-learn, XGBoost, Feature Engineering",
        "featured": True,
        "status": "completed",
    },
    {
        "title": "Marketing Campaign Analysis",
        "description": "Analyzed multi-channel marketing campaigns, optimizing spend allocation and increasing ROI by 34% through data-driven insights.",
        "technologies": "R, ggplot2, SQL, Google Analytics",
        "featured": True,
        "status": "completed",
    },
]

# Add skills
print("Adding sample skills...")
for skill_data in skills_data:
    skill, created = Skill.objects.get_or_create(
        name=skill_data["name"],
        defaults={
            "category": skill_data["category"],
            "proficiency": skill_data["proficiency"],
            "icon": skill_data["icon"],
            "order": skill_data["order"],
        }
    )
    if created:
        print(f"  ✅ Created: {skill.name}")
    else:
        print(f"  ℹ️  Already exists: {skill.name}")

# Add projects
print("\nAdding sample projects...")
for proj_data in projects_data:
    project, created = Project.objects.get_or_create(
        title=proj_data["title"],
        defaults={
            "description": proj_data["description"],
            "technologies": proj_data["technologies"],
            "featured": proj_data["featured"],
            "status": proj_data["status"],
        }
    )
    if created:
        print(f"  ✅ Created: {project.title}")
    else:
        print(f"  ℹ️  Already exists: {project.title}")

print("\n✅ Sample data setup complete!")
print("   - 6 skills added to database")
print("   - 3 featured projects added to database")
print("   - Visit /admin/ to manage all content")
print("   - Visit / to see the homepage with sample data")
