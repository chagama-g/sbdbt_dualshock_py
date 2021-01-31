from sbdbt_dualshock_py import SBDBT

import time


def main(serial_name):
    sbdbt = SBDBT(serial_name)

    while True:
        rx = sbdbt.receive()
        if rx is not None:
            data = SBDBT.parse(rx)
            print(data)
        time.sleep(0.0005)


if __name__ == '__main__':
    try:
        main("COM3")
    except KeyboardInterrupt:
        print("Keyboard Interrupted.")
