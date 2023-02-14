from django.apps import AppConfig



# class FooConfig(AppConfig):
#     name = 'full.python.path.to.your.app.auth'
#     label = 'my.auth'


class AuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    label = 'auth'

# from django.apps import AppConfig

# class FooConfig(AppConfig):
#     name = 'full.python.path.to.your.app.auth'
#     label = 'my.auth'