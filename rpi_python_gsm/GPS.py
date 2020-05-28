from rpi_python_gsm.GSM import GSM

class GPS(GSM):
    """Class to handle GPS commands for the GSM"""

    def __init__(self, pwr_pin = 23, port='/dev/ttyS0', baudrate=115200, timeout=5):
        super().__init__(pwr_pin, port, baudrate, timeout)

    def gpsOn(self):
        """Turn the GPS on"""
        cmd = self.cmd(b'AT+CGPS=1,1\r')
        return {'Command': cmd[0]}

    def gpsOff(self):
        """Turn the GPS off"""
        cmd = self.cmd(b'AT+CGPS=0,1\r')
        return {'Command': cmd[0]}

    def getFixedPosition(self):
        """Get GPS fixed position"""
        cmd = self.cmd(b'AT+CGPSINFO\r')
        return {'Command': cmd[0], 'Position': cmd[1]}
