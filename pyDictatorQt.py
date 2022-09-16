#!/usr/bin/env python
from PyQt5 import QtCore, QtGui, QtWidgets
import os, types ,sys

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

def make_icon(n=None, set='Fluent'):
	icon = QtGui.QIcon()
	lset = f'/home/hoefkens/.local/share/icons/{set}/symbolic/actions/{n}.svg'
	dset = f'/home/hoefkens/.local/share/icons/{set}-dark/symbolic/actions/{n}.svg'
	icon.addPixmap(QtGui.QPixmap(dset), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	icon.addPixmap(QtGui.QPixmap(lset), QtGui.QIcon.Normal, QtGui.QIcon.On)
	return icon

def make_SizePol(wgt,hpol=None,vpol=None):
	Policy={
	'P':QtWidgets.QSizePolicy.Preferred,
	'M':QtWidgets.QSizePolicy.Maximum,
	'm':QtWidgets.QSizePolicy.Minimum,
	'E':QtWidgets.QSizePolicy.Expanding,
	}
	sizePolicy = QtWidgets.QSizePolicy(Policy[hpol], Policy[vpol])
	wgt.setSizePolicy(sizePolicy)
	return wgt

def make_exspacer(w=1, h=1):
	wgt,lay = Wgt(t='h')
	polEx=QtWidgets.QSizePolicy.Expanding
	polMin=QtWidgets.QSizePolicy.Minimum
	spacer = QtWidgets.QSpacerItem(w, h,polEx , polMin )
	lay.addItem(spacer)
	return wgt

def iBtn(n, bi=False, h=20, w=20):
	icon = make_icon(n)
	btn = QtWidgets.QToolButton()
	btn.setObjectName(f'iBtn{n}')
	btn.setIcon(icon)
	btn.setIconSize(QtCore.QSize(32, 32))
	btn.setMaximumSize(QtCore.QSize(w, h))
	btn.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
	btn.setCheckable(bi)
	return btn

def tBtn(n, bi=False):
	btn = QtWidgets.QToolButton()
	btn.setObjectName(f'tBtn{n}')
	btn.setText(n)
	btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
	btn.setCheckable(bi)
	return btn

def lbl(n):
	lbl = QtWidgets.QLabel()
	lbl.setObjectName(f'lbl{n}')
	lbl.setText(f'{n}')
	lbl.setContentsMargins(5, 0, 5, 0)
	lbl=make_SizePol(lbl,hpol='P',vpol='P')
	return lbl

def trDict():
	trDict = QtWidgets.QTreeWidget()
	trDict = make_SizePol(trDict, hpol='E',vpol='E')
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

class QtGui(object):
	def CreateUi(self,Ui):
		self.tbtnExit=tBtn('Exit')
		self.tbtnSave=tBtn('Save As')
		self.tbtnPrint=tBtn('Print')
		self.exSpacerAppCtl=make_exspacer()

		self.wgtFileCtl,self.layFileCtl = Wgt(t='h')
		self.layFileCtl.addWidget(self.tbtnPrint)
		self.layFileCtl.addWidget(self.tbtnSave)
		self.wgtAppCtl,self.layAppCtl = Wgt(t='h')
		self.layAppCtl.addWidget(self.exSpacerAppCtl)
		self.layAppCtl.addWidget(self.tbtnExit)
		self.wgtCtl,self.layCtl=Wgt(t='h')
		self.layCtl.addWidget(self.wgtFileCtl)
		self.layCtl.addWidget(self.wgtAppCtl)

		self.trDict=trDict()

		Ui.addWidget(self.wgtCtl)
		Ui.addWidget(self.trDict)

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
		gui = QtGui()
		gui.CreateUi(wgt)
		# init()
		# connect()
		return gui
	App = QtApp()
	App.wgtQt5,App.layQt5 = Wgt(n='Qt5',t='v')
	App.Ui = create(App.layQt5)
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
	QtApp.wgtQt5.show()
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