class TMP117:
    
    i2c_ch = 1
    reg_temp = 0x00
    reg_config = 0x01
    bus = smbus.SMBus(i2c_ch)
    readable = True
    read_val = 0.0
    
    def is_readable(self):
        return self.readable
    
    def __init__(self, address, title):
        self.title = title
        logging.debug(self.title+' init started')
        self.i2c_address = address
        val = self.bus.read_i2c_block_data(self.i2c_address, self.reg_config, 2)
        val[1] = val[1] & 0b00111111
        val[1] = val[1] | (0b10 << 6)
        self.bus.write_i2c_block_data(self.i2c_address, self.reg_config, val)
        val = self.bus.read_i2c_block_data(self.i2c_address, self.reg_config, 2)
        
        
    def measure(self):
        pass
        
        
    def get_title(self):
        return self.title
        
    def get_read_val(self):
        val = self.bus.read_i2c_block_data(self.i2c_address, self.reg_temp, 2)
        temp_c = (val[0] << 8) | (val[1] )
        temp_c = temp_c * 0.0078125
        return temp_c

        
    def is_measuring(self):
        return False
        
ADRmu4_temp_sensor=TMP117(address=0x49, title="ADRmu4 Temp Sensor")
print(ADRmu4_temp_sensor.get_read_val())