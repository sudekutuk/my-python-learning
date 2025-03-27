from scapy.all import sniff
import time

sure = 5  
sinir_degeri = 100
paket_sayisi = 0
starting_time = time.time()

def paketleri_yakala(paket):
    global paket_sayisi, starting_time

   
    current_time = time.time()
    if current_time - starting_time > sure:
     
        print(f"{sure} saniyede gelen paket sayısı: {paket_sayisi}")
        if paket_sayisi > sinir_degeri:
            print("Olası saldırı tespit edildi!")
        paket_sayisi = 0
        starting_time = current_time

   
    paket_sayisi += 1

print("Ağ trafiği izleniyor... (Çıkmak için CTRL+C)")
sniff(prn=paketleri_yakala)