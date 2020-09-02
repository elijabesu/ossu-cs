import calendar

# Plain text calendar
c = calendar.TextCalendar(calendar.MONDAY)
st = c.formatmonth(2020, 9, 0, 0)
print(st)

# HTML calendar
#hc = calendar.HTMLCalendar(calendar.MONDAY)
#hst = hc.formatmonth(2020, 9)
#print(hst)

# loop over the days of a month
#for i in c.itermonthdays(2020, 9):
#    print(i)
# extra zeros mean days of the week that belong to a different month

# locale names of months and days
#for name in calendar.month_name:
#    print(name)

#for day in calendar.day_name:
#    print(day)

print("Team meetings will be on: ")
for m in range(1,13):
    cal = calendar.monthcalendar(2020, m)
    week1 = cal[0]
    week2 = cal[1]

    if week1[calendar.FRIDAY] != 0:
        meetday = week1[calendar.FRIDAY]
    else:
        meetday = week2[calendar.FRIDAY]

    print("%10s %2d" % (calendar.month_name[m], meetday))