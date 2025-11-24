# Overview
who will ever read this, if this was a real applicatoin it would talk about features. But this is just for demo. Someone make this nice? 

## Install and Setup
Clone the repository and create a new Python virtual environment:

    python -m venv .venv
    source .venv/bin/activate        # Linux / macOS
    .venv\Scripts\activate           # Windows

Install project dependencies:

    pip install -r requirements.txt

Apply the initial database migrations:

    python manage.py migrate

Start the development server:

    python manage.py runserver

You can now access the application locally at http://127.0.0.1:8000/.

### Temporary Email Demonstration
Presently, the email sending service is not integrated into the website. To wittness the email, just run the server in shell. 

    python manage.py shell
Then run the following to actually send the email. You must have first set up the local_settings.py as discussed below. 

    from notifier.utils import send_demo_email
    send_demo_email()

    exit()

If everything functioned properly, you will receive a '1' after send_demo_email(). 

## Creating local_settings.py
This project uses a separate settings file to hold email configuration and other developer-specific values.  
This file is not tracked in version control and must be created by each developer.

Create a file named `local_settings.py` in the same directory as `settings.py` and add the following structure:
    
	EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
	EMAIL_HOST = 'smtp.gmail.com'
	EMAIL_PORT = 587
	EMAIL_USE_TLS = True

	EMAIL_HOST_USER = 'example.sender@gmail.com'
	EMAIL_HOST_PASSWORD = 'demo password' 
	DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

	DEFAULT_TEST_EMAIL = 'example.recipent@proton.me'

Developers should substitute their own SMTP host and credentials.  
Do not commit this file. The `.gitignore` entry ensures it remains local-only.

