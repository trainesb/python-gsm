from rpi_python_gsm.GSM import GSM

class Network(GSM):
    """Class to handle Network commands for the GSM"""

    def __init__(self, pwr_pin = 23, port='/dev/ttyS0', baudrate=115200, timeout=5):
        super().__init__(pwr_pin, port, baudrate, timeout)

    def getRegistered(self):
        rtrn = self.cmd(b'AT+CREG?\r')
        n, stat = rtrn[1].split()[1].split(',')
        if int(n) == 0:
            n = 'disable network registration unsolicited result code'
        elif int(n) == 1:
            n = 'enable network registration unsolicited result code +CREG: <stat>'
        else:
            n = ' enable network registration and location information unsolicited result code +CREG: <stat>[,<lac>,<ci>]'

        if int(stat) == 0:
            stat = 'not registered, ME is not currently searching a new operator to register to'
        elif int(stat) == 1:
            stat = 'registered, home network'
        elif int(stat) == 2:
            stat = 'not registered, but ME is currently searching a new operator to register to'
        elif int(stat) == 3:
            stat = 'registration denied'
        elif int(stat) == 4:
            stat = 'unknown'
        else:
            stat = 'registered, roaming'
        return {'Command': rtrn[0], 'n': n, 'stat': stat}

    def getOperator(self):
        cmd = self.cmd(b'AT+COPS?\r')
        return {'Command': cmd[0], 'Operator': cmd[1]}

    def getOperators(self):
        cmd = self.cmd(b'AT+COPS=?\r')
        return {'Command': cmd[0], 'Operators': cmd[1]}

    def getAPN(self):
        cmd = self.cmd(b'AT+CGDCONT?\r')
        return {'Command': cmd[0], 'APN': cmd[1]}
