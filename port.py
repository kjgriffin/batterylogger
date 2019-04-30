#!/usr/bin/python3.6
import serial
import serial.tools.list_ports
import io


def main():
    # list all the ports
    port = ""

    for port in serial.tools.list_ports.comports():
        #if port[2] != 'n/a':
        print(port)


    ser = serial.Serial("COM1", 9600, timeout=0, parity=serial.PARITY_NONE, rtscts=1)
    ser.open()
    while True:
        x = ser.read(1)
        print(x)



if __name__ == "__main__":
    main()
