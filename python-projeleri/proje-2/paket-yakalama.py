from collections import defaultdict
from scapy.all import sniff
import time
import logging

logging.basicConfig(filename="attack_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")


sure = 5  
sinir_degeri = 100
paket_sayisi = 0
starting_time = time.time()
ip_sayac = defaultdict(int)
protokol_sayaci = {"TCP": 0,"UDF": 0, "ICMP": 0}
blacklist = set()


def logla(mesaj):
    with open("attack_log.txt","a") as dosya:
        dosya.write(f"{time.ctime()} - {mesaj}")



def paketleri_yakala(paket):
    global paket_sayisi, starting_time,ip_sayac, protokol_sayaci,blacklist

   
    current_time = time.time()
    if current_time - starting_time > sure:
        
        en_cok_gonderilen_ip = max(ip_sayac, key = ip_sayac.get, default="bilinmiyor")


        print(f"{sure} saniyede gelen paket sayısı: {paket_sayisi}")
        print(f"en cok gonderilen ip: {en_cok_gonderilen_ip}")
        print(f"TCP: {protokol_sayaci['TCP']},UDF: {protokol_sayaci['UDF']},ICMP: {protokol_sayaci['ICMP']}")
        if paket_sayisi > sinir_degeri:
            mesaj = print(f"Olası saldırı tespit edildi! {paket_sayisi} paket alindi. en cok trafik {en_cok_gonderilen_ip}den geldi")
            print(mesaj)
            logla(mesaj)
            blacklist.add(en_cok_gonderilen_ip)

        paket_sayisi = 0
        ip_sayac.clear()
        protokol_sayaci = {"TCP": 0,"UDF": 0, "ICMP": 0}
        starting_time = current_time
   
    paket_sayisi += 1

    if paket.haslayer("IP"):
        src_ip = paket["IP"].src
        ip_sayac[src_ip] += 1

        if src_ip in blacklist:
            print(f"⚠️ Şüpheli IP algılandı: {src_ip}")
            logla(f"Şüpheli IP algılandı: {src_ip}")

    if paket.haslayer("TCP"):
        protokol_sayaci["TCP"] += 1
    elif paket.haslayer("UDF"):
        protokol_sayaci["UDF"] += 1
    elif paket.haslayer("ICMP"):
        protokol_sayaci["ICMP"] += 1

print("Ağ trafiği izleniyor... (Çıkmak için CTRL+C)")
sniff(prn=paketleri_yakala)