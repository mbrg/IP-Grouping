"""
IP Manipulation functions
- String, Decimal and Binary format transformations
- Astrix notation
- Binary Intervals utils

Author: mibarg
"""

import math


''' IP Conversions '''

def IpStringToDecimal(str_ip):
    """
    :param str_ip: IPv4 in string notation, e.g. 10.0.0.1
    :return:  IPv4 in decimal notation, e.g. 167772161
    """
    classes = str_ip.split('.')
    assert len(classes)==4

    return \
        int(classes[0]) * pow(256,3)  + \
        int(classes[1]) * pow(256, 2) + \
        int(classes[2]) * pow(256, 1) + \
        int(classes[3]) * pow(256, 0)

def IpDecimalToString(dec_ip):
    """
    :param str_ip: IPv4 in decimal notation, e.g. 167772161
    :return: IPv4 in string notation, e.g. 10.0.0.1
    """
    class_a = math.floor((dec_ip                                                               ) / pow(256, 3))
    class_b = math.floor((dec_ip - class_a*pow(256,3)                                          ) / pow(256, 2))
    class_c = math.floor((dec_ip - class_a*pow(256,3) - class_b*pow(256,2)                     ) / pow(256, 1))
    class_d = math.floor((dec_ip - class_a*pow(256,3) - class_b*pow(256,2) - class_c*pow(256,1)) / pow(256, 0))

    return '%d.%d.%d.%d' % (class_a, class_b, class_c, class_d)


def IpDecimalToBinary(decimal_ip, binary_size=32):
    """
    :param decimal_ip: IPv4 in decimal notation, e.g. 167772161
    :param binary_size: IP size in binary, default is 32 for IPv4
    :return: IPv4 in binary notation, e.g. 00001010000000000000000000000001
    """
    return ('0'*binary_size + bin(decimal_ip)[2:])[-binary_size:]


def IpBinaryToDecimal(bin_ip):
    """
    :param bin_ip: IPv4 in binary notation, e.g. 00001010000000000000000000000001
    :return: IPv4 in decimal notation, e.g. 167772161
    """
    return int(bin_ip, 2)


''' Astrix notation and Binary Intervals '''

def RangeBitDiff(start, end):
    """
    :param start: IPv4 in decimal notation
    :param end: IPv4 in decimal notation
    :return: size(start) - (longest shared substring of most significant bits for start, end)
    """
    return math.floor(math.log(start ^ end,2)+1) if start!=end else 0


def BinaryIntervalLen(astrix_ip):
    """
    :param astrix_ip: IPv4 range in astrix notation
    :return: range length
    """
    return IpBinaryToDecimal(astrix_ip.replace('*', '1')) - IpBinaryToDecimal(astrix_ip.replace('*', '0')) + 1


def GetSlashNotation(astrix_ip, binary_size=32):
    """
    :param astrix_ip: IPv4 range in astrix notation
    :param binary_size: IP size in binary, default is 32 for IPv4
    :return: IPv4 range in slash notation
    """

    res = astrix_ip.count('*')
    return \
        IpDecimalToString(IpBinaryToDecimal(astrix_ip.replace('*','0'))) + \
        '/%d' % (binary_size-res)

