# Data Analyst Portfolio - Multi-Page Django Application

A comprehensive, fully-managed data analyst portfolio website built with Django, featuring a modern glassmorphic design, complete admin CRUD functionality, and responsive multi-page structure.

## 🚀 Features

### Multi-Page Structure

- **Home** - Landing page with hero section, creative profile picture, stats, featured projects, and skills preview
- **About** - Full biography, experience timeline, education history, and skills summary
- **Skills** - Comprehensive skills showcase with category filtering and proficiency levels
- **Projects** - Portfolio gallery with filtering/sorting and detailed project pages
- **Certificates** - Professional certifications with expiry tracking and credential verification
- **Contact** - Contact form with FAQ section and direct contact information

### Complete Admin CRUD Management

Every aspect of your portfolio is fully editable through Django Admin:

#### About Section

- Personal information (name, title, location)
- Contact details (email, phone)
- Professional bio
- Profile image and resume
- Social media links (LinkedIn, GitHub, Twitter)

#### Skills Management

- Skill name, category, and proficiency level (0-100)
- Color-coded categories (Technical, Tools, Analytics, Soft Skills)
- Visual proficiency bars in admin
- Custom ordering
- Bulk mark as featured/unfeatured

#### Projects Management

- Project title, description, detailed description
- Technologies (comma-separated for easy tag display)
- Project and GitHub URLs
- Featured status with starred indicator
- Status tracking (Completed, In Progress, Archived)
- Category selection (Data Analysis, Dashboard, Visualization, ML, Other)
- Key achievements with bullet-point display
- Duplicate project action

#### Certificates Management

- Certificate name, issuing organization
- Issue and expiry dates (supports lifetime certifications)
- Credential ID and verification URL
- Visual expiry status (Valid, Expiring Soon, Expired, Lifetime)
- Certificate image/logo
- Duplicate certificate action

#### Experience Management

- Company, position, location
- Employment duration with current/past status
- Description and achievements (newline-separated for bullet points)
- Company logo
- Visual timeline display
- Mark as current/past bulk actions

#### Education Management

- Institution, degree, field of study
- Study duration with current/completed status
- Grade/GPA field
- Institution logo
- Mark as current/completed bulk actions

#### Contact Messages

- All contact form submissions stored and viewable
- Read/unread status tracking
- Bulk mark as read/unread
- Search by name, email, subject, or message content
- Read-only display of message content

### Design Features

- **Glassmorphic Design** - Modern frosted glass effect with gradient borders
- **Dark Theme** - Eye-friendly dark color scheme with cyan/blue accents
- **Creative Profile Picture** - 3D holographic card effect with mouse tracking
- **Responsive Layout** - Desktop (1200px+), Tablet (768px-1199px), Mobile (<768px)
- **Smooth Animations** - Fade-in, hover effects, scroll-triggered animations
- **Grid Background** - Subtle animated gradient grid backdrop

### Technologies

- **Backend**: Django 5.2.9, Python
- **Database**: SQLite (production-ready for PostgreSQL)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Forms**: Django Forms with built-in validation
- **Admin**: Enhanced Django Admin with custom displays and bulk actions

## 📁 Project Structure

```
data_analyst_portfolio/
├── manage.py
├── populate_sample_data.py
├── requirements.txt
├── README.md
├── media/
│   ├── profile/
│   ├── projects/
│   ├── certificates/
│   ├── companies/
│   └── institutions/
├── static/
│   ├── css/
│   └── js/
├── portfolio/
│   ├── admin.py              # Enhanced admin interfaces
│   ├── models.py             # All data models with methods
│   ├── views.py              # All view functions
│   ├── urls.py               # URL routing
│   ├── apps.py
│   ├── tests.py
│   ├── migrations/
│   └── templates/portfolio/
│       ├── base.html         # Master template
│       ├── home.html         # Landing page
│       ├── about.html        # Biography page
│       ├── skills.html       # Skills showcase
│       ├── projects.html     # Projects gallery
│       ├── project_detail.html  # Individual project page
│       ├── certificates.html # Certifications page
│       └── contact.html      # Contact page & form
└── portfolio_project/
    ├── settings.py
    ├── urls.py
    ├── wsgi.py
    ├── asgi.py
    └── __pycache__/
```

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.8+
- pip
- Virtual Environment (recommended)

### Quick Start

1. **Create virtual environment**

```bash
python -m venv venv
source venv/Scripts/activate  # Windows
source venv/bin/activate      # macOS/Linux
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

4. **Create superuser (admin account)**

```bash
python manage.py createsuperuser
```

5. **Populate sample data** (optional)

```bash
python manage.py shell < populate_sample_data.py
```

6. **Run development server**

```bash
python manage.py runserver
```

7. **Access the portfolio**

- Website: http://localhost:8000
- Admin Panel: http://localhost:8000/admin

## 📖 URL Routes

| URL               | View              | Description                        |
| ----------------- | ----------------- | ---------------------------------- |
| `/`               | home              | Landing page with featured content |
| `/about/`         | about_page        | Full biography and timeline        |
| `/skills/`        | skills_page       | Skills showcase with filtering     |
| `/projects/`      | projects_page     | Projects gallery with sort/filter  |
| `/projects/<id>/` | project_detail    | Individual project details         |
| `/certificates/`  | certificates_page | Certifications list                |
| `/contact/`       | contact_page      | Contact form and information       |
| `/admin/`         | Django Admin      | Content management interface       |

## 🎨 Design Customization

### Color Scheme

Edit `base.html` CSS variables to customize colors:

```css
:root {
  --primary: #0a84ff; /* Main blue */
  --accent: #00d9ff; /* Cyan accent */
  --secondary: #ff6b35; /* Orange */
  --dark: #0a0e27; /* Dark blue */
  --darker: #050816; /* Almost black */
  --light: #e8ecf4; /* Light text */
  --grid-color: rgba(10, 132, 255, 0.1); /* Grid overlay */
}
```

### Fonts

- **Headings**: Syne (bold, 700-800 weight)
- **Body**: JetBrains Mono (regular, 400-600 weight)

## 💾 Database Models

### About

Contains single portfolio owner information with contact and social details.

### Skill

Professional skills with category and proficiency level (0-100).

### Project

Portfolio projects with descriptions, technologies, links, and achievement tracking.

### Certificate

Professional certifications with expiry tracking and credential verification.

### Experience

Work history with timeline, achievements, and employment status.

### Education

Educational background with timeline, grades, and completion status.

### ContactMessage

Contact form submissions with read/unread status tracking.

## 🔧 Admin Panel Features

### Visual Enhancements

- **Colored category badges** for skills
- **Proficiency bars** for visual skill levels
- **Featured indicators** for projects (⭐ emoji)
- **Technology tags** preview in projects
- **Timeline display** for experience with date ranges
- **Expiry status** for certificates (Valid/Expiring/Expired/Lifetime)
- **Read/Unread badges** for contact messages

### Bulk Actions

- Mark projects as featured/unfeatured
- Mark experiences as current/past employment
- Mark education as current/completed
- Mark contact messages as read/unread
- Duplicate projects/certificates

### Search & Filtering

- Search by name, content, organization
- Filter by category, status, date ranges
- Sort by order, date, name

## 📱 Responsive Design

All pages are fully responsive with breakpoints:

| Screen Size | Breakpoint   | Changes                                        |
| ----------- | ------------ | ---------------------------------------------- |
| Desktop     | 1200px+      | Full layout, 3-column grids                    |
| Tablet      | 768px-1199px | 2-column grids, adjusted spacing               |
| Mobile      | <768px       | Single column, hamburger menu, touch-optimized |

## 🔒 Security Features

- CSRF protection on forms
- XSS protection through template escaping
- SQL injection prevention (ORM queries)
- Email validation on contact forms
- File upload restrictions (media directory)
- Admin authentication required

## 🚀 Deployment on PythonAnywhere

1. **Upload files** to PythonAnywhere web directory
2. **Create virtualenv** and install requirements
3. **Configure web app** to use `portfolio_project/wsgi.py`
4. **Set up static/media directories** in web app settings
5. **Run migrations**: `python manage.py migrate`
6. **Collect static files**: `python manage.py collectstatic`
7. **Configure ALLOWED_HOSTS** and set `DEBUG = False`

### Environment Configuration

```python
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
DEBUG = False
STATIC_ROOT = '/home/username/mysite/static/'
MEDIA_ROOT = '/home/username/mysite/media/'
```

## 🐛 Troubleshooting

### Images Not Displaying

- Ensure `MEDIA_ROOT` and `MEDIA_URL` are configured
- Run `python manage.py collectstatic`
- Check file permissions on media directory

### Admin Panel Issues

- Run `python manage.py collectstatic`
- Clear browser cache
- Verify `STATIC_URL` configuration

### Contact Form Not Working

- Check `ALLOWED_HOSTS` includes your domain
- Verify CSRF token in form
- Check form validation in views.py

### Database Errors

- Run `python manage.py migrate`
- Check database file permissions
- Ensure database driver is installed

## 📝 Content Management Workflow

1. **Log in to admin panel** at `/admin/`
2. **Edit About section** - Your personal info and bio
3. **Add Skills** - Organize by category, set proficiency
4. **Add Projects** - With technologies and achievements
5. **Add Certificates** - With expiry dates and verification URLs
6. **Add Experience** - Work history with timeline
7. **Add Education** - Study history with grades
8. **View Contact Messages** - From form submissions

## 📄 Template Files

All templates use Django template language with:

- Base template inheritance from `base.html`
- Responsive grid layouts
- CSS animations and transitions
- Form validation and error handling
- Social media integration

## 🎯 Key Admin Features by Model

### About Admin

- Single entry enforcement
- Deletion prevention
- Social links management

### Skill Admin

- Color-coded category display
- Visual proficiency bars
- Bulk order editing

### Project Admin

- Featured project indicators
- Technology tag preview
- Status and category management
- Duplicate action

### Certificate Admin

- Expiry status with color coding
- Credential verification links
- Duplicate action

### Experience Admin

- Timeline date range display
- Current/past employment toggle
- Bulk status updates

### Education Admin

- Timeline display
- Grade tracking
- Current/completed status

### Contact Admin

- Message view-only display
- Read/unread status tracking
- Bulk status updates

## 🔐 Creating Additional Admin Users

```bash
python manage.py createsuperuser
```

## 📊 Performance Tips

1. Compress images before uploading
2. Use descriptive file names for SEO
3. Keep descriptions concise
4. Use comma-separated technologies for projects
5. Regularly clean up old contact messages

## 📈 Analytics Integration

To add analytics, update base.html with your tracking code:

```html
<!-- Google Analytics, Hotjar, etc. -->
```

## 🎨 Customization Guide

### Adding New Fields to Models

1. Edit `models.py` to add field
2. Create migration: `python manage.py makemigrations`
3. Apply migration: `python manage.py migrate`
4. Update admin.py fieldsets
5. Update relevant templates

### Styling Changes

- Edit CSS in template `<style>` blocks
- Use CSS variables for consistency
- Test responsive breakpoints

### Adding New Pages

1. Create template in `templates/portfolio/`
2. Add view function in `views.py`
3. Add URL pattern in `urls.py`
4. Add navigation link in `base.html`

## 💡 Tips for Success

- Keep project descriptions under 150 characters for cards
- Use emoji icons for visual interest
- Organize skills by relevance
- Feature your best 3 projects
- Keep about bio to 2-3 sentences
- Use professional profile picture
- Add links to live projects and GitHub repos
- Update certifications as you earn them
- Respond to contact messages promptly

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Support

For issues or questions:

1. Check the troubleshooting section
2. Review Django documentation
3. Contact through portfolio contact form

## 🎯 Future Enhancements

- Dark/Light mode toggle
- Blog/Article section
- Advanced search functionality
- Project filtering by technology
- Analytics dashboard
- API endpoints
- Progressive Web App features

---

**Made with Django & ❤️**

Version: 2.0 (Multi-Page)
Last Updated: 2024

Then paste the contents of `populate_sample_data.py` or run:

```bash
python manage.py shell < populate_sample_data.py
```

This creates sample entries for About, Skills, Projects, Certificates, Experience, and Education.

## Running Locally

### Start the Development Server

```bash
python manage.py runserver
```

You should see output like:

```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### Access Your Portfolio

- **Portfolio Website**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/
  - Login with your superuser credentials created earlier

### Troubleshooting Local Setup

**Port Already in Use:**

```bash
python manage.py runserver 8001  # Use port 8001 instead
```

**Database Issues:**

```bash
# Reset database (WARNING: deletes all data)
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

**Static Files Not Loading:**

```bash
python manage.py collectstatic --noinput
```

## Admin Panel Guide

The Django admin panel is your control center for managing portfolio content.

### Accessing Admin

1. Go to http://127.0.0.1:8000/admin/
2. Log in with your superuser credentials
3. You'll see sections for each model

### Managing Content

#### About Section

- Only one about entry (represents you)
- Edit profile image, resume, bio, and contact information
- Update social media links

**Fields:**

- Name: Your full name
- Title: Your professional title
- Bio: Professional biography
- Email: Contact email
- Phone: Contact phone (optional)
- Location: City/location
- Profile Image: Your profile picture
- Resume: PDF or document file
- LinkedIn/GitHub/Twitter URLs

#### Skills

- Create skills organized by category
- Set proficiency level (0-100%)
- Add icon emoji or class
- Order skills by dragging in the admin list

**Categories:**

- Technical (Python, SQL, R, etc.)
- Tools & Software (Tableau, Power BI, Excel, etc.)
- Analytics (Statistical Analysis, ML, etc.)
- Soft Skills (Communication, Problem Solving, etc.)

#### Projects

- Create featured (highlighted) and regular projects
- Add project images, descriptions, and technology tags
- Link to live project and GitHub repository
- Set project order and completion date

**Tips:**

- Featured projects appear first on the portfolio
- Technologies should be comma-separated (Python, Pandas, Tableau)
- Leave URLs blank if not applicable

#### Certificates

- Add professional certifications with dates
- Include credential links for verification
- Track expiry dates for time-sensitive certificates

**Tips:**

- Use MM/DD/YYYY format for dates
- Add credential URLs for verifiable certificates

#### Experience

- Record work history with detailed descriptions
- Add bullet-point achievements
- Mark current position to show "Present" instead of end date
- Include company logo

**Tips:**

- Achievements should be separated by newlines (press Enter)
- Achievements appear as bullet points on the portfolio

#### Education

- Add educational background
- Include degree, institution, and field of study
- Show current enrollment status
- Add GPA or grades if applicable

#### Contact Messages

- View and manage messages from the contact form
- Mark messages as read
- Search by name, email, or subject
- No direct deletion to prevent accidental loss (archive system could be added)

### Admin Tips & Tricks

**Filtering:**

- Use filters on the right side to view specific items (featured projects, current positions, etc.)
- Filter by date to see recent entries

**Searching:**

- Use the search box to find projects by title or description
- Search for skills by name
- Search contact messages by email or subject

**Bulk Actions:**

- Select multiple items using checkboxes
- Perform bulk operations from the action dropdown

**List Editing:**

- Edit fields directly in the list view (order, proficiency, featured status)
- Changes save immediately without opening the detail page

## Customization Tips

### Changing Portfolio Information

1. **Update About Section:**

   - Go to Admin > About Section
   - Edit name, title, and bio
   - Upload profile image and resume

2. **Add Your Skills:**

   - Go to Admin > Skills
   - Click "Add Skill"
   - Choose category and set proficiency level
   - Add emoji icon (e.g., 🐍 for Python)

3. **Showcase Your Projects:**

   - Go to Admin > Projects
   - Click "Add Project"
   - Upload project image
   - Add technologies as comma-separated values
   - Check "Featured" for top 3 projects

4. **Add Your Experience:**
   - Go to Admin > Experiences
   - Click "Add Experience"
   - Fill in company, position, dates
   - Add achievements (one per line)

### Customizing Design

The design is embedded in the template. To customize:

1. **Edit `portfolio/templates/portfolio/portfolio.html`**
2. **CSS Variables** (in `<style>` tag):

   - `--primary`: Main accent color (#0A84FF)
   - `--secondary`: Secondary color (#FF6B35)
   - `--accent`: Highlight color (#00D9FF)
   - `--dark`: Dark background (#0A0E27)
   - `--darker`: Darker background (#050816)

3. **Example Color Change:**
   ```css
   :root {
     --primary: #ff6b35; /* Change from blue to orange */
     --secondary: #0a84ff;
     --accent: #00d9ff;
   }
   ```

### Adding Sections

To add new sections:

1. Create a Django model in `portfolio/models.py`
2. Register it in `portfolio/admin.py`
3. Add admin configuration
4. Query it in `portfolio/views.py`
5. Render it in the template

## PythonAnywhere Deployment Guide

### Step 1: Create PythonAnywhere Account

1. Go to https://www.pythonanywhere.com
2. Sign up for a free account
3. Verify your email

### Step 2: Upload Your Files

**Option A: Using Web Interface**

1. In Dashboard, go to "Files"
2. Upload your project files
3. Create directory structure:
   ```
   /home/yourusername/
   └── data_analyst_portfolio/
       ├── manage.py
       ├── requirements.txt
       ├── db.sqlite3
       ├── portfolio_project/
       ├── portfolio/
       ├── static/
       └── media/
   ```

**Option B: Using Git (Recommended)**

1. Open Bash console in PythonAnywhere
2. Clone your repository:
   ```bash
   cd ~
   git clone https://github.com/yourusername/data_analyst_portfolio.git
   cd data_analyst_portfolio
   ```

### Step 3: Set Up Virtual Environment

In PythonAnywhere Bash console:

```bash
cd ~/data_analyst_portfolio

# Create virtual environment
mkvirtualenv --python=/usr/bin/python3.9 myenv

# Activate it (should happen automatically)
source /home/yourusername/.virtualenvs/myenv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 4: Configure Django Settings

Edit `portfolio_project/settings.py`:

```python
# Find and update these settings:

DEBUG = False

ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']

CSRF_TRUSTED_ORIGINS = ['https://yourusername.pythonanywhere.com']

# Uncomment SECRET_KEY configuration for production
SECRET_KEY = 'your-new-secret-key-here'  # Generate a new one

# Static files configuration
STATIC_ROOT = '/home/yourusername/data_analyst_portfolio/staticfiles'
STATIC_URL = '/static/'

# Media files
MEDIA_ROOT = '/home/yourusername/data_analyst_portfolio/media'
MEDIA_URL = '/media/'
```

### Step 5: Configure Web App

1. Go to "Web" tab in Dashboard
2. Click "Add a new web app"
3. Choose "Manual configuration"
4. Choose Python 3.9
5. In the Web app settings:

**Edit WSGI Configuration File:**

Click on the WSGI config file path shown in the Web tab. Replace contents with:

```python
import os
import sys

path = '/home/yourusername/data_analyst_portfolio'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolio_project.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

**Set Virtualenv:**

In the Web app settings, set:

- Virtualenv path: `/home/yourusername/.virtualenvs/myenv`

### Step 6: Configure Static & Media Files

In the Web app settings, scroll to "Static files" section and add:

**For Static Files:**

- URL: `/static/`
- Directory: `/home/yourusername/data_analyst_portfolio/staticfiles/`

**For Media Files:**

- URL: `/media/`
- Directory: `/home/yourusername/data_analyst_portfolio/media/`

### Step 7: Collect Static Files

In Bash console:

```bash
cd ~/data_analyst_portfolio
python manage.py collectstatic --noinput
```

### Step 8: Run Migrations

In Bash console:

```bash
cd ~/data_analyst_portfolio
python manage.py migrate
```

### Step 9: Create Superuser

In Bash console:

```bash
cd ~/data_analyst_portfolio
python manage.py createsuperuser
```

### Step 10: Reload Web App

1. Go back to Web tab
2. Click the "Reload" button

Your portfolio should now be live at: `https://yourusername.pythonanywhere.com`

### Accessing Admin on PythonAnywhere

Visit: `https://yourusername.pythonanywhere.com/admin/`

Log in with your superuser credentials.

### Troubleshooting PythonAnywhere Deployment

**502 Bad Gateway Error:**

Check the error log:

1. Go to Web tab
2. Scroll down to "Log files"
3. Click "Error log"
4. Common issues:
   - Missing virtual environment path
   - Missing WSGI configuration
   - Python path issues in WSGI file

**Static Files Not Loading:**

1. Clear browser cache
2. Run collectstatic again:
   ```bash
   python manage.py collectstatic --noinput
   ```
3. Reload web app

**Database Errors:**

1. Ensure migrations are run:
   ```bash
   python manage.py migrate
   ```
2. Check database file permissions
3. Recreate database if corrupted

**Updating Your Site**

After making changes in the admin or pulling new code:

```bash
# Pull latest changes (if using git)
git pull origin main

# Run migrations if you added new models
python manage.py migrate

# Collect static files if you changed CSS/JS
python manage.py collectstatic --noinput

# Reload web app from PythonAnywhere dashboard
```

## PythonAnywhere Deployment Checklist

Before deployment, ensure you have:

- [ ] Updated SECRET_KEY in settings.py
- [ ] Set DEBUG = False
- [ ] Updated ALLOWED_HOSTS with your domain
- [ ] Configured CSRF_TRUSTED_ORIGINS
- [ ] Set up STATIC_ROOT path
- [ ] Set up MEDIA_ROOT path
- [ ] Run collectstatic
- [ ] Run migrations
- [ ] Created superuser
- [ ] Tested admin panel access
- [ ] Tested contact form submission
- [ ] Verified media uploads work
- [ ] Added SSL certificate (free with PythonAnywhere)
- [ ] Set up environment variables if needed
- [ ] Backed up database
- [ ] Documented custom settings for future reference

## Project Structure

```
data_analyst_portfolio/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── populate_sample_data.py   # Sample data script
├── README.md                 # This file
├── db.sqlite3                # SQLite database (created after migrate)
├── portfolio_project/        # Main Django project
│   ├── __init__.py
│   ├── settings.py          # Project settings
│   ├── urls.py              # URL routing
│   ├── asgi.py              # ASGI config
│   └── wsgi.py              # WSGI config
├── portfolio/               # Django app
│   ├── models.py            # Database models (7 models)
│   ├── views.py             # Views (home, contact)
│   ├── urls.py              # App URL routing
│   ├── admin.py             # Admin configurations
│   ├── apps.py              # App config
│   ├── tests.py             # Tests
│   ├── migrations/          # Database migrations
│   └── templates/
│       └── portfolio/
│           └── portfolio.html  # Main template
├── static/                  # Static files (CSS, JS, images)
│   ├── css/
│   └── js/
├── media/                   # User uploaded files
│   ├── profile/             # Profile images
│   ├── resumes/             # Resume files
│   ├── projects/            # Project images
│   ├── certificates/        # Certificate images
│   ├── companies/           # Company logos
│   └── institutions/        # Institution logos
└── venv/                    # Virtual environment (local only)
```

## Database Models Overview

### About

Stores portfolio owner information (name, title, bio, contact info, social links)

### Skill

Professional skills with category, proficiency level (0-100), and icon

### Project

Portfolio projects with title, description, technologies, links, featured status

### Certificate

Professional certifications with issue dates, expiry dates, credential links

### Experience

Work experience with company, position, dates, description, achievements

### Education

Educational background with institution, degree, field of study, dates

### ContactMessage

Messages from contact form with name, email, subject, message, read status

## Common Tasks

### Update Your Bio

1. Go to Admin > About Section
2. Edit the bio field
3. Click Save
4. Changes appear immediately on your portfolio

### Add a New Project

1. Go to Admin > Projects
2. Click "Add Project"
3. Fill in title, description, technologies
4. Upload image
5. Check "Featured" if you want it in top 3
6. Click Save

### Change Portfolio Colors

1. Edit `portfolio/templates/portfolio/portfolio.html`
2. Find `:root` CSS variables at top of `<style>`
3. Change color values (e.g., `#0A84FF` to your color)
4. Save and refresh browser

### Download Backup of Database

1. In PythonAnywhere, go to Files
2. Find `db.sqlite3`
3. Right-click and select Download
4. Save in safe location

### Reset Contact Messages

1. Go to Admin > Contact Messages
2. Select all messages
3. In Action dropdown, choose Delete
4. Confirm deletion

## Security Considerations

### Production Deployment (PythonAnywhere)

✅ **Do This:**

- Keep `DEBUG = False`
- Use strong SECRET_KEY
- Update ALLOWED_HOSTS
- Use HTTPS only
- Regularly backup database
- Keep Django and dependencies updated

❌ **Don't Do This:**

- Commit SECRET_KEY to public repositories
- Set DEBUG = True in production
- Use default admin username
- Share database credentials
- Disable CSRF protection

### Securing Your Admin Panel

1. Use a strong, unique password for admin
2. Regularly change admin password
3. Consider limiting admin access by IP
4. Monitor admin activity logs
5. Use email notifications for important changes

## Maintenance

### Regular Tasks

**Weekly:**

- Check contact messages in admin
- Verify site is running correctly

**Monthly:**

- Backup database
- Review and update project descriptions
- Check external links still work

**Quarterly:**

- Update skills/proficiencies
- Add new certificates
- Review and update bio
- Backup all files

### Updates

```bash
# Check for Django updates
pip list --outdated

# Update packages
pip install --upgrade <package-name>

# Test locally before deploying
python manage.py runserver
```

## Troubleshooting

### Site Not Loading

1. Check if development server is running:

   ```bash
   python manage.py runserver
   ```

2. Clear browser cache (Ctrl+Shift+Delete)

3. Check error logs:
   - Terminal for local errors
   - PythonAnywhere Error log for production

### Contact Form Not Working

1. Verify messages are being saved in admin
2. Check email configuration if sending emails
3. Ensure CSRF token is in form (it is by default)

### Images Not Displaying

1. Verify image files exist in media folder
2. Check image permissions
3. Run:

   ```bash
   python manage.py collectstatic --noinput
   ```

4. Reload web app on PythonAnywhere

### Admin Panel Access Denied

1. Ensure you're logged in
2. Check URL is `/admin/`
3. Reset password if forgotten:
   ```bash
   python manage.py changepassword admin_username
   ```

## Support & Resources

### Django Documentation

- https://docs.djangoproject.com/

### PythonAnywhere Help

- https://help.pythonanywhere.com/
- https://www.pythonanywhere.com/help/

### Python Documentation

- https://docs.python.org/3/

## License

This project is provided as-is for personal portfolio use.

## Contributing

Feel free to customize and extend this project for your own needs.

## Changelog

### Version 1.0 (Initial Release)

- 7 comprehensive models
- Enhanced admin interface
- Contact form with message handling
- Responsive design
- PythonAnywhere deployment ready
- Sample data script
- Comprehensive documentation

---

**Last Updated:** December 2024
**Built With:** Django 5.2.9, Python 3.8+
