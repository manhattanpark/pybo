import pandas as pd
import numpy as np
from zootopia import Cat
from common import gen_logger
import time

import logging


def test_cat_analyse_arbitrage_buy_low_sell_high():
    gen_logger('bigonetest_cat_analyse_arbitrage_buy_low_sell_high')
    logger = logging.getLogger("bigone")
    cat = Cat("ymt")
    cat.get_markets()
    for market in cat.markets_list:
        symbol,action_counts,total_counts = cat.analyse_arbitrage_buy_low_sell_high(market)
        logger.info("SYMBOL:{}, ACTIONS:{}/{}".format(symbol, action_counts, total_counts))

if __name__ == "__main__":
    test_cat_analyse_arbitrage_buy_low_sell_high()
