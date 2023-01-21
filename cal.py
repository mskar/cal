import re
import pathlib
import datetime


class Calendar:
    def __init__(self, start_date: str = "1970-01-01", n_days: int = 7):
        self.dates = [
            datetime.date.fromisoformat(start_date) + datetime.timedelta(days=d)
            for d in range(n_days)
        ]
        self.name = f"{self.dates[0].isoformat()}_{self.dates[-1].isoformat()}"
        self.head = (
            "<!DOCTYPE html>\n<html>\n\n<head>\n\t"
            '<link rel="stylesheet" href="cal.css">\n'
            "</head>\n\n<body>\n\t<main>\n\t\t"
        )
        self.foot = "\t</main>\n</body>\n\n</html>"
        self.body = "".join([
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
                    for d in self.dates
                ])
        self.html = self.head + self.body + self.foot

    def __str__(self):
        return self.name.replace("_", " to ")

    def __repr__(self):
        return f"Calendar(start_date={self.dates[0]}, n_days={len(self.dates)})"

    def write_file(self, filename: str = None):
        if not filename:
            filename = self.name + ".html"
        pathlib.Path(filename).write_text(self.html)
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
    # Generate html files for each week in 2023
    start = datetime.date.fromisoformat("2023-01-23")
    dates = [start] + [
        start + datetime.timedelta(days=7*n)
        for n in range(50)
    ]
    dates
    cals = [Calendar(d.isoformat()).write_file() for d in dates]
    cals