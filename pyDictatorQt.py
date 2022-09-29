#!/usr/bin/env python
from PyQt5 import QtCore, QtGui, QtWidgets
import types ,sys
import base64


sPols 			= 	{
	'P' 			: QtWidgets.QSizePolicy.Preferred,
	'M' 			: QtWidgets.QSizePolicy.Maximum,
	'm' 			: QtWidgets.QSizePolicy.Minimum,
	'E'				:	QtWidgets.QSizePolicy.Expanding,
	'mE'			:	QtWidgets.QSizePolicy.MinimumExpanding,
	'F'				:	QtWidgets.QSizePolicy.Fixed,
	}
ico					=		{
	'Search'  : [ b'PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXciIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KIDxwYXRoIGQ9Im02LjUgMWMzLjAzNzYgMCA1LjUgMi40NjI0IDUuNSA1LjUgMCAxLjMzODgtMC40NzgzIDIuNTY1OS0xLjI3MzQgMy41MTk2bDQuMTI3IDQuMTI2OGMwLjE5NTIgMC4xOTUzIDAuMTk1MiAwLjUxMTkgMCAwLjcwNzItMC4xNzM2IDAuMTczNS0wLjQ0MyAwLjE5MjgtMC42Mzc5IDAuMDU3OGwtMC4wNjkzLTAuMDU3OC00LjEyNjgtNC4xMjdjLTAuOTUzNyAwLjc5NTEtMi4xODA4IDEuMjczNC0zLjUxOTYgMS4yNzM0LTMuMDM3NiAwLTUuNS0yLjQ2MjQtNS41LTUuNSAwLTMuMDM3NiAyLjQ2MjQtNS41IDUuNS01LjV6bTAgMWMtMi40ODUzIDAtNC41IDIuMDE0Ny00LjUgNC41IDAgMi40ODUzIDIuMDE0NyA0LjUgNC41IDQuNSAyLjQ4NTMgMCA0LjUtMi4wMTQ3IDQuNS00LjUgMC0yLjQ4NTMtMi4wMTQ3LTQuNS00LjUtNC41eiIgZmlsbD0iIzM2MzYzNiIvPgo8L3N2Zz4K' ,
								b'PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXciIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KIDxwYXRoIGQ9Im02LjUgMWMzLjAzNzYgMCA1LjUgMi40NjI0IDUuNSA1LjUgMCAxLjMzODgtMC40NzgzIDIuNTY1OS0xLjI3MzQgMy41MTk2bDQuMTI3IDQuMTI2OGMwLjE5NTIgMC4xOTUzIDAuMTk1MiAwLjUxMTkgMCAwLjcwNzItMC4xNzM2IDAuMTczNS0wLjQ0MyAwLjE5MjgtMC42Mzc5IDAuMDU3OGwtMC4wNjkzLTAuMDU3OC00LjEyNjgtNC4xMjdjLTAuOTUzNyAwLjc5NTEtMi4xODA4IDEuMjczNC0zLjUxOTYgMS4yNzM0LTMuMDM3NiAwLTUuNS0yLjQ2MjQtNS41LTUuNSAwLTMuMDM3NiAyLjQ2MjQtNS41IDUuNS01LjV6bTAgMWMtMi40ODUzIDAtNC41IDIuMDE0Ny00LjUgNC41IDAgMi40ODUzIDIuMDE0NyA0LjUgNC41IDQuNSAyLjQ4NTMgMCA0LjUtMi4wMTQ3IDQuNS00LjUgMC0yLjQ4NTMtMi4wMTQ3LTQuNS00LjUtNC41eiIgZmlsbD0iI2RlZGVkZSIvPgo8L3N2Zz4K'] ,
	'Next'    :	[ b'PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZlcnNpb249IjEuMSI+CiA8ZGVmcz4KICA8c3R5bGUgaWQ9ImN1cnJlbnQtY29sb3Itc2NoZW1lIiB0eXBlPSJ0ZXh0L2NzcyI+LkNvbG9yU2NoZW1lLVRleHQgeyBjb2xvcjojMzYzNjM2OyB9PC9zdHlsZT4KIDwvZGVmcz4KIDxwYXRoIGNsYXNzPSJDb2xvclNjaGVtZS1UZXh0IiBkPSJNIDQuNjM2NywxLjYzNjcgMTEsOCA0LjYzNjcsMTQuMzYzMyAzLjkyOTY3LDEzLjY1NjI3IDkuNTg1ODcsOC4wMDAwNyAzLjkyOTY3LDIuMzQzODcgNC42MzY3LDEuNjM2ODQgWiIgZmlsbD0iY3VycmVudENvbG9yIi8+Cjwvc3ZnPgo=' ,
								b'PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZlcnNpb249IjEuMSI+CiA8ZGVmcz4KICA8c3R5bGUgaWQ9ImN1cnJlbnQtY29sb3Itc2NoZW1lIiB0eXBlPSJ0ZXh0L2NzcyI+LkNvbG9yU2NoZW1lLVRleHQgeyBjb2xvcjojZGVkZWRlOyB9PC9zdHlsZT4KIDwvZGVmcz4KIDxwYXRoIGNsYXNzPSJDb2xvclNjaGVtZS1UZXh0IiBkPSJNIDQuNjM2NywxLjYzNjcgMTEsOCA0LjYzNjcsMTQuMzYzMyAzLjkyOTY3LDEzLjY1NjI3IDkuNTg1ODcsOC4wMDAwNyAzLjkyOTY3LDIuMzQzODcgNC42MzY3LDEuNjM2ODQgWiIgZmlsbD0iY3VycmVudENvbG9yIi8+Cjwvc3ZnPgo='],
	'Prev'    :	[ b'PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZlcnNpb249IjEuMSI+CiA8ZGVmcz4KICA8c3R5bGUgaWQ9ImN1cnJlbnQtY29sb3Itc2NoZW1lIiB0eXBlPSJ0ZXh0L2NzcyI+LkNvbG9yU2NoZW1lLVRleHQgeyBjb2xvcjojMzYzNjM2OyB9PC9zdHlsZT4KIDwvZGVmcz4KIDxwYXRoIGQ9Im0xMC4zNjMgMS42MzY3LTYuMzYzMyA2LjM2MzMgNi4zNjMzIDYuMzYzMyAwLjcwNzAzLTAuNzA3MDMtNS42NTYyLTUuNjU2MiA1LjY1NjItNS42NTYyLTAuNzA3MDMtMC43MDcwM3oiIGNsYXNzPSJDb2xvclNjaGVtZS1UZXh0IiBzdHlsZT0iZmlsbDpjdXJyZW50Q29sb3IiLz4KPC9zdmc+Cg==',
								b'PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZlcnNpb249IjEuMSI+CiA8ZGVmcz4KICA8c3R5bGUgaWQ9ImN1cnJlbnQtY29sb3Itc2NoZW1lIiB0eXBlPSJ0ZXh0L2NzcyI+LkNvbG9yU2NoZW1lLVRleHQgeyBjb2xvcjojZGVkZWRlOyB9PC9zdHlsZT4KIDwvZGVmcz4KIDxwYXRoIGQ9Im0xMC4zNjMgMS42MzY3LTYuMzYzMyA2LjM2MzMgNi4zNjMzIDYuMzYzMyAwLjcwNzAzLTAuNzA3MDMtNS42NTYyLTUuNjU2MiA1LjY1NjItNS42NTYyLTAuNzA3MDMtMC43MDcwM3oiIGNsYXNzPSJDb2xvclNjaGVtZS1UZXh0IiBzdHlsZT0iZmlsbDpjdXJyZW50Q29sb3IiLz4KPC9zdmc+Cg=='],
	'Inc'     : [ b'PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXciIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KIDxyZWN0IHg9IjIiIHk9IjciIHdpZHRoPSIxMSIgaGVpZ2h0PSIxIiBmaWxsPSIjMzYzNjM2Ii8+Cjwvc3ZnPgo=',
								b'PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXciIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KIDxyZWN0IHg9IjIiIHk9IjciIHdpZHRoPSIxMSIgaGVpZ2h0PSIxIiBmaWxsPSIjZGVkZWRlIi8+CiA8cmVjdCB0cmFuc2Zvcm09InJvdGF0ZSg5MCkiIHg9IjIiIHk9Ii04IiB3aWR0aD0iMTEiIGhlaWdodD0iMSIgZmlsbD0iI2RlZGVkZSIvPgo8L3N2Zz4K'],
	'Dec'     :	[ b'PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXciIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KIDxwYXRoIGQ9Im0zIDhoMTB2MWgtMTB6IiBjb2xvcj0iIzM2MzYzNiIgZmlsbD0iIzM2MzYzNiIgb3ZlcmZsb3c9InZpc2libGUiIHN0cm9rZS13aWR0aD0iLjcwNzExIi8+Cjwvc3ZnPgo=',
								b'PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXciIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KIDxwYXRoIGQ9Im0zIDhoMTB2MWgtMTB6IiBjb2xvcj0iI2RlZGVkZSIgZmlsbD0iI2RlZGVkZSIgb3ZlcmZsb3c9InZpc2libGUiIHN0cm9rZS13aWR0aD0iLjcwNzExIi8+Cjwvc3ZnPgo='],
	'Edit'    :	[ b'PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KIDxwYXRoIGQ9Im0xMi4yMzggMS0wLjM1MyAwLjM2LTguOTY5IDkuMDk1LTAuMDMgMC4wNDVjLTAuMDYxIDAuMDk5LTAuMjcgMC40NS0wLjU4MyAxLjA4OC0wLjMxNCAwLjYzOC0wLjcgMS41MS0xLjAxMiAyLjQ5MmwtMC4yOTEgMC45MiAwLjkyLTAuMjkxYTE4LjE2MyAxOC4xNjMgMCAwIDAgMi40OTItMS4wMTJjMC42MzgtMC4zMTQgMC45ODctMC41MiAxLjA4OC0wLjU4NGwwLjA0NS0wLjAyOSA5LjQ1NS05LjMyMnptLTguMzQ3IDkuODkgMS4yMTggMS4yMi0wLjE3NyAwLjE3NWM3ZS0zIC01ZS0zIC0wLjM3OSAwLjIyNy0wLjk2MSAwLjUxNC0wLjIxNCAwLjEwNS0wLjUzNiAwLjIyMi0wLjgzNCAwLjMzOGwtMC4yNzQtMC4yNzRjMC4xMTYtMC4yOTggMC4yMzMtMC42MiAwLjMzOC0wLjgzNCAwLjI4Ny0wLjU4MiAwLjUxOC0wLjk2NiAwLjUxNC0wLjk2eiIgZmlsbD0iIzM2MzYzNiIgZm9udC1zaXplPSIxNSIgbGV0dGVyLXNwYWNpbmc9IjAiIHdvcmQtc3BhY2luZz0iMCIvPgo8L3N2Zz4K',
								b'PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KIDxwYXRoIGQ9Im0xMi4yMzggMS0wLjM1MyAwLjM2LTguOTY5IDkuMDk1LTAuMDMgMC4wNDVjLTAuMDYxIDAuMDk5LTAuMjcgMC40NS0wLjU4MyAxLjA4OC0wLjMxNCAwLjYzOC0wLjcgMS41MS0xLjAxMiAyLjQ5MmwtMC4yOTEgMC45MiAwLjkyLTAuMjkxYTE4LjE2MyAxOC4xNjMgMCAwIDAgMi40OTItMS4wMTJjMC42MzgtMC4zMTQgMC45ODctMC41MiAxLjA4OC0wLjU4NGwwLjA0NS0wLjAyOSA5LjQ1NS05LjMyMnptLTguMzQ3IDkuODkgMS4yMTggMS4yMi0wLjE3NyAwLjE3NWM3ZS0zIC01ZS0zIC0wLjM3OSAwLjIyNy0wLjk2MSAwLjUxNC0wLjIxNCAwLjEwNS0wLjUzNiAwLjIyMi0wLjgzNCAwLjMzOGwtMC4yNzQtMC4yNzRjMC4xMTYtMC4yOTggMC4yMzMtMC42MiAwLjMzOC0wLjgzNCAwLjI4Ny0wLjU4MiAwLjUxOC0wLjk2NiAwLjUxNC0wLjk2eiIgZmlsbD0iI2RlZGVkZSIgZm9udC1zaXplPSIxNSIgbGV0dGVyLXNwYWNpbmc9IjAiIHdvcmQtc3BhY2luZz0iMCIvPgo8L3N2Zz4K'],
	'Copy'    : [ b'PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXciIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KIDxwYXRoIGQ9Im02IDBjLTEuMTA0NiAwLTIgMC44OTU0My0yIDJ2MTBjMCAxLjEwNDYgMC44OTU0MyAyIDIgMmg2YzEuMTA0NiAwIDItMC44OTU0IDItMnYtMTBjMC0xLjEwNDYtMC44OTU0LTItMi0yem0tMSAyYzAtMC41NTIyOCAwLjQ0NzcyLTEgMS0xaDZjMC41NTIzIDAgMSAwLjQ0NzcyIDEgMXYxMGMwIDAuNTUyMy0wLjQ0NzcgMS0xIDFoLTZjLTAuNTUyMjggMC0xLTAuNDQ3Ny0xLTF6bS0zIDJjMC0wLjc0MDI4IDAuNDAyMi0xLjM4NjYgMS0xLjczMjR2MTAuMjMyYzAgMS4zODA3IDEuMTE5MyAyLjUgMi41IDIuNWg2LjIzMjRjLTAuMzQ1OCAwLjU5NzgtMC45OTIxIDEtMS43MzI0IDFoLTQuNWMtMS45MzMgMC0zLjUtMS41NjctMy41LTMuNXoiIGZpbGw9IiMzNjM2MzYiLz4KPC9zdmc+Cg==',
								b'PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXciIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KIDxwYXRoIGQ9Im02IDBjLTEuMTA0NiAwLTIgMC44OTU0My0yIDJ2MTBjMCAxLjEwNDYgMC44OTU0MyAyIDIgMmg2YzEuMTA0NiAwIDItMC44OTU0IDItMnYtMTBjMC0xLjEwNDYtMC44OTU0LTItMi0yem0tMSAyYzAtMC41NTIyOCAwLjQ0NzcyLTEgMS0xaDZjMC41NTIzIDAgMSAwLjQ0NzcyIDEgMXYxMGMwIDAuNTUyMy0wLjQ0NzcgMS0xIDFoLTZjLTAuNTUyMjggMC0xLTAuNDQ3Ny0xLTF6bS0zIDJjMC0wLjc0MDI4IDAuNDAyMi0xLjM4NjYgMS0xLjczMjR2MTAuMjMyYzAgMS4zODA3IDEuMTE5MyAyLjUgMi41IDIuNWg2LjIzMjRjLTAuMzQ1OCAwLjU5NzgtMC45OTIxIDEtMS43MzI0IDFoLTQuNWMtMS45MzMgMC0zLjUtMS41NjctMy41LTMuNXoiIGZpbGw9IiNkZWRlZGUiLz4KPC9zdmc+Cg=='],
	}
lays				=		{
	'H' 			:	QtWidgets.QHBoxLayout,
	'V' 			: QtWidgets.QVBoxLayout,
	'G' 			:	QtWidgets.QGridLayout,
	'F' 			:	QtWidgets.QFormLayout,
					}

def QtBlocks():
	def Elements():
		def Wgt(**k):
			def widget():
				wgt = QtWidgets.QWidget()
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
			margin	=	k.get('mrg') or [0,0,0,0]
			wgt			=	widget()
			wgt			=	layout() if Layout else wgt
			return wgt

		def Spcr(**k):
			w=k.get('w')
			h=k.get('h')
			hpol,vpol=k.get('t')
			wgt=QtWidgets.QSpacerItem(w, h, sPols[hpol], sPols[vpol])
			return wgt

		def iBtn(n,bi=False, h=20, w=20):
			def make_icon(n=None):
				with open('iconl.svg','wb') as l:
					l.write(base64.b64decode(ico[n][0]))
				with open('icond.svg','wb') as d:
					d.write(base64.b64decode(ico[n][1]))

				icon = QtGui.QIcon()
				icon.addPixmap(QtGui.QPixmap('iconl.svg'), QtGui.QIcon.Normal, QtGui.QIcon.On)
				icon.addPixmap(QtGui.QPixmap('icond.svg'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
				return icon
			btn = QtWidgets.QToolButton()
			btn.setObjectName(f'iBtn{n}')
			btn.setIcon(make_icon(n))
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
			lbl=  blk.Layouts.sPol(lbl, h='P', v='P')
			return lbl
		def ledit(n,ro=False):
			txt = QtWidgets.QLineEdit()
			txt.setObjectName(f'txt{n}')
			txt.setReadOnly(ro)
			txt=blk.Layouts.sPol(txt, h='E', v='P')
			return txt
		def Tree(**k):
			def create():
				wgt	=	QtWidgets.QTreeWidget()
				wgt.setObjectName(name)
				return wgt
			def init(wgt):
				wgt = blk.Layouts.sPol(wgt, h='E', v='mE')
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
			margins=k.get('mrg') or [0,0,0,0]
			wgt	= create()
			wgt	= init(wgt)
			return wgt

		Elmt = types.SimpleNamespace()
		Elmt.Wgt			= Wgt
		Elmt.Spcr			=	Spcr
		Elmt.iBtn			=	iBtn
		Elmt.tBtn			=	tBtn
		Elmt.lbl			=	lbl
		Elmt.ledit		=	ledit
		Elmt.Tree			= Tree
		return Elmt
	def Layouts():
		def sPol(wgt, h=None, v=None):
			Pol = QtWidgets.QSizePolicy(sPols[h], sPols[v])
			wgt.setSizePolicy(Pol)
			return wgt
		def siblings(wgts, t, margin=[0,0,0,0]):
			wgt,lay=	 blk.Elements.Wgt(t=t)
			wgt.setContentsMargins(*margin)
			for item in wgts:
				lay.addWidget(item)
			return wgt
		def center(child,	**k):
			w = k.get('w') or 0
			mrg = k.get('mrg') or [w,0,w,0]
			lSpcFix= blk.Elements.SpcFix(w=w)
			rSpcFix= blk.Elements.SpcFix(w=w)
			wgt,lay= blk.Elements.Wgt(t='h')
			lay.addWidget(lSpcFix)
			lay.addWidget(child)
			lay.addWidget(rSpcFix)
			wgt.setContentsMargins(*mrg)
			return wgt
		Lay 					= types.SimpleNamespace()
		Lay.sPol 			= sPol
		Lay.siblings 	= siblings
		Lay.center		= center
		return Lay
	def Widgets():
		def SpcFix(**k):
			wgt,lay=Wgt(t='h')
			w			=	k.get('w')	or 0
			h			=	k.get('h')	or 0
			hPol 	= 'F' if k.get('w') else 'P'
			vPol	=	'F'	if k.get('h') else 'P'
			wgt.SpcFix = blk.Elements.Spcr(	w=w, h=h, t=[hPol,vPol])
			lay.addItem(wgt.SpcFix)
			wgt.setContentsMargins(0,0,0,0)
			lay.setContentsMargins(0,0,0,0)
			return wgt
		def SpcEx(**k):
			w=k.get('w')
			h=k.get('h')
			t=k.get('t') or 'h'
			wgt,lay=Wgt(t=t)
			pol= ['F','P'] * (t == 'h') + ['P','F'] *  (t == 'v')
			width= 0 * (t == 'v') + w *(t == 'h')
			wgt.SpcFix = blk.Elements.Spcr(w=w, h=h, t=pol)
			wgt.setContentsMargins(0,0,0,0)
			lay.setContentsMargins(0,0,0,0)
			lay.addItem(wgt.SpcFix)
		def Tree(*a,**k):
			def create(wgt):
				wgt.Tree 		= blk.Elements.Tree(n='Tree',mrg=margin)
				return wgt
			def layout(wgt):
				wgt =blk.Layouts.sPol(wgt, h='E', v='mE')
				wgt.Tree.setContentsMargins(*margin)
				wgt.setContentsMargins(*margin)
				return wgt
			def add(wgt,lay):
				lay.addWidget(wgt.Tree)
				return lay
			def fnx(wgt):
				def resizeCols(wgt):
					def resizeCols():
						wgt.Tree.expandAll()
						wgt.Tree.resizeColumnToContents(0)
						wgt.Tree.resizeColumnToContents(1)
						wgt.Tree.collapseAll()
					return resizeCols
				def colWidth(wgt):
					def colWidth():
						w1 = wgt.Tree.columnWidth(0)
						w2 = wgt.Tree.columnWidth(1)
						return [w1,w2]
					return colWidth
				def setColWidth(wgt):
					def setColWidth(col,rel=None,tot=None):
						if rel:
							w=wgt.Tree.columnWidth(col)
							w =	w + rel
						else:
							w	=	tot
						wgt.Tree.setColumnWidth(col,w)
					return setColWidth
				wgt.fittCols 		= resizeCols(wgt)
				wgt.colWidth		=	colWidth(wgt)
				wgt.setColWidth = setColWidth(wgt)
				return wgt
			def conn(wgt):
				wgt.Selected=wgt.Tree.itemClicked.connect
				wgt.FoundSel	=	wgt.Tree.itemSelectionChanged.connect
				return wgt
			name=k.get('n') or 'wgtTree'
			margin=k.get('mrg') or  [0,0,0,0]
			wgt,lay =	blk.Elements.Wgt(n=name,t='h')
			wgt=create(wgt)
			wgt=layout(wgt)
			lay=add(wgt,lay)
			wgt=fnx(wgt)
			wgt=conn(wgt)
			return wgt
		def IncDec(**k):
			def create(wgt):
				wgt.btnExp 		= blk.Elements.iBtn('Inc',h=15,w=15)
				wgt.btnCol 		= blk.Elements.iBtn('Dec',h=15,w=15)
				return wgt
			def layout(wgt):
				wgt = blk.Layouts.sPol(wgt, h='P', v='P')
				wgt.setContentsMargins(*margin)
				return wgt
			def add(wgt,lay):
				lay.addWidget(wgt.btnExp)
				lay.addWidget(wgt.btnCol)
				return lay
			def conn(wgt):
				wgt.fnI=wgt.btnExp.clicked.connect
				wgt.fnD=wgt.btnCol.clicked.connect
				return wgt

			margin=k.get('mrg') or [5,0,5,0]
			wgt,lay =	 blk.Elements.Wgt(n='wgtIncDec',t='h')
			wgt=create(wgt)
			lay=add(wgt,lay)
			wgt=layout(wgt)
			wgt=conn(wgt)
			wgt.setContentsMargins(*margin)
			return wgt
		def Search():
			def createElements(wgt):
				wgt.btnNext 			= Elmt.iBtn('Next', w=12)
				wgt.btnPrev 			= Elmt.iBtn('Prev', w=12)
				wgt.btnSearch 		= Elmt.iBtn('Search')
				wgt.txt 					=	Elmt.ledit('Search')
				wgt.wgtPN 				= blk.Layouts.siblings([wgt.btnPrev,wgt.btnNext],t='h',margin=[0,0,0,0])
				wgt.wgtCtl			 	= blk.Layouts.siblings([wgt.wgtPN,wgt.btnSearch],t='h',margin=[0,0,0,0])
				wgt.wgtSearch			= blk.Layouts.siblings([wgt.txt,wgt.wgtCtl],t='h',margin=[0,0,5,0])
				return wgt
			def addElements(wgt,lay):
				lay.addWidget(wgt.wgtSearch)
			def init(wgt):
				wgt.btnPrev.setHidden(True)
				wgt.btnNext.setHidden(True)
				wgt	= blk.Layouts.sPol(wgt, h='E', v='F')
				wgt.Found = None
				return wgt
			def fnx(wgt):
				def dispPN(wgt):
					def dispPN(show):
						wgt.btnPrev.setHidden(not show)
						wgt.btnNext.setHidden(not show)
					return dispPN
				def selNext(Tree):
					def sel():
						item=wgt.Found.pop(0)
						Tree.setCurrentItem(wgt.Found[0])
						wgt.Found.append(item)
					return sel
				def selPrev(Tree):
					def sel():
						item=wgt.Found.pop(-1)
						Tree.setCurrentItem(item)
						wgt.Found=[item,*wgt.Found]
					return sel

				wgt.showPN 	= dispPN(wgt)
				wgt.selNext		=	selNext
				wgt.selPrev		=	selPrev
				return wgt
			def conn(wgt):
				wgt.Find		=	wgt.btnSearch.clicked.connect
				wgt.Next		= wgt.btnNext.clicked.connect
				wgt.Prev		=	wgt.btnPrev.clicked.connect
				return wgt
			Elmt=Elements()
			wgt,lay = Elmt.Wgt(n='Search',t='h')
			wgt = createElements(wgt)
			lay = addElements(wgt,lay)
			wgt = init(wgt)
			wgt =	fnx(wgt)
			wgt	= conn(wgt)
			return wgt
		def Path():
			def create(wgt):
				wgt.txt 		= Elmt.ledit(n='Path',ro=True)
				wgt.btnCopy = Elmt.iBtn('Copy')
				return wgt
			def add(wgt,lay):
				lay.addWidget(wgt.txt)
				lay.addWidget(wgt.btnCopy)
				return lay
			def conn(wgt):
				wgt.Copy=wgt.btnCopy.clicked.connect
				return wgt
			Elmt = Elements()
			wgt,lay = Elmt.Wgt(n='Path',t='h')
			wgt = create(wgt)
			lay = add(wgt,lay)
			wgt = conn(wgt)
			return wgt
		def EditProp(n,fnSet):
			def createElements(wgt):
				wgt.lbl 		= QtElmt.lbl(f'{n}:')
				wgt.txt 		= QtElmt.ledit(n,ro=True)
				wgt.txtdup	= QtElmt.ledit(n,ro=True)
				wgt.btnSet 	= QtElmt.tBtn('Set')
				wgt.btnEdit =	QtElmt.iBtn('Edit', bi=True)
				return wgt
			def addElements(wgt,lay):
				lay.addWidget(wgt.lbl)
				lay.addWidget(wgt.txt)
				lay.addWidget(wgt.txtdup)
				lay.addWidget(wgt.btnSet)
				lay.addWidget(wgt.btnEdit)
				return lay
			def init(wgt):
				wgt.btnSet.setHidden(True)
				wgt.txt.setReadOnly(True)
				wgt.txtdup.setHidden(True)
				wgt	= blk.Layouts.sPol(wgt, h='E', v='F')
				return wgt
			def fnx(wgt):
				def txtText(wgt):
					def txtText(text):
						wgt.txt.setText(text)
						wgt.txtdup.setText(text)
					return txtText
				def setText(wgt):
					def setText():
						nText=  wgt.txt.text()
						wgt.txtdup.setText(nText)
						wgt.btnEdit.setChecked(False)
						wgt.btnSet.setHidden(True)
						fnSet(nText)
					return setText
				def edit(wgt):
					def edit(state):
						wgt.btnEdit.setChecked(state)
						wgt.txt.setReadOnly(not state)
						wgt.btnSet.setHidden(not state)
						if not state:
							wgt.txt.setText(wgt.txtdup.text())
					return edit
				wgt.Edit 		= edit(wgt)
				wgt.txtText = txtText(wgt)
				wgt.setText	= setText(wgt)
				return wgt
			def conn(wgt):
				wgt.btnEdit.clicked.connect(wgt.Edit)
				wgt.btnSet.clicked.connect(wgt.setText)
				wgt.txt.returnPressed.connect(wgt.setText)
				return wgt
			QtElmt=Elements()
			wgt,lay =	QtElmt.Wgt(n=n,t='h')
			wgt 		= createElements(wgt)
			lay 		= addElements(wgt,lay)
			wgt			=	init(wgt)
			wgt 		= fnx(wgt)
			wgt			=	conn(wgt)
			return wgt
		def AppCtl(**k):
			def createElements(wgt):
				wgt.hSpc			=	QtElmt.SpcEx()
				wgt.btnExit		=	QtElmt.tBtn('Exit')
				wgt.btnSave		=	QtElmt.tBtn('Save As')
				wgt.btnPrint	=	QtElmt.tBtn('Print')
				return wgt
			def addElements(wgt,lay):
				lay.addWidget(wgt.btnPrint)
				lay.addWidget(wgt.btnSave)
				lay.addWidget(wgt.hSpc)
				lay.addWidget(wgt.btnExit)
				return lay
			def init(wgt):
				wgt.setContentsMargins(*wgt.mrg)
				wgt= blk.Layouts.sPol(wgt,h='E',v='P')
				return wgt
			def fnx(wgt):
				wgt.mrg=k.get('mrg') or [0,0,0,0]
				return wgt
			def conn(wgt):
				wgt.fnPrint=wgt.btnPrint.clicked.connect
				wgt.fnSave=wgt.btnSave.clicked.connect
				return wgt
			QtElmt = Elements()
			wgt,lay = QtElmt.Wgt(n='wgtAppCtl',t='h')
			wgt=createElements(wgt)
			lay=addElements(wgt,lay)
			wgt=fnx(wgt)
			wgt=init(wgt)
			wgt=conn(wgt)
			return wgt
		Wgt = types.SimpleNamespace()
		Wgt.Tree			=	Tree
		Wgt.Search		= Search
		Wgt.Path			=	Path
		Wgt.IncDec		=	IncDec
		Wgt.EditProp	= EditProp
		Wgt.AppCtl		=	AppCtl
		return Wgt
	blk = types.SimpleNamespace()
	blk.Elements	=	Elements()
	blk.Layouts		=	Layouts()
	blk.Widgets		=	Widgets()
	return blk


def construct_Qt5Ui(data):

	def QtApp():
		app 				= types.SimpleNamespace()
		app.QtWin 	= QtWidgets.QApplication(sys.argv)
		app.Blocks		= QtBlocks()
		return app

	def Fnx(App):
		def search(App):
			# def find():
			# 	found=App.Main.Tree.Tree.findChild(str, App.Main.Search.txt.text(), QtCore.Qt.MatchFlag.MatchRecursive)
			# 	found2=App.Main.Tree.Tree.findChild(str , App.Main.Search.txt.text(), QtCore.Qt.MatchFlag.MatchContains)
			# 	print(App.Main.Search.txt.text(),found,found2)
			# return find
			def  searchTree():
				searchStr= App.Main.Search.txt.text()
				Opts =  (QtCore.Qt.MatchRecursive|QtCore.Qt.MatchRegExp|QtCore.Qt.CaseInsensitive)
				findkeys	=	App.Main.Tree.Tree.findItems(searchStr,Opts, 0)
				findvals	=	App.Main.Tree.Tree.findItems(searchStr,Opts, 1)
				find			=	[*findkeys,*findvals]
				if len(find) > 1 :
					App.Main.Search.showPN(True)
					App.Main.Tree.Tree.setCurrentItem(find[0])
				elif len(find) == 1 :
					App.Main.Search.showPN(False)
					App.Main.Tree.Tree.setCurrentItem(find[0])
				else:
					App.Main.Search.showPN(False)
				App.Main.Search.Found=find
			return searchTree

		def searchSel(App):
			def searchSel():
				App.Main.Tree.Tree.currentItemChanged.connect(App.Fnx.OnSelect)
			return searchSel

		def select(*a,**k):
			Key=k.get('Key')
			Val=k.get('Val')
			Path=k.get('Path')
			txtBox = [Key.txt, Val.txt, Path.txt ]
			def select(data):
				for idx, txtbox in zip([0, 3, 2], txtBox):
					txtbox.setText(data.text(idx))
			return select

		def copytoclip(txt):
			def toclip():
				App.Clip.setText(txt.text())
			return toclip

		def allign(gui):
			maxwidth=max(gui.Main.Key.lbl.width(),gui.Main.Val.lbl.width())
			gui.Main.Key.lbl.setMinimumWidth(maxwidth)
			gui.Main.Val.lbl.setMinimumWidth(maxwidth)
			App.Allign 	=	allign
			App.Select 	=	select
			return App

		def make_tree(App, branches=[], **k):
			keylist=[]
			def make_branch(root, dct, path ,keylist=keylist):
				for key in dct:
					data = dct[key]
					keylist+=[key]
					dictpath = f"{path}['{key}']"
					branch = QtWidgets.QTreeWidgetItem()
					branch.setText(0, str(key))
					branch.setText(2, dictpath)
					keystr=''.join([f"['{key}']" for key in keylist])
					branch.setText(4,keystr)
					if isinstance(data, dict):
						make_branch(branch, data, dictpath,keylist=keylist)
					else:

						data = str(data)
						w = App.Main.Tree.Tree.columnWidth(1)
						data = repr(data) if callable(data) else data
						dispdata = f'{data[0:w - 4]}...' if len(data) > w - 4 else data
						branch.setText(1, dispdata)
						branch.setText(3, data)
					keylist.pop(-1)

					root.addChild(branch)
			name = k['name']
			data = k['data']
			root = QtWidgets.QTreeWidgetItem()
			root.setText(0, name)
			root.setText(2, name)
			make_branch(root, data, name)
			return root

		def stdf(base,**k):
			def Dct(*a,**k):
				with open(file , 'a') as f:
					dct = k.get('dct') or base
					ident = k.get('ident') or 3
					def testkey(content, ident):
						if isinstance(dct[key], dict):
							tabs = ident * '\t'
							f.write(tabs)

							f.write(f"'{key}'\t:\t")
							f.write('{\n')
							f.flush()
							ident += 2
							Dct(dct=dct[key], ident=ident)
						else:
							# ident -= 1
							tabs = ident * '\t'
							f.write(tabs)
							f.write(f"\t'{key}'")
							f.write('\t:\t')
							f.write(f"'{dct[key]}'\t,")
							f.write('\n')
							f.flush()
					for key in dct:
						testkey(dct[key], ident)
					tabs = ident * '\t'
					f.write(tabs)
					f.write('}\n')

			file=k.get('file')
			with open(file , 'w') as f:
				f.write(f'{k.get("name")}\t=\t')
				f.write('{\n')

			return Dct

		def stdw(base,**k):
			def Tree(*a,**k):
				d = k.get('d') or base
				indent = k.get('indent') or 0
				for key in d:
					if isinstance(d[key], dict):
						sys.stdout.write('  ┃  ' * (indent) + '  ┣━━ ' + '\x1b[1;32m' + str(key) + ':' + '\x1b[0m\n')
						Tree(d=d[key],indent=indent + 1)
					else:
						sys.stdout.write('  ┃  ' * (indent) + '  ┣━━ ' + str(key) + '\t:\t' + str(d[key]) + '\n')
			return Tree

		fnx= types.SimpleNamespace()
		fnx.select 			= select
		fnx.copytoclip  =	copytoclip
		fnx.allign      =	allign
		fnx.makeTree		=	make_tree
		fnx.stdf				=	stdf
		fnx.stdw				= stdw
		fnx.OnSelect		= select(Key=App.Main.Key,Val=App.Main.Val,Path=App.Main.Path)
		fnx.PathToClip	=	copytoclip(App.Main.Path.txt)
		fnx.Searched		=	search(App)
		fnx.Found				=	searchSel(App)
		fnx.stdf 				=	stdf(dct,file='test.txt',name='Test')
		fnx.stdo				=	stdw(dct,name='Test')
		fnx.selNext			= App.Main.Search.selNext(App.Main.Tree.Tree)
		fnx.selPrev			= App.Main.Search.selPrev(App.Main.Tree.Tree)
		return fnx

	def create(App):
		def MainWgt():
			wgt,lay = App.Blocks.Elements.Wgt(n='Qt5',t='v')
			Main=wgt
			Main.lay=lay
			return Main

		def Elements():
			Element				= types.SimpleNamespace()
			Element.Tree			=	App.Blocks.Widgets.Tree()
			Element.Search		= App.Blocks.Widgets.Search()
			Element.ExpCol		=	App.Blocks.Widgets.IncDec()
			Element.Path 			= App.Blocks.Widgets.Path()
			Element.Key 			= App.Blocks.Widgets.EditProp('Key',print)
			Element.Val 			= App.Blocks.Widgets.EditProp('Val',print)
			Element.AppCtl		=	App.Blocks.Widgets.AppCtl()
			return Element

		def Modules():
			Module					= types.SimpleNamespace()
			Module.TreeCtl		=	App.Blocks.Layouts.siblings([Main.Element.ExpCol,Main.Element.Search],t='h')

			Module.WrpPath	=	App.Blocks.Layouts.center(Main.Element.Path,w=5,margin=[0,0,0,5])
			Module.Edit			=	App.Blocks.Layouts.siblings([Main.Element.Key,Main.Element.Val],'v',margin=[25,0,25,5])
			# Module.wrpEdit	=	App.Blocks.Layouts.center(App.Main.Edit,w=25)
			Module.TrDisp		=	App.Blocks.Layouts.siblings([Main.Element.Tree,Module.wgtCtl],t='v')
			Module.Tools		=	App.Blocks.Layouts.siblings([Module.WrpPath,Module.Edit],'v',margin=[0,0,0,5])
			return Module

		def add():
			Main.lay.addWidget(Main.Module.TrDisp)
			Main.lay.addWidget(Main.Module.Tools)
			Main.lay.addWidget(Main.Module.AppCtl)
			return Main.lay
		Main=MainWgt()
		Main.Element	=	Elements()
		Main.Module 	=	Modules()
		Main.Layout		=	add()
		return App.Main

	def conn(App):
		App.Main.ExpCol.fnI(App.Main.Tree.Tree.expandAll)
		App.Main.ExpCol.fnD(App.Main.Tree.Tree.collapseAll)
		App.Main.Tree.Selected(App.Fnx.OnSelect)
		App.Main.Tree.FoundSel(App.Fnx.Found)
		App.Main.AppCtl.fnSave(App.Fnx.stdf)
		App.Main.AppCtl.fnPrint(App.Fnx.stdo)
		App.Main.Path.Copy(App.Fnx.PathToClip)
		App.Main.Search.Find(App.Fnx.Searched)
		App.Main.Search.Next(App.Fnx.selNext)
		App.Main.Search.Prev(App.Fnx.selPrev)
		return App

	App = QtApp()
	App.Main			= create(App)
	App.Fnx				= Fnx(App)
	App.Conn			=	conn(App)
	App.Clip			= App.QtWin.clipboard()
	return App
def browse(**k):
	kv = k.popitem()
	QtApp = construct_Qt5Ui(kv[1])
	trunk = QtApp.Fnx.makeTree(QtApp, name=kv[0], data=kv[1])
	QtApp.Main.Tree.Tree.addTopLevelItem(trunk)
	QtApp.Main.show()
	QtApp.Fnx.allign(QtApp)
	QtApp.Main.Tree.fittCols()
	sys.exit(QtApp.QtWin.exec())







if __name__ == '__main__' :
	dct = {
		'a' : {
						'aa' : 'aa',
						'ab'  : 'ab'

		},
		'b'  : { 'ba' : 'ba',
	            'bb':  {  'bba' : ['bba', 'ccc'],
	                      'bbb' :	'ffff',}
		}}
	browse(test=dct)





Path, Type =QtWidgets.QFileDialog.getSaveFileName(QtWidgets.QWidget(),"Save As","","All Files (*)")





