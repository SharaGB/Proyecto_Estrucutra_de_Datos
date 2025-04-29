from decouple import config


class Config:
    # Database configuration
    SECRET_KEY = config('SECRET_KEY')


class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig
}
