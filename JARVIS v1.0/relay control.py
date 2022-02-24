 from os import write
 import serial

 Arduino_Serial = serial.Serial('com12', 9600)

 while True:
     Arduino_Serial.write(str.encode('on1'))
     print("relay1on")

     input_data = input()

     if(input_data == 'on1'):
         Arduino_Serial.write(str.encode('on1'))
         print("relay1on")

     if(input_data == 'off1'):
         Arduino_Serial.write(str.encode('off1'))
         print("relay1off")

     if(input_data == 'on2'):
         Arduino_Serial.write(str.encode('on2'))
         print("relay1on")

     if(input_data == 'off2'):
         Arduino_Serial.write(str.encode('off2'))
         print("relay1off")
     break
