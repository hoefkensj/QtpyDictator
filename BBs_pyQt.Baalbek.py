#!/usr/bin/env python

import types

def Layouts():
	def Format():
		from PyQt5  import	 QtWidgets
		formats				=		{
		'hBox' 			:	QtWidgets.QHBoxLayout,
		'vBox' 			: QtWidgets.QVBoxLayout,
		'Grid' 			:	QtWidgets.QGridLayout,
		'Form' 			:	QtWidgets.QFormLayout,
		}
		return formats
	Layouts = {}
	Layouts['Format'] = Format

	return Layouts


def Elements():
	from PyQt5 import QtCore, QtGui, QtWidgets
	def Widget(*a,**k):
		def create():
			def c(Wgt,**k):
				Wgt.setObjectName(f'wgt{}')
			return c
		def addSubs():
		def layout():


		Widget={}
		Widget['make']			=	QtWidgets.QWidget
		Widget['create'] 		= create
		Widget['addSubs']		=	addSubs
		Widget['layout']		=	layout

				Widget={}
		Widget['make']			=	QtWidgets.QWidget
		Widget['create'] 		= create
		Widget['addSubs']		=	addSubs
		Widget['layout']		=	layout
		Wgt.

	def Wgt(**k):
		def widget():
			wgt =
			wgt.setObjectName(f'wgt{Name}')
			wgt.setContentsMargins(*margin)
			return wgt
		def layout():
			makelay = lays.get(Layout.upper())
			lay	= makelay(wgt)
			lay.setObjectName(f'lay{Name}')
			lay.setContentsMargins(*margin)
			lay.setSpacing(0)
			wgt.lay=lay
			return wgt
		Name		=	k.get('n')
		Layout	=	k.get('t')
		margin	=	k.get('margin') or [0,0,0,0]
		wgt			=	widget()
		wgt			=	layout() if Layout else wgt
		return wgt
	def icon_dl(n=None):
		icon_states={
			0 : QtGui.QIcon.On,
			1 :	QtGui.QIcon.Off,	}
		icon = QtGui.QIcon()
		def  make_icon(icon,state):
			with open(f'icon{state}.svg','wb') as l:
				l.write(base64.b64decode(ico[n][state]))
			icon.addPixmap(QtGui.QPixmap(f'icon{state}.svg'), QtGui.QIcon.Normal, icon_states[state])
			return icon
		icon = make_icon(icon,0)
		icon = make_icon(icon,1)
		return icon
	def Spcr(**k):
		w=k.get('w')
		h=k.get('h')
		hpol,vpol=k.get('t')
		wgt=QtWidgets.QSpacerItem(w, h, sPols[hpol], sPols[vpol])
		return wgt
	def chkBox(n,**k):
		h=k.get('h') or 20
		w=k.get('w') or 20

		cBox 	= QtWidgets.QCheckBox()
		cBox.setObjectName(f'chk{n}')
		cBox	=	QtBlocks.Layouts.sPol(cBox, h='P', v='P')
		cBox.setIcon(icon_dl('RegEx'))
		cBox.setIconSize(QtCore.QSize(w-5, h-5))
		cBox.setMaximumSize(QtCore.QSize(w*3, h))

		return cBox
	def iBtn(n,**k):
		bi=k.get('bi') or False
		h=k.get('h') or 20
		w=k.get('w') or 20
		btn = QtWidgets.QToolButton()
		btn.setObjectName(f'iBtn{n}')
		btn.setIcon(icon_dl(n))
		btn.setIconSize(QtCore.QSize(32, 32))
		btn.setMaximumSize(QtCore.QSize(w, h))
		btn.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
		btn.setCheckable(bi)
		btn.setHidden(False)
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
		lbl=  QtBlocks.Layouts.sPol(lbl, h='P', v='P')
		return lbl
	def ledit(n,ro=False):
		txt = QtWidgets.QLineEdit()
		txt.setObjectName(f'txt{n}')
		txt.setReadOnly(ro)
		txt=QtBlocks.Layouts.sPol(txt, h='E', v='P')
		return txt
	def Tree(**k):
		def create():
			wgt	=	QtWidgets.QTreeWidget()
			wgt.setObjectName(name)
			return wgt
		def init(wgt):
			wgt = QtBlocks.Layouts.sPol(wgt, h='E', v='mE')
			# wgt.setFrameShape(QtWidgets.QFrame.NoFrame)
			wgt.setAlternatingRowColors(True)
			wgt.setAnimated(True)
			wgt.setHeaderHidden(True)
			wgt.setColumnCount(5)
			wgt.hideColumn(2)
			wgt.hideColumn(3)
			wgt.hideColumn(4)
			wgt.setMinimumHeight(10)
			wgt.setAllColumnsShowFocus(True)
			wgt.setMinimumHeight(50)
			wgt.setContentsMargins(*margins)
			return wgt
		name=k.get('n') or 'Tree'
		margins=k.get('margin') or [0,0,0,0]
		wgt	= create()
		wgt	= init(wgt)
		return wgt

	Elements= {}
	Elements['Wgt']						= Wgt
	Elements['Spcr']					=	Spcr
	Elements['chkBox']				=	chkBox
	Elements['iBtn']					=	iBtn
	Elements['tBtn']					=	tBtn
	Elements['lbl']						=	lbl
	Elements['lneEd']					=	ledit
	Elements['TreeBrowse']		= Tree
	return Elements