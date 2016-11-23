def application(environ, start_response):
	
	status = '200 OK'
	headers = [ ('Content-type', 'text/plain')]
	qs = environ['QUERY_STRING'].split('&')
	start_response(status, headers)
	qs = [item.encode('utf-8')+b"\n" for item in qs]
	return qs