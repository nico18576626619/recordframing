#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import subprocess
import os
from LoadSpeed import ffmpeg
from LoadSpeed import Utils

BASE_PATH=os.path.dirname(os.path.dirname(__file__))


def pull_video_file():

    videoFileName = ""
    p = subprocess.Popen('adb shell ls -l /sdcard/DCIM/Camera/', shell=True, stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT,encoding='gbk')

    picfiles = p.stdout.readlines()
    picfiles.reverse()

    for line in picfiles:
        print(line)
        if line.strip().endswith('.mp4'):
            videoFileName = line[line.rindex(' '):].strip()
            break

    if videoFileName:
        print(f'videoFileName:{videoFileName}')
        filedir = f"{BASE_PATH}/result/video"
        if not os.path.exists(filedir):
            os.makedirs(filedir)
        subprocess.call(f"adb pull /sdcard/DCIM/Camera/{videoFileName} {filedir}")
    else:
        print("error:can not find video file")
    return videoFileName.strip('.mp4')




if __name__ == '__main__':
    print ('开始导出')
    video_name = pull_video_file()
    print (f'视频文件({video_name})导出完成{"-"*30}')
    print (f'开始视频分帧处理{"-"*30}')
    ff = ffmpeg.FFMpegUtil()
    ff.runFFMpeg(video_name)
    path=ff.getConparaPicPath()+os.path.sep+video_name
    Utils.rename(path)

    print ('分帧处理完成..............................................')
