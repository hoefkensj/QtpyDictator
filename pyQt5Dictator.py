from PyQt5 import QtCore, QtGui, QtWidgets
import os, types

def Wgt(n=None, t='h'):
	wgt=None
	lay=None
	def create(wgt,lay):
		wgt = QtWidgets.QWidget()
		if t == 'h':
			lay = QtWidgets.QHBoxLayout(wgt)
		elif t == 'v':
			lay = QtWidgets.QVBoxLayout(wgt)
		return wgt,lay
	def init(wgt,lay):
		wgt.setObjectName(f'wgt{n}')
		lay.setObjectName(f'lay{n}')
		wgt.setContentsMargins(0, 0, 0, 0)
		lay.setContentsMargins(0, 0, 0, 0)
		lay.setSpacing(0)
		return wgt,lay
	wgt, lay = create(wgt,lay)
	wgt, lay = init(wgt, lay)	
	return wgt,lay
	
# def ns(nwgt):
	# 	nwgt.add = nwgt.lay.addWidget
	# 	nwgt.app = nwgt.lay.addItem
	# 	nwgt.width= nwgt.wgt.width
	# 	return nwgt
	
	
	
	
def make_icon(n=None, set='Fluent'):
	icon = QtGui.QIcon()
	lset = f'/home/hoefkens/.local/share/icons/{set}/symbolic/actions/{n}.svg'
	dset = f'/home/hoefkens/.local/share/icons/{set}-dark/symbolic/actions/{n}.svg'
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

def wgtEditProp(n):
	lbln = lbl(n)
	txt = make_ledit(ro=True)
	btnSet = pBtn('Set')
	tBtn =iBtn('edit-symbolic', bi=True)
	wgt,lay = Wgt(t='h')
	lay.addWidget(lbln.lbl)
	lay.addWidget(txt)
	lay.addWidget(btnSet)
	lay.addWidget(tBtn)
	# print(lbln.getWidth())
	return wgt,lay

def make_wgtSearch():
	btnSearch = iBtn('search-symbolic')
	btnNext = iBtn('carousel-arrow-next-symbolic', w=12)
	btnPrev = iBtn('carousel-arrow-previous-symbolic', w=12)
	wgt,lay = Wgt(t='h')
	txt = make_ledit()
	hWgt_lay.addWidget(txt)
	hWgt_lay.addWidget(btnPrev)
	hWgt_lay.addWidget(btnNext)
	hWgt_lay.addWidget(btnSearch)
	return wgt,lay

def spacer_ex(w=1, h=1):
	spacerItem = QtWidgets.QSpacerItem(w, h, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
	return spacerItem

def spacer_fix(w=1, h=1):
	spacerItem = QtWidgets.QSpacerItem(w, h, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
	return spacerItem

def make_wgtPath():
	hWgt_wgt,hWgt_lay = Wgt(t='h')
	hWgt_wgt.setContentsMargins(0, 0, 0, 5)
	lblPath = lbl('Path:')
	txt = make_ledit(ro=True)
	btnCopy = pBtn('Copy')
	hWgt_lay.addWidget(lblPath.lbl)
	hWgt_lay.addWidget(txt)
	hWgt_lay.addWidget(btnCopy)
	return hWgt_wgt,hWgt_lay

def make_wgtCtrl():
	btnExp = iBtn('value-increase-symbolic')
	btnColl = iBtn('value-decrease-symbolic')
	wgt,lay = Wgt(t='h')
	lay.addWidget(btnExp)
	lay.addWidget(btnColl)
	return  wgt,lay

def make_Tinterface():
	wgt,lay = Wgt(t='h')
	wgt.setContentsMargins(0, 0, 0, 2)
	wgtCtrl,layCtrl = make_wgtCtrl()
	wgtSearch,laySearch = make_wgtSearch()
	lay.addWidget(wgtCtrl)
	lay.addWidget(wgtSearch)
	return wgt,lay

def make_wgtTree():
	hWgt_wgt,hWgt_lay = Wgt(t='h')
	wgtTree = QtWidgets.QTreeWidget()
	wgtTree.setObjectName("treeWidget")
	wgtTree.headerItem().setText(0, "1")
	hWgt_lay.addWidget(wgtTree)
	return hWgt_wgt,hWgt_lay

def wgtMainCtl():
	spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
	def fileCtl():
		btnPrint = pBtn('Print')
		btnSave = pBtn('Save As')
	  hWgt_wgt,hWgt_lay = Wgt(t='h')
		hWgt_lay.addWidget(btnPrint)
		hWgt_lay.addWidget(btnSave)
		return hWgt_wgt,hWgt_lay
		
	def appCtl():
		btnExit = pBtn('Exit')
		hWgt_wgt,hWgt_lay = Wgt(t='h')
		hWgt_lay.additem(spacerItem)
		hWgt_lay.addWidget(btnExit)
		return hWgt_wgt,hWgt_lay

	filectl_wgt, filectl_lay=fileCtl()
	appctl_wgt, appctl_lay=appCtl()
	hWgt_wgt,hWgt_lay = Wgt(t='h')
	hWgt_lay.addWidget(filectl_wgt)
	hWgt_lay.addWidget(appctl_wgt)
	return hWgt_wgt,hWgt_lay

def make_wgtEditKV():
	wgtEditKey,layEditKey = wgtEditProp('Key')
	wgtEditVal,layEditVal = wgtEditProp('Val')
	wgtEditKV,layEditKV = Wgt(n='Edit',t='v')
	wgtEditKV.setContentsMargins(5, 0, 0, 2)
	layEditKV.addWidget(wgtEditKey)
	layEditKV.addWidget(wgtEditVal)
def make_wgtEditKV():

	wgt, lay = Wgt(t='h')
	spc = spacer_fix(w=25)
	wgtEditWrap.lay.addItem(spc)
	wgtEditWrap.addWidget(wgtEdit.wgt)
	wgtEditWrap.lay.addItem(spc)
	return wgtEditWrap

class Ui_Form(object):
	def setupUi(self,Form):
		
	  self.wgtTreeDisp		,	self.layTreeDisp	= Wgt(t='v')
	  self.wgtData				,	self.layData		 	= Wgt(t='v')



	  self.wgtTree				,	self.layTree				=	make_wgtTree()
	  self.wgtTInterface	,	self.layTInterface	= make_Tinterface()
	  self.wgtEditKV			, self.layEditKV			= make_wgtEditKV()
	  self.wgtPath				,	self.layPath				= make_wgtPath()


		
		self.layTreeDisp.addWidget(self.wgtTree)
		self.layTreeDisp.addWidget(self.wgtTInterface)
		self.layData.addWidget(self.wgtEditKV)
		self.layData.addWidget(self.wgtPath)
		# Form.resize(325, 465)
		# self.mainLay = QtWidgets.QVBoxLayout(Form.wgt)
		# self.widget_16 = QtWidgets.QWidget(Form)
		# self.widget_1 = makeWgt(1)
		
		
		
		# wgtTree = make_wgtTree()
		# wgtTInterface = make_Tinterface()
		# wgtTreeDisp = Wgt(t='v')
		# wgtTreeDisp.addWidget(wgtTree.wgt)
		# wgtTreeDisp.addWidget(wgtTInterface.wgt)
		
		# wgtEditKV = make_wgtEditKV()
		
		# wgtPath = make_wgtPath()
		# wgtData = Wgt(t='v')
		# wgtData.addWidget(wgtEditKV.wgt)
		# wgtData.addWidget(wgtPath.wgt)
		self.btnExit	=	pBtn('Exit')
		self.btnExp 	= iBtn('value-increase-symbolic')
		self.btnColl 	= iBtn('value-decrease-symbolic')
		self.btnSet 	= pBtn('Set')
		self.btnEdit	=	iBtn('edit-symbolic', bi=True)
		self.btnPrint = pBtn('Print')
		self.btnSave 	= pBtn('Save As')

		wgtTools_wgt,hWgt_lay =Wgt(t='v')
		# wgtTools.addWidget(wgtSearch.wgt)
		wgtTools.addWidget(self.Disp.wgtData.wgt)
		wgtTreeMain_wgt,hWgt_lay =Wgt(t='v')
		wgtTreeMain.addWidget(self.Disp.wgtTreeDisp.wgt)
		wgtTreeMain.addWidget(wgtTools.wgt)
		wgtFile = make_wgtFile()
		self.wgtFile= wgtFile
		# self.vLay16 = QtWidgets.QVBoxLayout(self.widget_16)
		# sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		# sizePolicy.setHorizontalStretch(0)
		# sizePolicy.setVerticalStretch(0)
		# sizePolicy.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
		# self.widget_9.setSizePolicy(sizePolicy)
		# wgt7.addWidget(self.toolButton_5)
		# wgt7.addWidget(self.ltxt2)
		# wgt7.addWidget(self.pushButton_7)
		# wgt7.addWidget(self.toolButton_8)
		# wgt7.addWidget(self.pushButton_8)
		Form.addWidget(wgtTreeMain.wgt)
		Form.addWidget(wgtFile.wgt)
		
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
	Qt5Gui=types.SimpleNamespace()
	
	Form_wgt,hWgt_lay = Wgt('Form', 'v')
	Qt5Gui.wgt=Form_wgt
	Qt5Gui.lay=hWgt_lay

	ui = Ui_Form()
	Qtui=ui.setupUi(Qt5Gui)
	# Qtui.wgt.show()
	Form.wgt.show()
	

	

	sys.exit(app.exec_())
