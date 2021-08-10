from flask import Flask
from util.Imagem import *
from util.MorfologiaMonocromatica import *
from util.MorfologiaBinaria import *
from util.Dithering import *
import numpy as np

app = Flask(__name__)

@app.route('/dithering/testSimpleThreshold')
def testSimpleThresholdDithering():
  imagem = Imagem()
  imagem.loadImage('img/lenna.jpg')
  imagem.toGray()
  dithering = Dithering()
  return dithering.simpleThreshold(imagem)

@app.route('/dithering/testRandomModulation')
def testRandomModulationDithering():
  imagem = Imagem()
  imagem.loadImage('img/lenna.jpg')
  imagem.toGray()
  dithering = Dithering()
  return dithering.randomModulation(imagem)

@app.route('/dithering/testModOrderedAglomeration')
def testModOrderedAglomeration():
  mat1 = np.array([[6, 8, 4], [1, 0, 3], [5, 2, 7]])
  imagem = Imagem()
  imagem.loadImage('img/lenna.jpg')
  imagem.toGray()
  dithering = Dithering()
  return dithering.modOrderedAglomeration(imagem, mat1)

@app.route('/dithering/testModOrderedDispersion')
def testModOrderedDispersion():
  mat1 = np.array([[6, 8, 4], [1, 0, 3], [5, 2, 7]])
  imagem = Imagem()
  imagem.loadImage('img/lenna.jpg')
  imagem.toGray()
  dithering = Dithering()
  return dithering.modOrderedDispersion(imagem, mat1)

@app.route('/dithering/testModOrderedAperiodicDispersed')
def testModOrderedAperiodicDispersed():
  imagem = Imagem()
  imagem.loadImage('img/lenna.jpg')
  imagem.toGray()
  dithering = Dithering()
  return dithering.modOrderedAperiodicDispersed(imagem)

@app.route('/morf-bi/testMorfBiDilate')
def testMorfBiDilate():
  mat = np.array([[0, 0, 255, 0, 0], [0, 255, 255, 255, 0], [
        255, 255, 255, 255, 255], [0, 255, 255, 255, 0], [0, 0, 255, 0, 0]])
  imgTeste = Imagem()
  imgTeste.loadImage('img/b.png')
  mono = MorfologiaBinaria()
  return mono.dilate(imgTeste, mat)

@app.route('/morf-bi/testMorfBiErode')
def testMorfBiErode():
  mat = np.array([[0, 0, 255, 0, 0], [0, 255, 255, 255, 0], [
        255, 255, 255, 255, 255], [0, 255, 255, 255, 0], [0, 0, 255, 0, 0]])
  imgTeste = Imagem()
  imgTeste.loadImage('img/b.png')
  mono = MorfologiaBinaria()
  return mono.erode(imgTeste, mat)

@app.route('/morf-bi/testMorfBiInternalBorder')
def testMorfBiInternalBorder():
  mat = np.array([[0, 0, 255, 0, 0], [0, 255, 255, 255, 0], [
        255, 255, 255, 255, 255], [0, 255, 255, 255, 0], [0, 0, 255, 0, 0]])
  imgTeste = Imagem()
  imgTeste.loadImage('img/b.png')
  mono = MorfologiaBinaria()
  return mono.internalBorder(imgTeste, mat)

@app.route('/morf-bi/testMorfBiExternalBorder')
def testMorfBiExternalBorder():
  mat = np.array([[0, 0, 255, 0, 0], [0, 255, 255, 255, 0], [
        255, 255, 255, 255, 255], [0, 255, 255, 255, 0], [0, 0, 255, 0, 0]])
  imgTeste = Imagem()
  imgTeste.loadImage('img/b.png')
  mono = MorfologiaBinaria()
  return mono.externalBorder(imgTeste, mat)

@app.route('/morf-bi/testMorfBiOpening')
def testMorfBiOpening():
  mat = np.array([[0, 0, 255, 0, 0], [0, 255, 255, 255, 0], [
        255, 255, 255, 255, 255], [0, 255, 255, 255, 0], [0, 0, 255, 0, 0]])
  imgTeste = Imagem()
  imgTeste.loadImage('img/b.png')
  mono = MorfologiaBinaria()
  return mono.opening(imgTeste, mat)

@app.route('/morf-bi/testMorfBiClosing')
def testMorfBiClosing():
  mat = np.array([[0, 0, 255, 0, 0], [0, 255, 255, 255, 0], [
        255, 255, 255, 255, 255], [0, 255, 255, 255, 0], [0, 0, 255, 0, 0]])
  imgTeste = Imagem()
  imgTeste.loadImage('img/b.png')
  mono = MorfologiaBinaria()
  return mono.closing(imgTeste, mat)

@app.route('/morf-mono/testMorfMonoErode')
def testMorfMonoErode():
  mat = np.array([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [
                    1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
  imgRGB = Imagem()
  imgRGB.loadImage('img/lennaRGB.jpg')
  imgRGB.toGray()
  mono = MorfologiaMono()
  return mono.erode(imgRGB, mat)

@app.route('/morf-mono/testMorfMonoDilate')
def testMorfMonoDilate():
  mat = np.array([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [
                    1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
  imgRGB = Imagem()
  imgRGB.loadImage('img/lennaRGB.jpg')
  imgRGB.toGray()
  mono = MorfologiaMono()
  return mono.dilate(imgRGB, mat)

@app.route('/morf-mono/testMorfMonoOpening')
def testMorfMonoOpening():
  mat = np.array([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [
                    1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
  imgRGB = Imagem()
  imgRGB.loadImage('img/lennaRGB.jpg')
  imgRGB.toGray()
  mono = MorfologiaMono()
  return mono.opening(imgRGB, mat)

@app.route('/morf-mono/testMorfMonoClosing')
def testMorfMonoClosing():
  mat = np.array([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [
                    1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
  imgRGB = Imagem()
  imgRGB.loadImage('img/lennaRGB.jpg')
  imgRGB.toGray()
  mono = MorfologiaMono()
  return mono.closing(imgRGB, mat)

@app.route('/morf-mono/testMorfMonoGradient')
def testMorfMonoGradient():
  mat = np.array([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [
                    1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
  imgRGB = Imagem()

  imgRGB.loadImage('img/lennaRGB.jpg')
  imgRGB.toGray()
  mono = MorfologiaMono()
  return mono.gradient(imgRGB, mat)


if __name__ == '__main__':
  app.run()