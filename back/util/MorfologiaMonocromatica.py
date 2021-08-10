from util.Imagem import *
import numpy as np


class MorfologiaMono(Imagem):

    def subtract(self, imgX: Imagem, imgY: Imagem):
        nChannels = imgX.getNChannels()
        height = imgX.getHeight()
        width = imgX.getWidth()
        matA = imgX.getMatrix()
        matB = imgY.getMatrix()

        colorSub = None
        matS = np.zeros((nChannels, height, width))

        for c in range(nChannels):
            for y in range(height):
                for x in range(width):
                    colorSub = matA[c][y][x] - matB[c][y][x]
                    if (colorSub < 0):
                        colorSub = 0
                    matS[c, y, x] = colorSub

        imagem = Imagem()
        imagem.setMatrixImage(matS)
        imagem.showImage('Subtraction image')
        return imagem.setMatrixImage(matS)

    def _subtract(self, imgX: Imagem, imgY: Imagem):
        nChannels = imgX.getNChannels()
        height = imgX.getHeight()
        width = imgX.getWidth()
        matA = imgX.getMatrix()
        matB = imgY.getMatrix()

        colorSub = None
        matS = np.zeros((nChannels, height, width))

        for c in range(nChannels):
            for y in range(height):
                for x in range(width):
                    colorSub = matA[c][y][x] - matB[c][y][x]
                    if (colorSub < 0):
                        colorSub = 0
                    matS[c, y, x] = colorSub

        imagem = Imagem()
        imagem.setMatrixImage(matS)
        return imagem.getMatrix()

    def erode(self, img: Imagem, mat, bool=False):
        nChannels = img.getNChannels()
        height = img.getHeight()
        width = img.getWidth()
        matE = img.getMatrix()
        matS = np.zeros((nChannels, height, width))
        radius = int((len(mat) - 1)/2)
        min = 900000000000000000

        for c in range(nChannels):
            for y in range((radius), (height-radius)):
                for x in range((radius), (width - radius)):
                    for z in range((-radius), (radius + 1)):
                        for w in range((-radius), (radius+1)):
                            if(min > matE[c][y + z][x+w] + mat[(z+radius)][(w+radius)]):
                                min = matE[c][y+z][x+w] + \
                                    mat[(z+radius)][(w+radius)]

                    if (min > 0):
                        matS[c, y, x] = min
                    else:
                        matS[c, y, x] = 0

                    min = 900000000000000000

        imagem = Imagem()
        imagem.setMatrixImage(matS)
        if (bool == True):
            imagem.showImage('Closing image')
        imagem.showImage('Erosion image')
        return imagem.setMatrixImage(matS)

    def dilate(self, img: Imagem, mat, bool):
        nChannels = img.getNChannels()
        height = img.getHeight()
        width = img.getWidth()
        matE = img.getMatrix()
        matS = np.zeros((nChannels, height, width))
        radius = int((len(mat) - 1)/2)
        max = -900000000000000000

        for c in range(nChannels):
            for y in range(radius, height - radius):
                for x in range(radius, width - radius):
                    for z in range(-radius, radius+1):
                        for w in range(-radius, radius+1):
                            if (max < matE[c][y+z][x+w] + mat[z+radius][w+radius]):
                                max = matE[c][y+z][x+w] + \
                                    mat[z+radius][w+radius]

                    if (max > 0):
                        matS[c, y, x] = max
                    else:
                        matS[c, y, x] = 0

                    max = -900000000000000000

        imagem = Imagem()
        imagem.setMatrixImage(matS)
        if (bool == True):
            imagem.showImage('Opening image')
        else:
            imagem.showImage('Dilation image')
        return imagem.setMatrixImage(matS)

    def _erode(self, img: Imagem, mat):
        nChannels = img.getNChannels()
        height = img.getHeight()
        width = img.getWidth()
        matE = img.getMatrix()
        matS = np.zeros((nChannels, height, width))
        radius = int((len(mat) - 1)/2)
        min = 900000000000000000

        for c in range(nChannels):
            for y in range((radius), (height-radius)):
                for x in range((radius), (width - radius)):
                    for z in range((-radius), (radius + 1)):
                        for w in range((-radius), (radius+1)):
                            if(min > matE[c][y + z][x+w] + mat[(z+radius)][(w+radius)]):
                                min = matE[c][y+z][x+w] + \
                                    mat[(z+radius)][(w+radius)]

                    if (min > 0):
                        matS[c, y, x] = min
                    else:
                        matS[c, y, x] = 0

                    min = 900000000000000000

        imagem = Imagem()
        imagem.setMatrixImage(matS)
        return imagem

    def _dilate(self, img: Imagem, mat):
        nChannels = img.getNChannels()
        height = img.getHeight()
        width = img.getWidth()
        matE = img.getMatrix()
        matS = np.zeros((nChannels, height, width))
        radius = int((len(mat) - 1)/2)
        max = -900000000000000000

        for c in range(nChannels):
            for y in range(radius, height - radius):
                for x in range(radius, width - radius):
                    for z in range(-radius, radius+1):
                        for w in range(-radius, radius+1):
                            if (max < matE[c][y+z][x+w] + mat[z+radius][w+radius]):
                                max = matE[c][y+z][x+w] + \
                                    mat[z+radius][w+radius]

                    if (max > 0):
                        matS[c, y, x] = max
                    else:
                        matS[c, y, x] = 0

                    max = -900000000000000000

        imagem = Imagem()
        imagem.setMatrixImage(matS)
        return imagem

    def opening(self, img: Imagem, mat):
        return self.dilate(self._erode(img, mat), mat, True)

    def closing(self, img: Imagem, mat):
        return self.erode(self._dilate(img, mat), mat, True)

    def gradient(self, img: Imagem, mat):
        imagem = Imagem()
        imagem.setMatrixImage(self._subtract(
            self._dilate(img, mat), self._erode(img, mat)))
        return imagem.showImage('Gradient image')
