# -*- coding:utf-8 -*-

# Author: ChenTong
# Date: 2021/6/2 09:26


import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'SUPER-SECRET'
    LOGFILE = "log.log"

class DevelopmentConfig(Config):
    DEBUG = True
    LOG_BACKTRACE = True
    LOG_LEVEL = 'DEBUG'


class ProductionConfig(Config):
    LOG_BACKTRACE = False
    LOG_LEVEL = 'INFO'


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}