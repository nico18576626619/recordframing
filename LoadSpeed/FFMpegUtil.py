# -*- coding: utf-8 -*-
import os
import sys
import subprocess


class FFMpegUtil(object):
    def __init__(self):
        pass

    def createFFMpehPath(self, dicname):
        filedic = '../result/ComparaPic/' + dicname
        if os.path.exists(filedic) == False:
            os.makedirs(filedic)

    def getConparaPicPath(self):
        path = os.path.dirname(os.path.realpath(__file__))
        return path[:path.rindex('\\')] + "\Result\ComparaPic"

    def getFFMpegPath(self):
        path = os.path.dirname(os.path.realpath(__file__))
        return path + '\\FFMpeg\\'

    def getResultFilePath(self, dirname):
        path = os.path.dirname(os.path.realpath(__file__))
        return path[:path.rindex('\\')] + "\\Result\\" + dirname

    def getVideoPath(self, videoname):
        return self.getResultFilePath('video') + '\\' + videoname + '.mp4'

    def getPicPath(self, picname):
        return self.getConparaPicPath() + '\\' + picname

    def runFFMpeg(self, videoname):
        videopath = self.getVideoPath(videoname)
        picpath = self.getPicPath(videoname)
        if os.path.exists(videopath) == False:
            os.makedirs(videopath)
        if os.path.exists(picpath) == False:
            os.makedirs(picpath)
        cmd = 'ffmpeg -i %s -r 20 -q:v 2 -f image2 %s' % (videopath, picpath) + '\%d.jpeg'
        # cmd = 'ffmpeg -i %s -r 20 -f -vf fps=fps=20 %s' % (videopath, picpath) + '\%d.jpeg'
        # cmd = 'ffmpeg -i %s -r 20 -f -vf fps=fps=20 %s' % (videopath, picpath) + '\%d.jpeg'
        # print self.getFFMpegPath() + cmd
        cmd=self.getFFMpegPath() + cmd
        # os.system('"{}"'.format(cmd))
        CREATE_NO_WINDOW = 0x08000000
        subprocess.call(cmd,creationflags=CREATE_NO_WINDOW)

if __name__ == '__main__':
    pass
