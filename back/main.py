from numpy.lib.type_check import imag
from util.Imagem import *
from util.MorfologiaMonocromatica import *
from util.MorfologiaBinaria import *
from util.Dithering import *
import numpy as np


def mainChoices():
    print('\n1- Dithering')
    print('\n2- Morfologia matemática binária')
    print('\n3- Morfologia matemática monocromática')
    value = input('\nPor favor, selecione uma das opcoes: \n')

    value = int(value)
    if (value == 1):
        return testingDithering()
    elif (value == 2):
        return testingMorfBi()
    else:
        return testingMorfMono()


def testingDithering():
    mat1 = np.array([[6, 8, 4], [1, 0, 3], [5, 2, 7]])
    imagem = Imagem()
    imagem.loadImage('img/lenna.jpg')
    imagem.toGray()
    print('\n1- Limiar simples')
    print('\n2- Limiar com modulação aleatória')
    print('\n3- Limiar com modulação ordenada periódico aglomerado')
    print('\n4- Limiar com modulação ordenada periódico disperso')
    print('\n5- Limiar com modulação ordenada aperiódico')
    value = input('\nPor favor, selecione uma das opcoes: \n')

    value = int(value)
    if (value == 1):
        return testSimpleThreshold(imagem)
    elif (value == 2):
        return testRandomModulation(imagem)
    elif (value == 3):
        return testModOrderedAglomeration(imagem, mat1)
    elif (value == 4):
        return testModOrderedDispersion(imagem, mat1)
    else:
        return testModOrderedAperiodicDispersed(imagem)


def testSimpleThreshold(img):
    dithering = Dithering()
    dithering.simpleThreshold(img)


def testRandomModulation(img):
    dithering = Dithering()
    dithering.randomModulation(img)


def testModOrderedAglomeration(img, mat):
    dithering = Dithering()
    dithering.modOrderedAglomeration(img, mat)


def testModOrderedDispersion(img, mat):
    dithering = Dithering()
    dithering.modOrderedDispersion(img, mat)


def testModOrderedAperiodicDispersed(img):
    dithering = Dithering()
    dithering.modOrderedAperiodicDispersed(img)


def testingMorfBi():
    mat1 = np.array([[0, 255, 0], [255, 255, 255], [0, 255, 0]])
    mat2 = np.array([[0, 0, 255, 0, 0], [0, 255, 255, 255, 0], [
        255, 255, 255, 255, 255], [0, 255, 255, 255, 0], [0, 0, 255, 0, 0]])

    imgTeste = Imagem()
    imgTeste.loadImage('img/b.png')
    print('\n1- Dilatação')
    print('\n2- Erosão')
    print('\n3- Abertura')
    print('\n4- Fechamento')
    print('\n5- Borda interna')
    print('\n6- Borda externa')
    value = input('\nPor favor, selecione uma das opcoes: \n')

    value = int(value)
    if (value == 1):
        return testMorfBiDilate(imgTeste, mat2)
    elif (value == 2):
        return testMorfBiErode(imgTeste, mat2)
    elif (value == 3):
        return testMorfBiOpening(imgTeste, mat2)
    elif (value == 4):
        return testMorfBiClosing(imgTeste, mat2)
    elif (value == 5):
        return testMorfBiInternalBorder(imgTeste, mat2)
    else:
        return testMorfBiExternalBorder(imgTeste, mat2)


def testMorfBiDilate(img, mat):
    mono = MorfologiaBinaria()
    mono.dilate(img, mat)


def testMorfBiErode(img, mat):
    mono = MorfologiaBinaria()
    mono.erode(img, mat)


def testMorfBiInternalBorder(img, mat):
    mono = MorfologiaBinaria()
    mono.internalBorder(img, mat)


def testMorfBiExternalBorder(img, mat):
    mono = MorfologiaBinaria()
    mono.externalBorder(img, mat)


def testMorfBiOpening(img, mat):
    mono = MorfologiaBinaria()
    mono.opening(img, mat)


def testMorfBiClosing(img, mat):
    mono = MorfologiaBinaria()
    mono.closing(img, mat)


def testingMorfMono():
    mat1 = np.array([[1, 1, 1], [1, 2, 1], [1, 1, 1]])
    mat2 = np.array([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [
                    1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])

    imgRBG = Imagem()
    imgRBG.loadImage('img/lennaRGB.jpg')
    imgRBG.toGray()

    print('\n1- Erosão')
    print('\n2- Dilatação')
    print('\n3- Abertura')
    print('\n4- Fechamento')
    print('\n5- Gradiente')
    value = input('\nPor favor, selecione uma das opcoes: \n')

    value = int(value)

    if (value == 1):
        return testMorfMonoErode(imgRBG, mat2)
    elif (value == 2):
        return testMorfMonoDilate(imgRBG, mat2)
    elif (value == 3):
        return testMorfMonoOpening(imgRBG, mat2)
    elif (value == 4):
        return testMorfMonoClosing(imgRBG, mat2)
    else:
        return testMorfMonoGradient(imgRBG, mat2)


def testMorfMonoErode(img, mat):
    mono = MorfologiaMono()
    mono.erode(img, mat)


def testMorfMonoDilate(img, mat):
    mono = MorfologiaMono()
    mono.dilate(img, mat)


def testMorfMonoOpening(img, mat):
    mono = MorfologiaMono()
    mono.opening(img, mat)


def testMorfMonoClosing(img, mat):
    mono = MorfologiaMono()
    mono.closing(img, mat)


def testMorfMonoGradient(img, mat):
    mono = MorfologiaMono()
    mono.gradient(img, mat)


mainChoices()
