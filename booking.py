from twisted.web import server, resource, error
from twisted.internet import defer, reactor
from twisted.enterprise import adbapi
import json
import cgi

dbpool = adbapi.ConnectionPool("MySQLdb", host="localhost", user="user", passwd="user123", db="db_baf")

class Booking(resource.Resource):
    def getChild(self, name, request):
        if name == '':
            return self
        return Data_booking(int(name))

    def _insert(self, cursor, IDUser, IDJadwal, jBooking):
        insert_stmt = 'INSERT INTO booking (IDUser, IDJadwal, jBooking) VALUES (%d, %d, %d)' % (IDUser, IDJadwal, jBooking)
        cursor.execute(insert_stmt)

    def insert(self, IDUser, IDJadwal, jBooking):
        return dbpool.runInteraction(self._insert, IDUser, IDJadwal, jBooking)

    def _updateJadwal(self, cursor, quota, id):
        update_stmt = 'UPDATE jadwal SET Quota = %d WHERE ID = %d'%(quota, id)
        return cursor.execute(update_stmt)

    def updateJadwal(self, quota, id):
        return dbpool.runInteraction(self._updateJadwal, quota, id)

    def queryAll(self):
        select_stmt = 'SELECT * FROM booking'
        return dbpool.runQuery(select_stmt)

    def render_POST(self, request):
        IDUser = (cgi.escape(request.args["iduser"][0]),)
        IDJadwal = (cgi.escape(request.args["idjadwal"][0]),)
        jbooking = (cgi.escape(request.args["jbooking"][0]),)
        quota = (cgi.escape(request.args["quota"][0]),)

        self.insert(int(IDUser[0]), int(IDJadwal[0]), int(jbooking[0]))
        qSisa = int(quota[0]) - int(jbooking[0])
        self.updateJadwal(qSisa, int(IDJadwal[0]))
        request.setResponseCode(201)
        dict_pesan = {"status" : "success"}
        text_json = json.dumps(dict_pesan)
        return text_json


    def render_GET(self, request):
        def query():
            return self.queryAll()
        def onResult(result):
            count = 0
            data = []
            for record in result:
                booking = {}
                booking["id"] = record[0]
                booking["IDUser"] = record[1]
                booking["IDJadwal"] = record[2]
                booking["jBooking"] = record[3]
                data.append(booking)
                count+=1
            dict_pesan = {
                "data" : data
            }
            text_json = json.dumps(dict_pesan)
            request.write(text_json)
            request.finish()

        d = query()
        d.addCallback(onResult)

        return server.NOT_DONE_YET

class Data_booking(resource.Resource):
    isLeaf = True
    id = 0
    def __init__(self,id):
        self.id = id

    def querySelf(self, id):
        select_stmt = 'SELECT f.*, j.JamTayang, j.Studio, b.jBooking FROM booking b INNER JOIN jadwal j ON b.idJadwal = j.id INNER JOIN user u ON b.IDUser = u.ID INNER JOIN film f ON j.idFilm = f.id WHERE u.id = %d'%(id)
        return dbpool.runQuery(select_stmt)

    def _update(self, cursor, kolom, modif, id):
        update_stmt = 'UPDATE booking SET %s = "%s" WHERE ID = %d'%(kolom, modif, id)
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
            print "called"
            if result :
                data = []
                for record in result:
                    booking = {}
                    booking["ID"] = record[0]
                    booking["Judul"] = record[1]
                    booking["Sinopsis"] = record[2]
                    booking["urlposter"] = record[3]
                    booking["JamTayang"] = record[4].strftime('%Y-%m-%d %H:%M:%S')
                    booking["Studio"] = record[5]
                    booking["jBooking"] = record[6]
                    data.append(booking)
                dict_pesan = {
                    "data" : data
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
