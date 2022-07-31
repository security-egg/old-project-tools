from scapy.all import *
import optparse
import os


ip_list = []

def scan():
	arp_request = ARP(pdst=ip)
	broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_request_broadcast = broadcast/arp_request
	answered_list = srp(arp_request_broadcast, timeout=1)[0]
	for element in answered_list:
		ip_list.append(element[1].psrc)
	for element in ip_list:
		print(element)
	
def rename():
	ip_list.remove("172.19.0.1")
	ip_list.remove("172.19.0.5")
	for target_ip, filename in zip(ip_list,os.listdir("/project/wordlists")):
		dst = target_ip
		src = "/project/wordlists/" + filename
		dst = "/project/wordlists/" + dst
		print("Renaming file " + src + "to " + dst) 
		os.rename(src,dst)


parser = optparse.OptionParser()

parser.add_option("-t","--target",dest="ip",help="set target's ip")
(options,arguments) = parser.parse_args()

ip = options.ip

scan()
rename()
