# Readme

## Archivo .env

```cmd
DJANGO_ADMIN_URL=ruta/al/admin/
DJANGO_ALLOWED_HOSTS=localhost,dominio.com
DJANGO_DEBUG=False
DJANGO_MEDIA_ROOT='full/path/public/media'
DJANGO_SECRET_KEY='secret-key'
DJANGO_SECURE_SSL_REDIRECT=True
DJANGO_STATIC_ROOT='full/path/public/static'

DB_CHARSET=UTF8
DB_CONN_MAX_AGE=60
DB_ENGINE=django.db.backends.postgresql
DB_HOST=localhost
DB_NAME=db_name
DB_PASSWORD='db_password'
DB_PORT=5432
DB_USER=db_user

DJANGO_EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
DJANGO_EMAIL_DEFAULT_FROM_EMAIL='correo@dominio.com'
DJANGO_EMAIL_HOST='mail.dominio.com'
DJANGO_EMAIL_HOST_PASSWORD='contraseña'
DJANGO_EMAIL_HOST_USER='correo@dominio.com'
DJANGO_EMAIL_PORT=465
DJANGO_EMAIL_USE_SSL=True

MAX_KEY_ATTEMPS=3

MIDDLEWARE_NOT_INCLUDE='urls/que,no/se,van/a/incluir'

YASG_TERMS_OF_SERVICE='https://www.dominio.com/policies/terms/'
YASG_DEFAULT_EMAIL='correo@dominio.com'
```

## Comandos

### Crear archivos de traducción

1. Crear la carpeta `locale` dentro de cada app
2. `django-admin makemessages -l es`
3. `django-admin compilemessages`
