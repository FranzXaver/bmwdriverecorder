#!/usr/bin/env python3

"""convert BMW Drive Recorder metadata to subtitles
"""

import json
from datetime import datetime

FPS = 30
FRAMETIME = 1.0/FPS

with open('Metadata.json') as jsonFile:
    data = json.load(jsonFile)
    with open('driverecorder.srt', 'w') as subFile:
        for entry in data[0]['entries']:
            frame = entry['id']
            timeFrom = datetime.fromtimestamp((frame-1)*FRAMETIME+82800).\
                strftime('%H:%M:%S,%f')[:-3]
            timeTo   = datetime.fromtimestamp(frame*FRAMETIME+82800).\
                strftime('%H:%M:%S,%f')[:-3]
            subFile.write('%i\n' % frame)
            subFile.write('%s --> %s\n' % (timeFrom, timeTo))
            subFile.write('%s %s\n' % (entry['date'], entry['time']))
            subFile.write('%.2fkm/h, lat=%.4f, long=%.4f\n\n' %
                          (entry['velocity'],
                           entry['latitude'],
                           entry['longitude']))