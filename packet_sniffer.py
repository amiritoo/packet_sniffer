import scapy.all as scapy

def sniff(interface):
    scapy.sniff(iface="wlp58s0",store=False,prn=sniffed_packet)

def sniffed_packet(packet):
    print(packet)

sniff("wlp58s0")