from flask import Flask


app = Flask(__name__)
#TEMPLATE_PATH.insert(0, './templates')
#view = functools.partial(jinja2_view, template_lookup=['templates'])

@app.route('/hello/<name>')   #127.0.0.1:8080/hello/dominic
def hello(name):
	return template('<b>Hello {{name}}</b>!', name=name)

@app.route('/')
def index():
	#return template('index.html')
	#raise html('index.html')
	return '<b> This is page without a template</b>'

@app.route('/parp/<number>')
def blogdetail(number):
	pass
	#return template('<h3>Routing provided by bottle for blog {{number}}</h3>!', number=number)

# @app.route("/templates/<filepath:re:.*\.html>")
# def html(filepath):
# 	return static_file(filepath, root="./templates")
#
# @app.route("/css/<filepath:re:.*\.css>")
# def css(filepath):
# 	return static_file(filepath, root="./css")
#
# @app.route("/js/<filepath:re:.*\.js>")
# def js(filepath):
# 	return static_file(filepath, root="./js")


#run(host='localhost', port=8080, reloader=True, debug=True)

if __name__ == '__main__':
	app.run()
