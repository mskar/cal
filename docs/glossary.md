## Glossary

### Date functions

- [x] greg2doty: month, day -> doty
- [x] doty2greg: doty -> month, day
- [x] greg2year: year, month -> year
- [x] doty2year: year, doty -> year
- [x] leap_year: year -> bool
- [ ] isoo2doty: "year-day" -> year, day
- [ ] isoo2deco: "year-day" -> "year+day"
- [ ] doty2isoo: year, doty -> "year-day"
- [ ] greg2isoc: year, month, day -> "year-mm-dd"
- [ ] doty2isoc: year, doty -> "year-mm-dd"
- [ ] greg2deco: year, month, day -> "year+day"

### Time functions
- [x] hour2zone: hour -> "Z"
- [x] zone2hour: zone -> hour
- [ ] time2doty: hour, minute, second, zone -> doty, zone
- [ ] doty2time: doty, zone -> hour, minute, second, zone
- [ ] time2isot: hour, minute, second, zone -> "hh:mm:ss"
- [ ] time2deco: hour, minute, second, zone -> ".dayZ"

### Datetime functions

- [ ] doty2deco: year, doty, zone -> "year+day.dayZ"
- [ ] doty2dote: year, doty, zone -> float
- [ ] unix2doty: ms -> year, doty
- [ ] unix2deco: ms -> "year+dayZ"
- [ ] deco2doty: ms -> year, doty
