from bottle import route, run
from bottle import request

@route('/hello')
def hello():
    return request.environ.get("REMOTE_ADDR")


run(host='0.0.0.0', port=8080, debug=True)
