from twisted.web import server, resource, error
from twisted.internet import defer, reactor
from twisted.enterprise import adbapi
import json
import cgi

dbpool = adbapi.ConnectionPool("MySQLdb", host="localhost", user="user", passwd="user123", db="db_baf")

class Film(resource.Resource):
    def getChild(self, name, request):
        if name == '':
            return self
        return Data_film(int(name))

    def queryAll(self):
        select_stmt = 'SELECT * FROM film'
        return dbpool.runQuery(select_stmt)

    def render_GET(self, request):
        def query():
            return self.queryAll()
        def onResult(result):
            if result :
                data = []
                for record in result:
                    film = {}
                    film["ID"] = record[0]
                    film["Judul"] = record[1]
                    film["Sinopsis"] = record[2]
                    film["urlposter"] = record[3]
                    data.append(film)
                dict_pesan = {
                    "data" : data
                }
                text_json = json.dumps(dict_pesan)
                request.setHeader('Access-Control-Allow-Origin', '*')
                request.write(text_json)
            else :
                request.setResponseCode(404)
                request.setHeader('Access-Control-Allow-Origin', '*')
                request.write('<html><body><b>404 DATA NOT FOUND</b></body></html>')
            request.finish()

        d = query()
        d.addCallback(onResult)

        return server.NOT_DONE_YET

class Data_film(resource.Resource):
    isLeaf = True
    id = 0
    def __init__(self,id):
        self.id = id

    def querySelf(self, id):
        select_stmt = 'SELECT * FROM film WHERE ID = %d'%(id)
        return dbpool.runQuery(select_stmt)

    def _update(self, cursor, kolom, modif, id):
        update_stmt = 'UPDATE film SET %s = "%s" WHERE ID = %d'%(kolom, modif, id)
        return cursor.execute(update_stmt)

    def update(self, kolom, modif, id):
        return dbpool.runInteraction(self._update, kolom, modif, id)

    def render_PUT(self, request):
        data = request.content.getvalue()
        fields = data.split('&')
        def query():
            return self.querySelf(self.id)
        def onResult(result):
            if result :
                data = []
                for field in fields :
                    parsed_data = field.split('=')
                    self.update(parsed_data[0],parsed_data[1],self.id)
                request.setResponseCode(201)
                dict_pesan = {"status" : "updated"}
                text_json = json.dumps(dict_pesan)
                request.setHeader('Access-Control-Allow-Origin', '*')
                request.write(text_json)
            else :
                request.setResponseCode(405)
                request.setHeader('Access-Control-Allow-Origin', '*')
                request.write('<html><body><b>405 METHOD NOT ALLOWED</b></body></html>')
            request.finish()
        d = query()
        d.addCallback(onResult)

        return server.NOT_DONE_YET

    def render_GET(self, request):
        def query():
            return self.querySelf(self.id)
        def onResult(result):
            if result :
                for record in result:
                    film = {}
                    film["ID"] = record[0]
                    film["Judul"] = record[1]
                    film["Sinopsis"] = record[2]
                    film["urlposter"] = record[3]
                dict_pesan = {
                    "data" : film
                }
                text_json = json.dumps(dict_pesan)
                request.setHeader('Access-Control-Allow-Origin', '*')
                request.write(text_json)
            else :
                request.setResponseCode(404)
                request.write('<html><body><b>404 THE PAGE NOT FOUND</b></body></html>')
            request.finish()
        d = query()
        d.addCallback(onResult)

        return server.NOT_DONE_YET
