#!/usr/bin/env python3
"""Simple RESTful API using http.server module."""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Request handler for our simple API."""

    def _set_headers(self, status=200, content_type='text/plain'):
        """Helper to set HTTP headers."""
        self.send_response(status)
        self.send_header('Content-Type', content_type)
        self.end_headers()

    def do_GET(self):
        """Handle GET requests for different endpoints."""
        if self.path == '/':
            self._set_headers(200, 'text/plain')
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            self._set_headers(200, 'application/json')
            payload = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(payload).encode('utf-8'))
        elif self.path == '/status':
            self._set_headers(200, 'text/plain')
            self.wfile.write(b"OK")
        else:
            self._set_headers(404, 'text/plain')
            self.wfile.write(b"Endpoint not found")


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    """Start the HTTP server."""
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == '__main__':
    run()
