from flask import request, jsonify, make_response
import functools

valid_hosts = ['https://to.tmcd.me/', 'http://to.tmcd.me/']

def validate_host(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if request.url_root in valid_hosts or 'http://localhost' in request.url_root:
            return func(*args, **kwargs)
        else:
            print('URL:', request.url_root)
            res_data = {
                'message': 'Unrecognized Host'
            }
            return make_response(jsonify(res_data), 400)
    return wrapper