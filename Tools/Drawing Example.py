
import sys, random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

#based on http://zetcode.com/gui/pyqt5/tetris/
""" This shows a drawable space being redrawn every 300ms, along side a button that does nothing, in a 3X2 grid layout"""
class PaintWidget(QWidget):
    Speed = 300#ms to redraw at

    def __init__(self):
        super().__init__()
        self.i = 0
        self.initUI()

    def initUI(self):
        self.text = "HI"
        self.i = self.i + 1

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Draw text')
        self.show()
        self.timer = QBasicTimer()#the timer is to redraw the screen (calls timerEvent )
        self.timer.start(PaintWidget.Speed, self)

    def paintEvent(self, event):

        qp = QPainter()
        #qp.setBackground(QBrush(QColor.green(self)))
        qp.begin(self)
        self.drawText(event, qp)
        qp.end()


    def drawText(self, event, qp):

        qp.setPen(QColor(168, 34, 3))
        qp.setFont(QFont('Decorative', 10))
        qp.drawText(event.rect(), Qt.AlignCenter, "Hi" + str(self.i))

    #unused but her eto show what it dose
    def drawPoints(self, qp):

        qp.setPen(Qt.red)
        size = self.size()

        for i in range(1000):
            x = random.randint(1, size.width()-1)
            y = random.randint(1, size.height()-1)
            qp.drawPoint(x, y)

    #unused but here to show what it does
    def drawSquare(self, painter, x, y):
        color = QColor(0xCC6666)
        painter.fillRect(x + 1, y + 1, self.squareWidth() - 2,
            self.squareHeight() - 2, color)

        #adds 3d efect to the edges
        painter.setPen(color.lighter())
        painter.drawLine(x, y + self.squareHeight() - 1, x, y)
        painter.drawLine(x, y, x + self.squareWidth() - 1, y)

        painter.setPen(color.darker())
        painter.drawLine(x + 1, y + self.squareHeight() - 1,
            x + self.squareWidth() - 1, y + self.squareHeight() - 1)
        painter.drawLine(x + self.squareWidth() - 1,
            y + self.squareHeight() - 1, x + self.squareWidth() - 1, y + 1)

    def timerEvent(self, event):
        self.i = self.i + 1
        if event.timerId() == self.timer.timerId():
            self.update()

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        title = QPushButton("eg", self)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 4, 0)
        pw = PaintWidget()
        grid.addWidget(pw, 1, 0, 2, 2)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
