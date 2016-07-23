import tornado.ioloop
import tornado.web
import googlefinance

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Welcome to googlefinance-proxy")

class GetQuotesHandler(tornado.web.RequestHandler):
    def get(self, symbol):
        quotes = googlefinance.getQuotes(symbol)
        self.write("getQuotes")

def make_app():
    return tornado.web.Application([
        (r"/getQuotes/(.*)", GetQuotesHandler),
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()