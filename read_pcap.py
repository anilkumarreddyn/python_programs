#SD
#This program reads PCAP and packet info. Mention an IP and it will look for all packets with that IP in the PCAP and displays TCP, HTTP, UDP count. You will need dpkt module to run this program. 
#http://code.google.com/p/dpkt/
#!/usr/bin/python 


import socket
import dpkt
import sys
import re
import sys
import math
from optparse import OptionParser

def getArguments():
  parser = OptionParser()
  parser.add_option("-f", "--pcapFile", dest="pcapFile",
                  help="PCAP filename", metavar="FILE")
  parser.add_option("-i", "--ueIp", dest="ueIp",
                  help="UE IP address in PCAP", metavar="10.10.10.1")
  parser.add_option("-s", "--serverIpList", dest="serverIpList",
                  help="Optional : Server IP address List in PCAP", metavar="172.10.10.1,192.168.1.23 -- code not there")
  (options, args) = parser.parse_args()

  if ((options.pcapFile == None) or (options.ueIp == None)):
    print "For help use -h or --help"
    sys.exit(2)
  else :
    pcapFile =  options.pcapFile
    ueIp = options.ueIp
    serverIpList = options.serverIpList
  return pcapFile, ueIp, serverIpList

def readPacket(ipProto, ipLen, srcPort, destPort):
  packetDict = {}
  if ipProto == 6:
    packetDict['1tcpPacket'] = 1
    packetDict['2tcpPacketLen'] = ipLen
    if srcPort == 80 or destPort == 80 :
      packetDict['3httpPacket'] = 1
      packetDict['4httpPacketLen'] = ipLen
  elif ipProto == 17:
    packetDict['5udpPacket'] = 1
    packetDict['6udpPacketLen'] = ipLen
    if srcPort == 53 or destPort == 53:
      packetDict['7dnsPacket'] = 1
      packetDict['8dnsPacketLen'] = ipLen
  else: 
    packetDict['9unknownPacket'] = 1
    packetDict['10unknownPacketLen'] = ipLen  
  return packetDict

def readPcap(ueIp, pcapFileName):
  try : 
    pcapReader = dpkt.pcap.Reader(file(pcapFileName, "rb"))
  except: 
    print "Cannot open file"
    sys.exit(2)
  pcapDict = {}
  i = 1
  for ts, data in pcapReader:
    ether = dpkt.ethernet.Ethernet(data)
    if ether.type != dpkt.ethernet.ETH_TYPE_IP: 
      #print "Not an IP packet -- > Packet # %s" % (i)
      i = i+1
    else: 
      ip = ether.data
      ip_data = ip.data
      packetDict = {}
      if ueIp == socket.inet_ntoa(ip.src) or ueIp == socket.inet_ntoa(ip.dst):
        packetDict = readPacket(ip.p,ip.len,ip_data.sport, ip_data.dport)
        for dict in packetDict:
          if dict not in pcapDict:
            pcapDict[dict] = packetDict[dict]
          else : 
            pcapDict[dict] += packetDict[dict]
      else : 
        #print "Not a UE packet --> packet # %s" % (i)
        i = i+1
  
  if pcapDict.keys() == [] :
    print "No Packets with UE IP found" 
  else : 
    for dict in sorted(pcapDict.keys()):
      print dict,"---->",pcapDict[dict]
 
def main():
  (pcapFile, ueIp, serverIpList) = getArguments()    
  print "UE IP --> %s" % ueIp
  print "PCAP location --> %s" % pcapFile

  if serverIpList == None :
    print "No server IPs given"
    readPcap(ueIp, pcapFile)
  else : 
    serverIp = []
    serverIp = re.split(',',serverIpList)
    for sIp in serverIp: 
      print "Sever IP --> %s" % sIp
    readPcap(ueIp,pcapFile)
    print "-s Code not there yet"

if __name__ == '__main__':
  main()

