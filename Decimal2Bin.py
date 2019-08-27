# 8 - 1000
# 5 - 101

def dec2bin(no):
    bin = 0
    mul = 1
    while no > 0:
        dig = no % 2
        bin = dig * mul + bin
        no = int(no / 2)
        mul *= 10
    return bin


dec_no = int(input('Enter a decimal no: '))
bin_no = dec2bin(dec_no)

print('Representation of {} in binary is: {}'.format(dec_no, bin_no))
