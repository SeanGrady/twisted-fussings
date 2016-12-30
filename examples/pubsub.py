import json
from collections import defaultdict
from twisted.internet import reactor, protocol, endpoints
from twisted.protocols import basic

class PubProtocol(protocol.Protocol):
    def __init__(self, factory):
        self.factory = factory

    #def connectionLost(self, reason):
    #    self.factory.clients.remove(self)

    def dataReceived(self, data):
        request = json.loads(data)
        command = request['command']
        topic = request['topic']
        if command == 'publish':
            for function in self.factory.topics[topic]:
                function(request['data'])
        elif command == 'subscribe':
            self.factory.topics[topic].add(request['function'])

class PubFactory(protocol.Factory):
    def __init__(self):
        self.topics = defaultdict(set)

    def buildProtocol(self, addr):
        return PubProtocol(self)

endpoints.serverFromString(reactor, 'tcp:8001').listen(PubFactory())
reactor.run()
