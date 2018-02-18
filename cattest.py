from zootopia import Cat
from common import gen_logger
import time

import logging

if __name__ == "__main__":
    gen_logger('bigonetest_cat')
    logger = logging.getLogger("bigone")
    cat = Cat("mama")
    r = cat.get_markets_list()
    while True:
        cat.log_markets()
        time.sleep(5)
        logger.info("{}".format(int(time.time())))
