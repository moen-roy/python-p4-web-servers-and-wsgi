#!/usr/bin/env python3
# server/werkzeug_app.py
from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    # This prints the visitor's address to your terminal
    print(f'This web server is running at {request.remote_addr}')
    # This sends a response back to the browser
    return Response('A WSGI generated this response!')

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple(
        hostname='localhost', # The server's address
        port=5555,            # The "door" to use
        application=application # The function to run
    )