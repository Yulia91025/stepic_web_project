def wsgi_application(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    body = ''
    for string in environ['QUERY_STRING'].split('&'):
        body = body + string + '\n'
    start_response(status, headers)
    return [body]