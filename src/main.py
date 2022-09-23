import sys

from components import App, Window


if __name__ == "__main__":
    app = App(sys.argv)
    window = Window()
    window.show()
    app.exec()
