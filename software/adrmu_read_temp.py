from smbus2 import SMBus

i2c_ch = 1
reg_temp = 0x00
reg_config = 0x01
bus = SMBus(i2c_ch)
readable = True
read_val = 0.0

def TMP117(address):
    val = bus.read_i2c_block_data(address, reg_config, 2)
    val[1] = val[1] & 0b00111111
    val[1] = val[1] | (0b10 << 6)
    bus.write_i2c_block_data(address, reg_config, val)
    val = bus.read_i2c_block_data(address, reg_config, 2)
    temp_c = (val[0] << 8) | (val[1] )
    temp_c = temp_c * 0.0078125
    return temp_c

 
#ADRmu1_temp_sensor=TMP117(address=0x48, title="ADRmu1 Temp Sensor")
#ADRmu2_temp_sensor=TMP117(address=0x4B, title="ADRmu2 Temp Sensor")
ADRmu3_temp_sensor=TMP117(address=0x4A)
#ADRmu4_temp_sensor=TMP117(address=0x49, title="ADRmu4 Temp Sensor")
print(TMP117(0x4A))