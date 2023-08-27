from mininet.topo import Topo

class custom_topo(Topo):
    def __init__(self):
        Topo.__init__(self)

        hosts = [None for _ in range(16)]
        switches = [None for _ in range(12)]

        for i in range(1, 12):
            switches[i] = self.addSwitch("s" + str(i))

        for i in range(1, 16):
            hosts[i] = self.addHost("h" + str(i))

        self.addLink(switches[1], switches[2])
        self.addLink(switches[2], switches[3])
        self.addLink(switches[3], switches[4])
        self.addLink(switches[4], switches[5])

        self.addLink(switches[1], switches[6])
        self.addLink(switches[1], switches[7])

        self.addLink(switches[3], switches[8])
        self.addLink(switches[3], switches[9])

        self.addLink(switches[5], switches[10])
        self.addLink(switches[5], switches[11])
        self.addLink(switches[6], switches[8])
        self.addLink(switches[8], switches[10])
  

        self.addLink(switches[2], hosts[1])
        self.addLink(switches[2], hosts[2])
        self.addLink(switches[4], hosts[3])

        self.addLink(switches[6], hosts[4])
        self.addLink(switches[6], hosts[5])

        self.addLink(switches[7], hosts[6])
        self.addLink(switches[7], hosts[7])

        self.addLink(switches[8], hosts[8])
        self.addLink(switches[8], hosts[9])
 

        self.addLink(switches[9], hosts[10])
        self.addLink(switches[9], hosts[11])

        self.addLink(switches[10], hosts[12])
        self.addLink(switches[10], hosts[13])

        self.addLink(switches[11], hosts[14])
        self.addLink(switches[11], hosts[15])



topos = { 'mytopo' : ( lambda : custom_topo()) }
