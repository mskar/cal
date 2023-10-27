# Digital calendar

4 main modes:

-   Year: “One week per 1 row” mode
	-   Landscape: 1 week per row on each half of the screen for a total of 140 weeks, 9 from the previous year, 52 or 53 from the current year, 52 or 53 from the next year, and 36 or 35 weeks from the year after next, scrolling works one year at a time with each subsequent year taking the place of the current year, each half on the screen has seven weekday columns to the right of the date interval column
	-   Portrait: 1 week per row on the entire screen for a total of 70 weeks, 9 from the previous year, 52 or 53 from the current year, and 9 or 8 weeks from the next year, scrolling works one year at a time with 8 or 9 weeks of overlap every time, there are seven weekday columns to the right of the date interval column
	
-   Month: “One day per 2 rows” mode
	-   Landscape: 5 weeks / 35 days across 70 rows on each half of the screen, scrolling is organized into blocks of 10 weeks with no overlap and the current week in the middle of the left half, so that the two previous weeks and the next 7 weeks are visible
	-   Portrait: 5 weeks / 35 days across 70 rows on the entire screen, scrolling is organized into blocks of 5 weeks with no overlap and the current week in the middle of the screen, so that the two previous weeks and the next two weeks are visible
-   Week: “One day per 10 rows” mode (1 week across 70 rows on the screen)
	-   Landscape: The current week is the entire left half of the screen and the next week is on the right half, each occupy 70 rows on their respective halves, so that scrolling moves two weeks at a time with no overlap
	-   Portrait: The current week occupies 70 rows on the entire screen, so that scrolling moves one week at a time with no overlap
-   Day:
	-   Landscape: The current day is the entire left half of the screen and the next day is on the right half, each occupy 70 rows on their respective halves, so that scrolling moves two days at a time with no overlap
	-   Portrait: The current day occupies 70 rows on the entire screen, so that scrolling moves one day at a time with no overlap

The number of rows in view is always 70 for all 4 modes.

The structure does not change when scrolling. Only the values are recalculated. The structure only changes when switching between modes.

Overall, the four main modes and two orientations make eight modes:
-   Day:
	-   1-day mode (portrait)
	-   2-day mode (landscape)
-   Week:
	-   1-week mode (portrait)
	-   2-week mode (landscape)
-   Month:
	-   5-week mode (portrait)
	-   10-week mode (landscape)
-   Year:
	-   70-week mode (portrait)
	-   140-week mode (landscape)

  
Add 5 columns to the 5-week mode?

Each column adds 36 minutes

```
0900 0936 1012 1048 1124

 375  400  425  450  475
```

No, don’t add vertical lines (columns), but a diagram showing vertical lines can be added to the documentation to explain how to use the calendar. 

For mobile, portrait modes show one page of 70 rows. In landscape mode mode, there are two pages shown side by side (this is the default view for computer monitors). Landscape mode allows users to see 2.69 years, 10 weeks, 2 weeks, or 2 days at a time, whereas portrait mode shows 1.346 years, 5 weeks, 1 week, or 1 day at a time, depending on the mode. The landscape and portrait modes aspect ratios are 16:9 versus 9:16, respectively. This impacts the row length but not the row count (the number of rows in view) which is always 70.

# Clock functionality in the Digital Calendar

**Calendar Modes**
-   Day:
	-   1-day mode (portrait)
	-   2-day mode (landscape) 
-   Week:
	-   1-week mode (portrait)
	-   2-week mode (landscape)
-   Month:
	-   5-week mode (portrait)
	-   10-week mode (landscape)
-   Year:
	-   70-week mode (portrait)
	-   140-week mode (landscape)

**“Proportion of day passed” line**

The current day is highlighted in all three modes and shows a line that indicates how much of the current day has passed.  In the year mode, the line is vertical and moves left to right. In the other two modes, the line is horizontal and moves top to bottom. 

Hovering over this line in year mode shows a short version of the clock, either to the left or to the right of the line, wherever there’s more room:

```
1600 |
 666 |
```

```
| 0900
|  375
```

Hovering over this line in the other two modes reveals a short version of the clock, either above or below the line, wherever there’s more room:

```
1600
 666
———-
```

```
———-
0900
 375
```

Clicking on the line in the calendar brings up the timer on-click modal from the clock.

The line and on-hover clock are most useful in the week (“one week per page”) mode, because times are listed there:

```
000
125
250
375
500
625
750
875
```

## Navigation between modes

The year mode has week numbers in the leftmost column. Clicking on a week number switches to that week in the middle of the “five weeks per page” mode. Clicking on one of the dates to the right of the week number in year mode, opens that date in the week (“one week per page”) mode. Similarly, clicking on a date in the month mode opens that date in the week (“one week per page”) mode and clicking on a date in the week mode opens that date in the day (“one day per page”) mode. 

Year->month->week->day

Year->week->day

Only Sundays and Mondays are visible as dates in year mode, while the other modes list all dates.

## Scheduler

Clicking on a text entry field in any of the modes opens the scheduling menu (scheduler). 

The year mode has seven columns for weekdays. These columns allow users to open specific days in the scheduler from the year mode.

I decided to have only one scheduling interface, but with 6 different modes:

```
Rn/yyyy-mm-dd.ddd/yyyy-mm-dd.ddd/PnX
Rn/yyyy-Www-d.ddd/yyyy-Www-d.ddd/PnX
Rn/yyyy-ddd.ddd/yyyy-ddd.ddd/PnX
Rn/yyyy-mm-ddThhmm/yyyy-mm-ddThhmm/PnX
Rn/yyyy-Www-dThhmm/yyyy-Www-dThhmm/PnX
Rn/yyyy-dddThhmm/yyyy-dddThhmm/PnX
```

The first datetime is the start, the second is the stop. The start and end times can be provided in either format and are shown in both formats when hovering over an event.

```
0900
 375

0936
 400
```

Only the first date is required. Other fields can be left empty to achieve various results:

**Whole day event**

-   Leave R, the times, and P blank for a whole day event:

-   Entry
```
R /2023-05-29.   /   -  -  .    /P
```

-   Display
```
   2023-05-29
```

**Multi-day event**

-   Leave R and time blank for a multi-day event repeated every day for period P:

-   Entry
```
R /2023-05-29.   /   -  -  .    /P7D
```

-   Display
```
   2023-05-29/P7D
```

**Alarm**

-   Leave R, end time, and P blank for an alarm:

-   Entry
```
R /2023-05-29.375/   -  -  .    /P
```

-   Display
```
   2023-05-29.375
```

**Event**

Leave R and P blank for an event:

-   Entry
```
R /2023-05-29.375/2023-05-29.500/P
```

-   Display
```
   2023-05-29.375/500
```

**Recurring alarm**

Leave end time blank for a recurring alarm:

-   Entry
```
R5/2023-05-29.375/    -  -  .   /P1W
```

-   Display
```
   2023-05-29.375/2023-05-29.500/P1W 
```

**Recurring event**

Leave nothing blank for a recurring event:

-   Entry
```
R5/2023-05-29.375/2023-05-29.500/P1W
```

-   Display
```
R5/2023-05-29.375/500/P1W
```

```
R5/2023-05-29.375/500/P1W
```
means 5 event starting on May 3rd from 9AM to noon on a weekly basis.

```
R5/2023-05-29.375/P1W
```
means 5 alarms starting on May 3rd at 9am on a weekly basis.

Note: in the mode shown above (Rn/yyyy-mm-dd.ddd/yyyy-mm-dd.ddd/PnX), the maximum number of characters (with no omitted fields) is 36. The mode with the greatest number of characters (38) is Rn/yyyy-mm-ddThhmm/yyyy-mm-ddThhmm/PnX.

**Calendar items**

The scheduling interface can be used to schedule 8 types of calendar items:

1.   Alarm: datetime
2.   Recurring alarm: R/datetime/P
3.   Event: 
	-   datetime/datetime
	-   datetime/P
4.   Recurring event: R/datetime/datetime/P
5.   Whole day event: date
6.   Multi-day event: 
	-   date/date
	-   date/P
7.   Recurring multi-day event: 
	-   R/date/P
	-   R/date/date/P
8.   Nested recurring events: Rn,n/date/PnX,nX

With R, the meaning of P changes from duration to the time between recurrences.

Multi-day events are contiguous. Recurring events can be noncontiguous.

-   Examples:

	-   Contiguous:
```
R5/2023-05-01/P1D
```
is the same as
```
   2023-05-29/P5D
```

-   Noncontiguous:
```
R5/2023-05-01/P1W
```

means 5 whole day events starting on 2023-05-29 that spaced one week apart (same day of the week)

Nested recurring events can recur at two different frequencies. For example, Mondays and Wednesdays on a weekly basis for 18 weeks:
```
R2,18/2023-05-01/P2D,1W
```

One clear use case for nested recurring events is scheduling university or training courses.

Mondays and Wednesdays on a weekly basis for 18 weeks every year for 3 years:
```
R2,18,3/2023-05-01/P2D,1W,1Y
```

Mondays and Wednesdays on a weekly basis for 16 weeks twice a year 8 months apart every year for 3 years:
```
R2,16,2,3/2023-01-16/P2D,1W,8M,1Y
```

This could cover 6 semesters over 3 years of a university course. The P8M can be adjusted to match the space between start of the spring semester and the start of the fall semester. The P1Y may need to be replaced with P52W to get the same days of the week in subsequent years. Honestly, a GUI will probably be necessary to set up something so complex, but this format is great because it can encode complex events as short strings.

To keep everything in alignment, R values greater 1 character should be replaced with an ellipsis character. Similarly, P values greater 2 character should be replaced with two ellipsis characters. This will keep all alarms to 22 characters and all events with two dates to 32 characters and events with dates and times to 38 characters, depending on the mode. The hidden values are revealed upon hover or click.
The example directly above would be displayed like this:
```
R…/2023-01-16/P……
```

There should be a tool that figures out the spacing between dates:
1.  Provide two dates
	Start of the Spring semester: January 16
	Start of the Fall semester: August 22
2.  Choose from the options
	Start on same day of month: P6M6D
	Start on same day of week: P25W

**Random Thoughts on Durations**

A duration can be provided instead of providing an end date for multi-day events.

Durations for time are not great because a T has to be added according to ISO 8601.

Plus and minus are already used for time zones so a duration using either of those symbols would be confusing.

With dates, metric time durations make more sense

```
2023-123.375/P.125D 
2023-05-03.375/P.125D 
2023-W18-3.375/P.125D 
```
all mean 9AM to noon on May 3rd.

Durations are good because an end date does not have to be provided and everything fits comfortably on one line.

Short metric time durations are not very readable in the the above format. 
Using 2 lines for the start (top) and end time (bottom) is much easier to read:
```
2023-123.375
         500
```
which means start at 9am and end noon the same day.

  
```
2023-123.875
2023-124.250
```
which means start at 9pm and end 6am the next day. This could be an overnight flight, for example.

For whole day events, only a date should be provided. For multi day events, a duration or end date can be added.

## Time zones

Times zones that are not multiples of 3 are tough:

9AM EDT is
```
0900-04
 375-167
```

9AM EST is
```
0900-05
 375-208
```

In China:
```
0900+08
 375+333
```

In Japan:
```
0900+09
 375+375
```

In New Zealand:
```
0900+12
 375+500
```

All time zones:
```
01 042
02 083
03 125
04 167
05 208
06 250
07 292
08 333
09 375
10 417
11 458
12 500
13 542
14 583
```

Mixing dates and times with times zones can be confusing, but this done in ISO 8601:

```
2023-123.375-167
2023-05-03.375-167
2023-W18-3.375-167
```
all mean 9AM EDT on May 3rd.

## Alarms

Alarms are denoted as lines. Events are shown as boxes. Alarms do not have end times. Whole day and multi-day events do not include times.

## 1 day calendar mode

The units are decimilliday.

There are 70 rows as in all other modes.

There are 70 times (0000 to 9875), 1 row per 125 decimilliday (12.5 milliday), except for the first 10 which use 1 rows for 25 milliday.

0000 to 2500 (not inclusive) equals 10 rows, while 2500 onward equals 60 rows.

9875 is the last time.

In other words, the times above 6AM are on a different scale than the rest of the times.

Therefore, the left margin should have a broken axis, because first 10 times increment by 250, the remaining 60 times increment by 125.

The last digit in the decimilliday time can be a light grey color to emphasis the milliday time.

Both decimilliday time and HHMM time use 4 digits, so the grey will serve the additional purpose of visually distinguishing these two formats.

Milliday times are more readable as shown in the table below.

| Metric | Regular  |
|--------|----------|
|   000  |   0d     |
|   050  |   1h 12m |
|   100  |   2h 24m |
|   150  |   3h 36m |
|   200  |   4h 48m |
|   250  |   6h     |
|   275  |   6h 36m |
|   300  |   7h 12m |
|   325  |   7h 48m |
|   350  |   8h 24m |
|   375  |   9h     |
|   400  |   9h 36m |
|   425  |  10h 12m |
|   450  |  10h 48m |
|   475  |  11h 24m |
|   500  |  12h     |
|   525  |  12h 36m |
|   550  |  13h 12m |
|   575  |  13h 48m |
|   600  |  14h 24m |
|   625  |  15h     |
|   650  |  15h 36m |
|   675  |  16h 12m |
|   700  |  16h 48m |
|   725  |  17h 24m |
|   750  |  18h     |
|   775  |  18h 36m |
|   800  |  19h 12m |
|   825  |  19h 48m |
|   850  |  20h 24m |
|   875  |  21h     |
|   900  |  21h 36m |
|   925  |  22h 12m |
|   950  |  22h 48m |
|   975  |  23h 24m |
|  1000  |   1d     |


**Examples**

```
2023-05-17.0000
           0250
           0500
           0750
           1000
           1250
           1500
           1750
           2000
           2250
           2500
           2625
           2750
           2875
           3000
           3125
           3250
           3375
           3500
           3625
           3750
           3875
           4000
           4125
           4250
           4375
           4500
           4625
           4750
           4875
           5000
           5125
           5250
           5375
           5500
           5625
           5750
           5875
           6000
           6125
           6250
           6375
           6500
           6625
           6750
           6875
           7000
           7125
           7250
           7375
           7500
           7625
           7750
           7875
           8000
           8125
           8250
           8375
           8500
           8625
           8750
           8875
           9000
           9125
           9250
           9375
           9500
           9625
           9750
           9875

2023-05-17T0000
           0036
           0112
           0148
           0224
           0300
           0336
           0412
           0448
           0524
           0600
           0618
           0636
           0654
           0712
           0730
           0748
           0806
           0824
           0842
           0900
           0918
           0936
           0954
           1012
           1030
           1048
           1106
           1124
           1142
           1200
           1218
           1236
           1254
           1312
           1330
           1348
           1406
           1424
           1442
           1500
           1518
           1536
           1554
           1612
           1630
           1648
           1706
           1724
           1742
           1800
           1818
           1836
           1854
           1912
           1930
           1948
           2006
           2024
           2042
           2100
           2118
           2136
           2154
           2212
           2230
           2248
           2306
           2324
           2342
```

**Row delimiters**

Each time above has two rows. The each row can represents 18 minutes after 6AM and 36 minutes before 6AM.
The solid lines can group together 36 minute blocks of time before 6AM and 1h12m blocks of time after 6AM.

| Metric  | Regular    | Row delimiter |
|---------|------------|---------------|
|   0     |   0h 0m    |   dashed      |
|   250   |   0h 36m   |   solid       |
|   500   |   1h 12m   |   dashed      |
|   750   |   1h 48m   |   solid       |
|   1000  |   2h 24m   |   dashed      |
|   1250  |   3h 0m    |   solid       |
|   1500  |   3h 36m   |   dashed      |
|   1750  |   4h 12m   |   solid       |
|   2000  |   4h 48m   |   dashed      |
|   2250  |   5h 24m   |   solid       |
|   2500  |   6h 0m    |   dashed      |
|   2625  |   6h 18m   |   solid       |
|   2750  |   6h 36m   |   dashed      |
|   2875  |   6h 54m   |   solid       |
|   3000  |   7h 12m   |   dashed      |
|   3125  |   7h 30m   |   solid       |
|   3250  |   7h 48m   |   dashed      |
|   3375  |   8h 6m    |   solid       |
|   3500  |   8h 24m   |   dashed      |
|   3625  |   8h 42m   |   solid       |
|   3750  |   9h 0m    |   dashed      |
|   3875  |   9h 18m   |   solid       |
|   4000  |   9h 36m   |   dashed      |
|   4125  |   9h 54m   |   solid       |
|   4250  |   10h 12m  |   dashed      |
|   4375  |   10h 30m  |   solid       |
|   4500  |   10h 48m  |   dashed      |
|   4625  |   11h 6m   |   solid       |
|   4750  |   11h 24m  |   dashed      |
|   4875  |   11h 42m  |   solid       |
|   5000  |   12h 0m   |   dashed      |
|   5125  |   12h 18m  |   solid       |
|   5250  |   12h 36m  |   dashed      |
|   5375  |   12h 54m  |   solid       |
|   5500  |   13h 12m  |   dashed      |
|   5625  |   13h 30m  |   solid       |
|   5750  |   13h 48m  |   dashed      |
|   5875  |   14h 6m   |   solid       |
|   6000  |   14h 24m  |   dashed      |
|   6125  |   14h 42m  |   solid       |
|   6250  |   15h 0m   |   dashed      |
|   6375  |   15h 18m  |   solid       |
|   6500  |   15h 36m  |   dashed      |
|   6625  |   15h 54m  |   solid       |
|   6750  |   16h 12m  |   dashed      |
|   6875  |   16h 30m  |   solid       |
|   7000  |   16h 48m  |   dashed      |
|   7125  |   17h 6m   |   solid       |
|   7250  |   17h 24m  |   dashed      |
|   7375  |   17h 42m  |   solid       |
|   7500  |   18h 0m   |   dashed      |
|   7625  |   18h 18m  |   solid       |
|   7750  |   18h 36m  |   dashed      |
|   7875  |   18h 54m  |   solid       |
|   8000  |   19h 12m  |   dashed      |
|   8125  |   19h 30m  |   solid       |
|   8250  |   19h 48m  |   dashed      |
|   8375  |   20h 6m   |   solid       |
|   8500  |   20h 24m  |   dashed      |
|   8625  |   20h 42m  |   solid       |
|   8750  |   21h 0m   |   dashed      |
|   8875  |   21h 18m  |   solid       |
|   9000  |   21h 36m  |   dashed      |
|   9125  |   21h 54m  |   solid       |
|   9250  |   22h 12m  |   dashed      |
|   9375  |   22h 30m  |   solid       |
|   9500  |   22h 48m  |   dashed      |
|   9625  |   23h 6m   |   solid       |
|   9750  |   23h 24m  |   dashed      |
|   9875  |   23h 42m  |   solid       |


This mode is only for the digital calendar app and not the paper calendar because it would require:
	1. 365 pages per year and the pages would be all the same except for the dates in the top left.
	2. changing the number of the times to be 68 to accommodate two additional date formats to match the week mode.

**Calendar utilities**

Class that represents an alarm: `Alarm`
Class that represents an event: `Event`

Both classes can
-   convert datetime objects to ISO 8601 date strings
-   convert ISO 8601 date strings to datetime objects

Instantiate:
```
Event.from_datetime(datetime.date())
Event.from_string("R2,18/2023-05-01/P2D,1W")
Event(recurrence=2, start="2023-05-01", stop="2023-09-01", period="1W")
```

Recurrence and period arguments can be lists or tuples:
```
Event(recurrence=[2, 2], start="2023-01-16", stop="2023-05-01", period=["2D", "16W"])
```
