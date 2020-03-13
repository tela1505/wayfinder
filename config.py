from os.path import dirname, abspath, join


class Config(object):
    CSRF_ENABLED = True
    SECRET_KEY = 't_lmesfQbbBzhV4CHD9ILw'
    DEBUG = False
    TESTING = False
    WTF_CSRF_SECRET_KEY = 'xzXK0qw6WJsVeDMaCchMAg'
    CWD = dirname(abspath(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(CWD, 'wayfinder.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    DEBUG = False
    TESTING = False


class TestConfig(Config):
    TESTING = True

class DevConfig(Config):
    DEBUG = True
