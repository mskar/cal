import calendar
import datetime
import pathlib
import re


class Calendar:
    def __init__(self, start_date: str = "1970-01-01", n_days: int = 365):
        self.dates = [
            datetime.date.fromisoformat(start_date) + datetime.timedelta(days=d)
            for d in range(n_days)
        ]
        self.year_months = sorted(list(set((d.year, d.month) for d in self.dates)))
        self.months = [
            list(calendar.Calendar().itermonthdates(*ym)) for ym in self.year_months
        ]
        self.month_dates = sorted(list(set(d for m in self.months for d in m)))
        self.weeks = list(zip(*[iter(self.month_dates)] * 7))
        self.__head = (
            "<!DOCTYPE html>\n<html>\n\n<head>\n\t"
            '<link rel="stylesheet" href="cal.css">\n'
            "</head>\n\n<body>\n\t<main>\n\t\t"
        )
        self.__foot = "\t</main>\n</body>\n\n</html>"

    def __str__(self):
        return self.name.replace("_", " to ")

    def __repr__(self):
        return f"Calendar(start_date={self.dates[0]}, n_days={len(self.dates)})"

    def write_times(self):
        for week in self.weeks:
            html = "".join(
                [
                    "<day>\n\t\t\t"
                    f"<date>{d.isoformat()}&nbsp&nbsp;</date>\n\t\t\t"
                    "<blank></blank>\n\t\t\t"
                    f"<date>W{d.strftime('%V-%u')}&nbsp&nbsp;</date>\n\t\t\t"
                    "<blank></blank>\n\t\t\t"
                    f"<date>{d.strftime('%j')}.000</date>\n\t\t\t"
                    "<dashed></dashed>\n\t\t\t"
                    "<time>125</time>\n\t\t\t"
                    "<solid></solid>\n\t\t\t"
                    "<time>250</time>\n\t\t\t"
                    "<dashed></dashed>\n\t\t\t"
                    "<time>375</time>\n\t\t\t"
                    "<solid></solid>\n\t\t\t"
                    "<time>500</time>\n\t\t\t"
                    "<dashed></dashed>\n\t\t\t"
                    "<time>625</time>\n\t\t\t"
                    "<solid></solid>\n\t\t\t"
                    "<time>750</time>\n\t\t\t"
                    "<dashed></dashed>\n\t\t\t"
                    "<time>875</time>\n\t\t</day>\n\t\t"
                    for d in week
                ]
            )
            pathlib.Path(
                f"{week[0].isoformat()}_{week[-1].isoformat()}_week.html"
            ).write_text(self.__head + html + self.__foot)
        return self

    def write_dates(self):
        for five_weeks in list(zip(*[iter(self.month_dates)] * 35)):
            html = "".join(
                [
                    "<day>\n\t\t\t"
                    f"<date>{d.isoformat()}&nbsp&nbsp;</date>\n\t\t\t"
                    "<dashed></dashed>\n\t\t\t"
                    f"<date>W{d.strftime('%V-%u')}&nbsp&nbsp;</date>\n\t\t\t"
                    "</day>\n\t\t"
                    for d in five_weeks
                ]
            )
            pathlib.Path(
                f"{five_weeks[0].isoformat()}_{five_weeks[-1].isoformat()}_month.html"
            ).write_text(self.__head + html + self.__foot)
        return self

    @staticmethod
    def increment_latest_file(directory: str = ".", n_days: int = 7):
        path = pathlib.Path(directory)
        text = sorted(list(path.glob("*.html")))[-1].read_text()

        # Get old and new YYYY-MM-DD dates
        matches = [m for m in re.finditer(r"\d{4}-\d{2}-\d{2}", text)]
        old_dates = [datetime.date.fromisoformat(m.group()) for m in matches]
        new_dates = [d + datetime.timedelta(days=n_days) for d in old_dates]

        # Replace YYYY-MM-DD dates
        for m, d in zip(matches, new_dates):
            text = text[: m.start()] + d.isoformat() + text[m.end() :]

        # Replace week of year and weekday
        for m, d in zip(matches, [m for m in re.finditer(r"W\d{2}-\d", text)]):
            text = text[: m.start()] + "W" + d.strftime("%V-%u") + text[m.end() :]

        # Replace day of year
        for m, d in zip(matches, [m for m in re.finditer(r"\d{3}\.000", text)]):
            text = text[: m.start()] + d.strftime("%j") + ".000" + text[m.end() :]

        return (
            path / f"{new_dates[0].isoformat()}_{new_dates[-1].isoformat()}.html"
        ).write_text(text)


if __name__ == "__main__":
    cal = Calendar("2023-01-23")
    cal.write_times()
    cal.write_dates()