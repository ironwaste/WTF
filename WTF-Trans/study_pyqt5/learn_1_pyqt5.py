from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # self.setFixedSize(400, 400)
        self.setWindowTitle('PyQt5')
        button = QPushButton('Press Me !')

        self.setCentralWidget(button)


app = QApplication(sys.argv) # sys.argv 是使用 命令行参数来控制其中qt控件，如果不需要则可以直接省略
# like this : -> app = QApplication([])

# 通常使用变量名称 window 来创建instance实例 QWidget
window = MainWindow()
window.show()
# start the event loop
app.exec() # 用于启动事件循环
