from django.apps import AppConfig


class ProfileViewConfig(AppConfig):
    name = 'profile_view'

    def ready(self):
    	import profile_view.signals