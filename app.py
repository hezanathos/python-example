import bottle
from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='http://python-example-dnns8457.kermit.itn.intraorange/', port=8080)