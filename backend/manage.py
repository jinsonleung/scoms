#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    '''
    此项可以配置开发环境或生产环境，步骤：
    1）在backend/backend目录下创建develop.py及release.py配置文件
    2）将settings.py中用于开发环境的配置copy到develop.py，同理配置生产环境
    3）修改下方os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings.开发环境/生产环境文件名')
    4）重新迁移，若已创建了超级管理员，则需要重新创建再迁移一次
    '''
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
