# 1101 - 13
# 101  - 5

def bin2dec(no):
    dec = 0
    deg = 0
    while no > 0:
        dig = no % 10
        dec = dec + (dig * 2**deg)
        no = int(no / 10)
        deg += 1
    return dec

bin_no = int(input('Enter a binary no: '))
dec_no = bin2dec(bin_no)

print('Representation of {} in decimal is: {}'.format(bin_no, dec_no))
