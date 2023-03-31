from smbus2 import SMBus, i2c_msg
from math import ceil
from time import sleep
import sys


def read_eeprom(bus, address, count, blocksize=32):
    print("reading "+str(count)+" bytes ...")
    data = []
    full_reads, remainder = divmod(count, blocksize)
    if remainder: full_reads += 1
    for i in range(full_reads):
        start = i*blocksize
        hb, lb = start >> 8, start & 0xff
        write = i2c_msg.write(address, [hb, lb])
        count = remainder if (remainder and i == full_reads-1) else blocksize
        read = i2c_msg.read(address, count)
        bus.i2c_rdwr(write, read)
        data += list(read)
    return data

def write_eeprom(bus, address, data, blocksize=32, sleep_time=0.01):
    print("writing "+str(len(data))+" bytes ...")
    b_l = len(data)
    b_c = int(ceil(b_l/float(blocksize)))
    blocks = [data[blocksize*x:][:blocksize] for x in range(b_c)]
    for i, block in enumerate(blocks):
        if sleep_time:
            sleep(sleep_time)
        start = i*blocksize
        hb, lb = start >> 8, start & 0xff
        data = [hb, lb]+block
        write = i2c_msg.write(address, data)
        bus.i2c_rdwr(write)

bus = SMBus(1)
i2c_address=0x50 #ADRmu 1
#i2c_address=0x51 #ADRmu 2
#i2c_address=0x52 #ADRmu 3
#i2c_address=0x53 #ADRmu 4


if (sys.argv[1]=="read"):
    read_result = read_eeprom(bus, i2c_address, 100)
    print(''.join(chr(i) for i in read_result))

elif( sys.argv[1]=="write"):
    write_eeprom(bus,i2c_address,[0xFF]*100)
    sleep(1)
    str_to_write="ADRmu S/N 4\nYYYY.MM.DD,VV.VVVVVVVV,TT.TTT\n2022.06.02,09.99785080,28.585"
    data = [ord(c) for c in str_to_write]
    write_eeprom(bus,i2c_address, data)
    sleep(1)
    read_result = read_eeprom(bus, i2c_address, len(data))
    print(''.join(chr(i) for i in read_result))
    assert(read_result == data)
