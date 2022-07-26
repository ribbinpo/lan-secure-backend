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

    # Make sure the Ethernet frame contains an IP packet
    if not isinstance(eth.data, dpkt.ip.IP):
        continue

    # Now unpack the data within the Ethernet frame (the IP packet)
    ip = eth.data

    # Pull out fragment information (flags and offset all packed into off field, so use bitmasks)
    do_not_fragment = bool(ip.off & dpkt.ip.IP_DF)
    more_fragments = bool(ip.off & dpkt.ip.IP_MF)
    fragment_offset = ip.off & dpkt.ip.IP_OFFMASK

    # Now check if this is an TCP packet
    if isinstance(ip.data, dpkt.tcp.TCP):
        tcp = ip.data

        # Extract related info
        fin_flag = (tcp.flags & dpkt.tcp.TH_FIN) != 0
        syn_flag = (tcp.flags & dpkt.tcp.TH_SYN) != 0
        rst_flag = (tcp.flags & dpkt.tcp.TH_RST) != 0
        psh_flag = (tcp.flags & dpkt.tcp.TH_PUSH) != 0
        ack_flag = (tcp.flags & dpkt.tcp.TH_ACK) != 0
        urg_flag = (tcp.flags & dpkt.tcp.TH_URG) != 0
        ece_flag = (tcp.flags & dpkt.tcp.TH_ECE) != 0
        cwr_flag = (tcp.flags & dpkt.tcp.TH_CWR) != 0

        # Now check if this is an TCP SYN packet
        if syn_flag == False: continue
        if ack_flag == True: continue

        src_port = tcp.sport
        dst_port = tcp.dport
        seq_number = tcp.seq
        ack_number = tcp.ack

        # Print out the info
        print('Timestamp: ', str(datetime.datetime.utcfromtimestamp(timestamp)))
        print('Ethernet Frame: ', mac_addr(eth.src), mac_addr(eth.dst), eth.type)
        print('IP: %s -> %s (len=%d ttl=%d DF=%d MF=%d offset=%d)' % \
            (inet_to_str(ip.src), inet_to_str(ip.dst), ip.len, ip.ttl, do_not_fragment, more_fragments, fragment_offset))
        print('TCP SYN: %d -> %d (seq=%d ack=%d)\n' % (src_port,dst_port,seq_number,ack_number))






