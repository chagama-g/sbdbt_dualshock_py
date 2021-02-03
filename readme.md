# SBDBT_DUALSHOCK_py

## Installation
```bash
git clone https://github.com/chagama-g/sbdbt_dualshock_py
pip install sbdbt_dualshock_py/
```
### USBシリアルのアクセス権限の設定。
mode666で読み込むようにする。
```bash
sudo nano /etc/udev/rules.d/65-serial.rules
```

```bash
# /etc/udev/rules.d/65-serial.rules
ACTION=="remove", GOTO="serial_end"
SUBSYSTEM!="tty", GOTO="serial_end"
KERNEL=="ttyUSB[0-9]*", MODE="0666"
LABEL="serial_end"
```

```bash
sudo udevadm control --reload
```

> 参考:  [第555回　いま，あらためてudev：Ubuntu Weekly Recipe｜gihyo.jp … 技術評論社](https://gihyo.jp/admin/serial/01/ubuntu-recipe/0555?page=3)
