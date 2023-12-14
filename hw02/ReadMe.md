1.	What's the min and max voltage?
Min = 231mV
Max = 259mV
2.	What period and frequency is it?
3.	Period = 1.025s Freq = 0.976Hz
4.	Run htop and see how much processor you are using.
5.	0.7%
4. Try different values for the sleep time. What's the shortest period you can get? Make a table of the fastest values you try and the corresponding period and processor usage. Try using markdown tables: https://www.markdownguide.org/extended-syntax/#tables
The shortest period is 400us
5. How stable is the period?
The period is not stable when CPU goes over 80%. However the frequency reaches its maximum around 40Hz, which only use 50% of the GPU.
6.	Try launching something like vi. How stable is the period?
Opening vi decrease the stability of the period
7.	Try cleaning up blinkLED.sh and removing unneeded lines. Does it impact the period?
I removed the sleep inbetween toggle
8. What's the shortest period you can get?
The shortest period is around 400us





Python
Modify blinkLED.py to toggle a gpio pin as fast as possible.
1.	What period and frequency is it?
Period:2.68ms	Frequency:380Hz
2.	Run htop and see how much processor you are using.
70%
3.	Present the shell script and Python script results in a table for easy comparison.

Modify blinkLED.c to toggle a gpio pin as fast as possible.
1.	What period and frequency is it?
Period:300us	Frequency:3.3kHz
2.	Run htop and see how much processor you are using.
16%
3.	Present the shell script and Python script results in a table for easy comparison.
|---|Python|Shell|C|Toggle1(py)|Toggle1(C)|Toggle2(py)|Toggle2.c|
|Min Period|286us|460us|295us|20us|40us|20us|455us|
|Max Freq(Hz)|3.5k|2k|3.4k|50k|25k|50k|3k|
|CPU Usage|70%|100%|16%|100%|100%|100%|100%|

