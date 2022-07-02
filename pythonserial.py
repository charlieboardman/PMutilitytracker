import serial

serialPort = serial.Serial(port = "COM5", baudrate=9600,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
count = 0

#serialPort.open()
while True:
  line =serialPort.readline() 
  if line:
        count = count + 1
    if count == 1:
        print(line)
        count = 0