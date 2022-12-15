
import calendar
date =  list(map(int, input().split()))
year = date[2]
month = date[0]
day = date[1]
day_num = calendar.weekday(year,month,day)
dict_day = {0:"Monday",1:"Tuesday",2:"Wednesday", 3:"Thursday",4:"Friday",5:"Saturday",6 :"Sunday"}
print(dict_day[day_num].upper())
