from bigone import BigOneClient
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



