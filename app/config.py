import os

dev_config = {
    "DEBUG": True,
    "SECRET_KEY": 'my_secret_key',
}


# class Config(object):
#     """Base configuration."""
#     APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
#     PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
#
#
# class ProdConfig(Config):
#     """Production configuration."""
#     ENV = 'prod'
#     DEBUG = False
#
#
# class DevConfig(Config):
#     """Development configuration."""
#     ENV = 'dev'
#     DEBUG = True
#
#
# class TestConfig(Config):
#     """Тестовая конфигурация."""
#     ENV = 'test'
#     TESTING = True
#     DEBUG = True