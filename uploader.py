import tornado.web
import tornado.ioloop

if (__name__ == '__main__'):
    app = tornado.web.Application([
        ('/imagesAttendence/(.*)',tornado.web.StaticFileHandler,{"path" : "imagesAttendence"})
    ])
    app.listen(8080)
    print("Listening on port 8080")

    tornado.ioloop.IOLoop.instance().start()