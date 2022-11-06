#!/usr/bin/env python
# Auth
from myPyQt.lib.wgt import Wgt
from PyQt5 import QtWidgets,QtCore,QtGui
from inspect import isfunction
def sPols(t):
	s 			= 	{
		'P'   : QtWidgets.QSizePolicy.Preferred,
		'M'   : QtWidgets.QSizePolicy.Maximum,
		'm'   : QtWidgets.QSizePolicy.Minimum,
		'E'   :	QtWidgets.QSizePolicy.Expanding,
		'mE'  :	QtWidgets.QSizePolicy.MinimumExpanding,
		'F'   :	QtWidgets.QSizePolicy.Fixed,
		}
	return s[t]

def sPls(t):
	P	 = QtWidgets.QSizePolicy.Preferred
	M	 = QtWidgets.QSizePolicy.Maximum
	m	 = QtWidgets.QSizePolicy.Minimum
	E	 =	QtWidgets.QSizePolicy.Expanding
	mE	=QtWidgets.QSizePolicy.MinimumExpanding
	F	 =	QtWidgets.QSizePolicy.Fixed
	return locals()[t]


def wLays(t):

	l				=		{
		'H'   :	QtWidgets.QHBoxLayout,
		'V'   : QtWidgets.QVBoxLayout,
		'G'   :	QtWidgets.QGridLayout,
		'F'   :	QtWidgets.QFormLayout,
						}
	return l[t.upper()]

def App():
	from sys import argv
	a = {}
	a['QtApp'] 		= QtWidgets.QApplication(argv)
	a['Clip']			= a['QtApp'].clipboard()

	return a

# def dClass(**k):
# 	from inspect import isfunction,ismethod,isclass
# 	cls={}
# 	for key in k:
# 		cls[key]={}
# 		cls[key]['Mtds']=Mtds
# 		cls[key]['Attr']=Attr

def Mtds():
	def Mtds(o):
		f={}
		for n in dir(o):
			m=getattr(o, n)
			if callable(m) and '__' not in n:
				f[n]=m
		return f

	# def A():
	# 		print('-'*80)
	# 		a={}
	# 		for n in d:
	# 			m=getattr(o, n)
	# 			if isinstance(m,(str|int|float|dict|list|tuple|set)):
	# 				d.pop(n)
	# 				a[n]=m
	# 		return a

	def mtds():
		def clj_mtds():
			mts=M()
			return mts
		return clj_mtds

	def attrs(t):
		def clj_attrs():
			ats=A()
			return ats
		return clj_attrs

	f={k:v for k,v in locals().items() if isfunction(v)}
	return f

def Make():
	def sPol(w, h=None, v=None):
		Pol = QtWidgets.QSizePolicy(sPols(h), sPols(v))
		w['Wgt'].setSizePolicy(Pol)
		return w['Wgt']

	# def Wgt(**k):
	# 	n,t,m,lay=[*[0]*4]
	#
	# 	def arg(**k):
	# 		nonlocal n,t,m,lay
	# 		n			= k.get("n") or None
	# 		t			= k.get("t") or None
	# 		m			=	k['m']	= k.get("m")	or [0,0,0,0]
	# 		k['n']= n
	# 		k['t']= t
	# 		k['m']= m
	# 		if t:
	# 			lay	= k['lay']	=wLays(t)
	# 		return k
	# 	def mtd():
	# 		dc = dClass(w)
	# 		f=Mtd(w)
	# 		return f
	# 	def lmtd():
	# 		Mtd = dClass('Lay')
	# 		f=Mtd(w)
	# 		return f
	#
	# 	def init():
	# 		def init():
	# 			w['Mtd']['setObjectName'](f'wgt{n}')
	# 			w['Mtd']['setContentsMargins'](*m)
	# 		init()
	# 		return init
	# 	def initl():
	# 		def init():
	# 			w['LMtd']['setObjectName'](f'lay{n}')
	# 			w['LMtd']['setContentsMargins'](*m)
	# 			w['LMtd']['setSpacing'](0)
	# 		init()
	# 		return init
	#
	#
	# 	w= {}
	# 	w['Arg']			=	arg(**k)
	# 	w['Wgt']			=	QtWidgets.QWidget()
	# 	w['Mtd']			=	mtd()
	# 	w['Init']			=	init()
	# 	if t:
	# 		w['Lay']			= lay(w['Wgt'])
	# 		w['LMtd']			= lmtd()
	# 		w['Initl']		=	initl()
	# 	return w

	def Icon(n=None,ico=None):
		import base64
		icon_states={
			0 : QtGui.QIcon.On,
			1 :	QtGui.QIcon.Off,	}
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

	def wgt(**k):
		return Wgt(**k)

	make={ 'Make' :  {k:v for k,v in locals().items() if isfunction(v)}}
	return make

def Elements():
	sPol = QtUi['Make']['sPol']
	Icon			=	QtUi['Make']['Icon']
	Data 			=	QtUi['Make']['Data']

	def Spcr(**k):
		p,n,w,h,vPol,hPol=[*[0]*6]
		def arg():
			nonlocal p,n,w,h,vPol,hPol
			n		=	k['n']	= k.get("n")	or 'N'
			w		=	k['w']	= k.get('w')	or 0
			h		=	k['h']	= k.get('h')	or 0
			p		=	k['p']	= k.get('p')	or 'E'
			if p == 'F' :
				hPol 	=	k['hPol']		= 'F' if k.get('w') else 'P'
				vPol	=	k['vPol']		=	'F'	if k.get('h') else 'P'
			else:
				hPol	=	k['hPol']		=	'E' if k.get('w') else 'P'
				vPol	=	k['vPol']		=	'E'	if k.get('h') else 'P'
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

	def SpcFix(**k):
		n,w,h,vPol,hPol=[*[0]*5]
		def arg():
			nonlocal n,w,h,vPol,hPol
			n				=	k['n']	= k.get("n")	or 'N'
			w				=	k['w']	= k.get('w')	or 0
			h				=	k['h']	= k.get('h')	or 0
			hPol 		=	k['hPol']	= 'F' if k.get('w') else 'P'
			vPol		=	k['vPol']	=	'F'	if k.get('h') else 'P'
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

	def SpcEx(**k):
		n,w,h,vPol,hPol=[*[0]*5]
		def arg():
			nonlocal n,w,h,vPol,hPol
			n			=	k['n']	=	k.get("n")
			w			=	k['w']	= k.get("w")	or 0
			h			=	k['h']	= k.get("h")	or 0
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
		wgt=None

		def Arg():
			nonlocal n,w,h,ico,lbl
			n		=	k['n']				=	k.get("n")
			w		=	k['w']				= k.get("w")	or 20
			h		=	k['h']				= k.get("h")	or 20
			ico	=	k['ico']			=	k.get('ico')
			lbl	=	k['lbl']			= k.get('lbl')
			return k
		def Mtd():
			Mtds(Wgt())

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
		b['Wgt'] 		= Wgt()
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
			w		=	k['w']				= k.get("w")	or 20
			h		=	k['h']				= k.get("h")	or 20
			bi	=	k['bi']				= k.get('bi') or False
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
		Mtd=     dClass('Mtds')('Wgt')
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
			w		=	k['w']				= k.get("w")	or 20
			h		=	k['h']				= k.get("h")	or 20
			bi	=	k['bi']				= k.get('bi') or False
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
		b['Arg']		= Arg()
		Mtd=     dClass('Mtds')('Wgt')
		b['Mtd']		= Mtd(b)
		b['Data']		=	Data(b)
		b['Fnx']		= Fnx()
		b['Conn']		=	Conn()
		b['Init']		= Init()
		return b

	def Lbl(**k):
		n,w,h,m,ico,lbl= [*[0] * 6]
		Mtd=     dClass('Mtds')('Wgt')
		def Arg():
			nonlocal n,w,h,ico,lbl,m
			n		=	k['n']				=	k.get('n')
			w		=	k['w']				= k.get('w')	or 20
			h		=	k['h']				= k.get('h')	or 20
			m		=	k['m']				= k.get('m')	or [0,0,0,0]
			ico	=	k['ico']			=	k.get('ico')
			lbl	=	k['lbl']			= k.get('lbl') or n
			return k
		def Fnx():
			f 					= {}
			return f
		def Init():
			# l['Wgt'] 	=sPol(l['Wgt'] , h='P', v='P')
			def Init():
				l['Mtd']['setObjectName'](f'lbl_{n}')
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
		l['Data']		= None
		l['Fnx']		= Fnx()
		l['Conn']		=	Conn()
		l['Init']		= Init()
		return l

	def lEdit(**k):
		n,w,h,ro=[*[0]*4]
		def Arg():
			nonlocal n,w,h,ro
			n		=	k['n']				=	k.get('n')
			w		=	k['w']				= k.get('w')	or 20
			h		=	k['h']				= k.get('h')	or 20
			ro	=	k['ro']				= k.get('ro')	or False

			return k
		def Fnx():
			f 					= {}
			f['Read']		=	l['Mtd']['text']
			f['Write']	=	l['Mtd']['setText']
			f['makeRO']			=	l['Mtd']['setReadOnly']
			f['RO']					=	l['Mtd']['isReadOnly']
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
			c['Entered']=l['Mtd']['returnPressed'].connect
			c['Changed']=l['Mtd']['textChanged'].connect
			c['Edited']=l['Mtd']['textEdited'].connect
			return c

		l={}
		l['Wgt'] 		=  QtWidgets.QLineEdit()
		l['Arg'] = Arg()
		Mtd=     dClass('Mtds')('Wgt')
		l['Mtd']		= Mtd(l)
		l['Data']		=	Data(l)
		l['Fnx']		= Fnx()
		l['Conn']		=	Conn()
		l['Init']		= Init()
		return l

	def Tree(**k):
		n,m=[*[0]*2]
		def Arg():
			nonlocal n,m
			n		=	k['n']				= k.get('n') or 'Tree'
			w		=	k['m']				= k.get('m') or [0,0,0,0]
			return k
		def Fnx():
			f 					= {}
			f['setHeader']				= t['Mtd']['setHeader']
			f['addTopLevelItem']	=	t['Mtd']['addTopLevelItem']
			f['setColumnWidth']		=	t['Mtd']['setColumnWidth']
			f['setCurrentItem']		=	t['Mtd']['setCurrentItem']
			f['expandAll']				= t['Mtd']['expandAll']
			f['collapseAll']			= t['Mtd']['collapseAll']
			return f
		def Init():
			t['Wgt'] 	=	sPol(t['Wgt'], h='E', v='mE')
			def Init():
				t['Mtd']['setObjectName'](f'tree{n}')
				t['Mtd']['setAlternatingRowColors'](True)
				t['Mtd']['setAnimated'](True)
				t['Mtd']['setHeaderHidden'](True)
				t['Mtd']['setColumnCount'](5)
				t['Mtd']['hideColumn'](2)
				t['Mtd']['hideColumn'](3)
				t['Mtd']['hideColumn'](4)
				t['Mtd']['setMinimumHeight'](10)
				t['Mtd']['setAllColumnsShowFocus'](True)
				t['Mtd']['setMinimumHeight'](50)
				t['Mtd']['setContentsMargins'](*m)
				Init()
			return Init
		def Conn():
			c={}
			c['itemClicked']=t['Mtd']['itemClicked'].connect
			return c

		t={}
		t['Wgt'] 		=  	QtWidgets.QTreeWidget()
		t['Arg']		=	Arg()
		t['Mtd']		= Mtd(t)
		t['Data']		=	Data(t)
		t['Fnx']		= Fnx()
		t['Conn']		=	Conn()
		t['Init']		= Init()
		return t

	sFnx={k:v for k,v in locals().items() if isfunction(v)}
	return sFnx

def Layouts():
	B=Make()
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


	sFnx={k:v for k,v in locals().items() if isfunction(v)}
	return sFnx

def Gui():
	g={}

	
QtUi={}
QtUi |= Make()



