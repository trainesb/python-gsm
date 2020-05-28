from rpi_python_gsm.GSM import GSM

class Ping(GSM):
    """Class to handle Ping commands for the GSM"""

    def __init__(self, pwr_pin = 23, port='/dev/ttyS0', baudrate=115200, timeout=5):
        super().__init__(pwr_pin, port, baudrate, timeout)

    def ping(self, url):
        """Ping url"""
        cmd = self.cmd(b'AT+CPING="'+url.encode()+b'",1,4,64,1000,10000,255\r')
        ping = self.wait()
        ping = ping.split()[1].split(',')
        return {'Command': cmd[0], 'requests': ping[1], 'responses': ping[2], 'failed_responses': ping[3], 'min_rtt': ping[4], 'max_rtt': ping[5], 'avg_rtt': ping[6]}
