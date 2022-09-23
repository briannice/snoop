import sys

from base.App import App
from base.Window import Window


if __name__ == "__main__":
    app = App(sys.argv)
    window = Window()
    window.show()
    app.exec()
