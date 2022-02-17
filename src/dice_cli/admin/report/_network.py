import ipaddress

import nmap

from dice_cli.admin.report import network


# def __scan_ip(ip_address: str) -> None:
#     # ip = ipaddress.ip_address(ip_address)
#     ip = ip_address

#     arp_req_frame = scapy.ARP(pdst=ip)
#     broadcast_ether_frame = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
#     arp_req_broadcast_frame = broadcast_ether_frame / arp_req_frame
#     answered_list = scapy.srp(arp_req_broadcast_frame, timeout=1, verbose=False)[0]

#     print(answered_list.summary())


def _scan_network(ip_network: str) -> None:

    nm = nmap.PortScanner()
    nm.scan(hosts=ip_network, arguments="-sP")
    all_hosts = nm.all_hosts()
    all_ips = [ipaddress.ip_address(h) for h in all_hosts]
    #TODO: add DHCP discovery to list "down" IPs
    for host in sorted(all_ips):
        print(nm[str(host)])
        # print(host, nm[str(host)]['status']['state'])

    return all_hosts
