# Calendar

I made a calendar using HTML, CSS, and Python.

# Description

Running the code will generate are 50 HTML and PDF files that span the 4th week of 2023 up to and including the first week of 2024. Each file has 70 lines across 7 days. Each day has three [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) dates:

1. Year, month, day of the month (YYYY-MM-DD)
2. week of the year and day of the week
3. day the year

In addition to day of the year, the third date also includes times in millidays (md) after the decimal. The milliday times divide up the 1000md (24-hour) day into eight segments of 125md (3 hours). These segments make it easy to convert millidays into hours, e.g. 375md is 9AM, 625md is 3PM, etc., as in the table below:

| Millidays | 24-hour time | 12-hour time |
|-----------|--------------|--------------|
| 000       | 00:00        | 12:00am      |
| 125       | 03:00        | 03:00am      |
| 250       | 06:00        | 06:00am      |
| 375       | 09:00        | 09:00am      |
| 500       | 12:00        | 12:00pm      |
| 625       | 15:00        | 03:00pm      |
| 750       | 18:00        | 6:00pm       |
| 875       | 21:00        | 9:00pm       |
| 1000      | 24:00        | 12:00am      |

# Code

The `cal.py` script creates a series of HTML files.
The `sel.py` script prints the HTML files to create PDF files.

# Build

To create weekly HTML and PDF files for 2023, these two shell commands should be enough:

```
python cal.py
python sel.py
``````

# Customize

To customize the calendar, it will be necessary to edit the code. I did not bother with creating a CLI, but I may do that when it's time to prepare my 2024 calendar. Modify the styling via the `cal.css` file, modify the HTML files via `cal.py`, and modify the PDF files via `sel.py` file.
