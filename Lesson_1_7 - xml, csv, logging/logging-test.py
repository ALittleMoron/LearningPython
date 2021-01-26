import logging
import logging.config
import random, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)

dictLogConfig = {
        "version":1,
        "handlers":{
            "fileHandler":{
                'level': 'WARNING',
                "class":"logging.FileHandler",
                "formatter":"myFormatter",
                "filename": os.path.join(BASE_DIR, 'log.log'),
            }
        },
        "loggers":{
            "exampleApp":{
                "handlers":["fileHandler"],
                "level":"WARNING",
            }
        },
        "formatters":{
            "myFormatter":{
                "format":"%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            }
        }
    }


logging.config.dictConfig(dictLogConfig)
logger = logging.getLogger('exampleApp')


def div(a, b) -> float:
    try:
        return a/b
    except ZeroDivisionError:
        logger.error('division by 0')
        return .0


def mult(a, b) -> int:
    logger.warning('test')
    return a*b


if __name__ == "__main__":
    for _ in range(100):
        a = div(random.randint(-25, 25), random.randint(-25, 25))
        b = mult(random.randint(-25, 25), random.randint(-25, 25))
        #print(a, b)
