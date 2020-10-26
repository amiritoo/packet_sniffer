import scapy.all as scapy
from scapy.layers import http
def sniff(interface):
    scapy.sniff(iface="wlp58s0",store=False,prn=sniffed_packet)

def sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
         if packet.haslayer(scapy.Raw):
            print(packet[scapy.Raw].load)

sniff("wlp58s0")