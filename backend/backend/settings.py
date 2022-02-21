"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os.path
import sys
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# 该语句的作用：让django到apps目录下寻找app
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-t3n#w1-qwto&+!lt!g(=kr0+97s%%kc%ue^8&gdbufbsa@4o!u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # ==框架==
    'rest_framework',  # rest框架
    'django_filters',   # django过滤器
    'corsheaders',  # 允许跨域请求
    # ==apps==
    'common',    # 公共app
    'enterprise',    # 企业信息
    # 'freightTools.airport',   # 全球机场三字代码
    'utils.universalCode',   # 国家/城市/机场代码
    'test0130',     # 用于测试
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # 允许跨域
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware', # 注释此行，否则POST请时出现Forbidden (CSRF cookie not set.)
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    # 'default': {  # 配置SQLITE数据库
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {  # 配置mysql数据库
        'ENGINE': 'django.db.backends.mysql',  # 数据库引擎
        'NAME': 'scomsdb',  # 数据库名，自己本地创建
        'USER': 'root',  # 数据库用户名
        'PASSWORD': 'China123',  # 数据库密码
        'HOST': 'localhost',  # MySQL服务所在主机IP
        'PORT': '3306',  # MySQL服务端口
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
# USE_TZ默认为为True，即有运用时区，设置为False则表示使用本地时间
USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ===================自行配置====================

# 1、***** 跨域配置 *****
# CORS_ORIGIN_ALLOW_ALL如果为True，则将不使用白名单，并且将接受所有来源。默认为False
CORS_ORIGIN_ALLOW_ALL = True
# 允许cookie, 指明在跨域访问中，后端是否支持对cookie的操作
CORS_ALLOW_CREDENTIALS = True
# 白名单，CORS_ORIGIN_ALLOW_ALL如果为True，则将不使用白名单
CORS_ORIGIN_WHITELIST = (   # 请求白名单
    ['http://127.0.0.1:*']
)

# CORS_ALLOW_METHODS = (  # 允许的请求方式
#     'DELETE',
#     'GET',
#     'OPTIONS',
#     'PATCH',
#     'POST',
#     'PUT',
#     'VIEW',
# )
#
# CORS_ALLOW_HEADERS = (  # 允许的请求头
#     'XMLHttpRequest',
#     'X_FILENAME',
#     'accept-encoding',
#     'authorization',
#     'content-type',
#     'dnt',
#     'origin',
#     'user-agent',
#     'x-csrftoken',
#     'x-requested-with',
# )

# 2、保存图片路径
IMG_UPLOAD = os.path.join(BASE_DIR, 'static/uploads')

# 3、保存商品图片路径
MEDIA_URL = '/media/'   # 保存文件时将放在这个目录下，以app名开始，如/media/goods/pic5-1.jpg
MEDIA_ROOT = (
    os.path.join(BASE_DIR, 'book_shop/media')   # 在根目录中创建'book_shop/media'目录，保存文件时将放在这个目录下
)

# 4、日期输入格式
# DATE_INPUT_FORMATS = ['%d/%m/%Y']

# REST_FRAMEWORK 相关配置
REST_FRAMEWORK = {
    #     'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    #     # 'DEFAULT_PERMISSION_CLASSES': (
    #     #     # 'rest_framework.permissions.IsAuthenticated',
    #     #     'enterprise.permissions.DisableOptionsPermission',
    #     # ),
    #     # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     #     'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    #     # ),
    #     # 'DEFAULT_METADATA_CLASS': None,
    #     'DEFAULT_RENDERER_CLASSES': (
    #         'rest_framework.renderers.JSONRenderer',
    #         'rest_framework.renderers.BrowsableAPIRenderer',
    #         'drf_renderer_xlsx.renderers.XLSXRenderer',
    #     ),
    #     'DEFAULT_PARSER_CLASSES': (
    #         'rest_framework.parsers.JSONParser',
    #         'rest_framework.parsers.FormParser',
    #         'rest_framework.parsers.MultiPartParser',
    #     ),
    # 格式化时间
    'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%S',
    'DATETIME_INPUT_FORMATS': ('%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M'),
    'DATE_FORMAT': '%Y-%m-%d',
    'DATE_INPUT_FORMATS': ('%Y-%m-%d',),
    'TIME_FORMAT': '%H:%M:%S',
    'TIME_INPUT_FORMATS': ('%H:%M:%S',),
    # DRF异常定制处理方法
    'EXCEPTION_HANDLER': 'utils.exceptionHandle.base_exception_handler',
    # DRF返回response定制json
    'DEFAULT_RENDERER_CLASSES': (
        'utils.rendererResponse.BaseJsonRenderer',
    ),
}
