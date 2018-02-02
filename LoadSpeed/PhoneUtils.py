#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import subprocess
import os
import FFMpegUtil
import Utils

def PullVideoFile():
    videoFileName = ""

    p = subprocess.Popen('adb shell ls -l /sdcard/DCIM/Camera/', shell=True, stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)

    picfiles = p.stdout.readlines()
    picfiles.reverse()

    for line in picfiles:
        if line.strip().endswith(".mp4") != False:
            videoFileName = line[line.rindex(' '):].strip()
            break

    if videoFileName != "":
        videoFileName = "".join(videoFileName.split())

        filedir = "../result/video"

        if os.path.exists(filedir) == False:
            os.makedirs(filedir)
        subprocess.call("adb pull /sdcard/DCIM/Camera/" + videoFileName + " " + filedir)
    else:
        print "error:can not find video file"

    return videoFileName.strip('.mp4')


if __name__ == '__main__':
    print ('开始导出'.decode('UTF-8').encode('GBK'))
    videoFileName = PullVideoFile()
    print ('视频文件（%s）导出完成.................................'.decode('UTF-8').encode('GBK')%videoFileName)
    print ('开始视频分帧处理..........................................'.decode('UTF-8').encode('GBK'))
    ff = FFMpegUtil.FFMpegUtil()
    ff.runFFMpeg(videoFileName)
    path=ff.getConparaPicPath()+os.path.sep+videoFileName
    Utils.rename(path)

    print ('分帧处理完成..............................................'.decode('UTF-8').encode('GBK'))
