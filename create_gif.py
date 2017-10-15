#!/usr/bin/python3
import os
import subprocess
import sys

input_fn = sys.argv[1]
print(input_fn)
output_fn = os.path.splitext(input_fn)[0] + '.gif'

start_time = '10:30'
duration = '10'
while True:
    start_time = input('Start time [%s]: ' % start_time) or start_time
    duration = input('Duration [%s]: ' % duration) or duration
    subprocess.call([
        'ffmpeg', '-ss', start_time, '-t', duration, '-i', input_fn,
        '-vf', 'fps=5,scale=320:-1:flags=lanczos,palettegen', '-y', 'palette.png'
    ])
    subprocess.call([
        'ffmpeg', '-ss', start_time, '-t', duration, '-i', input_fn, '-i', 'palette.png',
        '-lavfi', 'fps=5,scale=320:-1:flags=lanczos [x]; [x][1:v] paletteuse', '-y', output_fn
    ])
    subprocess.call(['eog', output_fn])
    ok = input('Ok? [Y/n]')
    if ok != 'n':
        break
