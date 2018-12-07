import datetime

#Inputs
START_DATE_EST = datetime.datetime(2018, 12, 7, 11, 45)
OUTPUT_FILE = 'out.tcx'

#time intervals
time = [
datetime.timedelta(minutes=0, seconds=0),
datetime.timedelta(minutes=3, seconds=45.6),
datetime.timedelta(minutes=3, seconds=46.5),
datetime.timedelta(minutes=3, seconds=47.2),
datetime.timedelta(minutes=3, seconds=47.5),
datetime.timedelta(minutes=3, seconds=47.7),
datetime.timedelta(minutes=3, seconds=47.3),

datetime.timedelta(minutes=5),

datetime.timedelta(minutes=4, seconds=33.4),
datetime.timedelta(minutes=4, seconds=32.8),
datetime.timedelta(minutes=4, seconds=33.4),
datetime.timedelta(minutes=4, seconds=32.9),
datetime.timedelta(minutes=4, seconds=29.2)
]

#hr data
hr = [
110,
160,
168,
170,
172,
172,
175,
100,
170,
172,
172,
174,
175
]


UTC = datetime.timedelta(hours=5)
START_UTC = START_DATE_EST + UTC


def date_format(time):
    return time.strftime('%Y-%m-%dT %H:%M:%SZ')


header = """
<?xml version="1.0" encoding="UTF-8"?>
<TrainingCenterDatabase xsi:schemaLocation="http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2 http://www.garmin.com/xmlschemas/TrainingCenterDatabasev2.xsd" xmlns:ns5="http://www.garmin.com/xmlschemas/ActivityGoals/v1" xmlns:ns3="http://www.garmin.com/xmlschemas/ActivityExtension/v2" xmlns:ns2="http://www.garmin.com/xmlschemas/UserProfile/v2" xmlns="http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
 <Activities>
  <Activity Sport="Other">
   <Id>{0}</Id>
   <Lap StartTime="{0}">
    <Intensity>Active</Intensity>
    <TriggerMethod>Manual</TriggerMethod>
      <Track>""".format(date_format(START_UTC))

footer = """
    </Track>
  </Lap>
  </Activity>
 </Activities>
</TrainingCenterDatabase>
"""

tracks = ''
for i in zip(time, hr):
    START_UTC += i[0]



    tracks += """
        <Trackpoint>
          <Time>{0}</Time>
          <HeartRateBpm>
           <Value>{1}</Value>
          </HeartRateBpm>
         </Trackpoint>""".format(date_format(START_UTC), i[1])


tcx = header + tracks + footer
print(tcx)

with open(OUTPUT_FILE, 'w') as fl:
    fl.write(tcx)
