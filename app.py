from flask import Flask, render_template


app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
	return render_template('<b>Hello {{name}}</b>!', name=name)

@app.route('/')
def index():
	return render_template('index.html')
	#raise html('index.html')
	#return '<b> This is page without a template</b>'

@app.route('/parp/<number>')
def blogdetail(number):
	pass
	#return template('<h3>Routing provided by flask for blog {{number}}</h3>!', number=number)

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
