from util.Imagem import *
import numpy as np
from random import random, randrange


class Dithering(Imagem):
    def simpleThreshold(self, img: Imagem):
        nChannels = img.getNChannels()
        height = img.getHeight()
        width = img.getWidth()
        matI = img.getMatrix()
        matO = np.zeros((nChannels, height, width))
        white = 255
        black = 0
        threshold = int((white + black) / 2)

        for c in range(nChannels):
            for y in range(height):
                for x in range(width):
                    if (matI[c][y][x] < threshold):
                        matO[c, y, x] = black
                    else:
                        matO[c, y, x] = white

        imagem = Imagem()
        imagem.setMatrixImage(matO)
        imagem.showImage('Simple threshold')
        return imagem

    def randomModulation(self, img: Imagem):
        nChannels = img.getNChannels()
        height = img.getHeight()
        width = img.getWidth()
        matI = img.getMatrix()
        matO = np.zeros((nChannels, height, width))
        white = 255
        black = 0
        threshold = int((white + black) / 2)

        for c in range(nChannels):
            for y in range(height):
                for x in range(width):
                    aux = matI[c][y][x] + randrange(-128, 128) - threshold
                    if (aux < threshold):
                        matO[c, y, x] = black
                    else:
                        matO[c, y, x] = white

        imagem = Imagem()
        imagem.setMatrixImage(matO)
        imagem.showImage('Random modulation')
        return imagem

    def quantize(self, img: Imagem, input, output):
        faixa = int(input/output)
        mat = img.getMatrix()
        nChannels = img.getNChannels()
        height = img.getHeight()
        width = img.getWidth()

        for c in range(nChannels):
            for y in range(height):
                for x in range(width):
                    color = int(mat[c][y][x]/faixa)
                    mat[c][y][x] = color

        imagem = Imagem()
        imagem.setMatrixImage(mat)
        return imagem

    def modOrderedAglomeration(self, img: Imagem, mat):
        nChannels = self.quantize(img, 256, len(
            mat)*(len(mat) + 1)).getNChannels()
        height = self.quantize(img, 256, len(mat)*(len(mat) + 1)).getHeight()
        width = self.quantize(img, 256, len(mat)*(len(mat) + 1)).getWidth()
        matI = self.quantize(img, 256, len(mat)*(len(mat) + 1)).getMatrix()
        coefficient = len(mat)
        matO = np.zeros((nChannels, height*coefficient, width*coefficient))
        white = 255
        black = 0

        for c in range(nChannels):
            for y in range(height):
                for x in range(width):
                    for z in range(len(mat)):
                        for w in range(len(mat[z])):
                            if (matI[c][y][x] > mat[z][w]):
                                matO[c, y*coefficient + z,
                                     x*coefficient + w] = white
                            else:
                                matO[c, y*coefficient + z,
                                     x*coefficient + w] = black

        imagem = Imagem()
        imagem.setMatrixImage(matO)
        imagem.showImage('Modulation ordered by agglomeration')
        return imagem

    def modOrderedDispersion(self, img: Imagem, mat):
        nChannels = self.quantize(img, 256, len(mat)*len(mat)).getNChannels()
        height = self.quantize(img, 256, len(mat)*len(mat)).getHeight()
        width = self.quantize(img, 256, len(mat)*len(mat)).getWidth()
        matI = self.quantize(img, 256, len(mat)*len(mat)).getMatrix()
        matO = np.zeros((nChannels, height, width))
        white = 255
        black = 0
        aux = len(mat)
        z = 0
        w = 0

        for c in range(nChannels):
            for y in range(height):
                w = y % aux
                for x in range(width):
                    z = x % aux

                    if (matI[c][y][x] > mat[w][z]):
                        matO[c, y, x] = white
                    else:
                        matO[c, y, x] = black

        imagem = Imagem()
        imagem.setMatrixImage(matO)
        imagem.showImage('modOrderedDispersion')
        return imagem

    def modOrderedAperiodicDispersed(self, img: Imagem):
        nChannels = img.getNChannels()
        height = img.getHeight()
        width = img.getWidth()
        matI = img.getMatrix()
        matO = np.zeros((nChannels, height, width))
        white = 255
        black = 0
        threshold = int((white + black + 1)/2)
        aux = None

        for c in range(nChannels):
            for x in range(width-1):
                for y in range(height-1):
                    if (matI[c][y][x] < threshold):
                        aux = matI[c][y][x] - black
                        matO[c, y, x] = black

                    else:
                        aux = matI[c][y][x] - white
                        matO[c, y, x] = white

                    matI[c][y+1][x] += int((3*aux)/8)
                    matI[c][y][x+1] += int((3*aux)/8)
                    matI[c][y+1][x+1] += int((aux/8))

        imagem = Imagem()
        imagem.setMatrixImage(matO)
        imagem.showImage('modOrderedAperiodicDispersed')
        return imagem
