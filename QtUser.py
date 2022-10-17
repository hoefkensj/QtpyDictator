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
	def sPol(w, h=None, v=None):
		Pol = QtWidgets.QSizePolicy(sPols(h), sPols(v))
		w['Wgt'].setSizePolicy(Pol)
		return w

	def Wgt(**k):
		def widget():
			wgt = QtWidgets.QWidget()
			wgt.setObjectName(f'wgt{Name}')
			wgt.setContentsMargins(*margin)
			return wgt
		def layout():
			makelay = wLays(Layout.upper())
			lay	= makelay(w['Wgt'])
			lay.setObjectName(f'lay{Name}')
			lay.setContentsMargins(*margin)
			lay.setSpacing(0)
			w['Lay'] = lay
			return w
		Name		=	k.get('n')
		Layout	=	k.get('t')
		margin	= k.get('margin') or [0,0,0,0]
		w= {}
		w['Wgt']			=	widget()
		w							=	layout() if Layout else w
		w['Fnx']			= Fnx(w)
		return w

	def Icon(n=None,ico=None):
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

	def Fnx(w):
		f = {}
		for n in dir(w['Wgt']):
			m = getattr(w['Wgt'], n)
			if callable(m) and not str(m).startswith('__'):
				f[n] = m
		return f
	
	def Data(w):
		d={}
		d['Name'] = w['Fnx']['objectName']
		d['Visible'] = not w['Fnx']['isHidden']
		return d

	b= {}
	b['sPol']			=	sPol
	b['wgt']			= Wgt
	b['icon']			=	Icon
	b['fnx']			=	Fnx
	b['data']			=	Data
	return b

def Elements():
	B					=	Base()
	sPol			=	B['sPol']
	Icon			=	B['icon']
	Fnx				= B['fnx']
	Data 			=	B['data']


		
	def Spcr(**k):
		p,n,w,h,vPol,hPol=[*[0]*6]
		def arg():
			nonlocal n,w,h,vPol,hPol
			n				=	k.get("n")	or 'N'
			w				= k.get('w')	or 0
			h				= k.get('h')	or 0
			p				=	k.get('p')	or 'E'
			if p == 'F' :
				hPol 		= 'F' if k.get('w') else 'P'
				vPol		=	'F'	if k.get('h') else 'P'
			else:
				hPol		=	'E' if k.get('w') else 'P'
				vPol		=	'E'	if k.get('h') else 'P'

			a = {
				'n' 		:n	,
				'w'			:w	,
				'h'			:h	,
				'hPol' 	:hPol,
				'vPol'	:vPol,
				}
			return a
		def init():
			def init():
				s['Fnx']['setObjectName'](f'spcEx{n}')
				s['Fnx']['setContentsMargins'](0,0,0,0)
			init()
			return init
		s={}
		s['Arg']			=	arg()
		s['Wgt'] 			= QtWidgets.QSpacerItem(w, h, sPols(hPol), sPols(vPol))
		s['Data']			=	Data(s)
		s['Fnx']			=	Fnx(s)
		s['Init']			= init()
		return s

	def SpcFix(**k):
		n,w,h,vPol,hPol=[*[0]*5]
		def arg():
			nonlocal n,w,h,vPol,hPol
			n				=	k.get("n")	or 'N'
			w				= k.get('w')	or 0
			h				= k.get('h')	or 0
			hPol 		= 'F' if k.get('w') else 'P'
			vPol		=	'F'	if k.get('h') else 'P'

			a = {
				'n' 		:n	,
				'w'			:w	,
				'h'			:h	,
				'hPol' 	:hPol,
				'vPol'	:vPol,
				}
			return a
		def init():
			def init():
				s['Fnx']['setObjectName'](f'spcEx{n}')
				s['Fnx']['setContentsMargins'](0,0,0,0)
			init()
			return init
		s={}
		s['Arg']			=	arg()
		s['Wgt'] 			= QtWidgets.QSpacerItem(w, h, sPols(hPol), sPols(vPol))
		s['Data']			=	Data(s)
		s['Fnx']			=	Fnx(s)
		s['Init']			= init()
		return s

	def SpcEx(**k):
		n,w,h,vPol,hPol=[*[0]*5]
		def arg():
			nonlocal n,w,h,vPol,hPol
			n				=	k.get("n")	or 'N'
			w				=	k.get("w")	or 0
			h				=	k.get("h")	or 0
			hPol		=	'E' if k.get('w') else 'P'
			vPol		=	'E'	if k.get('h') else 'P'

			a = {
				'n' 		:n	,
				'w'			:w	,
				'h'			:h	,
				'hPol' 	:hPol,
				'vPol'	:vPol,
				}
			return a
		def init():
			def init():
				s['Fnx']['setObjectName'](f'spcEx{n}')
				s['Fnx']['setContentsMargins'](0,0,0,0)
			init()
			return init
		s={}
		s['Arg']			=	arg()
		s['Wgt'] 			= QtWidgets.QSpacerItem(w, h, sPols(hPol), sPols(vPol))
		s['Data']			=	Data(s)
		s['Fnx']			=	Fnx(s)
		s['Init']			= init()
		return s

	def chkBox(n,**k):
		n,w,h,ico=[*[0]*5]
		def arg():
			nonlocal n,w,h,ico
			n				=	k.get("n")	or 'N'
			w				=	k.get("w")	or 20
			h				=	k.get("h")	or 20
			ico			=	k.get('icons')
			a = {
				'n' 		:n	,
				'w'			:w	,
				'h'			:h	,
				'ico'		:ico,
				}
			return a
		def fnx():
			def toggle():
				state=b['Fnx']['isChecked']
				b['Fnx']['setChecked'](not state)
			f 					= {}
			f['Toggle']	= toggle
			return f
		def init():
			F=b['Fnx']
			b['Wgt'] 	=	sPol( b['Wgt'] , h='P', v='P')
			def init():
				F['setObjectName'](f'chk{n}')
				F['setIcon'](Icon(n,ico=ico))
				F['setIconSize'](QtCore.QSize(w-5, h-5))
				F['setMaximumSize'](QtCore.QSize(w*3, h))
			init()
			return init
		def conn():
			c={}
			c['clicked'] = b['Wgt'].clicked.connect
			c['clicked'](b['Fnx']['toggle'])
			return c

		b={}
		b['Wgt'] 		= QtWidgets.QCheckBox()
		b['Fnx']		= Fnx(b)
		b['fnx']		= fnx()
		b['Conn']		=	conn()
		b['Data']		=	Data(b)
		b['Init']		= init()
		return b

	def iBtn(n,**k):
		def init():
			F=b['Fnx']
			def init():
				F['setObjectName'](f'iBtn{n}')
				F['setIcon'](Icon(n,ico=ico))
				F['setIconSize'](QtCore.QSize(32, 32))
				F['setCheckable'](bi)
				F['setMaximumSize'](QtCore.QSize(w, h))
				F['setToolButtonStyle'](QtCore.Qt.ToolButtonIconOnly)
				F['setMaximumHeight'](20)
			init()
			return init


		def conn():
			c={}
			c['clicked'] = btn['Wgt'].clicked.connect
			return c
		bi=k.get('bi') or False
		h=k.get('h') or 20
		w=k.get('w') or 20
		ico=k.get('icons')
		b={}
		b['Wgt'] 		= QtWidgets.QToolButton()
		b['Fnx']		= Fnx()
		b['Conn']		=	conn()
		b['Data']		=	Data()
		b['Init']		= init()
		return b

	def tBtn(n, bi=False):
		def fnx():
			F=Fnx(btn['Wgt'])
			f= {k:F[k] for k in F if not k.startswith('__')}
			return f
		def init():
			btn['Fnx']['setObjectName'](f'tBtn{n}')
			btn['Fnx']['setText'](n)
			btn['Fnx']['setCheckable'](bi)
			btn['Wgt'].setMaximumHeight(20)
			btn['Wgt'].setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
		def conn():
			c={}
			c['clicked'] = btn['Wgt'].clicked.connect
			return c
		def data():
			d={}
			d['Name'] = btn['Fnx']['objectName']
			d['Text']	=	btn['Fnx']['text']
			d['Visible'] = not btn['Fnx']['isHidden']
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
