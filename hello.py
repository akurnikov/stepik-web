def app(environ, start_responce):
	data = environ['QUERY_STRING'].split('&')
	status = '200 OK'
	headers = [('Content-Type', 'text/plain')]
	start_responce(status, headers)
	return '\n'.join(data)