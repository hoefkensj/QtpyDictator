#!/usr/bin/env python
from PyQt5 import QtCore, QtGui, QtWidgets
import os, types ,sys

def Wgt(n=None, t=None ):
	Name=n
	layout=t
	def make():
		def makelay():
			lays={
				'H'	:	QtWidgets.QHBoxLayout,
				'V'	: QtWidgets.QVBoxLayout,
				'G'	:	QtWidgets.QGridLayout,
				'F'	:	QtWidgets.QFormLayout,
			}
			makelay = lays[t.upper()]
			lay	= makelay(wgt)
			lay.setObjectName(f'lay{n}')
			lay.setContentsMargins(0, 0, 0, 0)
			lay.setSpacing(0)
			return lay
		wgt = QtWidgets.QWidget()
		wgt.setObjectName(f'wgt{n}')
		wgt.setContentsMargins(0, 0, 0, 0)
		lay=makelay() if layout else None
		return wgt,lay
	return make()

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

def SpcEx(w=1, h=1):
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
	btn.setMaximumHeight(20)
	return btn

def lbl(n):
	lbl = QtWidgets.QLabel()
	lbl.setObjectName(f'lbl{n}')
	lbl.setText(f'{n}')
	lbl.setContentsMargins(0, 0, 5, 0)
	lbl=make_SizePol(lbl,hpol='P',vpol='P')
	return lbl

def ledit(n,ro=False):
	txt = QtWidgets.QLineEdit()
	txt.setObjectName(f'txt{n}')
	txt.setReadOnly(ro)
	txt=make_SizePol(txt,hpol='E',vpol='P')
	return txt

def wgtTrDict():
	wgt,lay 		=Wgt(t='h')
	wgt.wgtTree = QtWidgets.QTreeWidget()
	wgt.wgtTree = make_SizePol(wgt.wgtTree, hpol='E',vpol='E')
	# wgt.trDict.setAutoFillBackground(True)
	# wgt.trDict.setFrameShape(QtWidgets.QFrame.NoFrame)
	# wgt.trDict.setFrameShadow(QtWidgets.QFrame.Plain)
	# wgt.trDict.setLineWidth(0)
	# wgt.trDict.setMidLineWidth(0)
	# wgt.trDict.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
	# wgt.trDict.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
	# wgt.trDict.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
	# wgt.trDict.setAutoScroll(False)
	# wgt.trDict.setAutoScrollMargin(16)
	# wgt.trDict.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked | QtWidgets.QAbstractItemView.SelectedClicked)
	# wgt.trDict.setProperty("showDropIndicator", True)
	# wgt.trDict.setAlternatingRowColors(True)
	# wgt.trDict.setUniformRowHeights(True)
	# wgt.trDict.setAnimated(True)
	# wgt.trDict.setAllColumnsShowFocus(True)
	# wgt.trDict.setWordWrap(True)
	wgt.wgtTree.setObjectName("wgtTree")
	# wgt.trDict.header().setMinimumSectionSize(100)
	# wgt.trDict.header().setStretchLastSection(True)
	lay.addWidget(wgt.wgtTree)
	return wgt

def wgtEditProp(n):
	wgt,lay 		=Wgt(t='h')
	wgt.lbl 		= lbl(f'{n}:')
	wgt.txt 		= ledit(n,ro=True)
	wgt.btnSet = tBtn('Set')
	wgt.btnEdit 		=	iBtn('edit-symbolic', bi=True)
	lay.addWidget(wgt.lbl)
	lay.addWidget(wgt.txt)
	lay.addWidget(wgt.btnSet)
	lay.addWidget(wgt.btnEdit)
	return wgt

def wgtPath():
	wgt,lay = Wgt(t='h')
	wgt.lbl = lbl('Path:')
	wgt.txt = ledit(n='Path',ro=True)
	wgt.btnCopy = tBtn('Copy')
	lay.addWidget(wgt.lbl)
	lay.addWidget(wgt.txt)
	lay.addWidget(wgt.btnCopy)
	return wgt

def wgtSearch():
	wgt,lay = Wgt(t='h')
	wgt.txt = ledit('Search')
	wgt.btnSearch = iBtn('search-symbolic')
	wgt.btnNext = iBtn('carousel-arrow-next-symbolic', w=12)
	wgt.btnPrev = iBtn('carousel-arrow-previous-symbolic', w=12)
	lay.addWidget(wgt.txt)
	lay.addWidget(wgt.btnPrev)
	lay.addWidget(wgt.btnNext)
	lay.addWidget(wgt.btnSearch)
	return wgt

def wgtTreeCtl():
	wgt,lay = Wgt(t='h')
	wgt.btnExp = iBtn('value-increase-symbolic',h=15,w=15)
	wgt.btnCol = iBtn('value-decrease-symbolic',h=15,w=15)
	lay.addWidget(wgt.btnExp)
	lay.addWidget(wgt.btnCol)
	return  wgt

def makesiblings(parent=None,**k):
	t=k['t']
	wgt,lay=Wgt(t=t)
	for child in  a:
		wgt.child

def SpcEx(w=1, h=1):
	wgt,lay=Wgt(t='h')
	wgt.SpcEx = QtWidgets.QSpacerItem(w, h, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
	lay.addItem(wgt.SpcEx)
	return wgt
def SpcFix(w=1, h=1):
	wgt,lay=Wgt(t='h')
	wgt.SpcFix = QtWidgets.QSpacerItem(w, h, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
	lay.addItem(wgt.SpcFix)
	return wgt


def siblings(wgt1,wgt2,t,margin=[0,0,0,0]):
	wgt,lay=Wgt(t=t)
	wgt.setContentsMargins(*margin)
	lay.addWidget(wgt1)
	lay.addWidget(wgt2)
	return wgt
def center(child,w=None):
	lSpcFix=SpcFix(w=w)
	rSpcFix=SpcFix(w=w)
	wgt,lay=Wgt(t='h')
	lay.addWidget(lSpcFix)
	lay.addWidget(child)
	lay.addWidget(rSpcFix)
	return wgt

class Qt5Gui(object):
	def CreateUi(self,Ui):


		self.SpcExAppCtl=SpcEx()
		self.btnExit=tBtn('Exit')
		self.btnSave=tBtn('Save As')
		self.btnPrint=tBtn('Print')


		self.wgtTrDict	= wgtTrDict()
		self.wgtSearch	=	wgtSearch()

		self.wgtEditKey	= wgtEditProp('Key')
		self.wgtEditVal = wgtEditProp('Val')
		self.wgtPath=wgtPath()

		self.wgtTrTools		=	center(self.wgtSearch,w=5)
		self.wgtTreeDisp	= siblings(self.wgtTrDict,self.wgtTrTools,'v',margin=[0,0,0,5])
		self.wgtFileCtl 	= siblings(self.btnPrint,self.btnSave,'h')
		self.wgtAppCtl		= siblings(self.SpcExAppCtl,self.btnExit,'h')
		self.wgtCtl				=	siblings(self.wgtFileCtl,self.wgtAppCtl,'h')
		self.wgtEdit			=	siblings(self.wgtEditKey,self.wgtEditVal,'v',margin=[0,0,0,5])

		self.wgtWrpEdit	=	center(self.wgtEdit,w=25)


		self.wgtWrpPath=center(self.wgtPath,w=20)
		self.wgtTreeDisp.wgtTrCtl		=	wgtTreeCtl()


		self.wgtTools,self.layTools=Wgt(t='v')
		self.layTools.addWidget(self.wgtWrpEdit)
		self.layTools.addWidget(self.wgtWrpPath)
		self.wgtTreeDisp


		Ui.addWidget(self.wgtTreeDisp)
		Ui.addWidget(self.wgtTools)
		Ui.addWidget(self.wgtCtl)


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
				w = gui.wgtTrDict.wgtTree.columnWidth(1)
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
		txtBox = [gui.wgtEditKey.txt, gui.wgtEditVal.txt, gui.wgtPath.txt, ]
		def fill():
			data = gui.wgtTrDict.wgtTree.selectedItems()
			for idx, txtbox in zip([0, 3, 2], txtBox):
				txtbox.setText(data[0].text(idx))
		return fill

	def fitt(gui):
		gui.wgtTrDict.wgtTree.expandAll()
		gui.wgtTrDict.wgtTree.resizeColumnToContents(0)
		w = gui.wgtTrDict.wgtTree.columnWidth(0)
		gui.wgtTrDict.wgtTree.setColumnWidth(0, w + 20)

		gui.wgtTrDict.wgtTree.resizeColumnToContents(1)
		w = gui.wgtTrDict.wgtTree.columnWidth(1)
		gui.wgtTrDict.wgtTree.setColumnWidth(1, w + 20)
		gui.wgtTrDict.wgtTree.collapseAll()

	def copytoclip(txt):
		def toclip():
			App.QtClip.setText(txt.text())
		return toclip

	def editkey(gui):
		def edit(state):
			gui.wgtEditKey.btnEdit.setChecked(state)
			gui.wgtEditKey.txt.setReadOnly(not state)
			gui.wgtEditKey.btnSet.setHidden(not state)

		return edit

	def editval(gui):
		def edit(state):
			gui.wgtEditVal.btnEdit.setChecked(state)
			gui.wgtEditVal.txt.setReadOnly(not state)
			gui.wgtEditVal.btnSet.setHidden(not state)
		return edit

	def search(gui):
		def find():
			found=gui.trDict.findChild(str, gui.txtSearch.text(), QtCore.Qt.MatchFlag.MatchRecursive)
			found2=gui.trDict.findChild(str , gui.txtSearch.text(), QtCore.Qt.MatchFlag.MatchContains)
			print(gui.txtSearch.text(),found,found2)
		return find

	def create(wgt):
		def init():
			gui.wgtTrDict.wgtTree.expandAll()
			gui.wgtTrDict.wgtTree.resizeColumnToContents(0)
			gui.wgtTrDict.wgtTree.resizeColumnToContents(1)
			gui.wgtTrDict.wgtTree.collapseAll()
			gui.wgtTrDict.wgtTree.expandItem(gui.wgtTrDict.wgtTree.topLevelItem(0))
			gui.wgtTrDict.wgtTree.setColumnCount(4)
			gui.wgtTrDict.wgtTree.hideColumn(2)
			gui.wgtTrDict.wgtTree.hideColumn(3)

			gui.wgtEditKey.btnEdit.setChecked(False)
			gui.wgtEditVal.btnEdit.setChecked(False)

			gui.wgtSearch.btnNext.hide()
			gui.wgtSearch.btnPrev.hide()
			gui.wgtEditKey.btnSet.setHidden(True)
			gui.wgtEditVal.btnSet.setHidden(True)


		def connect():

			gui.wgtTrDict.wgtTree.itemClicked.connect(select(gui))
			gui.wgtTreeDisp.wgtTrCtl.btnExp.clicked.connect(gui.wgtTrDict.wgtTree.expandAll)
			gui.wgtTreeDisp.wgtTrCtl.btnCol.clicked.connect(gui.wgtTrDict.wgtTree.collapseAll)
			# gui.btnCopy.clicked.connect(copytoclip(gui.txtPath))
			# gui.btnSearch.clicked.connect(search(gui))
			# gui.btnAbout.clicked.connect(copytoclip)
			gui.wgtEditKey.btnEdit.clicked.connect(editkey(gui))
			gui.wgtEditVal.btnEdit.clicked.connect(editval(gui))
			gui.btnExit.clicked.connect(sys.exit)
		gui = Qt5Gui()
		gui.CreateUi(wgt)

		init()
		connect()
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
	QtApp.Ui.wgtTrDict.wgtTree
	QtApp.Ui.wgtTrDict.wgtTree.addTopLevelItem(trunk)
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