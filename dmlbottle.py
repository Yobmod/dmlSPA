from bottle import Bottle, jinja2_view, Jinja2Template, url, route, run, template, get, post, request, static_file, response, debug
import functools
import beaker

app = Bottle()
view = functools.partial(jinja2_view, template_lookup=['templates'])

@route('/hello/<name>')   #127.0.0.1:8080/hello/dominic
def hello(name):
	return template('<b>Hello {{name}}</b>!', name=name)

@route('/')
def index():
	return template('index.html')

@get("/templates/<filepath:re:.*\.html>")
def html(filepath):
	return static_file(filepath, root="./templates")

@get("/css/<filepath:re:.*\.css>")
def css(filepath):
	return static_file(filepath, root="./css")

@get("/js/<filepath:re:.*\.js>")
def js(filepath):
	return static_file(filepath, root="./js")


run(host='localhost', port=8080, reloader=True, debug=True)
