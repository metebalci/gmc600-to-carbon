#!/usr/bin/python
from flask import Flask, request
import socket
import time

CARBON_SERVER = '127.0.0.1'
CARBON_PORT = 2003

app = Flask(__name__)


# ?AID=&GID=&CPM=&ACPM=&uSV=
@app.route('/geiger', methods=['GET'])
def geiger():
    cpm = request.args.get('CPM')
    acpm = request.args.get('ACPM')
    usv = request.args.get('uSV')
    t = int(time.time())
    msg_cpm = 'geiger.cpm %s %d\n' % (cpm, t)
    msg_acpm = 'geiger.acpm %s %d\n' % (acpm, t)
    msg_usv = 'geiger.usv %s %d\n' % (usv, t)
    sock = socket.socket()
    sock.connect((CARBON_SERVER, CARBON_PORT))
    sock.sendall(msg_cpm.encode('ascii'))
    sock.sendall(msg_acpm.encode('ascii'))
    sock.sendall(msg_usv.encode('ascii'))
    sock.close()
    return ""

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9006)
