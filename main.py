from twisted.web import server, resource, error
from twisted.internet import defer, reactor
from twisted.enterprise import adbapi
import user
import film
import jadwal
import booking
import json
import cgi

dbpool = adbapi.ConnectionPool("MySQLdb", host="localhost", user="user", passwd="user123", db="db_baf")

class Home(resource.Resource):
    isLeaf = True
    def getChild(self, name, request):
        if name == '':
            return self
        return Resource.getChild(self, name, request)

    def render_GET(self, request):
        return '<html><body>Hello This is Home</body></html>'

root = resource.Resource()
root.putChild("", Home())
root.putChild("User", user.User())
root.putChild("Film", film.Film())
root.putChild("Jadwal", jadwal.Jadwal())
root.putChild("Booking", booking.Booking())

factory = server.Site(root)
reactor.listenTCP(8001, factory)
reactor.run()
