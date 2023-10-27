# test by running the following in a UNIX shell:
# for tz in 'Pacific/Samoa' 'America/Los_Angeles' 'Etc/UTC' 'Asia/Shanghai' 'Pacific/Kiritimati'; do; echo \\n$tz; env TZ=$tz python centiday.py; done;
from datetime import datetime, timezone
import time

utc = datetime.now(timezone.utc)
mid = utc.replace(hour=0, minute=0, second=0, microsecond=0)
seconds_since_midnight = (utc - mid).total_seconds()
centiday = seconds_since_midnight / 8640
offset = round(time.timezone / 8640)
sign = "-" if offset > 0 else "+"
offset_centiday = centiday - offset
normalized_centiday = (
    offset_centiday - 10 * (offset_centiday > 10) + 10 * (offset_centiday < 0)
)
print(
    f"{datetime.now().strftime('%H:%M')}{sign}{str(int(abs(time.timezone) / 3600)).zfill(2)}"
)
print(f" {normalized_centiday:.2f}{sign}{abs(offset)}")
