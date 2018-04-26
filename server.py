"""
import cherrypy
from app import app

cherrypy.tree.graft(app, '/')

cherrypy.config.update({
        'engine.autoreload_on': True,
        'log.screen': True,
        'server.socket_port': 5000,
        'server.socket_host': '127.0.0.1',
    })


if __name__ == '__main__':
    cherrypy.engine.start()
    cherrypy.engine.block()
"""

from cheroot.wsgi import Server, PathInfoDispatcher
from app import app

address = '127.0.0.1', 5000
dispatcher = PathInfoDispatcher({'/': app})
server = Server(address, dispatcher)

if __name__ == '__main__':
    try:
        print(f'* Cheroot server starting at {address} ...')
        server.start()
    except KeyboardInterrupt:
        server.stop()
        print('* Cheroot server stopped')
    except Exception as e:
        print(e)
