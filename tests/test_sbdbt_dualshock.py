from sbdbt_dualshock_py import SBDBT

import time
import sys


def main():
    port = sys.argv[1]
    sbdbt = SBDBT(port)

    while True:
        rx = sbdbt.receive()
        if rx is not None:
            data = SBDBT.parse(rx)
            print(data)
        time.sleep(0.0005)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise Exception("Specify the serial port as an argument")

    try:
        main()
    except KeyboardInterrupt:
        print("Keyboard Interrupted.")
