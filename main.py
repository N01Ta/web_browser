import sys

from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QApplication, QHBoxLayout, QLineEdit, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.qwidget = QWidget(self)
        self.setWindowTitle("project browser") # делаем заголовок приложения

        self.view = QWebEngineView() # ядро
        self.view.load(QUrl("http://n01ta.space/")) # загруженная страница
        self.view.urlChanged.connect(self.url_changed) # подключаем нашу строку чтоб из нее загружались данные

        self.back_button = QPushButton("<-") # кнопка назад, дальше такие же методы
        self.forward_button = QPushButton("->")
        self.url_box = QLineEdit()
        self.open_button = QPushButton("open")
        self.reload_button = QPushButton("@")

        self.back_button.clicked.connect(self.view.back) # метод 'назад' для нашей кнопки, подключаем разные методы к соответствующим кнопкам
        self.forward_button.clicked.connect(self.view.forward)
        self.open_button.clicked.connect(self.url_set)
        self.reload_button.clicked.connect(self.view.reload)

        self.tabs = QHBoxLayout() # создали табы - верхнюю линию где кнопки с строка
        widgets = [self.back_button, self.forward_button, self.url_box, self.open_button, self.reload_button] # список с нашими кнопками-строками
        for widget in widgets: self.tabs.addWidget(widget) # прошлись по списку с нашими кнопками-строками и добавили каждую, можно это было расписать на каждую строку, но так удобнее

        self.mainBrowser = QVBoxLayout() # создали окно
        self.mainBrowser.addLayout(self.tabs) # добавили табы и браузер в окно
        self.mainBrowser.addWidget(self.view)

        self.qwidget.setLayout(self.mainBrowser) # добавили в виджет наше окно и поставили виджет центральным
        self.setCentralWidget(self.qwidget)

    def url_changed(self, url): # функция для обновления строки
        self.url_box.setText(url.toString())

    def url_set(self): # функция для загрузки строки
        self.view.setUrl(QUrl(self.url_box.text()))

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
