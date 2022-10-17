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

def QtApp():
	from sys import argv
	a 						= {}
	a['QtApp'] 		= QtWidgets.QApplication(argv)
	a['Clip']			= a['QtApp'].clipboard()
	a['Mtd']			= Mtd(a)
	return a

def Mtd(w):
	o=w.get('Wgt') or w.get('QtApp')
	f = {}
	for n in dir(o):
		m = getattr(o, n)
		if callable(m) and not str(m).startswith('__'):
			f[n] = m
	return f

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
		w['Mtd']			= Mtd(w)
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

	def Data(w):
		d={}
		d['Name'] = w['Mtd']['objectName']
		d['Visible'] = not w['Mtd']['isHidden']
		return d

	b= {}
	b['QtApp']		= QtApp
	b['sPol']			=	sPol
	b['Wgt']			= Wgt
	b['Icon']			=	Icon
	b['Mtd']			=	Mtd
	b['Data']			=	Data
	return b

def Elements():
	B					=	Base()
	sPol			=	B['sPol']
	Icon			=	B['Icon']
	Data 			=	B['Data']

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
		def Init():
			def Init():
				s['Mtd']['setObjectName'](f'spcEx{n}')
				s['Mtd']['setContentsMargins'](0,0,0,0)
			Init()
			return Init
		s={}
		s['Arg']			=	arg()
		s['Wgt'] 			= QtWidgets.QSpacerItem(w, h, sPols(hPol), sPols(vPol))
		s['Data']			=	Data(s)
		s['Mtd']			=	Mtd(s)
		s['Init']			= Init()
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
		def Init():
			def Init():
				s['Mtd']['setObjectName'](f'spcEx{n}')
				s['Mtd']['setContentsMargins'](0,0,0,0)
			Init()
			return Init
		s={}
		s['Arg']			=	arg()
		s['Wgt'] 			= QtWidgets.QSpacerItem(w, h, sPols(hPol), sPols(vPol))
		s['Data']			=	Data(s)
		s['Mtd']			=	Mtd(s)
		s['Init']			= Init()
		return s

	def SpcEx(**k):
		n,w,h,vPol,hPol=[*[0]*5]
		def arg():
			nonlocal n,w,h,vPol,hPol
			n			=	k['n']	=	k.get("n")
			w			=	k['w']	=	k.get("w")	or 0
			h			=	k['h']	=	k.get("h")	or 0
			hPol	=	k['hPol']	=	'E' if k.get('w') else 'P'
			vPol	=	k['vPol']	=	'E'	if k.get('h') else 'P'
			return k
		def Init():
			def Init():
				s['Mtd']['setObjectName'](f'spcEx{n}')
				s['Mtd']['setContentsMargins'](0,0,0,0)
			Init()
			return Init
		s={}
		s['Arg']			=	arg()
		s['Wgt'] 			= QtWidgets.QSpacerItem(w, h, sPols(hPol), sPols(vPol))
		s['Data']			=	Data(s)
		s['Mtd']			=	Mtd(s)
		s['Init']			= Init()
		return s

	def chkBox(**k):
		n,w,h,ico,lbl=[*[0]*5]
		def Arg():
			nonlocal n,w,h,ico,lbl
			n		=	k['n']				=	k.get("n")
			w		=	k['w']				=	k.get("w")	or 20
			h		=	k['h']				=	k.get("h")	or 20
			ico	=	k['ico']			=	k.get('ico')
			lbl	=	k['lbl']			= k.get('lbl')
			return k
		def Fnx():
			def toggle():
				state=b['Mtd']['isChecked']
				b['Mtd']['setChecked'](not state)
			f 					= {}
			f['Toggle']	= toggle
			return f
		def Init():
			b['Wgt'] 	=	sPol( b['Wgt'] , h='P', v='P')
			def Init():
				b['Mtd']['setObjectName'](f'chk{n}')
				b['Mtd']['setIcon'](Icon(n,ico=ico))
				b['Mtd']['setIconSize'](QtCore.QSize(w-5, h-5))
				b['Mtd']['setMaximumSize'](QtCore.QSize(w*3, h))
			Init()
			return Init
		def Conn():
			c={}
			c['clicked'] = b['Wgt'].clicked.connect
			c['clicked'](b['Mtd']['toggle'])
			return c

		b={}
		b['Wgt'] 		= QtWidgets.QCheckBox()
		b['Arg']		=	Arg()
		b['Mtd']		= Mtd(b)
		b['Data']		=	Data(b)
		b['Fnx']		= Fnx()
		b['Conn']		=	Conn()
		b['Init']		= Init()
		return b

	def iBtn(**k):
		n,w,h,bi,ico,lbl=[*[0]*6]
		def Arg():
			nonlocal n,w,h,bi,ico,lbl
			n		=	k['n']				=	k.get("n")
			w		=	k['w']				=	k.get("w")	or 20
			h		=	k['h']				=	k.get("h")	or 20
			bi	=	k['bi']				=	k.get('bi') or False
			ico	=	k['ico']			=	k.get('ico')
			lbl	=	k['lbl']			= k.get('lbl')
			return k
		def Fnx():
			f 					= {}
			return f
		def Init():
			F=b['Mtd']
			def Init():
				F['setObjectName'](f'iBtn{n}')
				F['setIcon'](Icon(n,ico=ico))
				F['setIconSize'](QtCore.QSize(32, 32))
				F['setCheckable'](bi)
				F['setMaximumSize'](QtCore.QSize(w, h))
				F['setToolButtonStyle'](QtCore.Qt.ToolButtonIconOnly)
				F['setMaximumHeight'](20)
			Init()
			return Init
		def Conn():
			c={}
			c['clicked'] = b['Wgt'].clicked.connect
			return c

		b={}
		b['Wgt'] 		= QtWidgets.QToolButton()
		b['Arg']		=	Arg()
		b['Mtd']		= Mtd(b)
		b['Data']		=	Data(b)
		b['Fnx']		= Fnx()
		b['conn']		=	Conn()
		b['Init']		= Init()
		return b

	def tBtn(**k):
		n,w,h,ico,lbl,bi=[*[0]*6]
		def Arg():
			nonlocal n,w,h,ico,lbl
			n		=	k['n']				=	k.get("n")
			w		=	k['w']				=	k.get("w")	or 20
			h		=	k['h']				=	k.get("h")	or 20
			bi	=	k['bi']				=	k.get('bi') or False
			ico	=	k['ico']			=	k.get('ico')
			lbl	=	k['lbl']			= k.get('lbl') or k.get("n")
			return k
		def Fnx():
			f 					= {}
			return f
		def Init():
			F=b['Mtd']
			def Init():
				F['setObjectName'](f'tBtn{n}')
				F['setText'](lbl)
				F['setCheckable'](bi)
				F['setMaximumSize'](QtCore.QSize(w, h))
				F['setToolButtonStyle'](QtCore.Qt.ToolButtonTextOnly)
				F['setMaximumHeight'](20)
			Init()
			return Init
		def Conn():
			c={}
			c['clicked'] = b['Wgt'].clicked.connect
			return c

		b={}
		b['Wgt'] 		= QtWidgets.QToolButton()
		b['Arg']		=	Arg()
		b['Mtd']		= Mtd(b)
		b['Data']		=	Data(b)
		b['Fnx']		= Fnx()
		b['Conn']		=	Conn()
		b['Init']		= Init()
		return b

	def Lbl(**k):
		n,w,h,m,ico,lbl=[*[0]*5]
		def Arg():
			nonlocal n,w,h,ico,lbl
			n		=	k['n']				=	k.get('n')
			w		=	k['w']				=	k.get('w')	or 20
			h		=	k['h']				=	k.get('h')	or 20
			m		=	k['m']				=	k.get('m')	or [0,0,0,0]
			ico	=	k['ico']			=	k.get('ico')
			lbl	=	k['lbl']			= k.get('lbl') or n
			return k
		def Fnx():
			f 					= {}
			return f
		def Init():
			l['Wgt'] 	=sPol(l['Wgt'] , h='P', v='P')
			def Init():
				l['Mtd']['setObjectName'](f'lbl{n}')
				l['Mtd']['setText'](f'{lbl}')
				l['Mtd']['setContentsMargins'](*m)
			Init()
			return Init
		def Conn():
			c={}
			return c

		l={}
		l['Wgt'] 		= QtWidgets.QLabel()
		l['Arg']		=	Arg()
		l['Mtd']		= Mtd(l)
		l['Data']		=	Data(l)
		l['Fnx']		= Fnx()
		l['Conn']		=	Conn()
		l['Init']		= Init()
		return l

	def lEdit(**k):
		n,w,h,ro=[*[0]*4]
		def Arg():
			nonlocal n,w,h,ro
			n		=	k['n']				=	k.get('n')
			w		=	k['w']				=	k.get('w')	or 20
			h		=	k['h']				=	k.get('h')	or 20
			ro	=	k['ro']				=	k.get('ro')	or False

			return k
		def Fnx():
			f 					= {}
			return f
		def Init():
			# l['Wgt'] 	=	sPol( l['Wgt'] , h='E', v='P')
			def Init():
				l['Mtd']['setObjectName'](f'txt{n}')
				l['Mtd']['setReadOnly'](ro)
			Init()
			return Init
		def Conn():
			c={}
			return c

		l={}
		l['Wgt'] 		=  QtWidgets.QLineEdit()
		l['Arg']		=	Arg()
		l['Mtd']		= Mtd(l)
		l['Data']		=	Data(l)
		l['Fnx']		= Fnx()
		l['Conn']		=	Conn()
		l['Init']		= Init()
		return l

	def Tree(**k):
		def create():
			wgt	=	QtWidgets.QTreeWidget()
			wgt.setObjectName(name)
			return wgt
		def Init(wgt):
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
		wgt	= Init(wgt)
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
