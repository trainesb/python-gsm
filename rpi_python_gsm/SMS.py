from rpi_python_gsm.GSM import GSM

class SMS(GSM):
    """Class to handle SMS commands for the GSM"""

    def __init__(self, pwr_pin = 23, port='/dev/ttyS0', baudrate=115200, timeout=5):
        super().__init__(pwr_pin, port, baudrate, timeout)

    def getTextMode(self):
        """Get the text mode"""
        cmd = self.cmd(b'AT+CMGF?\r')
        mode = 'PDU mode'
        if cmd[1].split()[1].strip() == '1':
            mode = 'Text mode'
        return {'Command': cmd[0], 'Mode': mode}

    def setTextMode(self):
        """Set the SIM module to text mode"""
        cmd = self.cmd(b'AT+CMGF=1\r')
        return {'Command': cmd[0]}

    def sendText(self, phone, msg):
        """Send the text message to `phone`"""
        cmd = self.cmd(b'AT+CMGS="' + phone.encode() + b'"\r')
        cmd = self.cmd(msg.encode() + b'\r\x1a')
