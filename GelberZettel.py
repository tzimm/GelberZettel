

from PySide import QtCore, QtGui
import GelberZettelGui
import GuiOverwrites
import sys
import os


class _scan_gui():

    def __init__(self, qtgui_mainwindow):
        self.GUI = GelberZettelGui.Ui_MainWindow()
        self.GUI.setupUi(qtgui_mainwindow)

        #__init__(self, None, QtCore.Qt.WindowStaysOnTopHint)
        self.skriptpath = self.GetSkriptpath()
        self.SetupTabs()

        self.GUI.Maintab.connect(self.GUI.Maintab, QtCore.SIGNAL("tabAdded"), self.ConnectSignal)
        self.GUI.Maintab.connect(self.GUI.Maintab, QtCore.SIGNAL("removeTab"), self.RemoveActiveTab)


    def SetupTabs(self):
        """
        creates tabs based on the txtfiles that remain in same directory
        """
        #how many txtfiles do I have
        nmbr_txts = self.count_available_txtfiles()
        for i in range(0, nmbr_txts):
            iteratetab = self.GUI.Maintab.appendTab()
            iteratetab.plainTextEdit.textChanged.connect(self.SaveTab)
            # open relevant textfile
            try:
                fileobject = open(self.ReturnTabpath(i + 1), 'r')
            except IOError:
                self.Say("Exception: SetupTabs: Failed to open: " + self.ReturnTabpath(i + 1))
            for line in fileobject:
                iteratetab.plainTextEdit.appendPlainText(line.replace("\n", ""))
            fileobject.close()

    def RemoveActiveTab(self):
        # removes active tabs, reset tabnames
        active_tab = self.GUI.Maintab.currentWidget()
        tab_nmbr = self.GUI.Maintab.indexOf(active_tab)
        MessageBox = QtGui.QMessageBox()

        ret = MessageBox.warning(self.GUI.Maintab, "Really?",
            "Do you really want to delete tab " + str(tab_nmbr + 1) + "?",
            MessageBox.Ok, MessageBox.Cancel)

        if (ret == MessageBox.Ok):
            print "Deleting Tab " + str(tab_nmbr + 1)
            self.GUI.Maintab.removeTab(tab_nmbr)
            self.ResetTabnames()

    def ResetTabnames(self):
        """
        remove all textfiles
        reset labels of the tabs
        save every tab again in a textfile
        """
        for i in range(0, self.GUI.Maintab.count()):
            current_widget = self.GUI.Maintab.widget(i)
            #remove txtfile
            try:
                os.remove(self.ReturnTabpath(i + 1))
            except OSError:
                self.Say("Failed to delete: " + self.ReturnTabpath(i + 1))

            #rename tab
            self.GUI.Maintab.setTabText(i, "Tab " + str(i + 1))

            #write txtfile
            try:
                # open relevant textfile
                fobj = open(self.ReturnTabpath(i + 1), 'w')
            except IOError:
                self.Say("Exception: SetupTabs: Failed to open: " + self.ReturnTabpath(i + 1))
            # write into file
            fobj.write(current_widget.plainTextEdit.toPlainText())
            fobj.close()
        #remove the remaining txtfile
        os.remove(self.ReturnTabpath(self.GUI.Maintab.count() + 1))

    def ConnectSignal(self):
        """
        required to be able to react to a double click on the tab widget
        the handling of a  corresponding txt file to the tab is done here
        """
        latest_tab_idx = self.GUI.Maintab.count()
        latest_tab = self.GUI.Maintab.widget(latest_tab_idx - 1)
        latest_tab.plainTextEdit.textChanged.connect(self.SaveTab)

    def GetSkriptpath(self):
        skriptpath = os.path.realpath(__file__)
        return skriptpath[:skriptpath.rfind("/")]

    def ReturnTabpath(self, tabnmbr):
        # starts counting from 1 and not from 0
        # return path of tab with number tabnmbr
        # @params int: tabnmbr
        return self.skriptpath + "/tab" + str(tabnmbr) + ".txt"

    def count_available_txtfiles(self):
        """
        look in the skript's path and return the number of already created tabs
        """
        i = 0
        while(1):
            # setze pfad zusammen
            i += 1
            txtpath = self.ReturnTabpath(i)
            if not os.path.isfile(txtpath):
                return i - 1

    def SaveTab(self):
        # search for active tab.
        currenttab = self.GUI.Maintab.currentWidget()
        # Note: indexes start with 0
        idx = self.GUI.Maintab.indexOf(currenttab) + 1
        # self.Say("saving \" Tab " + str(idx) + "\"")
        # self.Say("returntabpath: " + self.ReturnTabpath(idx))
        try:
            fobj = open(self.ReturnTabpath(idx), 'w')
        except IOError:
            self.Say("Exception: SetupTabs: Failed to open: " + self.ReturnTabpath(idx))
        # write into file
        fobj.write(currenttab.plainTextEdit.toPlainText())
        fobj.close()

    def Say(self, saystring):
        #
        # just print saystring into every outlet
        #
        print(saystring)


app = QtGui.QApplication(sys.argv)
window = QtGui.QMainWindow()
#Force Window always on top
window.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
scan_gui = _scan_gui(window)
window.show()
sys.exit(app.exec_())

