from rpi_python_gsm.GSM import GSM
from rpi_python_gsm.SMS import SMS
from rpi_python_gsm.Ping import Ping
from rpi_python_gsm.SMTP import SMTP
from rpi_python_gsm.Network import Network

if __name__ == '__main__':
    #print('GSM\n')
    #gsm = GSM()
    #gsm.turnOn()

    #print('\nCheck: ', gsm.check())

    #print('\nService Provider: ', gsm.getServiceProvider())

    #print('\nSignal Quality: ', gsm.getSignalQuality())

    #print('\nPower Supply Voltage: ', gsm.getPowerVoltage())

    #print('\nDevice Temp: ', gsm.getTemp())


    #smtp = SMTP()
    #smtp.turnOn()

    #print('\nSet server and port: ', smtp.setServerAndPort('smtp-mail.outlook.com', 587))
    #print('\nGet server and port: ', smtp.getServerAndPort())

    #print('\nSet SMTP authentication: ', smtp.setAuth('ben_traines@consultnetgroup.com', 'RASP1#68ben!'))
    #print('\nGet SMTP authentication: ', smtp.getAuth())

    #print('\nGet SMTP sender address and name: ', smtp.getSenderAddressName())
    #print('\nSet SMTP sender address and name: ', smtp.setSenderAddressName('ben_traines@consultnetgroup.com', 'ben'))

    #print('\nSet email recipient: ', smtp.setRecipientAddressName('trainesben68@gmail.com', 'trainesb'))
    #print('\nGet email recipient: ', smtp.getRecipientAddressName())

    #print('\nSet email subject: ', smtp.setEmailSubject('subject'))
    #print('\nGet email subject: ', smtp.getEmailSubject())

    #print('\nSet email body: ', smtp.setEmailBody('Body'))
    #print('\nGet email body: ', smtp.getEmailBody())

    #print('\nSend sms: ', smtp.send())

    #network = Network()
    #network.turnOn()

    #print('\nGet Network registration info: ', network.getRegistered())

    #print('\nGet Operator: ', network.getOperator())

    #print('\nGet Operators: ', network.getOperators())

    #print('\nCheck APN: ', network.getAPN())

    #sms = SMS()
    #sms.turnOn()

    #print('\nSet Text mode: ', sms.setTextMode())

    #print('\nGet Text mode: ', sms.getTextMode())

    #print('\nSend SMS: ', sms.sendText('+12317147967', 'Test'))

    ping = Ping()
    ping.turnOn()

    print('\nPing Google: ', ping.ping('www.google.com'))
