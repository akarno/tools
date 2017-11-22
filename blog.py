import requests

class Blogsx:
    def __init__(self, name):
        self.name = name

    def req_get(self, uri, **kwargs):
        return requests.Session().get(uri, **kwargs)

    def posts(self, uri, **kwargs):
        while True:
            try:
                response = self.req_get(uri, **kwargs)
                break
            except requests.ConnectionError:
                print('AAA\n')

        return response

    def __repr__(self):
        return '<Blog: {}>'.format(self.name)