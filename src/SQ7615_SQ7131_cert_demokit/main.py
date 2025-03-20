import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
from gui import MyApp  

if __name__ == '__main__':
    print("Application initialized")
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    # 測試：2 秒後把 Combo1 下第 1 顆變紅
    QTimer.singleShot(2000, lambda: window.change_color(1, 0, "red"))
    # 測試：4 秒後把 Combo2 下第 3 顆變綠
    QTimer.singleShot(4000, lambda: window.change_color(2, 2, "yellow"))
    sys.exit(app.exec_())
