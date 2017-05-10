from scapy.all import *

target = "8.8.8.8"

#ping = IP(dst= target, ttl=(1,25),id=RandShort())/ ICMP()
#ping = IP(dst= target, ttl=(1,25))/ ICMP()
p_80 = IP(dst= target, ttl=(1,25),id=RandShort())/ TCP(sport=RandShort(), dport=80, flags=0x2)
p_53 = IP(dst= target, ttl=(1,25),id=RandShort())/ TCP(sport=RandShort(), dport=53, flags=0x2)


ans, unans = sr(p_53, timeout=2)

ans.summary()
print

for snd, rcv in ans:
    print snd.ttl, rcv.src, isinstance(rcv.payload, TCP)

print ("-------------------------------------------------------------------------")
ans,unans=traceroute(target, maxttl=20)

print ("\n DNS-------------------------------------------------------------------------")
ans,unans=traceroute(target, l4=UDP(sport=RandShort())/DNS(qd=DNSQR(qname="www.tudelft.nl")))
