# Readme

## Archivo .env

```cmd
DJANGO_ALLOWED_HOSTS=ejemplo.com,localhost,127.0.0.1,0.0.0.0
DJANGO_SECRET_KEY='secret-django-key'
DJANGO_DEBUG=True
DJANGO_ADMIN_URL=admin/
DJANGO_SECURE_SSL_REDIRECT=False

DB_CHARSET=UTF8
DB_CONN_MAX_AGE=60
DB_ENGINE=django.db.backends.engine
DB_HOST=localhost
DB_NAME=db_name
DB_USER=db_username
DB_PASSWORD=db_password
DB_PORT=db_port

DJANGO_EMAIL_USE_SSL=True # False => TLS:True

DJANGO_EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
DJANGO_EMAIL_HOST_USER=email_host_user
DJANGO_EMAIL_HOST_PASSWORD=email_host_password
DJANGO_EMAIL_HOST=email_host
DJANGO_EMAIL_PORT=email_port
DJANGO_EMAIL_DEFAULT_FROM_EMAIL=email_default_from

SPIRIT_PERMISSION_GROUP_NAME=spirit_custom_group_name
```

## Comandos

### Crear archivos de traducción

1. Crear la carpeta `locale` dentro de la app
2. `django-admin makemessages -l es`
3. `django-admin compilemessages`
