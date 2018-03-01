from bigone import BigOneClient
import pandas as pd
import numpy as np
import time


class Cat(BigOneClient):

    markets_list = []

    def __init__(self, account):
        BigOneClient.__init__(self, account)

    def get_markets_list(self):
        r = self.get_markets()
        for a in r:
            self.markets_list.append({
                "symbol": a['symbol'],
                "base": a['base'],
                "quote": a['quote']
            })
        return r

    def log_markets(self):
        for market in self.markets_list:
            order_book = self.get_order_book(market['symbol'])
            bid_price = order_book['bids'][0]['price']
            ask_price = order_book['asks'][0]['price']
            bid_amount = order_book['bids'][0]['amount']
            ask_amount = order_book['asks'][0]['amount']
            # TIME:{}, SYMBOL:{}, BID_PRICE:{}, BID_AMOUNT:{}, ASK_PRICE:{}, ASK_AMOUNT:{}
            with open('logs/'+market['symbol']+'.json', 'a+') as f:
                row = "{} {} {} {} {} {}\n".format(
                    int(time.time()),
                    market['symbol'],
                    bid_price,
                    bid_amount,
                    ask_price,
                    ask_amount
                )
                f.write(row)

    def analyse_arbitrage_buy_low_sell_high(self, market, profit_ratio=1.011):
        """
        在一个交易对中发现低买高卖的次数，用来确定该交易对能用来做"低买高卖"策略
        TODO:
        1. 需要加上市场的交易数据（交易次数，成交量），市场交易不频繁也无法执行"低买高卖"策略
        2. 预期执行次数需要加上间隔判断，和成交量判断
        :param market: 交易对
        :param profit_ratio: 低买高卖的预期收益率
        :return: symbol: 交易对的名字, action_counts: 预期执行策略次数, total_counts: 抓取数据的总次数
        """
        symbol = market['symbol']
        df = pd.read_csv('logs/'+symbol+'.json', sep=' ', names=["TIME", "SYMBOL", "BID_PRICE", "BID_AMOUNT", "ASK_PRICE", "ASK_AMOUNT"])
        df['PROFIT'] = df["ASK_PRICE"] / df["BID_PRICE"]
        df['ACTION'] = np.sign(df['PROFIT'] - profit_ratio)
        df['ACTION'].replace([-1, 0, 1], [False, False, True], inplace=True)
        sum = df['ACTION'].value_counts()
        action_counts = sum[True] if True in sum else 0
        total_counts = len(df)
        return symbol, action_counts, total_counts





