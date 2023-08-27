import httplib
import json
 
class StaticEntryPusher(object):
    def __init__(self, server):
        self.server = server
 
    def get(self, data):
        ret = self.rest_call({}, 'GET')
        return json.loads(ret[2])
 
    def set(self, data):
        ret = self.rest_call(data, 'POST')
        return ret[0] == 200
 
    def remove(self, objtype, data):
        ret = self.rest_call(data, 'DELETE')
        return ret[0] == 200
 
    def rest_call(self, data, action):
        path = '/wm/staticentrypusher/json'
        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
            }
        body = json.dumps(data)
        conn = httplib.HTTPConnection(self.server, 8080)
        conn.request(action, path, body, headers)
        response = conn.getresponse()
        ret = (response.status, response.reason, response.read())
        print ret
        conn.close()
        return ret
 

pusher = StaticEntryPusher('127.0.0.1')


sources_and_destinations = [
    ('06', '15'),
    ('03', '04'),
    ('01', '12')
]
switches_in_the_path = [
    ('07','01','06','08','0a','05','0b'),
    ('04','03','02','01','06'),
    ('02','03','08','0a')
]
in_ports = [
    ('2','3','1','2','2','2','1'),
    ('3', '2', '2','1','1'),
    ('3', '1', '1','2')
]
out_ports = [
    ('1','2','2','3','1','3','3'),
    ('1', '1', '1','2','3'),
    ('2', '3', '3','3')
]


flows = list(list())

for i in range(3):
    flows.append(list())
    for j in range(len(switches_in_the_path[i])):
        flows[i].append(None)

for i in range(3):
    for j in range(len(switches_in_the_path[i])):
        flows[i][j] = {
            'switch': '00:00:00:00:00:00:00:' + switches_in_the_path[i][j],
            'name': 'flow' + str(i) + '.' + str(j),
            'eth_type': '0x0800',
            'ipv4_src': '10.0.0.' + sources_and_destinations[i][0],
            'ipv4_dst': '10.0.0.' + sources_and_destinations[i][1],
            'priority': '32768',
            'in_port': in_ports[i][j],
            'active': 'true',
            'actions': 'output=' + out_ports[i][j]
        }

for i in range(3):
    flows.append(list())
    for j in range(len(switches_in_the_path[i])):
        print flows[i][j]
 

for i in range(3):
    for j in range(len(switches_in_the_path[i])):
	   pusher.set(flows[i][j])
 
