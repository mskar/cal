# Metric Clock

Clock component [what happens if there’s an alarm with less than 1 day remaining] (what does the on-hover modal display) {what does the on-click modal display}

1.  Cyan “seconds remaining in current minute” countdown [turns into white “HHMMSS time until next alarm”countdown] (if there is at least one alarm, a list of HHMMSS times remaining in alarms, otherwise hover does nothing) {current HHMMSS time and text fields to enter HHMMSS time remaining for new alarms}
2.  Cyan HHMMSS time (current “YYYY-MM-DD HHMM” timestamp and the “YYYY-MM-DD HHMM” timestamps of set alarms) {current YYYY-MM-DD date and HHMMSS time and text fields for entry of YYYY-MM-DD date and HHMM time pairs to set alarms}
3.  Green centimilliday metric time (current YYYY-DDD.microdays timestamp and the YYYY-DDD.microdays timestamps of set alarms) {current YYYY-DDD.microdays timestamp and text fields for entry of YYYY-DDD.microdays timestamps to set alarms}
4.  Green “centimillidays remaining in current milliday” countdown [turns into yellow “centimillidays remaining until next alarm“ countdown] (if there is at least one alarm, a list of centimillidays remaining in alarms, otherwise hover does nothing) {current centimilliday time and text fields to enter centimillidays time remaining for new alarms}

Next steps:

-   After after 1 decimilliday (8.64 seconds) of inactivity, the display changes
	from
	```
			59
	160001
	 66666
			34
	```
	to
	```
	1600
	 666
	```
	- Components 2 and 3 are hidden. In components 2 and 3, seconds and centimillidays are hidden, leaving only HHMM and milliday. The font size increases greatly (133%) and the text is centered in the middle of the rings. All changes are undone by user activity. The transition should be smooth in both directions.
-   Add an on-hover modal to component 2 that shows the current “YYYY-MM-DD HHMM” timestamp
-   Add an on-hover modal to component 3 that shows the current YYYY-microdays timestamp for component 3
-   Add a button to toggle between ISO Ordinal Date, ISO Week Date, and ISO Calendar Date modes in the on-hover modal of component 2
-   Add a button to toggle between ISO Ordinal Date, ISO Week Date, and ISO Calendar Date modes in the on-hover modal of component 3
-   Add an on-click modal to component 2 to set “YYYY-MM-DD HHMM” alarms
-   Add an on-click modal to component 3 to set YYYY-microdays alarms
-   Add an “YYYY-MM-DD HHMM” alarm list to the on-hover modal of component 2
-   Add an YYYY-microdays alarm list to the on-hover modal of component 3
-   Add the ability to set alarms in all 3 modes (ISO Ordinal Date, ISO Week Date, and ISO Calendar Date) to component 2
-   Add the ability to set alarms in all 3 modes (ISO Ordinal Date, ISO Week Date, and ISO Calendar Date) to component 3

**Useful conversion points:**

- 27 seconds = 312.5 microday = 31.25 centimilliday
- 54 seconds = 625 microday
- 9 minutes = 6.25 milliday = 625 centimilliday
- 18 minutes = 12.5 milliday = 125 centimilliday
- 36 minutes = 25 milliday = 250 centimilliday
- 1.2 hours = 50 milliday
- 3 hours = 125 milliday

## Count by 9s

| Milliday | Minutes | Hours  | Duration   | Factor |
| ---      | ---     | ---    | ---        | ---    |
| 0.3125   | 0.45    | 0.0075 | 0h 0m 27s  | 0.5    |
| 0.625    | 0.9     | 0.015  | 0h 0m 54s  | 1      |
| 1.25     | 1.8     | 0.03   | 0h 1m 48s  | 2      |
| 1.875    | 2.7     | 0.045  | 0h 2m 42s  | 3      |
| 2.5      | 3.6     | 0.06   | 0h 3m 36s  | 4      |
| 3.125    | 4.5     | 0.075  | 0h 4m 30s  | 5      |
| 3.75     | 5.4     | 0.09   | 0h 5m 24s  | 6      |
| 4.375    | 6.3     | 0.105  | 0h 6m 18s  | 7      |
| 5        | 7.2     | 0.12   | 0h 7m 12s  | 8      |
| 5.625    | 8.1     | 0.135  | 0h 8m 6s   | 9      |
| 6.25     | 9       | 0.15   | 0h 9m 0s   | 10     |
| 6.875    | 9.9     | 0.165  | 0h 9m 54s  | 11     |
| 7.5      | 10.8    | 0.18   | 0h 10m 48s | 12     |
| 8.125    | 11.7    | 0.195  | 0h 11m 42s | 13     |
| 8.75     | 12.6    | 0.21   | 0h 12m 36s | 14     |
| 9.375    | 13.5    | 0.225  | 0h 13m 30s | 15     |
| 10       | 14.4    | 0.24   | 0h 14m 24s | 16     |
| 10.625   | 15.3    | 0.255  | 0h 15m 18s | 17     |
| 11.25    | 16.2    | 0.27   | 0h 16m 12s | 18     |
| 11.875   | 17.1    | 0.285  | 0h 17m 6s  | 19     |
| 12.5     | 18      | 0.3    | 0h 18m 0s  | 20     |
| 13.125   | 18.9    | 0.315  | 0h 18m 54s | 21     |
| 13.75    | 19.8    | 0.33   | 0h 19m 48s | 22     |
| 14.375   | 20.7    | 0.345  | 0h 20m 42s | 23     |
| 15       | 21.6    | 0.36   | 0h 21m 36s | 24     |
| 15.625   | 22.5    | 0.375  | 0h 22m 30s | 25     |
| 16.25    | 23.4    | 0.39   | 0h 23m 24s | 26     |
| 16.875   | 24.3    | 0.405  | 0h 24m 18s | 27     |
| 17.5     | 25.2    | 0.42   | 0h 25m 12s | 28     |
| 18.125   | 26.1    | 0.435  | 0h 26m 6s  | 29     |
| 18.75    | 27      | 0.45   | 0h 27m 0s  | 30     |
| 19.375   | 27.9    | 0.465  | 0h 27m 54s | 31     |
| 20       | 28.8    | 0.48   | 0h 28m 48s | 32     |
| 20.625   | 29.7    | 0.495  | 0h 29m 42s | 33     |
| 21.25    | 30.6    | 0.51   | 0h 30m 36s | 34     |
| 21.875   | 31.5    | 0.525  | 0h 31m 30s | 35     |
| 22.5     | 32.4    | 0.54   | 0h 32m 24s | 36     |
| 23.125   | 33.3    | 0.555  | 0h 33m 18s | 37     |
| 23.75    | 34.2    | 0.57   | 0h 34m 12s | 38     |
| 24.375   | 35.1    | 0.585  | 0h 35m 6s  | 39     |
| 25       | 36      | 0.6    | 0h 36m 0s  | 40     |
```
0900 0936 1012 1048 1124
 375  400  425  450  475

1200
 500
```

## Count by fractions

```
T03 T04 T06 T08 T09 T12 T15 T16 T18 T20 T21
1/8 1/6 1/4 1/3 3/8 1/2 5/8 2/3 3/4 5/6 7/8
125 166̅ 250 333̅ 375 500 625 666̅ 750 833̅ 875
```


Start work at 375 milliday = 9AM
Finish work at 700 milliday = 1648 = 4:48PM
or at 725 = 1724 = 5:24PM

## Count by sixteenths

1/16 of day is 0.0625d = 62.5 decimilliday = 90 minutes

| Frac. | Decimal | Duration |
| ---   | ---     | ---      |
| 1/16  | 0.0625  | 1h 30m   |
| 1/8   | 0.125   | 3h       |
| 3/16  | 0.1875  | 4h 30m   |
| 1/4   | 0.25    | 6h       |
| 5/16  | 0.3125  | 7h 30m   |
| 3/8   | 0.375   | 9h       |
| 7/16  | 0.4375  | 10h 30m  |
| 1/2   | 0.5     | 12h      |
| 9/16  | 0.5625  | 13h 30m  |
| 5/8   | 0.625   | 15h      |
| 11/16 | 0.6875  | 16h 30m  |
| 3/4   | 0.75    | 18h      |
| 13/16 | 0.8125  | 19h 30m  |
| 7/8   | 0.875   | 21h      |
| 15/16 | 0.9375  | 22h 30m  |
| 1     | 1       | 1d       |


# Component 1 design notes

1.  Alarms set in the component 1 on-click modal are stored in HHMMSS format
2.  The maximum number of hours is very high (16 digits, alarms outside the range are only shown in component 2). The timer will only be displayed in component 1 if it can fit within 22 digits, if it is more than that it does not show up on the clock (which will continue to count down from a minute in cyan rather than count from the alarm time remaining in white) and flashes “>=1e17 hours” in the on-hover modal
3.  The default timer is 9 minutes
4.  Alarms are sorted from least to most time
5.  Recurring alarms are only shown once (a new alarm with PnX duration is created after the old one runs out)

Buttons:

-   Delete alarm
-   Clone alarm
-   Pause/resume alarm

Format:

```
HH:MM:SS
```

Width: 22

Alignment: right

# Component 2 design notes

1.  Alarms set in the component 2 on-click modals are stored in HHMMSS format, but seconds are omitted in the ISO Week Date and ISO Calendar Date modes of the component 2 on-hover and on-click modals
2.  There are different text entry fields depending on the mode:
3.  ISO ordinal date mode:
	1.  Year
	2.  Day of the year
	3.  HH
	4.  MM
	5.  SS
4.  ISO week date mode:
	1.  Year
	2.  Week
	3.  Day of the week
	4.  HH
	5.  MM
5.  ISO calendar date mode:
	1.  Year
	2.  Month
	3.  Day of the month
	4.  HH
	5.  MM
6.  All 5 have validation checks:
	1.  \d{4}, minimum=current year
	2.  \d{2}, minimum=1, maximum=12 or 54
	3.  \d{2} or \d, minimum=1, maximum=31 or 7
	4.  \d{2}, minimum=0, maximum=23
	5.  \d{2}, minimum=0, maximum=59
	6.  \d{7}, minimum=0, maximum=7654321
7.  All 6 have defaults:
	1.  current year
	2.  current month
	3.  tomorrow
	4.  07
	5.  00
	6.  0 (No recurrence)
8.  Alarms can only recur every 1-99 years/months/weeks/days (recurrence by the hour minute or second is not allowed), i.e. X can only be Y, M, W, or D
9.  Blanks in the on-hover modal indicate a value that is the same as the value above (avoids repetition). All values are always shown in the on-click modal.
10. Multiple levels of recurrence are allowed, with values being separated by commas during input
	1. If the number of R values is greater than the number of P values, the last P value is repeated as many times as needed.
	2. If the number of P values is greater than the number of R values, the superfluous P values are ignored.
	3. To make sure everything is aligned, the maximum display width is 22 characters:
      - R values greater than one character are truncated, i.e. they are replaced by an ellipsis (…) character.
      - P values greater than two characters are truncated, i.e. they are replaced by two ellipsis (…) characters.
      - Truncated values are revealed upon hover or click

Buttons:

-   Toggle between ISO Week Date mode (Default), ISO Calendar Date mode, and ISO Ordinal Date mode
-   Delete alarm
-   Clone alarm

Examples:

Input:
```
Rn/yyyy-mm-ddThhmm/PnX
R5/2023-05-01T1600/P1D
```

Display:
```
R5/2023-05-01T1600/P1D
```
Meaning: repeat five times on a daily basis, i.e.
```
Rn/yyyy-mm-ddThhmm/PnX
   2023-05-01T1600
   2023-05-02T1600
   2023-05-03T1600
   2023-05-04T1600
   2023-05-05T1600

Rn/yyyy-Www-dThhmm/PnX
   2023-W18-1T1600
   2023-W18-2T1600
   2023-W18-3T1600
   2023-W18-4T1600
   2023-W18-5T1600

Rn/yyyy-dddThhmmss/PnX
   2023-121 160000
   2023-122 160000
   2023-123 160000
   2023-124 160000
   2023-125 160000
R4/2023-05-01T1600/P1W
```

---

Input:
```
Rn/yyyy-mm-ddThhmm/PnX
R2/2023-05-01T1600/P2D
```

Display:
```
R2/2023-05-01T1600/P2D
```

Meaning: Repeat twice every two days (e.g. Tuesday and Thursday)

---

Input:
```
Rn/yyyy-mm-ddThhmm/PnX
R2/2023-05-02T1600/P2D
```

Display:
```
R3/2023-05-01T1600/P2D
```

Meaning: Repeat thrice every two days (e.g. Monday & Wednesday & Friday) i.e.


Input:
```
Rn,nn/yyyy-mm-ddThhmm/PnX,nX
R3,16/2023-05-01T1600/P2D,1W
```

Display:
```
R…/2023-05-01T1600/P……
```
Meaning: Repeat the MWF recurrence on a weekly basis for 16 weeks

---

Input:
```
Rn/yyyy-mm-ddThhmm/PnX
R4/2023-05-01T1600/P1W
```

Display:
```
R4/2023-05-01T1600/P1W
```

Meaning: repeat four times on a weekly basis:
```
Rn/yyyy-mm-ddThhmm/PnX
   2023-05-01T1600
   2023-05-08T1600
   2023-05-15T1600
   2023-05-22T1600

Rn/yyyy-Www-DThhmm/PnX
   2023-W18-1T1600
   2023-W19-1T1600
   2023-W20-1T1600
   2023-W21-1T1600

Rn/yyyy-dddThhmmss/PnX
   2023-121T160000
   2023-122T160000
   2023-123T160000
   2023-124T160000
```

Width: 22

# Component 3 design notes

1.  Alarms set in the component 3 on-click modals are stored in microdays, but only decimillidays are shown in the ISO Week Date and ISO Calendar Date modes of the component 3 on-hover and on-click modals
2.  There are different text entry fields depending on the mode:

3.  ISO ordinal date mode:

	1.  Year
	2.  Day of the year
	3.  Milliday
	4.  Microday

4.  ISO week date mode:

	1.  Year
	2.  Week
	3.  Day of the week
	4.  Milliday
	5.  Decimilliday

5.  ISO calendar date mode:

	1.  Year
	2.  Month
	3.  Day of the month
	4.  milliday
	5.  decimilliday

6.  All of the above have validation checks:

	1.  Year: \d{4}, minimum=current year
	2.  Day of the year: \d{3}, minimum=1, maximum=366
	3.  Day of the month: \d{2}, minimum=1, maximum=31
	4.  Day of the week: \d, minimum=1, maximum=7
	5.  Week: \d{2}, minimum=1, maximum=53
	6.  Month: \d{2}, minimum=1, maximum=12
	7.  Milliday: \d{3}
	8.  Decimilliday: \d
	9.  Microday: \d{3}

7.  All of the above have defaults:

	1.  Year: current year
	2.  Day of the year: tomorrow
	3.  Day of the month: tomorrow
	4.  Day of the week: tomorrow’s day of the week
	5.  Week: tomorrow’s month
	6.  Month: tomorrow’s month
	7.  Milliday: 300 (7:12AM)
	8.  decimilliday : 0
	9.  microday: 000

8.  If the entry for milliday ends in any number other than 5, that number is repeated for decimilliday and microday, i.e. 00, 11, 22, 33, 44, 66, or 88. If the entry for milliday ends in 5, the decimilliday and microday fields are filled with zeros.
9.  Alarms can only recur every 1-9 years/months/weeks/days (recurrence by the hour minute or second is not allowed), i.e. X can only be Y, M, W, or D
10.  Blanks in the on-hover modal indicate a value that is the same as the value above (avoids repetition). All values are always shown in the on-click modal.
11. Multiple levels of recurrence are allowed, with values being separated by commas during input
	1. If the number of R values is greater than the number of P values, the last P value is repeated as many times as needed.
	2. If the number of P values is greater than the number of R values, the superfluous P values are ignored.
	3. To make sure everything is aligned, the maximum display width is 22 characters:
      - R values greater than one character are truncated, i.e. they are replaced by an ellipsis (…) character.
      - P values greater than two characters are truncated, i.e. they are replaced by two ellipsis (…) characters.
      - Truncated values are revealed upon hover or click

Buttons:

-   Toggle between ISO Calendar Date (Default), ISO Week Date, and ISO Calendar Date
-   Delete alarm
-   Clone alarm

Examples:

```
Rn/yyyy-mm-dd.dddd/PnX
R7/2023-05-01.6666/P1D
```

Means repeat seven times on a daily basis:

```
Rn/yyyy-ddd.dddddd/PnX
   2023-121.666666
   2023-122.666666
   2023-123.666666
   2023-124.666666
   2023-125.666666
   2023-126.666666
   2023-127.666666

Rn/yyyy-mm-dd.dddd/PnX
   2023-05-01.6666
   2023-05-02.6666
   2023-05-03.6666
   2023-05-04.6666
   2023-05-05.6666
   2023-05-06.6666
   2023-05-07.6666

Rn/yyyy-Www-d.dddd/PnX
   2023-W18-1.6666
   2023-W18-2.6666
   2023-W18-3.6666
   2023-W18-4.6666
   2023-W18-5.6666
   2023-W18-6.6666
   2023-W18-7.6666
```

Width: 22

# Component 4 design notes

1.  Alarms set in the component 4 on-click modal are stored in microday format, but displayed as centimillidays
2.  The maximum number of days is very high (18 digits, alarms outside the range are only shown in component 3), the timer will only be displayed in component 4 if it can fit within 22 digits for centimillidays, if it is more than that it does not show up on the clock (which will continue to count down from a milliday in green rather than count from the alarm time remaining in yellow) and flashes “>=1e23 centimillidays” in the on-hover modal
3.  default value of 625 centimillidays (9 minutes, 9 / 0.0144)
4.  Alarms are sorted from least to most time
5.  Recurring alarms are only shown once (a new alarm with PnX duration is created after the current one runs out)

Buttons:

-   Delete alarm
-   Clone alarm
-   Pause/resume alarm

Format:  centimillidays

Alignment: right

Width: 22

Examples:

9 minutes
```
                   625
```

18 minutes
```
                  1250
```

54 minutes
```
                  3750
```

63 minutes
```
                  4375
```

1 day
```
                100000
```

1.5 days
```
                150000
```

1 week
```
                700000
```

1 year
```
              36500000
```

**Older descriptions (may not longer apply):**

-   “seconds in current minute” cyan ring [ends in a “seconds remaining before alarm” white ring that ends with a red dot]: pop up shows current hover position and the length of cyan ring and white ring (next alarm only)
-   “centimillidays in current milliday” green ring [and “centimillidays remaining in current milliday before alarm” yellow ring that ends with a red dot]: pop up shows current hover position and the length of green ring and yellow ring (next alarm only)
-   “centimillidays in current day” greenring [and “centimillidays remaining in current day before alarm” yellow ring that ends with a red dot]: pop up shows current hover position and the length of green ring and yellow ring (next alarm only)


Outer green ring that shows current time in centimillidays (proportion of day completed) outside the first green ring.

Setting an alarm or timer for more than a milliday adds a red dot on top of the track of the outside green ring. A yellow ring shows the time remaining before the end of the outer green ring meets the red dot. If the time left is less than a milliday, a red circle is added on top of the track of the inside green ring. A yellow ring shows the time remaining before the inner green ring meets the red circle. If the time left is less than a minute, a red circle is added on top of the track of the cyan ring. A white ring shows the time remaining before the cyan ring meets the red circle. The red circles on the ring tracks only appear when when the time remaining is sufficient (difference between microdays/seconds remaining in timer versus microdays/seconds remaining in day/milliday/minute). The red circles and yellow/white rings move with the green/cyan ring until the timer/alarm is started and then the red circle stays in place while the yellow/white ring diminishes as the green/cyan ring consumes it.

Next steps:

1.  HHMMSS timer, add a red text entry field above the cyan time. Entering the time, begins a countdown.
2.  Metric timer, add a red text entry field below the green time.
3.  Have the timers update each other, translating HHMMSS time to metric time and vice versa.
4.  Add red dots to the rings when appropriate
5.  Add yellow/white rings when red dots appear

Clicking on cyan time activates text fields to set an alarm (cyan) where the time was displayed and the time remaining (red) above where the time was displayed.

Clicking on green time activates text fields to set an alarm (green) where time was displayed and the time remaining (red) below  where the time was displayed. Clicking elsewhere deactivates the text field and shows the time again.

Reach goal: Add popups on hover over all of the objects

Reach goal: Make the red circles slide-able with a click-and-drag of the mouse, so that the text input is not the only way to adjust a timer/alarm. Add a red circle with a click to any of the rings, so that the text input is not the only way to set a timer/alarm.
