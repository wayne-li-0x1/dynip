from bottle import route, run
from bottle import request

@route('/get_my_ip')
def get_my_ip():
    return request.environ.get("REMOTE_ADDR")

@route('/get_my_ip.json')
def get_my_ip_json():
    clientip = request.environ.get("REMOTE_ADDR")
    return {"ip":clientip}

@route('/env')
def get_env():
    import json
    d = {}	
    ks = list(request.environ)
    s = ""
    ks.sort()
    for k in ks:
        s = s + "%s : %s\n"%(k, request.environ[k])
    from bottle import response
    response.content_type='text/plain'
    return s
     
     


run(host='0.0.0.0', port=8080, debug=True)
