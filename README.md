# ADR1000 10V standard

![rendering](https://github.com/marcoreps/ADRmu/raw/main/images/render.png)
![ppm over 24h](https://github.com/marcoreps/ADRmu/raw/main/images/24hppm.jpg)

## Scope

Low cost 10V DC reference standard in DIN 41612 modular enclosure. Based on ovenized LTZ1000 / LTZ1000A or ADR1000A zener diodes.

## TODO

Reduce core losses

Inrush trips battery OC

Add fuel gauge to battery

Charge battery with LTC4079 maybe

Battery charge input protection diodes

Lower battery charge current to 600mA

EEPROM in BOM doesn't allow addressing, maybe switch to i.e. BR24H64FVM-5ACTR

## Assembly advice

Recommended ~5 transformer windings pri & sec

## Spec speculations

### Output Voltage Stability (± µV/V):

24 hour: < 0.3

30 day:

90 day:

1 year:

### Output Voltage Noise (0.1 - 10 Hz)(±µV/V rms)

< 0.02

### Output Voltage Tempco (±µV/K)

< 0.2

### Short circuit current (mA)

10

### Battery life (h)

\> 24

### Isolation (MΩ to AC,PE)

\> 10 000 MΩ

< 1000 pF

### Output Protection

Output can be shorted indefinitely with battery life derating. Output protected against ESD.

### Temperature Range (°C)

15 - 35

## Measured results:
| SN | Rev. |      U202      |   .1-10Hz Noise   | 24h Stab ±µV/V | 30d Stab ±µV/V | 90d Stab ±µV/V | 1yr Stab ±µV/V |
| -- | ---- | -------------- | ----------------- | -------------- | -------------- | -------------- | -------------- |
| 1  |   1  | ADR1000A #1727 | 141 nVrms 100 sec |      0.25      |                |                |                |
