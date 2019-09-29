import logging.config
import os

from common.log import Log
from utils.redis import RedisClient

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SERVICE_NAME = "api"
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

    # 数据库配置
    DB_HOST = os.environ.get('DB_HOST') or "127.0.0.1"
    DB_PORT = os.environ.get('DB_PORT') or 3306
    DB_USER = os.environ.get('DB_USER') or "root"
    DB_PASS = os.environ.get('DB_PASS') or "123"
    DB_NAME = os.environ.get('DB_NAME') or "root"


    # 构建日志相关信息
    LOG_DIR = os.path.join(basedir, 'logs')
    if not os.path.isdir(LOG_DIR):
        os.mkdir(LOG_DIR)

    Log.LOG_PATH = LOG_DIR
    Log.SERVICE_NAME = SERVICE_NAME
    logging.config.dictConfig(Log.LOG_CONFIG_DICT)

    @classmethod
    def init_app(cls, app):
        app.redis = RedisClient.get_client(cls.REDIS_HOST, cls.REDIS_PORT,
                                           cls.REDIS_DB, cls.REDIS_PASS)
        app.logger = logging.getLogger("full_logger")

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
