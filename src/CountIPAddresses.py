# Count IP Addresses
# https://www.codewars.com/kata/526989a41034285187000de4


def ips_between(start, end):
    bit_shift = 8 * 3
    result = 0
    for start_octet, end_octet in zip(start.split('.'), end.split('.')):
        parts_diff = int(end_octet) - int(start_octet)
        result += parts_diff << bit_shift
        bit_shift -= 8
    return result
