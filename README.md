# nano_GPIO
Jetson Nano는 확장 헤더(J6) 40개의 핀으로 전원(3.3v, 5v, GND),PWM (펄스 폭 변조), I2C, SPI, UART 통신 기능이 있음.

<p align="center">
  <img src="https://github.com/user-attachments/assets/30771849-e8b7-4a97-bacb-ed24cc72023d" width="500" height="500">\
  <strong>40-Pin Header (J6)</strong>
</p>


# 단일 LED ON/OFF
LED는 22번 PIN, GND는 20번 PIN 사용
 1. 220옴 저항과 LED의 +핀을 연결
 2. 저항의 다른 한 쪽과 Jetson Nano GPIO 핀 22번과 연결
 3. LED의 -핀을 Jetson Nano의 GPIO GND 핀 20번과 연결

https://github.com/user-attachments/assets/1963db58-cf10-4d38-976d-783e9d947cc8


# RGB LED
 1. 1k옴 저항과 RGB LED의 R에 연결, 저항의 다른 한 쪽과 Nano GPIO 핀  11번 핀을 연결
 2. 1k옴 저항과 RGB LED의 G에 연결, 저항의 다른 한 쪽과 Nano GPIO 핀 12번 핀을 연결
 3. 1k옴 저항과 RGB LED의 B에 연결, 저항의 다른 한 쪽과 Nano GPIO 핀 13번 핀을 연결
 4. RGB LED의 -핀을 Jetson Nano의 GPIO GND 핀 14번과 연결

