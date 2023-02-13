import string
import math

def strlst(value1, value2):
    return value1.split(value2)

def differ(val1, val2):
    if val1 >= val2:
        return val1 - val2


    else:
        return val2 - val1


print('Select Process: (Store/View/Calculate)')
process = input('')

if 'CAL' in process.upper():
    coord1 = strlst(input('coord1: '), ' ')
    print(coord1)
    coord2 = strlst(input('coord2: '), ' ')
    print(coord2)

    if input('2D Plane? [Y/N]').upper() == 'Y':
        x1 = int(coord1[0])
        z1 = int(coord1[2])
        x2 = int(coord2[0])
        z2 = int(coord2[2])
        xdif = differ(x1, x2)
        print(xdif)
        zdif = differ(z1, z2)
        print(zdif)
        totblocks = math.sqrt((xdif ** 2) + (zdif ** 2))
        print('Total Block Distance =', totblocks)
