import time
from pyModbusTCP.client import ModbusClient
import speech_recognition as sr

server_host = "192.168.3.250"
server_port = 502
plc = ModbusClient(host="88.248.184.172",port=502)
is_open = True
ses = sr.Recognizer()
#plc.host(server_host)
#plc.port(server_port)


with sr.Microphone() as source:
    print("Listening...")
    audio = ses.listen(source)


while True:
    if not plc.is_open:
        if not plc.open( ):
            print ( "unable to connect to "+ server_host +" : "+str(server_port))
            time.sleep(2) 
    if plc.is_open:
    
        komut = ses.recognize_google(audio)
        quadro = input()
        if (komut == "koruk") :
            plc.write_single_coil(2111,1) #koruk 1 yaz

        if (komut == "quadro"):
            plc.write_single_coil(2113,1) #quadro 1 yaz
