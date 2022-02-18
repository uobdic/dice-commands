import ipaddress
from typing import Any, Dict, List, Optional, Union

import dns.resolver
import dns.reversename
import nmap
from plumbum import ProcessExecutionError, local

from dice_cli.cache import admin_cache
from dice_cli.logger import admin_logger


@admin_cache.memoize(expire=60 * 15, tag="_ip_to_fqdn")
def _ip_to_fqdn(
    ip_address: Union[ipaddress.IPv4Address, ipaddress.IPv6Address]
) -> Optional[str]:
    host_name: Optional[str] = None
    address = dns.reversename.from_address(str(ip_address))
    try:
        host_name = dns.resolver.query(address, "PTR")[0].to_text()
    except dns.resolver.NXDOMAIN:
        admin_logger.debug(f"No DNS entry for {ip_address}")

    return str(host_name)


@admin_cache.memoize(expire=60 * 15, tag="_get_dns_hosts")
def _get_dns_hosts(ip_network: str) -> List[Dict[str, str]]:
    network = ipaddress.ip_network(ip_network)
    all_ips = list(network.hosts())
    dns_hosts = []
    dns_entries = [_ip_to_fqdn(ip) for ip in all_ips]

    for entry, ip in zip(dns_entries, all_ips):
        if entry is None:
            continue
        dns_hosts.append({"fqdn": entry, "ipv4": str(ip)})

    return dns_hosts


@admin_cache.memoize(expire=60 * 15, tag="_get_all_active_ips")
def _get_all_active_ips(ip_network: str) -> List[Dict[str, str]]:
    admin_logger.debug(f"Scanning network {ip_network}")
    nm = nmap.PortScanner()
    nm.scan(hosts=ip_network, arguments="-sP")
    all_hosts = nm.all_hosts()
    all_ips = [ipaddress.ip_address(h) for h in all_hosts]
    admin_logger.debug(f"Found {len(all_ips)} active IPs in {ip_network}")
    # example = {'hostnames':
    # [
    #     {'name': '<hostname>', 'type': 'PTR'}
    # ],
    # 'addresses': {'ipv4': '<ipv4>'},
    # 'vendor': {},
    # 'status': {'state': 'up', 'reason': 'syn-ack'}
    # }
    result = []
    for host in sorted(all_ips):
        host_info = nm[str(host)]
        admin_logger.debug(f"{host} | {host_info['status']['state']}")
        result.append(
            dict(
                name=host_info["hostnames"][0]["name"],
                ipv4=host_info["addresses"]["ipv4"],
                status=host_info["status"]["state"],
            )
        )

    return result


def _scan_network(ip_network: str) -> List[Dict[str, Any]]:
    # get all IP addresses in the network
    # check DNS entries for all IP addresses
    # ping all DNS records
    # check if anything NOT in DNS responds to ping
    dns_hosts: List[Dict[str, str]] = _get_dns_hosts(ip_network)
    ping_once = local["ping"]["-c", "1", "-W", "1"]

    for host in dns_hosts:
        try:
            ping_once(host["ip"])
            status = "UP"
        except ProcessExecutionError:
            status = "DOWN"
        admin_logger.debug(f"{host['fqdn']} responded: {status}")
        host["status"] = status

    # all_active_ips = _get_all_active_ips(ip_network)

    # get IPv6 for all active IPs
    # print(all_active_ips)

    return dns_hosts
