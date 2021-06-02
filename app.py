
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from config import config
from loguru import logger
import logging

db = SQLAlchemy()


# 创建一个自定义处理程序
class InterceptHandler(logging.Handler):
    def emit(self, record):
        logger_opt = logger.opt(depth=6, exception=record.exc_info)
        logger_opt.log(record.levelno, record.getMessage())


# 应用工厂模式
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    # 定义了日志属性 in config.py
    logger.start(app.config['LOGFILE'], level=app.config['LOG_LEVEL'], format="{time} {level} {message}",
                 backtrace=app.config['LOG_BACKTRACE'], rotation='25 MB')

    # 将loguru注册为处理程序
    app.logger.addHandler(InterceptHandler())

    # 在此处注册蓝图
    # ...

    return app


app = create_app(config_name="development")

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
