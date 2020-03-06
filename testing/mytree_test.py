from PySide import QtGui, QtCore


class MyItem(QtGui.QTreeWidgetItem):
    def __init__(self, tree, data):
        super(MyItem, self).__init__(tree)
        self.my_data = data

        print self.data
        self.setText(0, str(self.my_data))




class MyTree(QtGui.QTreeWidget):
    def __init__(self, parent):
        super(MyTree, self).__init__(parent)
        self.setColumnCount(2)
        for i in range(10):
            pass
            MyItem(self, i)




