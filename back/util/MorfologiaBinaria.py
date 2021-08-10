from util.Imagem import *
import numpy as np


class MorfologiaBinaria(Imagem):

    def subtract(self, imgX: Imagem, imgY: Imagem):
        nChannels = imgX.getNChannels()
        height = imgX.getHeight()
        width = imgX.getWidth()
        matX = imgX.getMatrix()
        matY = imgY.getMatrix()

        colorSub = None
        matS = np.zeros((nChannels, height, width))

        for c in range(nChannels):
            for y in range(height):
                for x in range(width):
                    colorSub = matX[c][y][x] - matY[c-1][y-1][x-1]
                    if (colorSub < 0):
                        colorSub = 0
                    matS[c, y, x] = colorSub

        return matS

    def erode(self, img: Imagem, mat, bool=False):
        nChannels = img.getNChannels()
        height = img.getHeight()
        width = img.getWidth()
        matE = img.getMatrix()
        matS = np.zeros((nChannels, height, width))
        radius = int((len(mat) - 1)/2)
        auxBool = False

        for c in range(nChannels):
            for y in range(radius, height-radius):
                for x in range(radius, width-radius):
                    for z in range(-radius, radius+1):
                        for w in range(-radius, radius+1):
                            if(mat[z+radius][w+radius] == 255):
                                if (matE[c][y+z][x+w] != mat[z+radius][w+radius]):
                                    auxBool = False

                    if(auxBool == True):
                        matS[c, y, x] = matE[c][y][x]
                    else:
                        matS[c, y, x] = 0
                    auxBool = True

        imagem = Imagem()
        imagem._setMatrixImage(matS)
        if (bool == True):
            imagem.showImage('Closing image')
        else:
            imagem.showImage('Erosion image')
        return imagem

    def dilate(self, img: Imagem, mat, bool=False):
        nChannels = img.getNChannels()
        height = img.getHeight()
        width = img.getWidth()
        matE = img.getMatrix()
        matS = np.zeros((nChannels, height, width))
        radius = int((len(mat) - 1)/2)
        auxBool = False

        for c in range(nChannels):
            for y in range(radius, height-radius):
                for x in range(radius, width-radius):
                    for z in range(-radius, radius+1):
                        for w in range(-radius, radius+1):
                            if (mat[z+radius][w+radius] == 255):
                                if (matE[c][y+z][x+w] == mat[z+radius][w+radius]):
                                    auxBool = True

                    if (auxBool == True):
                        matS[c, y, x] = 255
                    else:
                        matS[c, y, x] = 0
                    auxBool = False

        imagem = Imagem()
        imagem._setMatrixImage(matS)
        if (bool == True):
            imagem.showImage('Opening image')
        else:
            imagem.showImage('Dilation image')
        return imagem

    def internalBorder(self, img: Imagem, mat):
        imagem = Imagem()
        imagem._setMatrixImage(self.subtract(img, self.erode(img, mat)))
        imagem.showImage('Internal border')
        return imagem

    def externalBorder(self, img: Imagem, mat):
        imagem = Imagem()
        imagem._setMatrixImage(self.subtract(self.dilate(img, mat), img))
        imagem.showImage('External border')
        return imagem

    def opening(self, img: Imagem, mat):
        return self.dilate(self.erode(img, mat), mat, True)

    def closing(self, img: Imagem, mat):
        return self.erode(self.dilate(img, mat), mat, True)
