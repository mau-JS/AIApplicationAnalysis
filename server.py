import json
import logging
import re
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from socketserver import ThreadingMixIn
import threading

hostName = "0.0.0.0"
serverPort = 80

class LocalData(object):
    records = {}

class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if re.search('/api/post/*', self.path):
            length = int(self.headers.get('content-length'))
            data = self.rfile.read(length).decode('utf8')

            record_id = self.path.split('/')[-1]
            LocalData.records[record_id] = data
            
            logging.info("add record %s: %s", record_id, data)
            self.send_response(200)
        else:
            self.send_response(403)
        self.end_headers()

    def do_GET(self):
        if re.search('/api/get/*', self.path):
            record_id = self.path.split('/')[-1]
            if record_id in LocalData.records:
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()

                data = json.dumps(LocalData.records[record_id]).encode('utf8')
                logging.info("get record %s: %s", record_id, data)
                self.wfile.write(data) # wfile.write: write from req body
            else:
                self.send_response(404, 'Not Found: record does not exist')
        else:
            self.send_response(403)
        self.end_headers()

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

if __name__ == '__main__':
    server = ThreadedHTTPServer((hostName, serverPort), 
                        HTTPRequestHandler)
    logging.info('Starting server http://%s:%s' % (hostName, serverPort))
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    server.server_close()
    logging.info('Stopping server...\n')