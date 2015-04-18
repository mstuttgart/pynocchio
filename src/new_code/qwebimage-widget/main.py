# -*- coding: utf-8 -*-
import sys

from qwebimage_widget import *


if __name__ == "__main__":
    app = QApplication(sys.argv)

    url = 'http://i997.mangapanda.com/fairy-tail/427/fairy-tail-5597543.jpg'
    url2 = 'file:images/00.jpg'

    web = QWebImageWidget()
    web.load_url(url)
    web.show()
    sys.exit(app.exec_())
