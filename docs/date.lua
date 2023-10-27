local function unix2deco(ms)
    local days = ms / 86400000 + 719468
    local era = (days >= 0 and days or days - 146096) // 146097
    local doe = days - era * 146097
    local year = math.floor((doe - doe / 1460 + doe / 36524 - doe / 146096) / 365) + era * 400
    local doty = days - math.floor(year * 365 + year / 4 - year / 100 + year / 400)
    return string.format("%s+%s", math.floor(year), math.floor(doty))
end

local function to_decalendar(date)
  local date = pandoc.utils.stringify(date)
  local unix = date:match("(%d+)")
  return date:gsub(unix, unix2deco(unix))
end

function Meta(m)
  m.date = to_decalendar(m.date)
  return m
end
