import html
import traceback

import psycopg2

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPClientError, HTTPServerError

@view_config(context=Exception, renderer='templates/exceptions.jinja2')
def uncaught_exception(exc, request):
    return {'error_type': 'Server error',
            'error_messages': ['<strong>%s</strong>: %s' % (exc.__class__.__name__, html.escape(str(exc)).replace('\n','<br>'))],
            'technical_messages': ['\n'.join(traceback.format_exception(exc.__class__,exc,exc.__traceback__))]}

@view_config(context=HTTPClientError, renderer='templates/exceptions.jinja2')
def user_http_error(exc, request):
    return {'error_type': 'Error: %s %s' % (exc.code, exc.title),
            'error_messages': [exc.explanation, exc.detail],
            'technical_messages': []}

@view_config(context=HTTPServerError, renderer='templates/exceptions.jinja2')
def server_http_error(exc, request):
    return {'error_type': 'Server error: %s %s' % (exc.code, exc.title),
            'error_messages': [exc.explanation, exc.detail],
            'technical_messages': ['\n'.join(traceback.format_exception(exc.__class__,exc,exc.__traceback__))]}

@view_config(context=psycopg2.Error, renderer='templates/exceptions.jinja2')
def database_exception(exc, request):
    result = uncaught_exception(exc, request)
    result['error_type'] = 'Database error'
    if exc.cursor and exc.cursor.query:
        result['technical_messages'].insert(0, '<strong>SQL Query:</strong><br>%s' % exc.cursor.query.decode())
    return result