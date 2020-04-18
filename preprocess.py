#!/usr/bin/python3.6
### Mario Ambrosino 2020/04/18
### 5G Academy
### Sensor Parser: maps sensor string in tuple output
### input string format: "--T 22.0 --H 65.0"
### output string json-like: { "temperature" : 22.0 ; "humidity" : 65.0 }"

# libreria per il parsing degli argomenti
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--T", type=float, default=0, help="Temperature [°C]")
parser.add_argument("--H", type=float, default=0, help="Humidity [%]")
opt = parser.parse_args()
print("{}; {};".format(opt.T,opt.H))