
# derived class for GelberZettel_GUI.py
# instead of self.Maintab =QtGui.QTabWidget(self.centralwidget)

#
# import GuiOverwrites
# self.Maintab = GuiOverwrites.MyTabWidget(self.centralwidget)

from PySide import QtCore, QtGui


class MyTabWidget(QtGui.QTabWidget):
    ##tabAdded = QtCore.SIGNAL()
    # to overwrite the EventHandler
    def __init__(self, centralwidget):
        super(MyTabWidget, self).__init__(centralwidget)

    def mouseDoubleClickEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.appendTab()
            self.emit(QtCore.SIGNAL("tabAdded"))
        elif event.buttons() == QtCore.Qt.RightButton:
            self.emit(QtCore.SIGNAL("removeTab"))

    def appendTab(self):
        newwidget = QtGui.QWidget()

        tabname = "Tab " + str(self.count() + 1)

        # setup the layout including a plainTextEdit in the new tab
        self.horizontalLayout = QtGui.QHBoxLayout(newwidget)
        self.horizontalLayout.setObjectName("horizontalLayout_" + tabname)
        newwidget.plainTextEdit = QtGui.QPlainTextEdit(newwidget)
        newwidget.plainTextEdit.setObjectName("plainTextEdit_" + tabname)
        self.horizontalLayout.addWidget(newwidget.plainTextEdit)

        self.addTab(newwidget, tabname)

        return newwidget
