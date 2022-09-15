#!/usr/bin/env python
import sys,os
import types
from PyQt5 import QtCore, QtGui, QtWidgets

def make_wgt(wgt, name):
	wgt.setObjectName(name)
	return wgt
def setLayout(QtWgt, name):
	QtWgt.setContentsMargins(0, 0, 0, 0)
	QtWgt.setSpacing(0)
	QtWgt.setObjectName(name)
	
	return QtWgt

def make_SizePol(wgt,HV):
	pol = {
		'm' :QtWidgets.QSizePolicy.Minimum,
		'mE': QtWidgets.QSizePolicy.MinimumExpanding,
		'E' : QtWidgets.QSizePolicy.Expanding,
		'F' :	QtWidgets.QSizePolicy.Fixed,
		'P' :QtWidgets.QSizePolicy.Preferred,
		'M' : QtWidgets.QSizePolicy.Maximum,
		}
	sizePolicy = QtWidgets.QSizePolicy(pol[HV[0]],pol[HV[1]])
	sizePolicy.setHorizontalStretch(0)
	sizePolicy.setVerticalStretch(0)
	sizePolicy.setHeightForWidth(wgt.sizePolicy().hasHeightForWidth())
	wgt.setSizePolicy(sizePolicy)
	return wgt

def make_lineEdit(wgt,text,name,ro,clear,HV=None):
	if HV:
		wgt=make_SizePol(wgt,HV)
	wgt.setText(text)
	wgt.setReadOnly(ro)
	wgt.setClearButtonEnabled(clear)
	wgt.setObjectName(name)
	return wgt

def make_btnPush(wgt,name,text,HV=None):
	if  HV:
		wgt = make_SizePol(wgt, HV)
	wgt.setMinimumSize(QtCore.QSize(0, 0))
	wgt.setMaximumSize(QtCore.QSize(9999, 9999))
	wgt.setFlat(False)
	wgt.setText(text)
	wgt.setObjectName(name)
	return wgt

def make_chkBox(wgt,name,text):
	wgt.setObjectName(name)
	wgt.setText(text)
	wgt.setCheckable(True)
	return wgt

def make_icon(name,ld='dark'):
	theme_path='/home/hoefkens/.local/share/icons/Fluent{ld}/symbolic/actions'
	iconpath1 = os.path.join(theme_path.format(ld='-dark'),name)
	iconpath2 = os.path.join(theme_path.format(ld=''),name)
	icon = QtGui.QIcon()
	icon.addPixmap(QtGui.QPixmap(iconpath1), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	icon.addPixmap(QtGui.QPixmap(iconpath2), QtGui.QIcon.Normal, QtGui.QIcon.On)
	# icon.addPixmap(QtGui.QPixmap(iconpath2), QtGui.QIcon.Disabled, QtGui.QIcon.On)
	return icon

def make_btnTool(wgt, name,bi, icon_name):
	btnicon1=make_icon(icon_name,)
	wgt.setIconSize(QtCore.QSize(32, 32))
	wgt.setIcon(btnicon1)
	wgt.setIconSize(QtCore.QSize(32, 32))
	wgt.setMaximumSize(QtCore.QSize(20, 20))
	wgt.setCheckable(bi)
	wgt.setChecked(False)
	wgt.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
	wgt.setAutoRaise(False)
	wgt.setArrowType(QtCore.Qt.NoArrow)
	wgt.setObjectName(name)
	return wgt

def make_frm(wgt,name,HV):
	wgt = make_SizePol(wgt,HV )
	wgt.setFrameShape(QtWidgets.QFrame.NoFrame)
	wgt.setFrameShadow(QtWidgets.QFrame.Plain)
	wgt.setObjectName(name)
	return wgt

def make_grp(wgt,title,name,HV=None):
	if HV:
		wgt = make_SizePol(wgt,HV)
	wgt.setTitle("")
	wgt.setAlignment(QtCore.Qt.AlignCenter)
	wgt.setFlat(False)
	wgt.setObjectName("grpTree")
	return wgt

def make_lbl(wgt,name,text):
	wgt.setText(text)
	wgt.setObjectName(name)
	return wgt

def make_trDict(parent):
	trDict = QtWidgets.QTreeWidget(parent)
	trDict = make_SizePol(trDict, ['E', 'E'])
	trDict.setAutoFillBackground(True)
	trDict.setFrameShape(QtWidgets.QFrame.NoFrame)
	trDict.setFrameShadow(QtWidgets.QFrame.Plain)
	trDict.setLineWidth(0)
	trDict.setMidLineWidth(0)
	trDict.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
	trDict.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
	trDict.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
	trDict.setAutoScroll(False)
	trDict.setAutoScrollMargin(16)
	trDict.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked | QtWidgets.QAbstractItemView.SelectedClicked)
	trDict.setProperty("showDropIndicator", False)
	trDict.setAlternatingRowColors(True)
	trDict.setUniformRowHeights(True)
	trDict.setAnimated(True)
	trDict.setAllColumnsShowFocus(True)
	trDict.setWordWrap(True)
	trDict.setObjectName("trDict")
	trDict.header().setMinimumSectionSize(100)
	trDict.header().setStretchLastSection(True)
	return trDict



	

class Ui_wgtQtpyDictator(object):
	
	
	def setupUi(self, wgtQtpyDictator):
		icon_collapse="value-decrease-symbolic.svg"
		icon_exp='value-increase-symbolic.svg'
		icon2='edit-symbolic.svg'
		spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		spacerItem2 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		spacerItem3 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
		
		wgtQtpyDictator.setObjectName("wgtQtpyDictator")
		wgtQtpyDictator.resize(386, 279)
		self.grpTree = QtWidgets.QGroupBox(wgtQtpyDictator)
		self.frmTree = QtWidgets.QFrame(self.grpTree)
		self.frmCtrl = QtWidgets.QFrame(self.frmTree)
		self.chkData = QtWidgets.QCheckBox(self.frmCtrl)
		# self.chkSearch = QtWidgets.QCheckBox(self.frmCtrl)
		self.btnPrint = QtWidgets.QPushButton(self.frmCtrl)
		self.btnCollapse = QtWidgets.QToolButton(self.frmCtrl)
		self.btnExp = QtWidgets.QToolButton(self.frmCtrl)
		self.frmSearch = QtWidgets.QFrame(self.frmTree)
		self.txtSearch   =QtWidgets.QLineEdit(self.frmSearch)
		self.btnSearch = QtWidgets.QPushButton(self.frmSearch)
		self.frmData = QtWidgets.QFrame(self.grpTree)
		self.frmPath = QtWidgets.QFrame(self.frmData)
		self.lblPath = QtWidgets.QLabel(self.frmPath)
		self.txtPath = QtWidgets.QLineEdit(self.frmPath)
		self.btnCopy = QtWidgets.QPushButton(self.frmPath)
		self.frmKeyVal = QtWidgets.QFrame(self.frmData)
		self.wgtKeyVal = QtWidgets.QWidget(self.frmKeyVal)
		self.grpKey = QtWidgets.QGroupBox(self.wgtKeyVal)
		self.grpVal = QtWidgets.QGroupBox(self.wgtKeyVal)
		self.lblKey = QtWidgets.QLabel(self.wgtKeyVal)
		self.lblVal = QtWidgets.QLabel(self.wgtKeyVal)
		self.txtKey = QtWidgets.QLineEdit(self.grpKey)
		self.txtVal = QtWidgets.QLineEdit(self.grpVal)
		self.btnEditKey = QtWidgets.QToolButton(self.grpKey)
		self.btnSetKey = QtWidgets.QPushButton(self.grpKey)
		self.btnEditVal = QtWidgets.QToolButton(self.grpVal)
		self.btnSetVal = QtWidgets.QPushButton(self.grpKey)
		self.btnAbout = QtWidgets.QPushButton(self.frmCtrl)
		self.btnExit = QtWidgets.QPushButton(self.frmCtrl)
		
		
		self.verticalLayout_5 = setLayout(QtWidgets.QVBoxLayout(wgtQtpyDictator),"verticalLayout_5")
		self.verticalLayout_3 = setLayout(QtWidgets.QVBoxLayout(self.grpTree),"verticalLayout_3")
		self.verticalLayout = setLayout(QtWidgets.QVBoxLayout(self.frmTree),"verticalLayout")
		self.horizontalLayout_5 = setLayout( QtWidgets.QHBoxLayout(self.frmSearch),"horizontalLayout_5")
		self.gridLayout_2 = setLayout(QtWidgets.QGridLayout(self.frmData), "gridLayout_2")
		self.horizontalLayout_3 = setLayout(QtWidgets.QHBoxLayout(self.frmPath), "horizontalLayout_3")
		self.horizontalLayout_2 = setLayout(QtWidgets.QHBoxLayout(self.frmCtrl),"horizontalLayout_2" )
		self.horizontalLayout = setLayout(QtWidgets.QHBoxLayout(self.frmKeyVal), "horizontalLayout")
		self.gridLayout = setLayout(QtWidgets.QGridLayout(self.wgtKeyVal), "gridLayout")
		self.hboxlayout = setLayout(QtWidgets.QHBoxLayout(self.grpVal), "hboxlayout")
		self.horizontalLayout_7 = setLayout( QtWidgets.QHBoxLayout(self.grpKey), "horizontalLayout_7")


		self.grpTree = make_grp(self.grpTree,'',"grpTree",['mE','E'])
		
		self.frmTree = make_frm(self.frmTree,"frmTree",['mE','P'])
		self.frmCtrl = make_frm(self.frmCtrl,"frmCtrl",['mE','P'])
		self.frmSearch = make_frm(self.frmSearch, "frmSearch", ['P', 'M'])
		self.frmData = make_frm(self.frmData,"frmData",['mE','P'])
		self.frmPath = make_frm(self.frmPath,'frmPath',['mE','P'])
		self.frmKeyVal=make_frm(self.frmKeyVal,'frmKeyVal',['mE','P'])
		self.grpVal  = make_grp(self.grpVal,'','grpVal')
		self.grpKey = make_grp(self.grpKey,'','grpKey')
		
		self.trDict = make_trDict(self.frmTree)
		
		self.chkData = make_chkBox(self.chkData,"chkData",'Tools')
		# self.chkSearch =make_chkBox(self.chkSearch,"chkSearch","Search")
		
		self.btnPrint = make_btnPush(self.btnPrint,'btnPrint','Print', )
		self.btnCopy= make_btnPush(self.btnCopy,'btnCopy','Copy',['P','P'])
		
		self.btnCollapse = make_btnTool(self.btnCollapse,"btnCollapse",False,icon_collapse)
		self.btnExp =  make_btnTool(self.btnExp,"btnExp",False,icon_exp)
		
		self.btnEditKey = make_btnTool(self.btnEditKey,"btnEditKey",True, icon2, )
		self.btnEditVal = make_btnTool(self.btnEditVal,"btnEditVal",True, icon2 )
		
		self.txtSearch = make_lineEdit(self.txtSearch,"","txtSearch", False , True)
		self.btnSearch = make_btnPush(self.btnSearch,"btnSearch",'Search',['F','F'])
		self.lblPath = make_lbl(self.lblPath,'lblPath','Path:')
		self.txtPath = make_lineEdit(self.txtPath, '', "txtPath",True,True)

		self.wgtKeyVal = make_wgt(self.wgtKeyVal,"wgtKeyVal")
		
		

		self.lblKey = make_lbl(self.lblKey,'lblKey','Key:')
		self.lblVal = make_lbl(self.lblVal,'lblVal','Val:')
		
		
		self.txtKey = make_lineEdit(self.txtKey,'','txtKey',True,True)
		self.txtVal = make_lineEdit(self.txtVal,'','txtVal',True,True)
		

		
		
		
		
		
		
		self.verticalLayout.addWidget(self.trDict)
		self.horizontalLayout_2.addWidget(self.chkData)
		self.horizontalLayout_2.addItem(spacerItem)
		# self.horizontalLayout_2.addWidget(self.chkSearch)
		self.horizontalLayout_2.addItem(spacerItem1)
		self.horizontalLayout_2.addWidget(self.btnPrint)
		self.horizontalLayout_2.addWidget(self.btnCollapse)
		self.horizontalLayout_2.addWidget(self.btnExp)

		self.verticalLayout.addWidget(self.frmCtrl)
		self.horizontalLayout_5.addItem(spacerItem2)
		self.horizontalLayout_5.addWidget(self.txtSearch)
		self.horizontalLayout_5.addWidget(self.btnSearch)
		self.horizontalLayout_5.addItem(spacerItem3)
		self.verticalLayout.addWidget(self.frmSearch)
		
		
		
		self.verticalLayout_3.addWidget(self.frmTree)
		self.horizontalLayout_3.addWidget(self.lblPath)
		self.horizontalLayout_3.addWidget(self.txtPath)
		self.horizontalLayout_3.addWidget(self.btnCopy)
		self.gridLayout_2.addWidget(self.frmPath, 5, 0, 1, 1)
		self.hboxlayout.addWidget(self.txtVal)
		self.hboxlayout.addWidget(self.btnEditVal)
		self.gridLayout.addWidget(self.grpVal, 1, 1, 1, 1)
		self.horizontalLayout_7.addWidget(self.txtKey)
		self.horizontalLayout_7.addWidget(self.btnEditKey)
		self.gridLayout.addWidget(self.grpKey, 0, 1, 1, 1)
		self.gridLayout.addWidget(self.lblKey, 0, 0, 1, 1)
		self.gridLayout.addWidget(self.lblVal, 1, 0, 1, 1)
		self.horizontalLayout.addWidget(self.wgtKeyVal)
		self.gridLayout_2.addWidget(self.frmKeyVal, 2, 0, 1, 1)
		self.verticalLayout_3.addWidget(self.frmData)
		self.verticalLayout_5.addWidget(self.grpTree)
		
		
		
		# self.frmCtrl.setLineWidth(0)


		# self.btnCollapse.setMinimumSize(QtCore.QSize(20, 20))
		# self.btnCollapse.setMaximumSize(QtCore.QSize(20, 20))
		# self.btnCollapse.setText("")
		self.wgtWindow = QtWidgets.QWidget(wgtQtpyDictator)
		self.frmCtrl = QtWidgets.QFrame(self.wgtWindow)
		self.frmCtrl= make_frm(self.frmCtrl,'frmCtrl',['mE','P'])



		self.wgtWindow = make_wgt(self.wgtWindow,'wgtWindow')
		self.wgtWindow = make_SizePol(self.wgtWindow,['mE','F'])

		self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frmCtrl)
		# self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
		# self.horizontalLayout_4.setSpacing(0)
		self.horizontalLayout_4.setObjectName("horizontalLayout_4")
		
		
		
		

		self.btnAbout = make_btnPush(self.btnAbout,'btnAbout','About',['P','P'])
		self.btnExit = make_btnPush(self.btnExit,"btnExit","Exit",['M','F'])
		
		self.horizontalLayout_4.addWidget(self.btnAbout)
		self.horizontalLayout_4.addItem(spacerItem4)
		self.horizontalLayout_4.addWidget(self.btnExit)
		self.verticalLayout_5.addWidget(self.frmCtrl)
		
		self.retranslateUi(wgtQtpyDictator)
		QtCore.QMetaObject.connectSlotsByName(wgtQtpyDictator)

	def retranslateUi(self, wgtQtpyDictator):
		_translate = QtCore.QCoreApplication.translate
		wgtQtpyDictator.setWindowTitle(_translate("wgtQtpyDictator", "Form"))
		self.trDict.headerItem().setText(0, _translate("wgtQtpyDictator", "Key"))
		self.trDict.headerItem().setText(1, _translate("wgtQtpyDictator", "Value"))
		self.chkData.setText(_translate("wgtQtpyDictator", "Tools"))


def make_tree(gui, branches=[], **k):
	def make_branch(root, dct, path):
		for key in dct.keys():
			data = dct[key]
			dictpath = f"{path}['{key}']"
			branch = QtWidgets.QTreeWidgetItem()
			branch.setText(0, str(key))
			branch.setText(2, dictpath)
			if isinstance(data, dict):
				make_branch(branch, data, dictpath)
			else:
				data = str(data)
				w = gui.trDict.columnWidth(1)
				data = repr(data) if callable(data) else data
				dispdata = f'{data[0:w - 4]}...' if len(data) > w - 4 else data
				branch.setText(1, dispdata)
				branch.setText(3, data)
			root.addChild(branch)
	name = k['name']
	data = k['data']
	root = QtWidgets.QTreeWidgetItem()
	root.setText(0, name)
	root.setText(2, name)
	make_branch(root, data, name)
	return root

def construct_Qt5Ui():
	def QtApp():
		app = types.SimpleNamespace()
		app.QtWin = QtWidgets.QApplication(sys.argv)
		app.QtClip = app.QtWin.clipboard()
		return app
	def disp(gui):
		frm = [gui.hide, '', gui.show]
		def showhide(state):
			frm[state]()
		return showhide
	def select(gui):
		txtBox = [gui.txtKey, gui.txtVal, gui.txtPath, ]
		def fill():
			data = gui.trDict.selectedItems()
			for idx, txtbox in zip([0, 3, 2], txtBox):
				txtbox.setText(data[0].text(idx))
		return fill
	def fitt(gui):
		gui.trDict.expandAll()
		gui.trDict.resizeColumnToContents(0)
		w = gui.trDict.columnWidth(0)
		gui.trDict.setColumnWidth(0, w + 20)
		
		gui.trDict.resizeColumnToContents(1)
		w = gui.trDict.columnWidth(1)
		gui.trDict.setColumnWidth(1, w + 20)
		gui.trDict.collapseAll()

	def copytoclip(txt):
		def toclip():
			App.QtClip.setText(txt.text())
		return toclip
	def editkey(gui):
		def edit(state):
			gui.btnEditKey.setChecked(state)
			gui.txtKey.setReadOnly(not state)
		return edit
	def editval(gui):
		def edit(state):
			gui.btnEditVal.setChecked(state)
			gui.txtVal.setReadOnly(not state)
		return edit
	def search(gui):
		def find():
			found=gui.trDict.findChild(str, gui.txtSearch.text(), QtCore.Qt.MatchFlag.MatchRecursive)
			found2=gui.trDict.findChild(str , gui.txtSearch.text(), QtCore.Qt.MatchFlag.MatchContains)
			print(gui.txtSearch.text(),found,found2)
		return find
	
	def create(wgt):
		def init():
			gui.trDict.expandAll()
			gui.trDict.resizeColumnToContents(0)
			gui.trDict.resizeColumnToContents(1)
			gui.trDict.collapseAll()
			gui.trDict.expandItem(gui.trDict.topLevelItem(0))
			gui.trDict.setColumnCount(4)
			gui.trDict.hideColumn(2)
			gui.trDict.hideColumn(3)
			gui.frmData.hide()
			# gui.chkSearch.hide()
			gui.frmSearch.hide()
			gui.btnEditKey.setCheckable(True)
			gui.btnEditKey.setChecked(False)
		def connect():

			# gui.chkSearch.stateChanged.connect(disp(gui.frmSearch))
			gui.chkData.stateChanged.connect(disp(gui.frmData))
			gui.trDict.itemClicked.connect(select(gui))
			gui.btnExp.clicked.connect(gui.trDict.expandAll)
			gui.btnCollapse.clicked.connect(gui.trDict.collapseAll)
			gui.btnCopy.clicked.connect(copytoclip(gui.txtPath))
			# gui.btnSearch.clicked.connect(search(gui))
			# gui.btnAbout.clicked.connect(copytoclip)
			gui.btnEditKey.clicked.connect(editkey(gui))
			gui.btnEditVal.clicked.connect(print)
			gui.btnExit.clicked.connect(sys.exit)
		gui = Ui_wgtQtpyDictator()
		gui.setupUi(wgt)
		
		init()
		connect()
		
		return gui
	App = QtApp()
	App.Qt5Wgt = QtWidgets.QWidget()
	App.Ui = create(App.Qt5Wgt)
	App.Disp = disp
	App.Search = search
	App.Select = select
	App.Fitt = fitt
	App.Create = create
	return App

def print_dicttree(dct, ident):
	def testkey(content, ident):
		if isinstance(dct[key], dict):
			tabs = ident * '\t'
			sys.stdout.write(tabs)
			sys.stdout.write(str(key))
			sys.stdout.write('\n')
			sys.stdout.flush()
			
			ident += 1
			print_dicttree(dct[key], ident)
		
		else:
			tabs = ident * '\t'
			sys.stdout.write(tabs)
			sys.stdout.write(key)
			sys.stdout.write('\t:\t')
			sys.stdout.write(str(dct[key]))
			sys.stdout.write('\n')
			sys.stdout.flush()
	for key in dct.keys():
		testkey(dct[key], ident)

def stdw_dct(d, indent=0):
	for key in d.keys():
		if isinstance(d[key], dict):
			sys.stdout.write('  ┃  ' * (indent) + '  ┣━━ ' + '\x1b[1;32m' + str(key) + ':' + '\x1b[0m\n')
			stdw_dct(d[key], indent + 1)
		else:
			sys.stdout.write('  ┃  ' * (indent) + '  ┣━━ ' + str(key) + '\t:\t' + str(d[key]) + '\n')

def browse(**k):
	QtApp = construct_Qt5Ui()
	kv = k.popitem()
	trunk = make_tree(QtApp.Ui, name=kv[0], data=kv[1])
	QtApp.Ui.trDict
	QtApp.Ui.trDict.addTopLevelItem(trunk)
	QtApp.Fitt(QtApp.Ui)
	QtApp.Qt5Wgt.show()
	sys.exit(QtApp.QtWin.exec())
	

if __name__ == '__main__' :
	dct = {
		'a' : {
						'aa' : 'aa',
						'ab'  : 'ab'
		},
		'b'  : { 'ba' : 'ba',
              'bb': 'bb'
		}}
	browse(test=dct)
	
App = QtWidgets.QApplication(sys.argv)
make_wgtQtpyDictator()
exit()
sys.exit()