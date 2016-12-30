from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor, endpoints
from json import loads


class Launch(Resource):
    def render_POST(self, request):
        return 'launch'


class StartMission(Resource):
    def render_POST(self, request):
        request_data = loads(request.content.getvalue())
        return str(request_data['mission_plan'])


class CancelMission(Resource):
    def render_POST(self, request):
        return 'cancel'


class RTL(Resource):
    def render_POST(self, request):
        return 'rtl'


def start_server():
    root = Resource()
    root.putChild('launch', Launch())
    root.putChild('start_mission', StartMission())
    root.putChild('cancel_mission', CancelMission())
    root.putChild('rtl', RTL())
    factory = Site(root)
    endpoint = endpoints.TCP4ServerEndpoint(reactor, 8000)
    endpoint.listen(factory)
    reactor.run()


def start_drone_things():
    # create pilot/navigator thread
    # should expect to receive navigator object back
    # so that it can call functions like rtl
    # create air sensor thread
    # create logging thread
    pass


if __name__ == '__main__':
    start_server()
    start_drone_things()
