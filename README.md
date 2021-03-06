# ADR1000 10V standard

![rendering](https://github.com/marcoreps/ADRmu/raw/main/images/render.png)
![ppm over 24h](https://github.com/marcoreps/ADRmu/raw/main/images/24hppm.jpg)

## Scope

Low cost 10V DC reference standard in DIN 41612 modular enclosure. Based on ovenized LTZ1000 / LTZ1000A or ADR1000A zener diodes.

## TODO

Align JP and R designators

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

## Measured results
| SN | Rev. |      U202      |   .1-10Hz Noise   | 24h Stab ±µV/V | 30d Stab ±µV/V | 90d Stab ±µV/V | 1yr Stab ±µV/V |
| -- | ---- | -------------- | ----------------- | -------------- | -------------- | -------------- | -------------- |
| 1  |   1  | ADR1000A #1727 | 141 nVrms 100 sec |      0.25      |                |                |                |

## Trim levels

The PCB is prepared for various configurations to adapt to different needs and part availabilities. For example:

### ADR1000 & Vishay 1445 All-in-one Resistor Network

My SN 1 is built this way. This is a no-bainer or easy mode. When I got my first glimpse at the ADR1000 datasheet I went straight to Vishay Foil Resistors and ordered an all-in-one resistor network with all the critical resistors from the datasheet plus a simple divider for buffering the 6.62V output to 10V. By specifying at least 2 ppm/°C TC tracking for the two critical dividers I am guaranteed great performance. And thanks to the hermetically sealed DIP14 package I expect little long term drift from the resistors. This solution comes at a hefty price.

### LTZ1000A & Discrete Resistors

My SN 2 is built this way. This is probably the most popular way of building LTZ1000 voltage standards. Digikey carries quite a few hermetically sealed Vishay Bulk Metal Foil resistors without MOQ these days, giving you all the design freedom. The two most critical parts are the LTZ-temperature-configration divder i.e. 13k/1k and the 7.1V to 10V buffer divder i.e. 2k/5k. For these two I used hermetically sealed Vishay VHD200 dividers. These have guaranteed TC tracking and little long term drift. The remaining LTZ-configruation resistors i.e. 70k, 70k, 120R are not very critical. For best performance you can add an additional resistor to LTZ pin 3 to improve the Vrefs tempco, see "Adjusting Temperature Coefficient in Unstabilized Applications" in the LTZ1000 datasheet. 20 Ohm seems to be a reasonable approximation, suitable for most LTZs. In my case I determined 18 Ohm to be an optimal resistor with a TC peak at the oven setpoint. Careful, this additional resistor, if equipped, has a lot of influence on zener voltage and should be of high quality.


