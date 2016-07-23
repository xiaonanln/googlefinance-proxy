import tornado.ioloop
import tornado.web
import googlefinance
import json

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Welcome to googlefinance-proxy")

class GetQuotesHandler(tornado.web.RequestHandler):
    def get(self, symbols):
        symbols = str(symbols).upper().split(',')
        quotes = googlefinance.getQuotes(symbols)
        quotesStr = json.dumps(quotes)
        self.write(quotesStr)

def make_app():
    return tornado.web.Application([
        (r"/getQuotes/(.*)", GetQuotesHandler),
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
