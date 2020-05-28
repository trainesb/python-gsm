import time
import serial
import RPi.GPIO as GPIO

class GSM:

    def __init__(self, pwr_pin=23, port='/dev/ttyS0', baudrate=115200, timeout=5):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.pwr_pin = pwr_pin
        self.ser = None
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pwr_pin, GPIO.OUT)

    def turnOn(self):
        """Turn the SIM7100A on"""
        GPIO.output(self.pwr_pin, GPIO.HIGH)
        time.sleep(10)
        self.ser = serial.Serial(port = self.port, baudrate = self.baudrate, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, bytesize = serial.EIGHTBITS, timeout = self.timeout)

    def turnOff(self):
        """Turn the SIM7100A off"""
        self.ser.write(b'AT+CPOWD\r')
        self.ser = None

    def isOpen(self):
        """Checks if the serial connection is open"""
        return self.ser.is_open

    def close(self):
        """Closes the serial connection"""
        return self.ser.close()

    def cmd(self, cmd):
        """Write a command to SIM7100A and wiat for response"""
        self.ser.write(cmd)
        return self.wait()

    def wait(self):
        """Wait for SIM7100A"""
        rtrn = []
        while True:
            line = self.ser.readline()
            line = line.decode().strip()
            #print('Line: ', line)
            rtrn.append(line)

            if line == 'OK': return rtrn
            elif line == 'ERROR': return False
            elif line == '>': return False
            elif '+CSMTPSSEND:' in line: return line
            elif '+CPING: 3,' in line: return line

    def check(self):
        """Perform a simple AT command"""
        rtrn = self.cmd(b'AT\r')
        return {'Command': rtrn[0], 'Response': rtrn[-1]}

    def getServiceProvider(self):
        """Get the devices service provider"""
        cmd = self.cmd(b'AT+CSPN?\r')
        rtrn = cmd[1].split()[1].split(',')
        if int(rtrn[1]):
            display = 'display PLMN'
        else:
            display = "doesn't display PLMN. Alerady registered on PLMN."
        return {'Command': cmd[0], 'Service Provider': rtrn[0], 'Display Mode': display}

    def getSignalQuality(self):
        """Get the system's signal quality"""
        cmd = self.cmd(b'AT+CSQ\r')
        rssi, ber = cmd[1].split()[-1].split(',')
        if int(rssi) == 99 or int(rssi) == 199: rssi = 'not known or not detectable'
        if int(ber) == 99: ber = 'not known or not detectable'
        return {'Command': cmd[0], 'Received Signal Strength': rssi, 'Channel Bit Error Rate': ber}

    def getPowerVoltage(self):
        """Get the voltage of the power supply"""
        cmd = self.cmd(b'AT+CBC\r')
        voltage = cmd[1].split()[1].strip()
        return {'Command': cmd[0], 'Voltage': voltage}

    def getTemp(self):
        """Get the temperture of the SIM7100A"""
        cmd = self.cmd(b'AT+CPMUTEMP\r')
        temp = cmd[1].split()[1].strip()
        return {'Command': cmd[0], 'Temperature': temp}
