def int32_to_ip(int32):
    ipnumber = int32
    octet1 = int(ipnumber / 16777216) % 256
    octet2 = int(ipnumber / 65536) % 256
    octet3 = int(ipnumber / 256) % 256
    octet4 = int(ipnumber) % 256
    return '%(octet1)s.%(octet2)s.%(octet3)s.%(octet4)s' % locals()