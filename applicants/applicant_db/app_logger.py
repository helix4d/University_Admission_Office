import logging
import re
from logging.handlers import TimedRotatingFileHandler


def initialise():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    log_level = 10
    handler = TimedRotatingFileHandler("app.log", when="midnight", interval=1)
    handler.setLevel(log_level)
    formatter = logging.Formatter(log_format)
    handler.setFormatter(formatter)
    handler.suffix = "%Y%m%d"
    handler.extMatch = re.compile(r"^\d{8}$")
    logger.addHandler(handler)
    return logger


def log_new(request, pk):
    log = initialise()
    msg = 'Добавлен новый абитуриент id %d оператором %s ' % (pk, request.user.username)
    log.info(msg)


def log_export(request):
    log = initialise()
    msg = 'Запрошены данные дляэкспорта оператором %s' % (request.user.username)
    log.info(msg)


def log_delete(request, id):
    log = initialise()
    msg = 'Удален абитуриент id %d, оператором %s ' % (id, request.user.username)
    log.info(msg)


def log_edit(request, pk):
    log = initialise()
    msg = 'Изменены данные абитуриента id %d, оператором %s ' % (pk, request.user.username)
    log.info(msg)
