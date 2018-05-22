import re
from rest_framework.status import is_client_error, is_success


class ResponseFormattingMiddleware:
    METHOD = ('GET', 'POST', 'PUT', 'PATCH', 'DELETE')

    def __init__(self, get_response):
        self.get_response = get_response
        self.API_URLS = [
            re.compile(r'^api'),
        ]

    def __call__(self, request):
        response = None
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response

    def process_response(self, request, response):
        path = request.path_info.lstrip('/')
        if request.method in self.METHOD and any(url.match(path) for url in self.API_URLS):
            response_format = {
                'result': {},
                'success': is_success(response.status_code),
                'message': None
            }

            if hasattr(response, 'data') and getattr(response, 'data') is not None:
                data = response.data
                try:
                    response_format['message'] = data.pop('message')
                except KeyError:
                    response_format.update({'result': data})
                except TypeError:
                    response_format.update({'result': data})
                finally:
                    if is_client_error(response.status_code):
                        response_format['result'] = None
                        response_format['message'] = data

                response.data = response_format
                response.content = response.render().rendered_content
            else:
                response.data = response_format

        return response
