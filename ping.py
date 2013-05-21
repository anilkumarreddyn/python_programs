#SD
#Ping program. Ping starts from ip .1 to .<ip_range>. ping_count is the number of ping packets sent
#!/usr/bin/python

import os 
import sys
import re
import subprocess

try:
  hostname, count, ip_range = sys.argv[1:]
except :
  print "Usage : python ping.py 192.168.1.x <ping_count> <ip_range>"
  sys.exit(2)

int_range = int(ip_range)
ip1,ip2,ip3,ip4 = re.split('\.', hostname)
host_alive = str(' ')
host_dead = str(' ')
ping_match_string = str(count+' received')

for x in range(1,int_range):
    ip_addr = str(ip1+'.'+ip2+'.'+ip3+'.'+`x`)
    ping_cmd = str("ping -c " + count + " " + ip_addr)
    ping_out=subprocess.Popen(ping_cmd, shell = True, stdout = subprocess.PIPE)
    ping_last = ping_out.stdout.read().splitlines()
    ping_temp = re.split('\,\s',ping_last[len(ping_last)-2])
    pkts_received, text = re.split('\s',ping_temp[1])
    if (ping_temp[1] == ping_match_string):
        arp_cmd = str("arp -a " + ip_addr)
        arp_out = subprocess.Popen(arp_cmd, shell = True, stdout = subprocess.PIPE)
	arp = re.split('\s', arp_out.stdout.read())
	ip_hname = str(ip_addr+' is Alive. ')        
	hname = str('Hostname: '+arp[0]+'. ')
	mac = str('MAC: '+arp[3]+'. ')
        iface = str('Interface: '+arp[6]+'. ')         
	print '\nHost Alive. %-30s%-50s%s  %s' % (ip_hname, hname, mac, iface)
    else: 
	print '\nHost Dead. '+str(ip_addr+' is currently down. Sent '+count+' packets. Received '+pkts_received+' packets')


