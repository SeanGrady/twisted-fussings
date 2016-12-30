from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor, endpoints
from json import loads


class Something(Resource):
    def render_GET(self, request):
        return 'something'

    def render_POST(self, request):
        request_data = loads(request.content.getvalue())
        return str(request_data['something'])

root = Resource()
root.putChild("something", Something())
factory = Site(root)
endpoint = endpoints.TCP4ServerEndpoint(reactor, 8880)
endpoint.listen(factory)
reactor.run()
