""" utility functions for working with network interfaces """


import os
import socket
import fcntl
import struct


def get_mac_address(ifname):
    """
    get hardware address from network interface name

    source: https://gist.github.com/zhenyi2697/6080400
    """
    if not is_available(ifname):
        return False
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(sock.fileno(), 0x8927, struct.pack('256s', ifname[:15]))
    return ''.join(['%02x:' % ord(char) for char in info[18:24]])[:-1]


def is_available(interface):
    """ check if interface provided by name exists """
    network_interfaces = os.listdir('/sys/class/net/')
    if interface not in network_interfaces:
        return False
    return True
