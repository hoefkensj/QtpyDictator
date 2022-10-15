#!/usr/bin/env python
# Auth

from PyQt5 import QtCore, QtGui, QtWidgets

def sPols(t):
	s 			= 	{
		'P'				: QtWidgets.QSizePolicy.Preferred,
		'M'				: QtWidgets.QSizePolicy.Maximum,
		'm'				: QtWidgets.QSizePolicy.Minimum,
		'E'				:	QtWidgets.QSizePolicy.Expanding,
		'mE'			:	QtWidgets.QSizePolicy.MinimumExpanding,
		'F'				:	QtWidgets.QSizePolicy.Fixed,
		}
	return s[t]

def wLays(t):
	l				=		{
		'H'				:	QtWidgets.QHBoxLayout,
		'V'				: QtWidgets.QVBoxLayout,
		'G'				:	QtWidgets.QGridLayout,
		'F'				:	QtWidgets.QFormLayout,
						}
	return l[t]

def Base():
	def sPol(wgt, h=None, v=None):
		Pol = QtWidgets.QSizePolicy(sPols(h), sPols(v))
		wgt.setSizePolicy(Pol)
		return wgt

	def Wgt(**k):
		def widget():
			wgt = QtWidgets.QWidget()
			wgt.setObjectName(f'wgt{Name}')
			wgt.setContentsMargins(*margin)
			return wgt
		def layout():
			makelay = wLays(Layout.upper())
			lay	= makelay(wgt)
			lay.setObjectName(f'lay{Name}')
			lay.setContentsMargins(*margin)
			lay.setSpacing(0)
			wgt.lay=lay
			return wgt
		Name		=	k.get('n')
		Layout	=	k.get('t')
		margin	= k.get('margin') or [0,0,0,0]
		wgt			=	widget()
		wgt			=	layout() if Layout else wgt
		return wgt

	def icon_dl(n=None,ico=None):
		import base64
		icon_states={
			0	: QtGui.QIcon.On,
			1	:	QtGui.QIcon.Off,	}
		icon = QtGui.QIcon()
		def  make_icon(icon,state):
			with open(f'icon{state}.svg','wb') as l:
				l.write(base64.b64decode(ico[n][state]))
			icon.addPixmap(QtGui.QPixmap(f'icon{state}.svg'), QtGui.QIcon.Normal, icon_states[state])
			return icon
		# with open('icond.svg','wb') as d:
		# 	d.write(base64.b64decode(ico[n][1]))
		icon = make_icon(icon,0)
		icon = make_icon(icon,1)
		return icon

	b= {}
	b['sPol']			=	sPol
	b['Wgt']			= Wgt
	b['icon_dl']	=	icon_dl
	return b

def Elements():
	B=Base()
	sPol=B['sPol']
	icon_dl	=	B['icon_dl']

	def Spcr(**k):
		w=k.get('w')
		h=k.get('h')
		hpol,vpol=k.get('t')
		wgt=QtWidgets.QSpacerItem(w, h, sPols(hpol), sPols(vpol))
		return wgt

	def SpcFix(**k):
		wgt=	B['Wgt'](t='h')
		w			= k.get('w')	or 0
		h			= k.get('h')	or 0
		hPol 	= 'F' if k.get('w') else 'P'
		vPol	=	'F'	if k.get('h') else 'P'
		wgt.SpcFix = 	Spcr( w=w, h=h, t=[hPol,vPol])
		wgt.lay.addItem(wgt.SpcFix)
		wgt.setContentsMargins(0,0,0,0)
		wgt.lay.setContentsMargins(0,0,0,0)
		return wgt

	def SpcEx(**k):
		n 	= k.get('n')
		w			= k.get('w')	or 0
		h			= k.get('h')	or 0
		hPol 	= 'E' if k.get('w') else 'P'
		vPol	=	'E'	if k.get('h') else 'P'
		def create(wgt):
			wgt.SpcEx = Spcr(w=w, h=h, t=[hPol,vPol])
			return wgt
		def layout(wgt):
			wgt = B['sPol'](wgt, h='P', v='P')
			return wgt
		def add(wgt):
			wgt.lay.addItem(wgt.SpcEx)
			return wgt.lay
		def init(wgt):
			wgt.setContentsMargins(0,0,0,0)
			wgt.lay.setContentsMargins(0,0,0,0)
			return wgt

		wgt = B['Wgt'](n=f'wgtSpcEx{n}',t='h')
		wgt=create(wgt)
		wgt=layout(wgt)
		wgt.lay=add(wgt)

		return wgt

	def chkBox(n,**k):
		h=k.get('h') or 20
		w=k.get('w') or 20
		ico=k.get('icons')
		cBox 	= QtWidgets.QCheckBox()
		cBox.setObjectName(f'chk{n}')
		cBox	=	sPol(cBox, h='P', v='P')
		cBox.setIcon(icon_dl(n,ico=ico))
		cBox.setIconSize(QtCore.QSize(w-5, h-5))
		cBox.setMaximumSize(QtCore.QSize(w*3, h))
		return cBox

	def iBtn(n,**k):
		bi=k.get('bi') or False
		h=k.get('h') or 20
		w=k.get('w') or 20
		ico=k.get('icons')
		btn = QtWidgets.QToolButton()
		btn.setObjectName(f'iBtn{n}')
		btn.setIcon(icon_dl(n,ico=ico))
		btn.setIconSize(QtCore.QSize(32, 32))
		btn.setMaximumSize(QtCore.QSize(w, h))
		btn.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
		btn.setCheckable(bi)
		btn.setHidden(False)
		return btn

	def tBtn(n, bi=False):
		def fnx():
			f= {}
			f['setName']	= btn['Wgt'].setObjectName
			f['Name']			=	btn['Wgt'].objectName
			f['setText']	=	btn['Wgt'].setText
			f['Text']			=	btn['Wgt'].text
			f['checkable']	=	btn['Wgt'].setCheckable
			f['setHidden']	=	btn['Wgt'].setHidden
			f['Hidden']		= btn['Wgt'].isHidden
			return f

		def init():
			btn['Fnx']['setName'](f'tBtn{n}')
			btn['Fnx']['setText'](n)
			btn['Fnx']['checkable'](bi)
			btn['Wgt'].setMaximumHeight(20)
			btn['Wgt'].setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
		def conn():
			c={}
			c['clicked'] = btn['Wgt'].clicked.connect
			return c
		def data():
			d={}
			d['Name'] = btn['Fnx']['Name']()
			d['Text']	=	btn['Fnx']['Text']()
			d['Visible'] = not btn['Fnx']['Hidden']()
		btn={}
		btn['Wgt'] = QtWidgets.QToolButton()
		btn['Fnx']	= fnx()
		btn['Conn']	=	conn()
		btn['Data']=	data()
		init()
		return btn

	def Lbl(n):
		lbl = QtWidgets.QLabel()
		lbl.setObjectName(f'lbl{n}')
		lbl.setText(f'{n}')
		lbl.setContentsMargins(0, 0, 5, 0)
		lbl=  sPol(lbl, h='P', v='P')
		return lbl

	def lEdit(n,ro=False):
		txt = QtWidgets.QLineEdit()
		txt.setObjectName(f'txt{n}')
		txt.setReadOnly(ro)
		txt=sPol(txt, h='E', v='P')
		return txt

	def Tree(**k):
		def create():
			wgt	=	QtWidgets.QTreeWidget()
			wgt.setObjectName(name)
			return wgt
		def init(wgt):
			wgt = sPol(wgt, h='E', v='mE')
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

	e = {}

	e['Spcr']			=	Spcr
	e['SpcFix']		= SpcFix
	e['SpcEx']		=	SpcEx
	e['chkBox']		=	chkBox
	e['iBtn']			=	iBtn
	e['tBtn']			=	tBtn
	e['Lbl']			=	Lbl
	e['lEdit']		=	lEdit
	e['Tree']			= Tree
	return e

def Layouts():
	B=Base()

	E=Elements()

	def siblings(wgts, t, margin=[0,0,0,0]):
		wgt=	 B['Wgt'](t=t)
		wgt.setContentsMargins(*margin)
		for item in wgts:
			wgt.lay.addWidget(item)
		return wgt

	def center(child,	**k):
		w = k.get('w') or 0
		margin = k.get('margin') or [w,0,w,0]
		lSpcFix= E['SpcFix'](w=w)
		rSpcFix= E['SpcFix'](w=w)
		wgt= B['Wgt'](t='h')
		wgt.lay.addWidget(lSpcFix)
		wgt.lay.addWidget(child)
		wgt.lay.addWidget(rSpcFix)
		wgt.setContentsMargins(*margin)
		return wgt
	l = {}

	l['siblings'] 	= siblings
	l['center']			= center
	return l
