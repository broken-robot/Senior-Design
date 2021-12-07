#Need to install pyserial from pip3

import serial

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)#change to Arduino Port before running
    ser.reset_input_buffer()

    ser.write(b'S\n')
    while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('uyf-8').rstrip()
                print(line)