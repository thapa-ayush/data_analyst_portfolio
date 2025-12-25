# Custom Domain & Email Setup Guide

This guide covers how to connect your Namecheap domain to PythonAnywhere and set up email forwarding for contact form submissions.

---

## Part 1: Add Custom Namecheap Domain to PythonAnywhere

### Prerequisites

- A PythonAnywhere **paid account** (Hacker plan or above - $5/month)
- A domain purchased from Namecheap
- Your site already deployed on PythonAnywhere

### Step 1: Add Domain in PythonAnywhere

1. Log in to **PythonAnywhere**
2. Go to the **Web** tab
3. Scroll down to **"Add a new web app"** or find your existing web app
4. Click on your web app name
5. Scroll to **"Add a new custom domain"**
6. Enter your domain name (e.g., `yourdomain.com`)
7. Click **Add**

### Step 2: Get PythonAnywhere DNS Information

After adding the domain, PythonAnywhere will show you:

- **CNAME target**: `webapp-XXXXX.pythonanywhere.com` (for subdomains like www)
- **A record IP**: `35.173.69.207` (for root domain - verify this in your dashboard.(ping yourusername.pythonanywhere.com) on bash)

> **Note**: The IP address may change. Always check PythonAnywhere's current IP in the Web tab.

### Step 3: Configure DNS in Namecheap

1. Log in to **Namecheap**
2. Go to **Domain List** → Click **Manage** next to your domain
3. Click on **Advanced DNS** tab
4. Delete any existing A records or CNAME records for @ and www

#### Add the following DNS records:

| Type         | Host | Value                              | TTL       |
| ------------ | ---- | ---------------------------------- | --------- |
| A Record     | @    | `35.173.69.207`                    | Automatic |
| CNAME Record | www  | `yourusername.pythonanywhere.com.` | Automatic |

> **Important**:
>
> - The `@` symbol represents your root domain (yourdomain.com)
> - The CNAME value must end with a period (.)
> - Replace `yourusername` with your actual PythonAnywhere username

### Step 4: Update Django Settings

Edit your `portfolio_project/settings.py`:

```python
ALLOWED_HOSTS = [
    'yourusername.pythonanywhere.com',
    'yourdomain.com',
    'www.yourdomain.com',
]

# For HTTPS (recommended)
CSRF_TRUSTED_ORIGINS = [
    'https://yourdomain.com',
    'https://www.yourdomain.com',
]
```

### Step 5: Wait for DNS Propagation

- DNS changes can take **15 minutes to 48 hours** to propagate
- You can check propagation status at: https://dnschecker.org

### Step 6: Enable HTTPS (Optional but Recommended)

1. In PythonAnywhere **Web** tab
2. Scroll to your custom domain
3. Click **"Enable HTTPS"** (available on paid plans)
4. PythonAnywhere will automatically get a Let's Encrypt certificate

### Troubleshooting

- **Site not loading**: Wait for DNS propagation
- **Certificate errors**: Make sure HTTPS is enabled in PythonAnywhere
- **"Invalid HTTP_HOST header"**: Add domain to `ALLOWED_HOSTS`

---

## Part 2: Email Forwarding for Contact Form

There are several ways to receive contact form submissions to your personal email.

### Option A: Use Gmail SMTP (Recommended)

This sends emails directly through Gmail's servers.

#### Step 1: Create Gmail App Password

1. Go to your **Google Account** → https://myaccount.google.com
2. Click **Security** (left sidebar)
3. Enable **2-Step Verification** if not already enabled
4. Go to **Security** → **2-Step Verification** → Scroll down
5. Click **App passwords**
6. Select app: **Mail**
7. Select device: **Other** → Enter "Django Portfolio"
8. Click **Generate**
9. **Copy the 16-character password** (save it securely!)

#### Step 2: Update Django Settings

Edit `portfolio_project/settings.py`:

```python
# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your.email@gmail.com'  # Your Gmail address
EMAIL_HOST_PASSWORD = 'xxxx xxxx xxxx xxxx'  # App password (with spaces)

# Default sender
DEFAULT_FROM_EMAIL = 'your.email@gmail.com'

# Where to receive contact form emails
CONTACT_EMAIL = 'your.email@gmail.com'
```

#### Step 3: Update Contact View

Make sure your contact form view sends to your email. In `portfolio/views.py`:

```python
from django.core.mail import send_mail
from django.conf import settings

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Compose email
        full_message = f"""
New Contact Form Submission

From: {name}
Email: {email}
Subject: {subject}

Message:
{message}
        """

        try:
            send_mail(
                subject=f'Portfolio Contact: {subject}',
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            messages.error(request, 'Failed to send message. Please try again.')

        return redirect('contact')

    return render(request, 'portfolio/contact.html')
```

### Option B: Use Environment Variables (More Secure)

For production, don't hardcode credentials. Use environment variables.

#### In PythonAnywhere:

1. Go to **Web** tab
2. Click on your web app
3. Go to **"WSGI configuration file"** link
4. Or set them in your **`.env`** file or **Bash console**:

```bash
export EMAIL_HOST_USER='your.email@gmail.com'
export EMAIL_HOST_PASSWORD='your-app-password'
```

#### In Django settings:

```python
import os

EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
CONTACT_EMAIL = os.environ.get('CONTACT_EMAIL', 'your.email@gmail.com')
```

### Option C: Using Namecheap Private Email

If you have Namecheap Private Email:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.privateemail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'contact@yourdomain.com'
EMAIL_HOST_PASSWORD = 'your-email-password'
```

### Testing Email Configuration

#### Test in PythonAnywhere Console:

```bash
cd ~/data_analyst_portfolio
source venv/bin/activate
python manage.py shell
```

```python
from django.core.mail import send_mail
send_mail(
    'Test Subject',
    'Test message body.',
    'your.email@gmail.com',
    ['your.email@gmail.com'],
    fail_silently=False,
)
```

If successful, you'll receive a test email.

### Common Email Issues

| Issue                   | Solution                                     |
| ----------------------- | -------------------------------------------- |
| "Authentication failed" | Check app password, ensure 2FA is enabled    |
| "Connection refused"    | Verify EMAIL_PORT (587 for TLS, 465 for SSL) |
| "Emails going to spam"  | Add SPF/DKIM records in Namecheap DNS        |
| "Not receiving emails"  | Check spam folder, verify recipient address  |

### Setting Up SPF Record (Reduces Spam Issues)

In Namecheap **Advanced DNS**, add:

| Type | Host | Value                                 | TTL       |
| ---- | ---- | ------------------------------------- | --------- |
| TXT  | @    | `v=spf1 include:_spf.google.com ~all` | Automatic |

---

## Quick Reference

### Files to Update:

1. `portfolio_project/settings.py` - Email and domain settings
2. `portfolio/views.py` - Contact form email sending

### PythonAnywhere Steps:

1. Add custom domain in Web tab
2. Enable HTTPS
3. Reload web app after settings changes

### Namecheap Steps:

1. Add A record pointing to PythonAnywhere IP
2. Add CNAME for www subdomain
3. Add SPF record for email deliverability

---

## After Making Changes

Always reload your PythonAnywhere web app:

1. Go to **Web** tab
2. Click the green **"Reload"** button

Or via Bash console:

```bash
touch /var/www/yourusername_pythonanywhere_com_wsgi.py
```
