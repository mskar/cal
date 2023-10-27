def is_leap(y):
    return y % 4 == 0 and y % 100 != 0 or y % 400 == 0


hex(10)[-1]


def unix2doty(s=0, ms=0, precision=0):
    days = s / 86400 + ms / 86400000 + 719468
    era = (days if days >= 0 else days - 146096) // 146097
    doe = days - era * 146097
    yoe = (doe - doe / 1460 + doe / 36524 - doe / 146096) // 365
    year = int(yoe + era * 400)
    if precision == 0:
        return f"{year:0<4}+{round(doe - (365 * yoe + yoe / 4 - yoe / 100)):0<3}"
    ts = days - (
        year * 365
        + sum(i % 4 == 0 and i % 100 != 0 or i % 400 == 0 for i in range(1, year + 1))
    )
    doy = int(ts.__floor__())
    return f"{year:0<4}+{doy:0<3}.{str(round((ts - doy) * 10 ** precision)).zfill(precision)}"


def ymd2doty(year=1970, month=1, day=1):
    year -= month <= 2
    doty = round((153 * (month - 3 if month > 2 else month + 9) + 2) / 5 + day - 1)
    return f"{year:0<4}+{doty:0<3}"


def date2doty(month=1, day=1):
    return (153 * (month - 3 if month > 2 else month + 9) + 2) // 5 + day - 1


date2doty(12, 32)


def doty2date(doty=306):
    m = (5 * doty + 2) // 153
    return m + 3 if m < 10 else m - 9, doty - (153 * m + 2) // 5 + 1


doty2date(0)

ymd2doty()

from time import time

is_leap(2023)
unix2doty()
unix2doty(86400)
unix2doty(0)
unix2doty(-86400)
unix2doty(1695340800, precision=5)
unix2doty(1695327225, precision=5)
"tr"


def date2doty(month=1, day=1):
    return (153 * (month - 3 if month > 2 else month + 9) + 2) // 5 + day - 1


date2doty()


def doty2date(doty=306):
    m = (5 * doty + 2) // 153
    return m + 3 if m < 10 else m - 9, doty - (153 * m + 2) // 5 + 1


doty2date()


def date2year(year=1969, month=1):
    return year - (month < 3)


date2year()


def doty2year(year=1969, doty=306):
    return year + (doty > 305)


doty2year()


def time2doty(hours=1, minutes=0, seconds=0):
    return hours / 24 + minutes / 1440 + seconds / 86400


f"{date2year():<04}+{date2doty():<03}.{round(time2doty(0) * 1e6):<05}"  # {hour2zone()}"


def doty2time(doty=1 / 24):
    hours = doty * 24
    floorHours = hours.__floor__()
    minutes = (hours - floorHours) / 60
    floorMinutes = minutes.__floor__()
    return floorHours, floorMinutes, round((minutes - floorMinutes) / 60)


(
    f"{doty2year():<04}-{'-'.join(map(lambda i: str(i).ljust(2, '0'), doty2date()))}"
    f"T{':'.join(map(lambda i: str(i).ljust(2, '0'), doty2time()))}"  # {zone2hour()}"
)

txt = "banana"

x = txt.ljust(20)

print(x, "is my favorite fruit.")


def hour2zone(hour=0):
    return (
        "Z"
        if hour == 0
        else chr(hour + 64)
        if 0 < hour < 10
        else chr(hour + 65)
        if 9 < hour < 13
        else chr(abs(hour) + 77)
        if -13 < hour < 0
        else "J"
    )


hour2zone()


def zone2hour(zone="Z"):
    return (
        0
        if zone == "Z"
        else ord(zone) - 64
        if "@" < zone < "J"
        else ord(zone) - 65
        if "J" < zone < "N"
        else -(ord(zone) - 77)
        if "M" < zone < "Z"
        else zone
    )


zone2hour()

f"{date2year():<04}+{date2doty():<3}"

f"{doty2year():<04}-{'-'.join(map(lambda i: str(i).rjust(2, '0'), doty2date()))}"

(
    f"{doty2year():<04}-{'-'.join(map(lambda i: str(i).rjust(2, '0'), doty2date()))}"
    f"T{':'.join(map(lambda i: str(round(i)).rjust(2, '0'), doty2time(0)))}{zone2hour()}"
)
