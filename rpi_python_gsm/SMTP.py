from rpi_python_gsm.GSM import GSM
import time

class SMTP(GSM):
    """Class to handle SMTP commands for the GSM"""

    def __init__(self, pwr_pin=23, port='/dev/ttyS0', baudrate=115200, timeout=5):
        super().__init__(pwr_pin, port, baudrate, timeout)

    def setServerAndPort(self, server, port):
        """Sets the SMTP server and port"""
        cmd = self.cmd(b'AT+CSMTPSSRV="' + server.encode() + b'",' + str(port).encode() + b',3\r')
        return {'Command': cmd[0]}

    def getServerAndPort(self):
        """Returns the set SMTP server and port"""
        cmd = self.cmd(b'AT+CSMTPSSRV?\r')
        server, port, type = cmd[1].split()[1].split(',')
        return {'Command': cmd[0], 'Server': server, 'Port': port, 'Type': type}

    def setAuth(self, username, password):
        """Sets username and password for the SMTP server"""
        cmd = self.cmd(b'AT+CSMTPSAUTH=1,"' + username.encode() + b'", "' + password.encode() + b'"\r')
        return {'Command': cmd[0]}

    def getAuth(self):
        """Returns the username and password for SMTP"""
        cmd = self.cmd(b'AT+CSMTPSAUTH?\r')
        id, username, password = cmd[1].split()[1].split(',')
        return {'Command': cmd[0], 'Username': username, 'Password': password}

    def setSenderAddressName(self, address, name):
        """Set SMTP sender address and name"""
        cmd = self.cmd(b'AT+CSMTPSFROM="' + address.encode() + b'","' + name.encode() + b'"\r')
        return {'Command': cmd[0]}

    def getSenderAddressName(self):
        """Get SMTP sender address and name"""
        cmd = self.cmd(b'AT+CSMTPSFROM?\r')
        address, name = cmd[1].split()[1].split(',')
        return {'Command': cmd[0], 'Address': address, 'Name': name}

    def setRecipientAddressName(self, address, name):
        """Set the recipient's address and name"""
        cmd = self.cmd(b'AT+CSMTPSRCPT=0,0,"' + address.encode() + b'","' + name.encode() + b'"\r')
        return {'Command': cmd[0]}

    def getRecipientAddressName(self):
        """Get the address and name of recipient"""
        cmd = self.cmd(b'AT+CSMTPSRCPT?\r')
        id, index, address, name = cmd[1].split()[1].split(',')
        return {'Command': cmd[0], 'Address': address, 'Name': name}

    def setEmailSubject(self, subject):
        """Set the E-mail subject"""
        cmd = self.cmd(b'AT+CSMTPSSUB=' + str(len(subject)).encode() + b',"utf-8"\r')
        cmd = self.cmd(subject.encode() + b'\r\x1a')
        time.sleep(5)

    def getEmailSubject(self):
        """Get the E-mail subject"""
        cmd = self.cmd(b'AT+CSMTPSSUB?\r')
        return {'Command': cmd[0], 'Subject': cmd[2]}

    def setEmailBody(self, body):
        """Set the E-mail body"""
        cmd = self.cmd(b'AT+CSMTPSBODY=' + str(len(body)).encode() + b'\r')
        cmd = self.cmd(body.encode() + b'\r\x1a')
        time.sleep(5)

    def getEmailBody(self):
        """Get the E-mail body"""
        cmd = self.cmd(b'AT+CSMTPSBODY?\r')
        return {'Command': cmd[0], "Body": cmd[2]}

    def setEmailAttachment(self, attachment):
        """Set an E-mail attachment"""
        cmd = self.cmd(b'AT+CSMTPSFILE=1,"' + attachment.encode() + b'"\r')
        return {'Command': cmd[0]}

    def getEmailAttachment(self, attachment):
        """Get the E-mail attachment"""
        cmd = self.cmd(b'AT+CSMTPSFILE?\r')
        return {'Command': cmd[0], 'Attachments': cmd[1:-1]}

    def send(self):
        """Initiate session and send the e-mail"""
        cmd = self.cmd(b'AT+CSMTPSSEND\r')
        self.wait()
        return {'Command': cmd[0]}

    def forceStop(self):
        """Force the system to stop sending e-mail"""
        cmd = self.cmd(b'AT+CSMTPSSTOP\r')
        return {'Command': cmd[0]}

    def clearEmail(self):
        """Clear the email content and settings"""
        cmd = self.cmd(b'AT+CSMTPSCLEAN\r')
        return {'Command': cmd[0]}
