from utils.data import data
baseURL =  'https://wetestoss.sflep.com/resource/sound/'
import wget
from os import makedirs as mkdir
import os
links = data['all_links']
data = data['data']

if not os.path.exists('audio'):
    mkdir('audio')

if not os.path.exists('pcm'):
    mkdir('pcm')

if not os.path.exists('dist'):
    mkdir('dist')

import ffmpeg

def convert_mp3_to_pcm(mp3_path, pcm_path):
    (
        ffmpeg
        .input(mp3_path)
        .output(pcm_path, format='s16le', acodec='pcm_s16le', ac=1, ar='16k')
        .overwrite_output()
        .run()
    )

for i in links:
    wget.download(baseURL+i,out='audio/'+i)
    convert_mp3_to_pcm(f'./audio/{i}', f'./pcm/{i}.pcm')
    continue

