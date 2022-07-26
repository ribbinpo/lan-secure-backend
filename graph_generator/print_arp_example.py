import dpkt
from dpkt.compat import compat_ord
import datetime
import socket

def inet_to_str(inet):
    """Convert inet object to a string

        Args:
            inet (inet struct): inet network address
        Returns:
            str: Printable/readable IP address
    """
    # First try ipv4 and then ipv6
    try:
        return socket.inet_ntop(socket.AF_INET, inet)
    except ValueError:
        return socket.inet_ntop(socket.AF_INET6, inet)

def mac_addr(address):
    """Convert a MAC address to a readable/printable string

       Args:
           address (str): a MAC address in hex form (e.g. '\x01\x02\x03\x04\x05\x06')
       Returns:
           str: Printable/readable MAC address
    """
    return ':'.join('%02x' % compat_ord(b) for b in address)

f = open('a004_20220201_000002.pcap','rb')
pcap = dpkt.pcap.Reader(f)

# For each packet in the pcap process the contents
for timestamp, buf in pcap:

     # Unpack the Ethernet frame (mac src/dst, ethertype)
     eth = dpkt.ethernet.Ethernet(buf)

     # Now check if this is an ARP packet
     if eth.type == dpkt.ethernet.ETH_TYPE_ARP:
         arp = eth.arp

         # Extract related info
         src_ipstr = socket.inet_ntoa(arp.spa)
         dst_ipstr = socket.inet_ntoa(arp.tpa)
         type = arp.op  # REQUEST-1, REPLY-2
         typestr = 'REQUEST' if type == 1 else 'REPLY'

         # Print out the info
         print('Timestamp: ', str(datetime.datetime.utcfromtimestamp(timestamp)))
         print('Ethernet Frame: ', mac_addr(eth.src), mac_addr(eth.dst), eth.type)
         print('ARP: %s -> %s (type=%s)' % (src_ipstr,dst_ipstr,typestr))
         print('')