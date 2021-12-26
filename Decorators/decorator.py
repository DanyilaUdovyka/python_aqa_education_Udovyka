import logging

logging.basicConfig(level=logging.DEBUG, handlers=[
    logging.FileHandler("debug.log"),
    logging.StreamHandler()
], format='%(asctime)s %(name)s %(levelname)s:%(message)s')
logger = logging.getLogger(__name__)


class NotValidType(Exception):
    pass


def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        for key, value in kwargs.items():
            logger.info("%s == %s - type %s" % (key, value, type(value)))
        for item in args:
            logger.info("arg %s - type %s" % (item, type(item)))
        logger.info("type of result - %s" % (type(return_value)))
        logger.info('[*] Время выполнения: {} секунд.'.format(end - start))

        return return_value

    return wrapper


@benchmark
def fetch_webpage(url, **kwargs):
    import requests
    if isinstance(url, str):
        webpage = requests.get(url)
        return webpage.text
    else:
        raise NotValidType(url, "Url is not string. URL - %s" % url)


try:
    webpage = fetch_webpage(12, first='Geeks', mid='for', last='Geeks')
except NotValidType:
    logger.error("Url is not correct")
