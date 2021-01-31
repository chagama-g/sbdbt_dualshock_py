import serial
from dataclasses import dataclass


class SBDBTException(Exception):
    pass


class SBDBTParseError(Exception):
    pass


class SBDBT:

    def __init__(self, _ser_name):

        self.ser = serial.Serial(_ser_name, baudrate=115200, timeout=0)
        self.ser_name = _ser_name

        self.__buf = []

    def close(self):
        if self.ser is None:
            raise SBDBTException("Serial is not opened")

        self.ser.close()

    def receive(self):

        if self.ser.in_waiting > 8:
            self.ser.reset_input_buffer()

        # print(self.ser.in_waiting)

        while self.ser.in_waiting > 0:

            read = self.ser.read(1)

            # 先頭の 0x80
            if read == b'\x80':
                # バッファにデータが存在したら破棄
                if len(self.__buf) > 0:
                    self.__buf = []

                # バッファに追加
                self.__buf.append(read)

            # データ本体
            else:
                if len(self.__buf) == 0:
                    pass
                elif len(self.__buf) < 8:
                    self.__buf.append(read)
                if len(self.__buf) == 8:
                    return self.__buf

    @staticmethod
    def parse(data_array):
        if len(data_array) != 8:
            raise SBDBTParseError("The number of data is invalid")

        int_data_array = []
        for data in data_array:
            int_data_array.append(int.from_bytes(data, 'big'))

        # check data integrity
        # if sum(data_array[1:-1]) % 0x7f != data_array[7]:
        #     raise SBDBTParseError("checksum error")

        data = SBDBTData(
            L_X=int_data_array[3],
            L_Y=int_data_array[4],
            R_X=int_data_array[5],
            R_Y=int_data_array[6],
            SQUARE=int_data_array[1] & 0x01 > 0,
            TRIANGLE=int_data_array[2] & 0x10 > 0,
            X=int_data_array[2] & 0x20 > 0,
            CIRCLE=int_data_array[2] & 0x40 > 0,
            R1=int_data_array[1] & 0x08 > 0,
            R2=int_data_array[1] & 0x10 > 0,
            R3=int_data_array[1] & 0x40 > 0,
            L1=int_data_array[1] & 0x02 > 0,
            L2=int_data_array[1] & 0x04 > 0,
            L3=int_data_array[1] & 0x20 > 0,
            UP=int_data_array[2] & 0x01 > 0,
            DOWN=int_data_array[2] & 0x02 > 0,
            LEFT=int_data_array[2] & 0x08 > 0,
            RIGHT=int_data_array[2] & 0x04 > 0,
            START=int_data_array[2] & 0x80 > 0,
            SELECT=int_data_array[1] & 0x20 > 0,
            checksum=int_data_array[7]
        )

        return data


@dataclass
class SBDBTData:
    L_X: int
    L_Y: int
    R_X: int
    R_Y: int
    SQUARE: bool
    TRIANGLE: bool
    X: bool
    CIRCLE: bool
    R1: bool
    R2: bool
    R3: bool
    L1: bool
    L2: bool
    L3: bool
    UP: bool
    DOWN: bool
    LEFT: bool
    RIGHT: bool
    START: bool
    SELECT: bool
    checksum: int
