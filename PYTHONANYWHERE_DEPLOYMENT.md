# Deploy to PythonAnywhere - Step by Step Guide

Your Django portfolio is ready to deploy to PythonAnywhere! Follow these steps to go live.

## Step 1: Create PythonAnywhere Account

1. Go to https://www.pythonanywhere.com
2. Click "Sign up for a free account"
3. Choose a username (this will be your domain: `yourusername.pythonanywhere.com`)
4. Complete the signup process

## Step 2: Upload Your Project

### Option A: Using Git (Recommended)

1. **Initialize Git repository:**

   ```powershell
   cd F:\data_analyst_portfolio
   git init
   git add .
   git commit -m "Initial portfolio commit"
   ```

2. **Push to GitHub:**

   - Create a repository on GitHub (without .git suffix in name)
   - Push your code

3. **In PythonAnywhere Dashboard:**
   - Open "Bash console"
   - Clone your repository:
   ```bash
   cd /home/yourusername
   git clone https://github.com/yourusername/data_analyst_portfolio.git
   ```

### Option B: Manual Upload

1. In PythonAnywhere, open "Files" tab
2. Create folder `/home/yourusername/data_analyst_portfolio`
3. Upload all files except:
   - `venv/` folder
   - `.git/` folder
   - `db.sqlite3` (will create new one)
   - `*.pyc` files

## Step 3: Create Virtual Environment

1. **Open Bash Console in PythonAnywhere:**

   - Go to "Consoles" → "Bash"

2. **Create and activate virtual environment:**

   ```bash
   cd /home/yourusername/data_analyst_portfolio
   python3.10 -m venv venv
   source venv/bin/activate
   ```

3. **Install requirements:**
   ```bash
   pip install -r requirements.txt
   ```

## Step 4: Configure Django Settings

1. **Edit `portfolio_project/settings.py`:**

   ```python
   # Add your PythonAnywhere domain
   ALLOWED_HOSTS = ['yourusername.pythonanywhere.com', 'www.yourusername.pythonanywhere.com']

   # Set Debug to False for production
   DEBUG = False

   # Update secret key (use environment variable)
   SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-...')

   # Static files configuration
   STATIC_URL = '/static/'
   STATIC_ROOT = '/home/yourusername/data_analyst_portfolio/staticfiles'

   # Media files configuration
   MEDIA_URL = '/media/'
   MEDIA_ROOT = '/home/yourusername/data_analyst_portfolio/media'

   # Email configuration for production
   EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
   EMAIL_HOST = 'smtp-mail.outlook.com'  # For Outlook
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
   EMAIL_HOST_USER = 'thapa.aayush@outlook.com'
   EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
   DEFAULT_FROM_EMAIL = 'thapa.aayush@outlook.com'
   CONTACT_EMAIL = 'thapa.aayush@outlook.com'
   ```

## Step 5: Create Database and Run Migrations

```bash
cd /home/yourusername/data_analyst_portfolio
source venv/bin/activate
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
```

Follow the prompts to create your admin user.

## Step 6: Configure Web App in PythonAnywhere

1. **Go to "Web" tab** in PythonAnywhere dashboard
2. **Click "Add a new web app"**
3. **Choose "Manual configuration"** → Python 3.10
4. **Edit WSGI file** at `/var/www/yourusername_pythonanywhere_com_wsgi.py`

Replace the entire content with:

```python
import os
import sys

path = '/home/yourusername/data_analyst_portfolio'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolio_project.settings'

from django.wsgi import get_wsgi_application
application = get_wsgi_application()
```

## Step 7: Set Up Environment Variables

1. **In PythonAnywhere Web tab:**

   - Scroll to "Web app security"
   - Add environment variables:
     - `SECRET_KEY`: Your Django secret key
     - `EMAIL_HOST_PASSWORD`: Your Outlook app password

2. **Or create `.env` file** in project root and use python-dotenv (add to requirements.txt)

## Step 8: Configure Static and Media Files

In **Web tab**, under "Static files":

1. **Add static file mapping:**

   - URL: `/static/`
   - Directory: `/home/yourusername/data_analyst_portfolio/staticfiles`

2. **Add media file mapping:**
   - URL: `/media/`
   - Directory: `/home/yourusername/data_analyst_portfolio/media`

## Step 9: Reload Web App

1. **In Web tab**, click the green "Reload" button
2. Wait 10-15 seconds for reload to complete

## Step 10: Test Your Site

1. Visit: `https://yourusername.pythonanywhere.com`
2. Check the admin panel: `https://yourusername.pythonanywhere.com/admin`
3. Test contact form: `https://yourusername.pythonanywhere.com/contact`

## Troubleshooting

### "ModuleNotFoundError" or "No module named 'portfolio'"

- Check WSGI file path is correct
- Ensure virtual environment is activated in WSGI file
- Check Python version matches requirements

### Static files not loading

- Run: `python manage.py collectstatic --noinput`
- Verify static file mapping in Web tab

### Email not sending

- Check EMAIL_HOST_PASSWORD environment variable is set
- Verify Outlook app password is correct
- Check EMAIL_HOST is 'smtp-mail.outlook.com' for Outlook

### Database not migrating

- Run migrations from Bash console
- Check database permissions

### 502 Bad Gateway

- Check error log in Web tab (stderr file)
- Look for Python errors in server logs
- Ensure WSGI file is correct

## Going Live with Custom Domain

1. **Buy domain** from any registrar (GoDaddy, Namecheap, etc.)
2. **Point domain to PythonAnywhere:**
   - Add A record: `124.45.71.123`
   - Wait 24-48 hours for DNS propagation
3. **Configure in PythonAnywhere:**
   - Web tab → "Web app"
   - Add domain to ALLOWED_HOSTS in settings
   - Add domain to Web app configuration

## Best Practices

✅ Always use environment variables for sensitive data
✅ Set DEBUG = False in production
✅ Use HTTPS (free on PythonAnywhere)
✅ Keep virtual environment updated
✅ Backup database regularly
✅ Monitor error logs weekly
✅ Use strong admin password

## Next Steps

- Monitor your site performance
- Set up scheduled backups
- Enable email notifications for errors
- Consider upgrading to paid plan for more resources

**Your portfolio is now live! Share your domain and start showcasing your projects!**
