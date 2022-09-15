from PyQt5 import QtCore, QtGui, QtWidgets
import os, types

def Wgt(n=None, t='h'):
	qtwgt = types.SimpleNamespace()
	def create(nwgt):
		nwgt.wgt = QtWidgets.QWidget()
		if t == 'h':
			nwgt.lay = QtWidgets.QHBoxLayout(nwgt.wgt)
		elif t == 'v':
			nwgt.lay = QtWidgets.QVBoxLayout(nwgt.wgt)
		return nwgt
	
	def init(nwgt):
		nwgt.wgt.setObjectName(f'wgt{n}')
		nwgt.lay.setObjectName(f'lay{n}')
		nwgt.wgt.setContentsMargins(0, 0, 0, 0)
		nwgt.lay.setContentsMargins(0, 0, 0, 0)
		nwgt.lay.setSpacing(0)
		return nwgt
		
	def ns(nwgt):
		nwgt.add = nwgt.lay.addWidget
		nwgt.app = nwgt.lay.addItem
		nwgt.width= nwgt.wgt.width
		return nwgt
		
	qtwgt=create(qtwgt)
	qtwgt=init(qtwgt)
	qtwgt=ns(qtwgt)
	return qtwgt
	
def make_icon(name, set='Fluent'):
	icon = QtGui.QIcon()
	lset = f'/home/hoefkens/.local/share/icons/{set}/symbolic/actions/{name}.svg'
	dset = f'/home/hoefkens/.local/share/icons/{set}-dark/symbolic/actions/{name}.svg'
	icon.addPixmap(QtGui.QPixmap(dset), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	icon.addPixmap(QtGui.QPixmap(lset), QtGui.QIcon.Normal, QtGui.QIcon.On)
	return icon

def iBtn(n, bi=False, h=20, w=20):
	icon = make_icon(n)
	btn = QtWidgets.QToolButton()
	btn.setObjectName(f'tBtn{n}')
	btn.setIcon(icon)
	btn.setIconSize(QtCore.QSize(32, 32))
	btn.setMaximumSize(QtCore.QSize(w, h))
	btn.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
	btn.setCheckable(bi)
	return btn

def pBtn(n, bi=False):
	sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
	btn = QtWidgets.QToolButton()
	btn.setObjectName(f'btn{n}')
	btn.setSizePolicy(sizePolicy)
	btn.setText(n)
	btn.setCheckable(bi)
	wo=btn.width()
	# print(wo)


	return btn


def lbl(n):
	lbl = QtWidgets.QLabel()
	lbl.setObjectName(f'lbl{n}')
	lbl.setText(f'{n}')
	lbl.setContentsMargins(5, 0, 5, 0)
	sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
	# lbl.setFixedWidth(30)
	lbl.setSizePolicy(sizePolicy)
	def sns():
		nlbl=types.SimpleNamespace()
		nlbl.lbl = lbl
		nlbl.getWidth=  lbl.width
		nlbl.setwidth= lbl.width
		return nlbl
	
	return sns()

def make_ledit(ro=False):
	txt = QtWidgets.QLineEdit()
	txt.setReadOnly(ro)
	sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
	txt.setSizePolicy(sizePolicy)
	return txt

def make_wgtEdit(n):
	lbln = lbl(n)
	txt = make_ledit(ro=True)
	btnSet = pBtn('Set')
	tBtn =iBtn('edit-symbolic', bi=True)
	hWgt = Wgt()
	hWgt.add(lbln.lbl)
	hWgt.add(txt)
	hWgt.add(btnSet)
	hWgt.add(tBtn)
	# print(lbln.getWidth())
	return hWgt

def make_wgtSearch():
	btnSearch = iBtn('search-symbolic')
	btnNext = iBtn('carousel-arrow-next-symbolic', w=12)
	btnPrev = iBtn('carousel-arrow-previous-symbolic', w=12)
	hWgtEd = Wgt()
	txt = make_ledit()
	hWgtEd.add(txt)
	hWgtEd.add(btnPrev)
	hWgtEd.add(btnNext)
	hWgtEd.add(btnSearch)
	return hWgtEd

def spacer_ex(w=1, h=1):
	spacerItem = QtWidgets.QSpacerItem(w, h, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
	return spacerItem

def spacer_fix(w=1, h=1):
	spacerItem = QtWidgets.QSpacerItem(w, h, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
	return spacerItem

def make_wgtPath():
	hWgt = Wgt()
	hWgt.wgt.setContentsMargins(0, 0, 0, 5)
	lblPath = lbl('Path:')
	txt = make_ledit(ro=True)
	btnCopy = pBtn('Copy')
	hWgt.add(lblPath.lbl)
	hWgt.add(txt)
	hWgt.add(btnCopy)
	return hWgt

def make_wgtCtrl():
	btnExp = iBtn('value-increase-symbolic')
	btnColl = iBtn('value-decrease-symbolic')
	hWgt = Wgt()
	hWgt.add(btnExp)
	hWgt.add(btnColl)
	return hWgt

def make_Tinterface():
	hWgt = Wgt()
	hWgt.wgt.setContentsMargins(0, 0, 0, 2)
	wgtCtrl = make_wgtCtrl()
	wgtSearch = make_wgtSearch()
	hWgt.add(wgtCtrl.wgt)
	hWgt.add(wgtSearch.wgt)
	
	return hWgt

def make_wgtTree():
	hWgt = Wgt()
	wgtTree = QtWidgets.QTreeWidget()
	wgtTree.setObjectName("treeWidget")
	wgtTree.headerItem().setText(0, "1")
	hWgt.add(wgtTree)
	return hWgt

def make_wgtFile():
	spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
	wgtOut = Wgt()
	btnPrint = pBtn('Print')
	btnSave = pBtn('Save As')
	wgtOut.add(btnPrint)
	wgtOut.add(btnSave)
	wgtOut.lay.addItem(spacerItem)
	btnExit = pBtn('Exit')
	wgtFile = Wgt()
	wgtFile.add(wgtOut.wgt)
	wgtFile.add(btnExit)
	return wgtFile

def make_wgtEditKV():
	wgtEdit_Key = make_wgtEdit('Key')
	wgtEdit_Val = make_wgtEdit('Val')
	wgtEdit = Wgt(n='Edit',t='v')
	wgtEdit.wgt.setContentsMargins(5, 0, 0, 2)
	wgtEdit.add(wgtEdit_Key.wgt)
	wgtEdit.add(wgtEdit_Val.wgt)
	wgtEditWrap = Wgt()
	spc = spacer_fix(w=25)
	wgtEditWrap.lay.addItem(spc)
	wgtEditWrap.add(wgtEdit.wgt)
	wgtEditWrap.lay.addItem(spc)
	return wgtEditWrap

class Ui_Form(object):
	def setupUi(self,Form):


		# Form.resize(325, 465)
		# self.mainLay = QtWidgets.QVBoxLayout(Form.wgt)
		# self.widget_16 = QtWidgets.QWidget(Form)
		# self.widget_1 = makeWgt(1)
		wgtTree = make_wgtTree()
		wgtTInterface = make_Tinterface()
		wgtTreeDisp = Wgt(t='v')
		wgtTreeDisp.add(wgtTree.wgt)
		wgtTreeDisp.add(wgtTInterface.wgt)
		
		wgtEditKV = make_wgtEditKV()
		
		wgtPath = make_wgtPath()
		wgtData = Wgt(t='v')
		wgtData.add(wgtEditKV.wgt)
		wgtData.add(wgtPath.wgt)
		
		wgtTools =Wgt(t='v')
		# wgtTools.add(wgtSearch.wgt)
		wgtTools.add(wgtData.wgt)
		wgtTreeMain =Wgt(t='v')
		wgtTreeMain.add(wgtTreeDisp.wgt)
		wgtTreeMain.add(wgtTools.wgt)
		wgtFile = make_wgtFile()
		self.wgtFile= wgtFile
		# self.vLay16 = QtWidgets.QVBoxLayout(self.widget_16)
		# sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		# sizePolicy.setHorizontalStretch(0)
		# sizePolicy.setVerticalStretch(0)
		# sizePolicy.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
		# self.widget_9.setSizePolicy(sizePolicy)
		# wgt7.add(self.toolButton_5)
		# wgt7.add(self.ltxt2)
		# wgt7.add(self.pushButton_7)
		# wgt7.add(self.toolButton_8)
		# wgt7.add(self.pushButton_8)
		Form.add(wgtTreeMain.wgt)
		Form.add(wgtFile.wgt)
		
		self.retranslateUi(Form.wgt)
		QtCore.QMetaObject.connectSlotsByName(Form.wgt)
		return Form
		
	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "Form"))
# self.toolButton_2.setText(_translate("Form", "..."))
# self.toolButton_3.setText(_translate("Form", "..."))
# self.toolButton_5.setText(_translate("Form", "..."))
# self.pushButton_7.setText(_translate("Form", "PushButton"))
# self.toolButton_8.setText(_translate("Form", "..."))
# self.pushButton_8.setText(_translate("Form", "PushButton"))
# self.label.setText(_translate("Form", "TextLabel"))
# self.pushButton_5.setText(_translate("Form", "PushButton"))
# self.toolButton_7.setText(_translate("Form", "..."))
# self.lbl2.setText(_translate("Form", "TextLabel"))
# self.pushButton_6.setText(_translate("Form", "PushButton"))
# self.toolButton_9.setText(_translate("Form", "..."))
# self.pushButton_4.setText(_translate("Form", "PushButton"))
# self.pushButton.setText(_translate("Form", "PushButton"))
# self.pushButton_2.setText(_translate("Form", "PushButton"))
# self.pushButton_3.setText(_translate("Form", "PushButton"))

if __name__ == "__main__":
	import sys
	

	app = QtWidgets.QApplication(sys.argv)
	Form = Wgt('Form', 'v')

	ui = Ui_Form()
	Qtui=ui.setupUi(Form)
	# Qtui.wgt.show()
	Form.wgt.show()

	

	sys.exit(app.exec_())
