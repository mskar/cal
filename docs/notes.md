Decimal Time

Clock/Watch

13:00:00-05
 5.50 00-2

 7:00:00-05
 3.00 00-2

13:00-05
 5.50-2

7:00-05
3.00-2
deciday

700-05
300-2
milliday (but offset is still deciday)

70000-05
30000-2
centimilliday (but offset is still deciday)

Removing delimiters changes the units:
- to milliday when precision mode is disabled
- to centimilliday when precision mode is enabled
Removing delimiters will often be paired with removing offsets. Setting all of the options to false gives the simplest display:

700
300
milliday

70000
30000
centimilliday

Stopwatch 

30.00
34.72

1:30.00
1 04.16

15:00.00
10 41.67

13:00:00.00
 5 50 00.00

 7:00:00.00
 3 00 00.00

130000.00
 55000.00

 70000.00
 30000.00

Regardless of delimiters or duration, the stopwatch units are always centimillidays. Removing delimiters makes sense if the durations we are recording are short.

Countdown timer

37h30m00s
15.62 50
deciday

30m00s
20.83
centiday

30s
35
centimilliday

1m00s
  69
centimilliday

373000
156250
centimilliday

3000
2083
centimilliday

Removing delimiters changes the units to centimilliday. If delimiters are enabled, the units depend on much time is left in the timer. When the duration remaining in the timer is
- above 2h24m, the units are decidays 
- between 2h24m and 14.4m, the units are centidays
- below 14.4m, the units are centimillidays

Current system: hourly-offset standard time (HOST) or hourly-offset Sumerian time (HOST) 
Intermediate system: hourly-offset decimal time (HODT, pronounced hot)
Proposed system: decidaily-offset decimal time (DODT, pronounced dot)

HODT is an exact conversion of our current time system into decimal time, while DODT no longer sets easy conversion as a goal and combines existing time zones into 36-degree deciday groups.

While HODT could be useful as an intermediary step, mixing decimal time and hour offsets is awkward and it would be better to switch to DODT entirely instead of using two systems in parallel.

The names of DODT zones can be used to differentiate between HOST and DODT.

Since DODT is offset by deciday, the time should be in deciday too.

13:00-05
 5.50-2

 7:00-05
 3.00-2

These two formats fit well together. If more precision is required then the display can be expanded to seconds and microdays:

13:00:00-05
 5.50 00-2

 7:00:00-05
 3.00 00-2

Microdays are too precise (move too fast) to look at on a clock, so that last digit can be hidden or de-emphasized with lower opacity. The opacity of that last digit can be set in the application settings. The greater precision mode shown above can be toggled on and off. When the greater precision mode is off, the opacity doesn’t matter.

The display for HODT with the hour offset translated to centiday is precise down to decimillidays by default:

12:00-05
50.00-21

 9:00-05
37.50-21

But can be precise down to decimicrodays if seconds are included:

12:00:00-05
50.00000-21

 9:00:00-05
37.50000-21

Decimicrodays are way too precise to look at. HODT will probably just be a stepping stone to DODT. It can used as a tool to teach people about decimal time. It can used when a more precise exact match to HOST is required. HODT could be a good option to include in an app, but to limit initial development time, it should be added after DODT is fully implemented.

More precision will certainly be required for stopwatches and timers. Stopwatches count up and timers count down. Both should use microday units.

Stopwatch

The stopwatch shows durations in centimillidays, whereas the watch/clock described above shows time in decidays. The stopwatch display starts with all zeros and increments once the user hits start:

mm:ss.ss
00:00.00
00 00.00
centimilliday

The displays adapts to fit the time that has passed. For durations less than an hour, the display does not need to change the number of digits:

mm:ss.ss
15:00.00
10 41.67
centimilliday

When the duration goes above an hour, add an hours place to the top:

1:15:00.00
  52 08.30

The bottom will not need another digit until 2h24m: 

2:30:00.00
1 04 16.67

6:15:00.00
2 60 41.67

When the duration goes above 10 hours, add another digit to the hours place:

12:15:00.00
 5 10 41.60

They bottom will need another digit after 24 hours: 

24:15:00.00
10 10 41.60

At this point, hours can go above 60. When the duration goes above 99 hours, add another digit in front:

240:15:00.00
100 10 41.60

This can continue forever, but only a certain number of digits can be displayed in an app so a limit can be placed at which the stopwatch will automatically stop.

Decimicrodays are 8.64ms long and thus are more precise than centiseconds. If even greater precision is required, more places after the decimals can be added. The precision and max value of the bottom timer will always be greater. 

Just like with the clock/watch, delimiters can be toggled off in the stopwatch. With or without delimiters, the stopwatch units are centimillidays. Getting rid of the delimiters in the stopwatch can be very satisfying, but brevity comes at the price of readability:

 11500.00
  5208.30

121500.00
 51041.60

Timer

Countdown timer

The timer typically shows centimillidays like the stopwatch, but when the duration remaining is more than 2h24, it shows decidays like the clock/watch.  The timer can switch from decidays to centimillidays as soon as the decimal is no longer needed.

Users can enter any two digit value for hours, minutes, and seconds. Once the timer is started, the values are recalculated to fit within the respective limits of each (either 24 or 60). Any number of days can be entered.

For durations less than an hour (most common usage), the display is 3-6 characters wide:

 9s
10

15s
17
centimilliday

30s
35
centimilliday

1m00s
  69
centimilliday

15m00s
10 41
centimilliday

99m00s
68 75
centimilliday

If the duration remaining is above an hour, the top will include an hours place:

1h15m00s
  52 08
centimilliday

If the duration remaining is above two hours 24 minutes, the bottom will include another digit:

6h15m00s
2.60 42
deciday

2h30m00s
1.04 17
deciday

When the duration remaining is above 10 hours, the top will need another digit: 

12h15m00s
 5.10 41
 deciday

At this point, any number of hours and decidays should work for the top and bottom. Toggling delimiters should be possible in the timer just like in the clock/watch and the stopwatch. Removing delimiters switches the units to centimillidays: 

 121500
  51042
  centimilliday

 241500
 101042
 centimilliday

Examples:

Noon UTC in DC in Eastern Standard Time (EST) and West Atlantic Americas (WAS) / Today Mid-Morning (TMM) time zones, which is 1/12dd or 12 minutes ahead.

07:00-05
 3.00-2


6pm UTC in DC in Eastern Standard Time (EST) and West Atlantic Americas (WAS) / Today Mid-Morning (TMM) time zones, which is 1/12dd or 12 minutes ahead.

13:00-05
 5.50-2

Noon UTC in LA in Pacific Standard Time (PST) and East Pacific Americas (EPA) / Today Early-Morning (TEM) time zones, which is 1/3dd or 48 minutes ahead.

05:00-08
 2.00-3

6pm UTC in LA in Pacific Standard Time (PST) and East Pacific Americas (EPA) / Today Early-Morning (TEM) time zones, which is 1/3dd or 48 minutes ahead.

10:00-08
 4.50-3

Clock/Watch apps should make it clear that these are two different times being shown, but they become equivalent when the offset is subtracted from the time to get the time UTC. The advantage to this display is that times will line up nicely on hours divisible by 3. The disadvantage is the times cannot be converted without including the offset, except for locations with -12, 0, and 12 hour UTC offsets, which do not need subtract the offset when converting. I’m convinced that displaying HOST and DODT time together with offsets will be best. The UTC offset is not typically shown in clock/watch apps, but including the offsets should be standard for showing HOST and DODT together. To obtain the DODT offset, the UTC offset is divided by 2.4 and rounded to the nearest whole deciday. To calculate DODT, the time at UTC is converted to decidays and the offset is added. The local time should not be used to calculate DODT. 

Javascript

https://gist.github.com/maptv/aa578dd0fcf562d946b56b185afb40cb

Python

https://gist.github.com/maptv/4e056422b490c38140c4259421527cef


1. Hourly-offset decimal time (HODT, pronounced hot): convert hours into decidays. The main advantage of this system is that it exactly matches our current time system. The disadvantage is that the hour offsets that are not evenly divisible by 3 look strange. The time can be shown with 3-5 digits. For the offset, 2 digits are enough to distinguish between time zones including those with quarter hour (1cd = 14.4m) and half hour (2cd = 28.8m) offsets. Regardless of hour many digits are displayed, the HODT will be calculated using exact times and offsets. Daylight savings times can be incorporated into HODT.
2. Decidaily-offset decimal time (DODT, pronounced dot): By agreement of all concerned parties, the existing hourly time zone system can be simplified to decidaily metric time zones. The simplest way to calculate the decidaily metric time zones is by rounding hourly metric times to the nearest deciday. Rather than drawing new time zones on the map, this method groups existing time zones into decidaily time zones. This method will not match hourly offset metric time, but may be surprisingly close in some time zones. The greatest difference (50md, 72m) is at UTC-6 and UTC+6. There is no difference at UTC, UTC-12, and UTC+12. This system is much less fine grained than HODT and joins together 2-3 hourly offsets including any quarter hour and half hour offsets in between. Joining together time zones eliminates differences between many standard and daylight savings time zones, with the exception of Alaska Time, Amazon Time, Atlantic Time (should only apply to Bermuda), Australian Eastern Time, Central Time, Central European Time, Chatham Time, Chile Time, Choibalsan Time, Easter Island Time, Falkland Island Time, Iran Time, Lord Howe Time, Paraguay Time, Samoa, Ulaanbaater Time, and West Africa Time. The remaining daylight savings time differences should be respected until they are eventually abolished.
3. Centidaily-offset decimal time (CODT, pronounced cot) time: Divide the current longitude by 3.6 and round to the nearest centiday. This method may not match DODT, because many times zones only loosely follow longitudinal divisions. Either way, only one digit should be used for DODT offsets, while HOST and CODT offsets should use two digits. CODT is a more objective system and could be used to determine the time at any location even if the time zone is unclear, for example in a remote location or on the border of two countries in different time zones. 

I think the better system will be to have fewer time zones, but CODT could have roughly 100 time zones. The rounding could be adjusted to have fewer time zones. For example, rounding to to the nearest multiple of 5 centiday (18 degrees) would be similar to the current system of 1 hour being 15 degrees, in that there would roughly 20 two-digit offsets. Having roughly 10 one-digit time zones system with DODT would be simpler, but CODT could be used when the time zone is unclear or a closer match to sunrise/sunset time is desired.

Clock/Watch apps should automatically determine the HODT time from the local time and UTC offset, but provide DODT and CODT time as alternatives. The default should be to show regular time and HODT time with milliday precision. For example, noon EST:

 5.00-0
12:00-00

Centiday precision is enough to distinguish between all time zones. Even though -21 is shown, the actual offset is 208.33333md and the actual time UTC will be 708.3333md. Adding 500md and 21cd to get 710md is close enough. The difference is 5/3md or 2.4 minutes (2m24s). 

Two-digit milliday HODT offsets represent exact matches of hourly offsets, while one-digit deciday DODT and CODT offsets signal that we are no longer trying to main the hourly offset system in parallel.

CODT can have different levels of precision from the default deciday to microday or even nanoday. The time and offset should have the same level of precision. Centimilliday is a good practical limit for the level of precision. A centimilliday is 0.864 seconds. A degree of longitude is 25/9 (2.77778) milliday or 4 minutes. A milliday is 0.36 degrees, a centimilliday is 0.0036 degrees. If longitude changes, CODT stops making sense, but it is the most objective system that should be most closely attuned to sunrise and sunset in any given location.

Examples

Calculate decidaily offset metric (DODT) time:

1. Find UTC time and convert to metric time (aka metric time UTC)
2. Find the hourly UTC offset, convert to metric time, and round to the nearest deciday
3. Sum the metric time and metric offset, report the sum together with the offset 

* West longitude is minus, East longitude is plus.

For example, NYC and DC are on Eastern Time, which means a -4 (EDT) or -5 (EST) hour UTC offset. Both of these convert to a deciday offset of -2:
* Current time UTC is 1800 or 750md
* Current time EDT is 1400
* Current time EST is 1300
* Current DODT time in NYC and DC is 550-2 or 13.2 hours or 13:12, a difference of only +12 minutes!

Calculate Longitudinally offset metric (CODT) time:

1. Find UTC time and convert to metric time (aka metric time UTC)
2. Find longitude in degrees, divide by 36, and round to nearest whole number, this is the metric offset in decidays
3. Sum the metric time and metric offset, report the sum together with the offset 

For example, NYC is -74 and DC is -77 longitude, which means a -02 metric UTC offset:
* Current time UTC is 1800 or 750md
* Current time EDT is 1400
* Current time EST is 1300
* Current CODT time in NYC and DC is 550-2 or 13.2 hours or 13:12, a difference of only +12 minutes from EST!

Another example, LA is -3
Current time UTC is 1800 or 750md
Current time PDT is 1100
Current time PST is 1000
Current metric time in LA is 450-3 or 10.8 hours or 10:48, a difference of -12 minutes from PDT!

Chicago is at -88 degrees longitude and thus has the same cutoff as NYC and DC

-90 is the cutoff when we round up to -3. The mainland US has only 2 time zones (-2 and -3) 

-126 is the cutoff when we round up to -3. Alaska and Hawaii are -4

All of South America is -2!

https://en.m.wikipedia.org/wiki/Extreme_points_of_South_America

Notes

Deciday works well for displaying times and offsets, but datetimes will require a different system:

YYYY-mm-dd.dddddZ
2023-07-20.50000Z
2023-W29-4.50000Z
2023-07-20.30000E
2023-07-20.90000I

Combining decimal time with hourly time zones may seem strange, but it makes it possible to recreate standard time from decimal time (with no information loss):
1. Get the hour offset:
    1. translate the letter to a number counting from A or N
    2. If you counted from A, the offset is negative
2. Get the deciday offset by dividing the hour offset by 2.4 and rounding it. Or use the “Fractions out of 24 Mnemonic” below to calculate the deciday offset without a calculator.
3. Subtract the deciday offset from decimal time to get decimal time at UTC 
4. Multiply the decimal time at UTC by 24 to get the decimal hour. Get decimal minutes by subtracting whole hours from decimal hours and dividing the difference by 60. Repeat the same process to get decimal seconds from decimal minutes. Combine the whole hour, whole minute, and decimal seconds to get the standard time at UTC.
5. Add the hour offset to UTC standard time from step 4 to get the local  standard time.

Fractions out of 24 Mnemonic: If the offset is divisible by 3, divide by 3 and multiply by 125, round to nearest 100, divide by 100 to get the deciday offset. If not, start at nearest multiple of 3 and count up or down by 42, e.g.

but millidays are less precise than minutes by .44 minutes, so rounding off the time to the nearest milliday occurs. If more precision is required, more places after the decimal can be included.

* 1 is closest to 3: 125 - 84 = 41 which rounds down to 0. 
* 2 is closest to 3: 125 - 42 = 83 which rounds up to 100. 
* 4 is close to 3: 125 + 42 = 167 which rounds up to 200. 
* 5 is close to 6: 250 - 42 = 208 which rounds down to 200.
* 7 is close to 6: 250 + 42 = 292 which rounds up to 300.
* 8 is close to 9: 375 - 42 = 333 which rounds down to 300.
* 10 is close to 9: 375 + 42 = 417 which rounds down to 400.
* 
Alternatively, count by 42s up to the hour offset and round to nearest 100, divide by 100 to get the deciday offset.

When naming files manually, use a clipboard utility to insert the ISO date and decimal time.
The javascript code for decimal time (in days):

const now = Date.now();
const decimalTime = now.getHours() / 24 + now.getMinutes() / 1440 + now.getSeconds() / 86400 + now.getMilliseconds() / 86400000;

const centimillidays = Math.round(decimalTime * 100000) / 100000

To get the day of the week, one has to look in a calendar. 

The decimal times above have centimilliday precision. Centimillidays are smaller than seconds. A second is 1.1574cmd. 1cmd = 0.864s. Centimillidays are a good default for timestamps, but if more or less precision is required, the number of places after the decimal can be adjusted. A microday is 0.0864s or 86.4ms. Decimicrodays are 8.64ms long. Centimicrodays are 0.864ms long. The level of precision can adjusted to match the HOST equivalent:
* Centimiliday: second
2023-07-20.95000+2
2023-07-20T18:00:00
* Centimicroday: millisecond
2023-07-20.95000000+2
2023-07-20T18:00:00.000+00
* Centinanoday: microsecond
2023-07-20.95000000000+2
2023-07-20T18:00:00.000000+00
* Centipicoday: nanosecond
2023-07-20.95000000000000+2
2023-07-20T18:00:00.000000000+00

Rename files based on time stamp in file metadata?
What files will I want to rename like this?
Binary files created manually (not programmatically):
Creation date:
- Scans
- Screenshots
Modified date:
- Spreadsheets
- Word processor documents
- Presentations
Use mdls to get kMDItemContentCreationDate
Format: 2020-12-31 16:01:33 +0000

https://gfxhacks.com/renaming-files-by-date-from-metadata/

YYYYMMDDhhmmss
20201231160000
2020123166667
       centimilliday

Convert
2020-12-31 16:00:00 +0000
to
2020-12-31.66667Z



17 characters wide.

All of the files will have unique names before renaming so there will be no name conflicts even if time stamps match (Not True for screenshots). The utility should modify filenames with dates in them, e.g 
Screenshot 2021-12-15 at 6.00.00 pm.png

2021-12-15.66667E_screenshot.png

One utility for all files:
1. Remove dates in other formats and those that are not at the beginning of the file
2. Add date from metadata, either modified date or created date:

date_rename *.png —-precision 3 —-created-date

date_rename *.png —-precision 5 —-modified-date

The default is centimilli precision (5) and modified date, because for files that are never modified, the modified date will be the same as the created date. 

Check if names are already up-to-date with metadata. Say which files were renamed and which were skipped because they are already up-to-date with metadata.

Files with creation date in the name can be under git version control, because the file name will not change but files with modified dates should not be in version control because the filename will change whenever the file does. Use the same format for Creation dates and Modified dates: centimilliday times. Renaming files with modified dates repeatedly will require removing previous time stamps. Screenshots taken with macOS have time stamps that should be replaced.

2020-12-31.66667Z_filename.ext
Regex: ^\d{4}—d{2}—d{2}.d{5}[+-]\d
Use sed to replace match with new time stamp.

The shell utility should offer the option to rename files by creation date or by modified date. I can imagine that I am passing manual edits on to someone and I want to let them see which is the latest version by the modified date. The shell utility should allow for selecting dates only (not times) for both creation time and modified time:

date_rename *.png —-precision base —-modified-date

date_rename *.png —-precision 0 —-modified-date

Datetimes meant for only human consumption should have milliday precision. 
YYYY-mm-dd.dddddZ
2023-07-20.75000Z
2023-W29-4.75000Z
2023-07-20.55000E
2023-07-20.95000Q
2023-07-20T18:00+00

All of the datetimes above should be safe for filenames.

Gēng (更) can be another name for deciday.

In the French Republican Calendar system, the hour was deciday (10^-1), the minute was milliday (10^-3), and the second was centimilliday (10^-5). Following this pattern, the French word tierce could represent a decimicroday (10^-7) and the French word quatierce could be a nanoday (10^-9).

Western European Time and Central European Time can be the same as metric UTC. Eastern European Time can +1

Mexico 

The offset can modify the date: At 600md in DC, it is midnight UTC and the beginning of the next calendar day

Users can either share location to get Longitude or set the UTC offset themselves.

Longitudinal metric time requires knowing the longitude and sometimes may cut in inconvenient places like the middle of a small country.
Longitudinal 

Translating existing time zones into metric zones time could be easier and more useful:

There are about 25 existing time zones, because zero is included.

Middle three metric time zones include three time hour time zones. Then, they move by 2 hour 


