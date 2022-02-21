from django.apps import AppConfig


class CommonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.public'    # 修改app名称，使应用可以在apps目录中存在，并且可以正常的导入到settings
