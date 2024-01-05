
# Configuration settings for the Flask application

class Config(object):
    """ Common configurations """

class DevelopmentConfig(Config):
    """ Development configurations """
    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """ Production configurations """
    DEBUG = False

# Select the appropriate configuration class based on the environment
app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
