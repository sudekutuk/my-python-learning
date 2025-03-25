# from scapy.all import sniff

# def paket_yakala(paket):
#     print(paket.summary())
from scapy.all import sniff, IP, TCP, UDP, ARP

def paketleri_yakala(paket):
    if IP in paket:
        print(f"IP Paketi: {paket[IP].src} -> {paket[IP].dst}")
    if TCP in paket:
        print(f"TCP Port: {paket[TCP].sport} -> {paket[TCP].dport}")
    if UDP in paket:
        print(f"UDP Port: {paket[UDP].sport} -> {paket[UDP].dport}")
    if TCP in paket:
        print(f"ARP Paketi: {paket[ARP].psrc} -> {paket[ARP].pdst}")

sniff(filter = "ip" , prn=paketleri_yakala, count=10)