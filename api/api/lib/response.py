import json
from pyramid.response import Response


def bad_request(message=None, errors=None):
    msg = message or "HTTPBadRequest"
    return Response(body=json.dumps({'message': msg,
                                     'errors': errors}),
                    status='400 - HTTPBadRequest',
                    status_code=400,
                    content_type='application/json')


def unauthorized(message=None, ext_info=None):
    msg = message or "HTTPUnauthorized"
    return Response(body=json.dumps({'message': msg}),
                    status='401 - Unauthorized',
                    status_code=401,
                    content_type='application/json')


def forbidden(message=None):
    msg = message or "HTTPForbidden"
    return Response(body=json.dumps({'message': msg}),
                    status='403 - HTTPForbidden',
                    status_code=403,
                    content_type='application/json')


def not_found(message=None):
    msg = message or "HTTPNotFound"
    return Response(body=json.dumps({'message': msg}),
                    status='404 - HTTPNotFound',
                    status_code=404,
                    content_type='application/json')


def conflict(message=None):
    msg = message or "HTTPConflict"
    return Response(body=json.dumps({'message': msg}),
                    status='409 - HTTPConflict',
                    status_code=409,
                    content_type='application/json')
