import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QTextEdit, QPushButton, QSpacerItem, QSizePolicy, QLabel,QTabWidget
from PyQt5.QtCore import QTimer

class MyPage(QWidget):
    def __init__(self, title):
        super().__init__()
        layout = QVBoxLayout(self)

        # 🔥 外層橫向，兩組 (Combo + 色塊區)
        combo_group_layout = QHBoxLayout()

        # ===== 左邊 Combo1 + 色塊 (上下排列) =====
        left_widget = QWidget()
        left_group = QVBoxLayout(left_widget)
        self.combo1 = QComboBox()
        self.combo1.addItems(["選項一", "選項二", "選項三"])
        self.combo1.setMinimumWidth(200)
        left_group.addWidget(self.combo1)

        color_layout1 = QHBoxLayout()
        color_layout1.addStretch()
        self.color_labels1 = []
        for _ in range(3):
            color_label = QLabel()
            color_label.setFixedSize(10, 10)
            color_label.setStyleSheet("""
                background-color: black;
                border-radius: 5px;
                border: 1px solid #333;
            """)
            self.color_labels1.append(color_label)
            color_layout1.addWidget(color_label)
        left_group.addLayout(color_layout1)
        combo_group_layout.addWidget(left_widget)

        # ===== 右邊 Combo2 + 色塊 (上下排列) =====
        right_widget = QWidget()
        right_group = QVBoxLayout(right_widget)
        self.combo2 = QComboBox()
        self.combo2.addItems(["選項一", "選項二", "選項三"])
        self.combo2.setMinimumWidth(200)
        right_group.addWidget(self.combo2)

        color_layout2 = QHBoxLayout()
        color_layout2.addStretch()
        self.color_labels2 = []
        for _ in range(3):
            color_label = QLabel()
            color_label.setFixedSize(10, 10)
            color_label.setStyleSheet("""
                background-color: black;
                border-radius: 5px;
                border: 1px solid #333;
            """)
            self.color_labels2.append(color_label)
            color_layout2.addWidget(color_label)
        right_group.addLayout(color_layout2)
        combo_group_layout.addWidget(right_widget)

        layout.addLayout(combo_group_layout)

        # 中間文字區
        text_area = QTextEdit()
        text_area.setReadOnly(True)
        text_area.setText("\n".join([f"{title} 假資料第 {i} 行" for i in range(1, 30)]))
        layout.addWidget(text_area)

        # 右下按鈕
        button_layout = QHBoxLayout()
        button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        btn1 = QPushButton("確定")
        btn2 = QPushButton("取消")
        button_layout.addWidget(btn1)
        button_layout.addWidget(btn2)
        layout.addLayout(button_layout)

    # 公用方法：獨立改色
    def change_color(self, group, index, color):
        if group == 1 and 0 <= index < len(self.color_labels1):
            self.color_labels1[index].setStyleSheet(
                f"background-color: {color}; border-radius: 5px; border: 1px solid #333;"
            )
        elif group == 2 and 0 <= index < len(self.color_labels2):
            self.color_labels2[index].setStyleSheet(
                f"background-color: {color}; border-radius: 5px; border: 1px solid #333;"
            )
class MyPage2(QWidget):
    def __init__(self, title):
        super().__init__()
        layout = QVBoxLayout(self)

        # 加這行，讓按鈕被推到底部
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # 右下按鈕
        button_layout = QHBoxLayout()
        button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        btn1 = QPushButton("確定")
        btn2 = QPushButton("取消")
        button_layout.addWidget(btn1)
        button_layout.addWidget(btn2)

        layout.addLayout(button_layout)


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('SQ7615+SQ7131 驗證工具')
        
        self.setMinimumSize(400, 300)

        main_layout = QVBoxLayout(self)

        # 底部的 QTabWidget
        tabs = QTabWidget()

        # 關鍵：self.page1 實例化保存起來
        self.page1 = MyPage("頁面一")
        tabs.addTab(self.page1, "驗證")
        tabs.addTab(MyPage2("頁面二"), "尚未開放")
        tabs.addTab(MyPage2("頁面三"), "尚未開放")
        tabs.setTabPosition(QTabWidget.South)

        main_layout.addWidget(tabs)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)


    # 加轉接 change_color
    def change_color(self, group, index, color):
        self.page1.change_color(group, index, color)
        

