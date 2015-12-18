import numpy as np
import cv2


class Buffer:

    Buf = []

    inputFrame = 0
    outputFrame = 0
    frameWidth = 0
    frameHeight = 0

    def __init__(self, frames, frameWidth, frameHeight):
        self.frameHeight = frameHeight
        self.frameWidth = frameWidth
        for i in range(frames):
            self.Buf.append(np.zeros((frameWidth, frameHeight, 3), np.uint8))

        self.inputFrame = frames - 1
        self.outputFrame = 0

    def getFrame(self):
        return self.Buf[self.outputFrame]

    def getFrames(self, n, x):
        frames = []

        for i in range(n):

            ind = self.inputFrame - i*x
            if ind < 0 :
                ind += len(self.Buf)

            frames.append(self.Buf[ind])

        return frames

    def addFrame(self, frame):

        self.Buf[self.inputFrame] = frame

        self.inputFrame+=1
        self.outputFrame+=1

        if self.inputFrame >= len(self.Buf):
            self.inputFrame = 0

        if self.outputFrame >= len(self.Buf):
            self.outputFrame = 0