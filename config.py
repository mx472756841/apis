import os

from utils.redis import RedisClient

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'CK7HjdKShHJTrDyftqCFSnpDscx!-=09'
    #: 权限白名单
    WHITE_ROUTE_LIST = [
        "^/login"
    ]
    #: 可跨域访问域名
    CORS_ORIGINS = []

    # redis配置
    REDIS_HOST = os.environ.get('REDIS_HOST') or "127.0.0.1"
    REDIS_PORT = os.environ.get('REDIS_PORT') or 6379
    REDIS_PASS = os.environ.get('REDIS_PASS') or "example"
    REDIS_DB = os.environ.get('REDIS_DB') or 0

    @classmethod
    def init_app(cls, app):
        app.redis = RedisClient.get_client(cls.REDIS_HOST, cls.REDIS_PORT,
                                           cls.REDIS_DB, cls.REDIS_PASS)

    # token缓存key
    TOKEN_KEY = "token:%s:key"

class DevelopmentConfig(Config):
    DEBUG = True
    CORS_ORIGINS = ["http://localhost:9527"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'mysql+pymysql://root:root@localhost:3306/root'

    REDIS_HOST = os.environ.get('REDIS_HOST') or "127.0.0.1"
    REDIS_PORT = os.environ.get('REDIS_PORT') or 6379
    REDIS_PASS = os.environ.get('REDIS_PASS') or "example"
    REDIS_DB = os.environ.get('REDIS_DB') or 0


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
