from datetime import datetime

df = [
    dict(Task='Food', Start='2020-01-01 01:00', Finish='2020-01-01 03:00', Resource='Passive'),
    dict(Task='Breakfast', Start='2020-01-01 03:00', Finish='2020-01-01 04:00', Resource='Passive'),
    dict(Task='Work', Start='2020-01-01 02:00', Finish='2020-01-01 05:00', Resource='Passive'),
    dict(Task='Break', Start='2020-01-01 04:30', Finish='2020-01-01 07:00', Resource='Passive'),
    dict(Task='Lunch', Start='2020-01-01 08:00', Finish='2020-01-01 09:00', Resource='Passive'),
    dict(Task='Work', Start='2020-01-01 07:00', Finish='2020-01-01 10:00', Resource='Passive'),
    dict(Task='Exercise', Start='2020-01-01 09:30', Finish='2020-01-01 11:30', Resource='Passive'),
    dict(Task='Post Workout Rest', Start='2020-01-01 11:30', Finish='2020-01-01 12:00', Resource='Passive'),
    dict(Task='Dinner', Start='2020-01-01 09:00', Finish='2020-01-01 13:00', Resource='Passive'),
    dict(Task='Evening Sleep', Start='2020-01-01 12:00', Finish='2020-01-01 14:00', Resource='Passive')
]

colors = dict(Passive = 'rgba(217, 30, 24, 1)',
              Active = 'rgba(30, 130, 76, 1)')

startTime = []
endTime = []

for index in range(len(df)):
    var = df[index]['Start'].split(" ")
    startTime.append(var[1])  

for index in range(len(df)):
    var = df[index]['Finish'].split(" ")
    endTime.append(var[1])

#endTime = sorted(endTime)

def Time(s, f ):
    start = s.split(":")
    finish = f.split(":")
    this_morning = datetime(2020, 12, 3, int(start[0]), int(start[1]))
    last_night = datetime(2020, 12, 3, int(finish[0]), int(finish[1]))
    return (this_morning.time() >= last_night.time())

def Activities(s, f):
    n = len(f)
    i = 0
    replace = df[0]["Resource"] = "Active"
    for j in range(n):
        if Time(s[j], f[i]):
            replace = df[j]["Resource"] = "Active"
            i = j