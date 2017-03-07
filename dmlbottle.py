from bottle import Bottle, route, run, template, get, post, request, static_file, response, debug

app = Bottle()

@route('/hello/<name>')   #127.0.0.1:8080/hello/dominic
def hello(name):
	return template('<b>Hello {{name}}</b>!', name=name)

@route('/')
def index():
	return template('index.html')

@get("/css/<filepath:re:.*\.css>")
def css(filepath):
	return static_file(filepath, root="./css")

@get("/js/<filepath:re:.*\.js>")
def js(filepath):
	return static_file(filepath, root="./js")


run(host='localhost', port=8080, reloader=True, debug=True)
