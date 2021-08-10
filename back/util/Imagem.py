import tkinter as tk
from PIL import Image, ImageTk


class Imagem:

    _img = None

    def MODE_RBG(self): return 'RGB'
    def MODE_GRAY(self): return 'L'
    def TYPE_JPG(self): return 'JPEG'
    def TYPE_PNG(self): return 'PNG'
    def TYPE_GIF(self): return 'GIF'
    def TYPE_PDF(self): return 'PDF'

    def loadImage(self, path):
        try:
            self._img = Image.open(path)
        except:
            print('Attention! Error when trying to open file: ' + path)

    def loadEmptyImage(self, type, height=0, width=0):
        if type == self.MODE_RBG():
            self._img = Image.new(type, (height, width), (0, 0, 0))
        else:
            self._img = Image.new(type, (height, width), (0))

    def setMatrixImage(self, mat):
        nChannels = len(mat)
        height = len(mat[0])
        width = len(mat[0][0])

        if (nChannels == 3):
            self.loadEmptyImage(self.MODE_RBG(), height, width)
            color = []
            for y in range(0, height):
                for x in range(0, width):
                    for c in range(0, nChannels):
                        color.append(int(mat[c][y][x]))
                    self._img.putpixel((x, y), tuple(color))
                    color.clear()

        else:
            self.loadEmptyImage(self.MODE_GRAY(), height, width)
            for y in range(height):
                for x in range(width):
                    self._img.putpixel((x, y), int(mat[0][y][x]))

    def _setMatrixImage(self, mat):
        nChannels = len(mat)
        height = len(mat[0])
        width = len(mat[0][0])

        if (nChannels == 3):
            self.loadEmptyImage(self.MODE_RBG(), height, width)
            color = []
            for y in range(0, height):
                for x in range(0, width):
                    for c in range(0, nChannels):
                        color.append(mat[c][y][x])
                    self._img.putpixel((x, y), tuple(color))
                    color.clear()

        else:
            self.loadEmptyImage(self.MODE_GRAY(), height, width)
            for y in range(height):
                for x in range(width):
                    self._img.putpixel((x-1, y-1), int(mat[0][y][x]))

    def toGray(self):
        self._img = self._img.convert(self.MODE_GRAY())

    def toRBG(self):
        self._img = self._img.convert(self.MODE_RBG())

    def getHeight(self):
        return self._img.height

    def getWidth(self):
        return self._img.width

    def getNChannels(self):
        if self._img.mode == self.MODE_RBG():
            return 3
        elif self._img.mode == self.MODE_GRAY():
            return 1
        else:
            print(
                'The image does not have one or three channels. Please convert it into RBG or gray')

    def getMatrix(self):
        nChannels = self.getNChannels()
        height = self.getHeight()
        width = self.getWidth()
        mat = []

        for c in range(nChannels):
            page = []
            for y in range(height):
                page += [([0]*width)]
            mat += [page]

        color = None
        vectorImg = self._img.load()

        if nChannels == 3:
            for y in range(0, height):
                for x in range(0, width):
                    color = vectorImg[x, y]

                    for c in range(0, nChannels):
                        mat[c][y][x] = color[c]

        else:
            for y in range(0, height):
                for x in range(0, width):
                    mat[0][y][x] = self._img.getpixel((x, y))

        return mat

    def saveImage(self, path, type):
        self._img.save(path, type)

    def showImage(self, title=''):
        root = tk.Tk()
        root.title(title)
        photo = ImageTk.PhotoImage(self._img)
        label = tk.Label(root, image=photo)
        label.image = photo
        label.grid(row=2, column=0)
        root.mainloop()
