# ADR1000 10V standard

![rendering](https://github.com/marcoreps/ADRmu/raw/main/images/render.png)
![ppm over 24h](https://github.com/marcoreps/ADRmu/raw/main/images/24hppm.jpg)
![one year drift](https://github.com/marcoreps/ADRmu/raw/main/results/mu_vs_mean.png)

## Scope

Low cost 10V DC reference standard in DIN 41612 modular enclosure. Based on ovenized LTZ1000 / LTZ1000A or ADR1000A zener diodes. Fits into standard 100x160mm project boxes too. The most promising strategies for configuring the zener and buffering the output are accommodated. Includes a high isolation DC-DC converter to attenuate the effects of common mode current.

## TODO

Align JP and R designators

Remove JPB and JPH enumeration

add lt5400 and other gain resistor options

discrete push-pull driver

snubber for the DC-DC converter?


## Assembly advice

Recommended 5:7 transformer (pri:sec) when using 12V input

## Spec speculations

After initial settling, tempco adjustment, continuously powered on, no ambient temperatures outside of specified range

### Output Voltage Stability (± µV/V):

24 hour: < 0.3

30 day: < 0.4

90 day: < 0.8

1 year: < 1.0

### Output Voltage Noise (0.1 - 10 Hz)(±µV/V rms)

< 0.02

### Output Voltage Tempco (±µV/V/K)

< 0.04

### Short circuit current (mA)

9-11

### Power consumption (W)

\< 2W

### Isolation (to DCin, Chassis)

\> 10 000 MΩ

< 1000 pF

### Output Protection

Output can be shorted indefinitely with battery life derating. Output protected against ESD and input up to 60V.

### Specified Temperature Range (°C)

15 - 35

### Oerational Temperature Range (°C)

-10 - 40

## Measured results
| SN    | U202  | .1-10Hz Noise   | Tempco 15-35°C    |  24h Stab  |  30d Stab  |  90d Stab  |  1yr Stab  |
| ---   | ----  | --------------  | ---------------   | ---------- | ---------- | ---------- | ---------- |
|       |       | \[µV/V rms\]    | \[µV/V/k\]        | \[µV/V\]   | \[µV/V\]   | \[µV/V\]   | \[µV/V\]   |
|   1   | ADR   | [0.0139][1]     |                   | 0.25       | 0.4        |            |            |
| ~~2~~ |~~LTZ-A~~| ~~[0.0175][2]~~|                  |            |            |            |            |
|   3   | LTZ-A | [0.0201][3]     | [-0.024][3tc]     |            |            |            |            |
|   4   |ADR1001| [0.0275][4]     | [-0.133][4tc]     |            |            |            |            |
| ~~5~~ |~~ADR~~|~~[0.0119][5]~~  |~~[+0.015][5tc]~~  |            |            |            |            |
| ~~7~~ |~~ADR~~|~~[0.0125][7]~~  |~~[+0.032][7tc]~~  |            |            |            |            |
|   9   |  ADR  |  [0.0121][9]    |  [+0.156][9tc]    |            |            |            |            |
|~~107~~|~~ADR~~|                 |~~[+0.049][107tc]~~|            |            |            |            |
|~~108~~|~~ADR~~|~~[0.0163][108]~~|~~[+0.030][108tc]~~|            |            |            |            |
|~~10~~ |~~ADR~~|~~[0.0115][10]~~ |~~[-0.028][10tc]~~ |            |            |            |            |
|  11   | ADR   | [0.0129][11]    | [+0.015][11tc]    |            |            |            |            |
|  12   | ADR   | [0.0116][12]    |                   |            |            |            |            |
|~~13~~ |~~ADR~~|~~[0.0132][13]~~ |~~[-0.024][13tc]~~ |            |            |            |            |
|~~F731B~~  |~~DH80417B~~| ~~[0.0272][731]~~  |       |            |            |            |            |
|   6   | ADR   |                 | [-0.018][6tc]     |            |            |            |            |
|~~14~~ |~~LTZ-A~~|               |~~[+0.025][14tc]~~ |            |            |            |            |
|  15   |  ADR  |   [0.0123][15]  |                   |            |            |            |            |
|  20   | LTZ-A |                 | -0.018            |            |            |            |            |
 
[1]:/results/ADRmu1_LFnoise.png
[2]:/results/ADRmu2_LFnoise.png
[3]:/results/ADRmu3_LFnoise.png
[4]:/results/ADRmu4_LFnoise_improved.png
[5]:/results/ADRmu5_LFnoise.png
[7]:/results/ADRmu7_LFnoise.png
[9]:/results/ADRmu9_LFnoise.png
[10]:/results/ADRmu10_LFnoise.png
[11]:/results/ADRmu11_LFnoise.png
[12]:/results/ADRmu12_LFnoise.png
[13]:/results/ADRmu13_LFnoise.png
[13]:/results/ADRmu15_LFnoise.png
[108]:/results/ADRmu108_LFnoise.png
[731]:/results/Fluke731B_LFnoise.png

[3tc]:/results/ADRmu3_TC.ipynb
[4tc]:/results/ADRmu4_TC.ipynb
[5tc]:/results/ADRmu5_TC.ipynb
[7tc]:/results/ADRmu7_TC.ipynb
[9tc]:/results/ADRmu9_TC.ipynb
[10tc]:/results/ADRmu10_TC.ipynb
[11tc]:/results/ADRmu11_TC.ipynb
[12tc]:/results/ADRmu12_TC.ipynb
[13tc]:/results/ADRmu13_TC.ipynb
[107tc]:/results/ADRmu107_TC.ipynb
[108tc]:/results/ADRmu108_TC.ipynb
[14tc]:/results/ADRmu14_TC.ipynb
[6tc]:/results/ADRmu6_TC.ipynb

Strikethrough: Device no longer in my possession




## Initial drift & burn-in
| SN  | PCB  |      U202      | Powered on | Preparation | Initial ΔV | Hours to plateau | .1-10Hz noise before | Special |
| --- | ---- | -------------- | ---------- | ----------- | ---------- | ---------------- | -------------------- |---------|
|   1 | 0.4  | ADR1000A 2017  | Jul 2021   |1yr dummy circuit| no data|                  |                      | VPG golden network |
|   2 | 0.4  |    LTZ1000A    | Apr 2022   | none        | no data    |                  |                      | LTZ1000A w/ VPG foil |
|   3 | 0.5  |    LTZ1000A    | Mar 2022   | none        | no data    |                  |                      | Cheapest LTZ variant |
|   4 |0.5SE |    ADR10001    | May 2022   | none        | no data    |                  |                      | ~~Popcorn noise~~ Healed? |
|   5 | 0.9  | ADR1000A 2022  | Jan 2023   | 7d 150°C b&b|            |                  |                      | Gone to new owner |
|   7 | 0.9  | ADR1000A 2022  | Jan 2023   | 7d 150°C b&b|            |                  |                      | No trim resistors |
|   9 | 0.9  | ADR1000A 2022  | Jan 2023   | none        | 1.1 µV/V   | 310              |                      | VPG golden network |
| 107 | 0.9  | ADR1000A 2018  | Dec 2022   | none        | 3.8 µV/V   | 640              |                      | Transplant to 108 |
| 108 | 0.9  | ADR1000A 2018  | Dec 2022   | none        | 3.8 µV/V   | 640              |                      | Gone to new owner |
|  10 | 0.9  | ADR1000A 2022  | Feb 2023   | none        |            |                  |                      | On/off cylcing 48h |
|  11 | 0.9  | ADR1000A 2022  | Feb 2023   |7d dummy circuit|         |                  |                      | No trim resistors |
|  12 | 0.9  | ADR1000A 2022  | Feb 2023   |7d in situ b&b|           |                  |                      | On/off cylcing 24h |
|  13 | 0.9  | ADR1000A 2022  | Feb 2023   |             |            |                  |                      | Ultrasonic cleaned |
|   6 | 1.1  | ADR1000A 2022  | Mar 2023   |30d dummy circuit|        |                  |                      | Chinese SMT assembly |
|  14 | 1.1  | LTZ1000A 2020  | Mar 2023   | none        |            |                  |                      | Chinese SMT assembly |
|  15 | 1.1  | LTZ1000A 2020  | Mar 2023   | none        |            |                  |                      | Chinese SMT assembly |
|  44 | 1.1  | LTZ1000A 2020  | Mar 2023   | none        |            |                  |                      | Chinese SMT assembly |
|  20 | 1.1  | LTZ1000A 2020  | Sep 2023   | none        |            |                  |                      | Chinese SMT assembly |

## Trim levels

The PCB is prepared for various configurations to adapt to different needs and part availabilities. Here's what I have built so far:

| SN  | U202 | R213 / Pin4 | R214 / Pin5 | R220 / Pin3 | Oven divider      | R225 / Iz Down | R223 / Iz Up | 10V gain divider |
| --- | ---- | ----------- | ----------- | ----------- | ----------------- | -------------- | ------------ | ---------------- |
|   1 | ADR  | 1445 95.3R  | 1445 61.9k  | 0R          | 1445 13 ratio     | open           | open         | 1445 2 ratio     |
|   2 |LTZ-A | Z201 100R   | 61.9k  Foil | SMD Foil    | VHD200 13 ratio   |                |              | VHD200 2.5 ratio |
|   3 |LTZ-A | 100R TOMC   | 50k S102    | 100R TOMC/5 | TDP10k 13.5 ratio | open           | 230k RN73    | TDP10k 2.5 ratio |
|   4 |ADR1k1| 100R VHP100T| integrated  | integrated  | integrated        |                |              | integrated       |
|   5 | ADR  | Alpha MCY   | Alpha MAY   | 0R          | TDP10k 11.5 ratio | open           | 470k RN73    | TDP10k 2 ratio   |
|   7 | ADR  | Z201        | Z201        | 0R          | TDP10k            | open           | open         | TDP10k 2 ratio   |
|   9 | ADR  | 1445 95.3R  | 1445 61.9k  | 0R          | 1445 13 ratio     | open           | open         | 1445 2 ratio     |
| 107 | ADR  | Z201T       | Z202T       | 0R          | TOMC10k 11.5 ratio| 200k RN73      | open         | TDP10k 2 ratio   |
| 108 | ADR  | Z201T       | Z202T       | 0R          | TOMC10k 11.5 ratio|                |              | TDP10k 2 ratio   |
|  10 | ADR  | RCK02       | RCK02       | 0R          | TDP10k 11.5 ratio | 493k RN73      | open         | TDP10k 2 ratio   |
|  11 | ADR  | Z201T       | Z201T       | 0R          | TDP10k 11.5 ratio |                |              | TDP10k 2 ratio   |
|  12 | ADR  | RCK02       | RCK02       | 0R          | TDP10k 12 ratio   | 1M             | open         | TDP10k 2 ratio   |
|  13 | ADR  | RCK02       | RCK02       | 0R          | TDP10k 11.5 ratio | open           | 1M           | TDP10k 2 ratio   |
|   6 | ADR  | PTF56       | PTF56       | 0R          | TDP10k 11.5 ratio |                |              | TDP10k 2 ratio   |
|  14 |LTZ-A | TDP         | 1% ax metal | TDP         | TDP10k 12   ratio | open           | open         | TDP10k 2.5 ratio |
|  15 |      |             |             |             |                   |                |              |                  |
|  44 | ADR  | Z201T       | Z202T       | 0R          | TDP10k 11.5 ratio | 900k           | open         | TDP10k 2 ratio   |
|  20 |LTZ-A | 100R TDP    | 40k Prec WW | 16.667R TDP | TDP10k 11.5 ratio | open           | 1M           | TDP10k 2.5 ratio |

## Raw Vz of 10 parts in datasheet default circuit, warmed up for a few minutes but not burnt in
| SN  |   Type  | Datecode |     Vz    | 
| --- | ------- | -------- | --------- |
| \#1 | ADR1000 | 2108     | 6.6556730 |
| \#8 | ADR1000 | 2108     | 6.6545676 |
| \#9 | ADR1000 | 2108     | 6.6531460 |
| \#10| ADR1000 | 2108     | 6.6609841 |
| \#11| ADR1000 | 2108     | 6.6690263 |
| \#12| ADR1000 | 2108     | 6.6534043 |
|   5 | ADR1000 | 2209     | 6.6457519 |
|   8 | ADR1000 | 2209     | 6.6509818 |
|   3 | ADR1000 | 1839     | 6.6707478 |
| \#7 | ADR1000 | 2108     | 6.6545726 |

### ADR1000 & Vishay 1445 All-in-one Resistor Network

My SN 1 is built this way. This is a no-brainer or easy mode. When I got my first glimpse at the ADR1000 datasheet I went straight to Vishay Foil Resistors and ordered an all-in-one resistor network with all the critical resistors from the datasheet plus a simple divider for buffering the 6.62V output to 10V ([Custom network specification][1445]). By specifying at least 2 ppm/°C TC tracking for the two critical dividers I am guaranteed great performance. And thanks to the hermetically sealed DIP14 package I expect little long term drift from the resistors. This solution comes at a hefty price and is not effortlessly adjustable after assembly.

[1445]:/datasheets/322146_p1-4_1445_Marco_Reps.pdf

### LTZ1000A & Discrete Vishay Foil Resistors

My SN 2 is built this way. This is probably the most popular way of building LTZ1000 voltage standards (i.e. [xDevs KX][kx]). Digikey carries quite a few hermetically sealed Vishay Bulk Metal Foil resistors ~~without MOQ these days~~ not any more LAME!, giving you all the design freedom. The two most critical parts are the LTZ-temperature-configuration divider i.e. 13k/1k and the 7.1V to 10V buffer divider i.e. 2k/5k. For these two I used hermetically sealed Vishay VHD200 dividers. These have guaranteed TC tracking and little long term drift. The remaining LTZ-configuration resistors i.e. 70k, 70k, 120R are not very critical. For best performance you can add an additional resistor to LTZ pin 3 to improve the Vrefs tempco, see "Adjusting Temperature Coefficient in Unstabilized Applications" in the LTZ1000 datasheet. 20 Ohm seems to be a reasonable approximation, suitable for most LTZs. In my case I determined 18 Ohm to be an optimal resistor with a TC peak at the oven setpoint. Careful, this additional resistor, if equipped, has a lot of influence on zener voltage and should be of high quality.

[kx]:https://xdevs.com/article/kx-ref/

### LTZ1000A & Thin film arrays

My SN 3 and 20 are built this way. This variant is inspired by Datron Wavetek 7000 DCV Standards ([EEVBlog forum thread][w7000]) and as such it has proven itself over a long time. Here the most critical voltage dividers for the LTZ1000 temperature and the 7->10V gain are implemented through an arrangement of monolithic thin film resistor arrays and their fantastic tracking temperature coefficients. Furthermore the overall output voltage tempco is fine-tuned after assembly through trim resistors R225 / R223. SN 3 is one of the cheapest ADRmus in my comparison, yet one of the most stable ones.

[w7000]:https://www.eevblog.com/forum/metrology/(3300)-wavetek-7000-the-hidden-gemstone/

### ADR1000 & Thin film arrays

Most of my ADRmus are built this way. This is the most cost-effective way to build a great performance 10V DC Standard. The same techniques that worked for LTZ in the past also apply to ADR1000, only the specific resistor values are slightly different. Based on my early ADR1000 samples I can see significantly longer initial settling times of ADR1000, which can be improved simply by power cycling a part in its default circuit (30 minutes off, 30 minutes on for a week). This new part exhibits lower low frequency noise than LTZ. A 10V buffer circuit with a low noise op amp and thin film arrays ([Excess Noise in Thin Film and Metal Foil Resistor Networks][beev]) passes this advantage right on to the output. 

[beev]:https://arxiv.org/abs/2109.02448

### ADR1001

I have been given one very early sample of this new part, so my results may not reflect the final parts performance. This new all-in-one ovenized zener reference & buffer makes it easier than ever before to deploy a high performance, environmentally tolerant voltage reference with few external parts and little research. My sample showed some popcorn noise at first ([Screenshot][popcorn]), which I seemingly improved by keeping the part powered on, externally heated to 110°C for a few weeks. This extreme measure made it impossible to judge early drift. Long-term drift and tempco now seem to fall easily within the datasheet spec. LF noise of the 10V output still appears to be slightly elevated, but the datasheet only specifies this for the 6P6 output. Overall this part is not the greatest performer in my comparison, it lacks a way of fine-tuning, but it's by far the easiest to use and its efficient overall heater makes it interesting for portable devices.

[popcorn]:/results/ADRmu4_LFnoise_popcorn.png

## Results

### Raw data

Unprocessed CSV files can be found here https://github.com/marcoreps/multiinstrumentalist/tree/master/csv These show direct readings by digital voltmeters, which are subject to temperature variations, adjustments and even modifications, resulting in large deviations of readings.

### Processed data

To attenuate voltmeter errors from the measurements, we use the mathematical difference between an ADRmu reading and the average of many ADRmu readings that were taken at the same time, with the same voltmeter. These results can be found here https://github.com/marcoreps/ADRmu/tree/main/results
