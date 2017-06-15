import os


class Config(object):
    """Base configuration."""
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    DEBUG = True


class ProdConfig(Config):
    """Production configuration."""
    DEBUG = False
    SECRET_KEY = 'my_prod_secret_key'


class DevConfig(Config):
    """Development configuration."""
    SECRET_KEY = 'my_secret_key'


class TestConfig(Config):
    """Тестовая конфигурация."""
    TESTING = True
    SECRET_KEY = 'my_test_secret_key'


if __name__ == '__main__':
    print(DevConfig.PROJECT_ROOT)
