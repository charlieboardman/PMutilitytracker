import time
import serial


#port is set to COM5 for my windows PC. When testing on linux laptop or macbook, will need to change this
#serialPort = serial.Serial(port = "COM5", baudrate=9600,bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

#Linux
serialPort = serial.Serial(port = "/dev/ttyACM0", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
count = 0
arr = [[],[]]
starttime = time.time()

#serialPort.open()
while True:
    if serialPort.in_waiting > 0:
        line = serialPort.readline().strip()
        arr[0].append(time.time()-starttime)
        arr[1].append(line)
        
    if time.time() - starttime >= 10:
        break
    
f = open('csvfile.csv','w')

for row in range(len(arr[0])):
    f.write(str(arr[0][row])+','+str(int(arr[1][row]))+'\n')
    
f.close()