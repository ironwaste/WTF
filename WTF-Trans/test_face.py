# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(1407, 908)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        widget.setFont(font)
        widget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)

        # 主布局 - 水平布局
        self.horizontalLayout = QtWidgets.QHBoxLayout(widget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # 左侧垂直布局 - 使用QWidget作为容器
        self.left_widget = QtWidgets.QWidget(widget)
        self.left_layout = QtWidgets.QVBoxLayout(self.left_widget)
        self.left_layout.setObjectName("left_layout")
        self.left_layout.setContentsMargins(20, 20, 20, 20)  # 增加内边距
        self.left_layout.setSpacing(20)  # 增加组件间距

        # 按钮行1 - 竞技导入/导出
        self.button_row1 = QtWidgets.QHBoxLayout()
        self.button_row1.setObjectName("button_row1")
        self.fight_import_button = QtWidgets.QPushButton(self.left_widget)
        self.fight_import_button.setObjectName("fight_import_button")
        self.button_row1.addWidget(self.fight_import_button)
        self.fight_output_buttom = QtWidgets.QPushButton(self.left_widget)
        self.fight_output_buttom.setObjectName("fight_output_buttom")
        self.button_row1.addWidget(self.fight_output_buttom)
        self.left_layout.addLayout(self.button_row1)

        # 按钮行2 - 品势导入/导出
        self.button_row2 = QtWidgets.QHBoxLayout()
        self.button_row2.setObjectName("button_row2")
        self.poomsae_import_button = QtWidgets.QPushButton(self.left_widget)
        self.poomsae_import_button.setObjectName("poomsae_import_button")
        self.button_row2.addWidget(self.poomsae_import_button)
        self.poomsae_output_button = QtWidgets.QPushButton(self.left_widget)
        self.poomsae_output_button.setObjectName("poomsae_output_button")
        self.button_row2.addWidget(self.poomsae_output_button)
        self.left_layout.addLayout(self.button_row2)

        # 按钮行3 - 成绩导入/导出
        self.button_row3 = QtWidgets.QHBoxLayout()
        self.button_row3.setObjectName("button_row3")
        self.poomsae_import_button_2 = QtWidgets.QPushButton(self.left_widget)
        self.poomsae_import_button_2.setObjectName("poomsae_import_button_2")
        self.button_row3.addWidget(self.poomsae_import_button_2)
        self.poomsae_output_button_2 = QtWidgets.QPushButton(self.left_widget)
        self.poomsae_output_button_2.setObjectName("poomsae_output_button_2")
        self.button_row3.addWidget(self.poomsae_output_button_2)
        self.left_layout.addLayout(self.button_row3)

        # 添加垂直弹簧 - 使日历和标签之间有弹性空间
        self.verticalSpacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                                    QtWidgets.QSizePolicy.Expanding)
        self.left_layout.addItem(self.verticalSpacer)

        # 日历部件容器 - 用于固定日历大小比例
        self.calendar_container = QtWidgets.QWidget(self.left_widget)
        self.calendar_layout = QtWidgets.QVBoxLayout(self.calendar_container)
        self.calendar_layout.setContentsMargins(0, 0, 0, 0)  # 移除内边距

        # 日历部件 - 使用布局管理器自适应调整
        self.calendarWidget = QtWidgets.QCalendarWidget(self.calendar_container)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setObjectName("calendarWidget")

        # 设置日历大小策略 - 允许扩展但保持比例
        self.calendarWidget.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding
        )

        # 添加日历到布局
        self.calendar_layout.addWidget(self.calendarWidget)

        # 设置容器大小策略
        self.calendar_container.setSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Preferred
        )

        # 设置容器的最小尺寸
        self.calendar_container.setMinimumSize(300, 200)

        self.left_layout.addWidget(self.calendar_container)

        # 添加另一个垂直弹簧 - 在日历和标签之间创建留白
        self.verticalSpacer2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                                     QtWidgets.QSizePolicy.Expanding)
        self.left_layout.addItem(self.verticalSpacer2)

        # 结果显示标签和输出标签容器
        self.label_container = QtWidgets.QWidget(self.left_widget)
        self.label_layout = QtWidgets.QVBoxLayout(self.label_container)
        self.label_layout.setContentsMargins(10, 10, 10, 10)  # 增加内边距

        # 结果显示标签
        self.label1 = QtWidgets.QLabel(self.label_container)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.label_layout.addWidget(self.label1)

        # 输出标签 - 添加背景和边框
        self.output_label = QtWidgets.QLabel(self.label_container)
        self.output_label.setText("")
        self.output_label.setObjectName("output_label")
        self.output_label.setStyleSheet("""
            QLabel {
                background-color: #f0f0f0;
                border: 1px solid #cccccc;
                border-radius: 5px;
                padding: 8px;
                min-height: 30px;
            }
        """)
        # 设置文本对齐方式 - 左对齐且垂直居中
        self.output_label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_layout.addWidget(self.output_label)

        self.left_layout.addWidget(self.label_container)

        # 添加左侧容器到主布局（左侧占比1）
        self.horizontalLayout.addWidget(self.left_widget, 1)

        # 右侧表格视图（右侧占比2）
        self.tableView = QtWidgets.QTableView(widget)
        self.tableView.setObjectName("tableView")
        self.tableView.setStyleSheet("""
            QTableView {
                border: 1px solid #cccccc;
                border-radius: 5px;
            }
        """)
        self.horizontalLayout.addWidget(self.tableView, 2)

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

        # 保存对主窗口的引用
        self.main_window = widget

        # 连接窗口大小变化信号
        self.main_window.resizeEvent = self.handle_resize

    def handle_resize(self, event):
        """处理窗口大小变化事件"""
        # 调用基类的事件处理
        QtWidgets.QWidget.resizeEvent(self.main_window, event)

        # 更新日历尺寸
        self.update_calendar_size()

    def update_calendar_size(self):
        """根据容器大小更新日历尺寸"""
        # 计算日历的最大尺寸（保持3:2比例）
        container_width = self.calendar_container.width()
        max_height = int(container_width * 2 / 3)

        # 设置日历的最大尺寸
        self.calendarWidget.setMaximumSize(container_width, max_height)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "跆拳道对阵表转换"))
        self.fight_import_button.setText(_translate("widget", "导入竞技对战表"))
        self.fight_output_buttom.setText(_translate("widget", "导出竞技前台表"))
        self.poomsae_import_button.setText(_translate("widget", "导入品势对战表"))
        self.poomsae_output_button.setText(_translate("widget", "导出品势前台表"))
        self.poomsae_import_button_2.setText(_translate("widget", "导入品势成绩"))
        self.poomsae_output_button_2.setText(_translate("widget", "导出品势成绩册"))
        self.label1.setText(_translate("widget", "结果显示："))


# app = QtWidgets.QApplication(sys.argv)
# widget = QtWidgets.QWidget()
# ui = Ui_widget()
# ui.setupUi(widget)
# widget.show()
# sys.exit(app.exec_())