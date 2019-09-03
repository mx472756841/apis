import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'CK7HjdKShHJTrDyftqCFSnpDscx'
    #: 权限白名单
    WHITE_ROUTE_LIST = [
        "^/login"
    ]
    #: 可跨域访问域名
    CORS_ORIGINS = []


class DevelopmentConfig(Config):
    DEBUG = True
    CORS_ORIGINS = ["http://localhost:9527"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'mysql+pymysql://root:root@localhost:3306/root'

    print(os.environ.get('DEV_DATABASE_URL'))


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
