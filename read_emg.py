import serial


def main():

    # Replace 'COM3' with your actual serial port name
    ser = serial.Serial("COM3", baudrate=9600, timeout=1)

    try:
        while True:
            # Read a line from the serial port
            emg_data = ser.readline().decode("utf-8").strip()

            # Print the received data
            print(f"Received: {emg_data}")

    except KeyboardInterrupt:
        # Close the serial port when the script is interrupted (Ctrl+C)
        ser.close()
        print("Serial port closed.")
    return 0


if __name__ == "__main__":
    main()
