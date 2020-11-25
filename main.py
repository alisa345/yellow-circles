import sys
import random

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)


    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            qual = random.randint(1, 10)
            for i in range(qual):
                self.draw_cicrle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_cicrle(self, qp):
        x = random.randint(70, 430)
        y = random.randint(40, 470)
        diametr = random.randint(5, 90)
        qp.setBrush(QColor(255, 203, 0))
        qp.drawEllipse(x, y, diametr, diametr)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())