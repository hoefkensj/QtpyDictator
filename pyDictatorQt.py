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
	'RegEx'		:	[	b'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiI+PHBhdGggZD0iTTEwLjUgMWMtLjI3NyAwLS41LjIyMy0uNS41djEuNzkzTDguNzMyIDIuMDI1YS40OTkuNDk5IDAgMSAwLS43MDcuNzA4TDkuMjkzIDRINy41YS40OTkuNDk5IDAgMSAwIDAgMWgxLjc5M0w4LjAyNSA2LjI2OGEuNDk5LjQ5OSAwIDEgMCAuNzA3LjcwN0wxMCA1LjcwN1Y3LjVhLjQ5OS40OTkgMCAxIDAgMSAwVjUuNzA3bDEuMjY4IDEuMjY4YS40OTkuNDk5IDAgMSAwIC43MDctLjcwN0wxMS43MDcgNUgxMy41YS40OTkuNDk5IDAgMSAwIDAtMWgtMS43OTNsMS4yNjgtMS4yNjhhLjUuNSAwIDAgMC0uNzA3LS43MDdMMTEgMy4yOTNWMS41YzAtLjI3Ny0uMjIzLS41LS41LS41em0tOCAxMWExLjUgMS41IDAgMSAwIDAgMyAxLjUgMS41IDAgMCAwIDAtM3oiIGZpbGw9IiMzNjM2MzYiLz48L3N2Zz4=',
								b'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiI+PHBhdGggZD0iTTEwLjUgMWMtLjI3NyAwLS41LjIyMy0uNS41djEuNzkzTDguNzMyIDIuMDI1YS40OTkuNDk5IDAgMSAwLS43MDcuNzA4TDkuMjkzIDRINy41YS40OTkuNDk5IDAgMSAwIDAgMWgxLjc5M0w4LjAyNSA2LjI2OGEuNDk5LjQ5OSAwIDEgMCAuNzA3LjcwN0wxMCA1LjcwN1Y3LjVhLjQ5OS40OTkgMCAxIDAgMSAwVjUuNzA3bDEuMjY4IDEuMjY4YS40OTkuNDk5IDAgMSAwIC43MDctLjcwN0wxMS43MDcgNUgxMy41YS40OTkuNDk5IDAgMSAwIDAtMWgtMS43OTNsMS4yNjgtMS4yNjhhLjUuNSAwIDAgMC0uNzA3LS43MDdMMTEgMy4yOTNWMS41YzAtLjI3Ny0uMjIzLS41LS41LS41em0tOCAxMWExLjUgMS41IDAgMSAwIDAgMyAxLjUgMS41IDAgMCAwIDAtM3oiIGZpbGw9IiNkZWRlZGUiLz48L3N2Zz4=']
	}
lays				=		{
	'H' 			:	QtWidgets.QHBoxLayout,
	'V' 			: QtWidgets.QVBoxLayout,
	'G' 			:	QtWidgets.QGridLayout,
	'F' 			:	QtWidgets.QFormLayout,
					}

def dummy(*a,**k):	pass

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
			# with open('icond.svg','wb') as d:
			# 	d.write(base64.b64decode(ico[n][1]))
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
			cBox	=	blk.Layouts.sPol(cBox, h='P', v='P')
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
			margins=k.get('margin') or [0,0,0,0]
			wgt	= create()
			wgt	= init(wgt)
			return wgt

		Elmt = types.SimpleNamespace()
		Elmt.Wgt			= Wgt
		Elmt.Spcr			=	Spcr
		Elmt.chkBox		=	chkBox
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
			wgt=	 blk.Elements.Wgt(t=t)
			wgt.setContentsMargins(*margin)
			for item in wgts:
				wgt.lay.addWidget(item)
			return wgt
		def center(child,	**k):
			w = k.get('w') or 0
			margin = k.get('margin') or [w,0,w,0]
			lSpcFix= blk.Widgets.SpcFix(w=w)
			rSpcFix= blk.Widgets.SpcFix(w=w)
			wgt= blk.Elements.Wgt(t='h')
			wgt.lay.addWidget(lSpcFix)
			wgt.lay.addWidget(child)
			wgt.lay.addWidget(rSpcFix)
			wgt.setContentsMargins(*margin)
			return wgt
		Lay 					= types.SimpleNamespace()
		Lay.sPol 			= sPol
		Lay.siblings 	= siblings
		Lay.center		= center
		return Lay
	def Widgets():
		def SpcFix(**k):
			wgt=blk.Elements.Wgt(t='h')
			w			=	k.get('w')	or 0
			h			=	k.get('h')	or 0
			hPol 	= 'F' if k.get('w') else 'P'
			vPol	=	'F'	if k.get('h') else 'P'
			wgt.SpcFix = blk.Elements.Spcr(	w=w, h=h, t=[hPol,vPol])
			wgt.lay.addItem(wgt.SpcFix)
			wgt.setContentsMargins(0,0,0,0)
			wgt.lay.setContentsMargins(0,0,0,0)
			return wgt
		def SpcEx(**k):
			n 	= k.get('n')
			w			=	k.get('w')	or 0
			h			=	k.get('h')	or 0
			hPol 	= 'E' if k.get('w') else 'P'
			vPol	=	'E'	if k.get('h') else 'P'
			def create(wgt):
				wgt.SpcEx = blk.Elements.Spcr(w=w, h=h, t=[hPol,vPol])
				return wgt
			def layout(wgt):
				wgt = blk.Layouts.sPol(wgt, h='P', v='P')
				return wgt
			def add(wgt):
				wgt.lay.addItem(wgt.SpcEx)
				return wgt.lay
			def init(wgt):
				wgt.setContentsMargins(0,0,0,0)
				wgt.lay.setContentsMargins(0,0,0,0)
				return wgt

			wgt = blk.Elements.Wgt(n=f'wgtSpcEx{n}',t='h')
			wgt=create(wgt)
			wgt=layout(wgt)
			wgt.lay=add(wgt)

			return wgt
		def chkRE(**k):
			def create(wgt):
				wgt.chkRE 		= blk.Elements.chkBox('RE',h=15,w=15)
				return wgt
			def layout(wgt):
				wgt = blk.Layouts.sPol(wgt, h='P', v='P')
				wgt.setContentsMargins(*margin)
				return wgt
			def add(wgt,lay):
				lay.addWidget(wgt.chkRE)
				return lay
			def conn(wgt):
				return wgt

			margin=k.get('margin') or [5,0,0,0]
			wgt =	 blk.Elements.Wgt(n='wgtRE',t='h')
			wgt=create(wgt)
			wgt.lay=add(wgt,wgt.lay)
			wgt=layout(wgt)
			wgt=conn(wgt)
			wgt.setContentsMargins(*margin)
			return wgt
		def Tree(*a,**k):
			def create(wgt):
				wgt.Tree 		= blk.Elements.Tree(n='Tree',margin=margin)
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
			margin=k.get('margin') or  [0,0,0,0]
			wgt =	blk.Elements.Wgt(n=name,t='h')
			wgt=create(wgt)
			wgt=layout(wgt)
			wgt.lay=add(wgt,wgt.lay)
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

			margin=k.get('margin') or [5,0,5,0]
			wgt =	 blk.Elements.Wgt(n='wgtIncDec',t='h')
			wgt=create(wgt)
			wgt.lay=add(wgt,wgt.lay)
			wgt=layout(wgt)
			wgt=conn(wgt)
			wgt.setContentsMargins(*margin)
			return wgt
		def Search():
			def create(wgt):
				wgt.btnNext 			= blk.Elements.iBtn('Next', w=12)
				wgt.btnPrev 			= blk.Elements.iBtn('Prev', w=12)
				wgt.btnSearch 		= blk.Elements.iBtn('Search')
				wgt.chkRegEx			=	Wgt.chkRE()
				wgt.txt 					=	blk.Elements.ledit('Search')
				wgt.wgtPN 				= blk.Layouts.siblings([wgt.btnPrev,wgt.btnNext],t='h',margin=[0,0,0,0])
				wgt.wgtCtl			 	= blk.Layouts.siblings([wgt.wgtPN,wgt.btnSearch],t='h',margin=[0,0,0,0])

				wgt.wgtSearch			= blk.Layouts.siblings([wgt.chkRegEx,wgt.txt,wgt.wgtCtl,],t='h',margin=[0,0,0,0])
				return wgt
			def add(wgt,lay):
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
			wgt = blk.Elements.Wgt(n='Search',t='h')
			wgt = create(wgt)
			wgt.lay = add(wgt,wgt.lay)
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
			wgt = Elmt.Wgt(n='Path',t='h')
			wgt = create(wgt)
			wgt.lay = add(wgt,wgt.lay)
			wgt = conn(wgt)
			return wgt
		def EditProp(n,**k):
			fnSet=k.get('fnset') or dummy
			def create(wgt):
				wgt.lbl 		= blk.Elements.lbl(f'{n}:')
				wgt.txt 		= blk.Elements.ledit(n,ro=True)
				wgt.txtdup	= blk.Elements.ledit(n,ro=True)
				wgt.btnSet 	= blk.Elements.tBtn('Set')
				wgt.btnEdit =	blk.Elements.iBtn('Edit', bi=True)
				return wgt
			def add(wgt):
				wgt.lay.addWidget(wgt.lbl)
				wgt.lay.addWidget(wgt.txt)
				wgt.lay.addWidget(wgt.txtdup)
				wgt.lay.addWidget(wgt.btnSet)
				wgt.lay.addWidget(wgt.btnEdit)
				return wgt.lay
			def init(wgt):
				wgt.btnSet.setHidden(True)
				wgt.txt.setReadOnly(True)
				wgt.txtdup.setHidden(True)
				wgt.Editable(not k.get('ed'))
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
				def editable(wgt):
					def editable(state):
						wgt.btnEdit.setHidden(state)
					return editable
				wgt.Edit 		= edit(wgt)
				wgt.txtText = txtText(wgt)
				wgt.setText	= setText(wgt)
				wgt.Editable = editable(wgt)
				return wgt
			def conn(wgt):
				wgt.btnEdit.clicked.connect(wgt.Edit)
				wgt.btnSet.clicked.connect(wgt.setText)
				wgt.txt.returnPressed.connect(wgt.setText)
				return wgt
			wgt 		=	blk.Elements.Wgt(n=n,t='h')
			wgt 		= create(wgt)
			wgt.lay = add(wgt)

			wgt 		= fnx(wgt)
			wgt			=	conn(wgt)
			wgt			=	init(wgt)

			return wgt
		def AppCtl(**k):
			def create(wgt):
				wgt.hSpc			=	Wgt.SpcEx()
				wgt.btnExit		= blk.Elements.tBtn('Exit')
				wgt.btnSave		=	blk.Elements.tBtn('Save As')
				wgt.btnPrint	=	blk.Elements.tBtn('Print')
				return wgt
			def add(wgt,lay):
				lay.addWidget(wgt.btnPrint)
				lay.addWidget(wgt.btnSave)
				lay.addWidget(wgt.hSpc)
				lay.addWidget(wgt.btnExit)
				return lay
			def init(wgt):
				wgt.setContentsMargins(*wgt.margin)
				wgt= blk.Layouts.sPol(wgt,h='E',v='P')
				return wgt
			def fnx(wgt):

				wgt.margin=k.get('margin') or [0,0,0,0]
				return wgt
			def conn(wgt):
				wgt.fnPrint=wgt.btnPrint.clicked.connect
				wgt.fnSave=wgt.btnSave.clicked.connect
				return wgt

			wgt = blk.Elements.Wgt(n='wgtAppCtl',t='h')
			wgt=create(wgt)
			wgt.lay=add(wgt,wgt.lay)
			wgt=fnx(wgt)
			wgt=init(wgt)
			wgt=conn(wgt)
			return wgt
		Wgt = types.SimpleNamespace()
		Wgt.SpcFix		= SpcFix
		Wgt.SpcEx			=	SpcEx
		Wgt.chkRE			= chkRE
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

def construct_Qt5Ui(data,beta):

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
				searchStr= App.Main.Element.Search.txt.text()
				Opts =  (QtCore.Qt.MatchRecursive|QtCore.Qt.MatchRegExp|QtCore.Qt.CaseInsensitive)
				findkeys	=	App.Main.Element.Tree.Tree.findItems(searchStr,Opts, 0)
				findvals	=	App.Main.Element.Tree.Tree.findItems(searchStr,Opts, 1)
				find			=	[*findkeys,*findvals]
				if len(find) > 1 :
					App.Main.Element.Search.showPN(True)
					App.Main.Element.Tree.Tree.setCurrentItem(find[0])
				elif len(find) == 1 :
					App.Main.Element.Search.showPN(False)
					App.Main.Element.Tree.Tree.setCurrentItem(find[0])
				else:
					App.Main.Element.Search.showPN(False)
				App.Main.Element.Search.Found=find
			return searchTree

		def searchSel(App):
			def searchSel():
				App.Main.Element.Tree.Tree.currentItemChanged.connect(App.Fnx.OnSelect)
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

		def allign(App):
			maxwidth=max(App.Main.Element.Key.lbl.width(),App.Main.Element.Val.lbl.width())
			App.Main.Element.Key.lbl.setMinimumWidth(maxwidth)
			App.Main.Element.Val.lbl.setMinimumWidth(maxwidth)
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
						w = App.Main.Element.Tree.Tree.columnWidth(1)
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

		def saveDialog():
			def saveDialog():
				Path, Type =QtWidgets.QFileDialog.getSaveFileName(QtWidgets.QWidget(),"Save As","","All Files (*)")
				return Path
			return saveDialog()


		def stdf(*a,**k):
			dct = k.get('dct')
			name=	k.get("name")
			def stdf():
				def Dct(dct=None,**k):
					ident = k.get('ident') or 3
					with open(File , 'a') as f:


						def testkey(content, ident):
							if isinstance(dct[key], dict):
								tabs = (ident+1) * '\t'
								f.write(tabs)

								f.write(f"'{key}'\t:\t")
								f.write('{\n')
								f.flush()
								ident += 1
								Dct(dct=dct[key], ident=ident)
							else:
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

				File=saveDialog()
				if not File:
					return
				else:
					with open(File , 'w') as f:
						f.write(f'{name}\t=\t')
						f.write('{\n')
					Dct(dct)
			return stdf

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
		fnx.saveDialog	=	saveDialog
		fnx.stdf				=	stdf
		fnx.stdw				= stdw
		fnx.OnSelect		= select(Key=App.Main.Element.Key,Val=App.Main.Element.Val,Path=App.Main.Element.Path)
		fnx.PathToClip	=	copytoclip(App.Main.Element.Path.txt)
		fnx.Searched		=	search(App)
		fnx.Found				=	searchSel(App)
		fnx.selNext			= App.Main.Element.Search.selNext(App.Main.Element.Tree.Tree)
		fnx.selPrev			= App.Main.Element.Search.selPrev(App.Main.Element.Tree.Tree)
		return fnx

	def create(App):
		def MainWgt():
			wgt = App.Blocks.Elements.Wgt(n='Qt5',t='v')
			return wgt

		def Elements():
			Element				= types.SimpleNamespace()
			Element.Tree			=	App.Blocks.Widgets.Tree()
			Element.Search		= App.Blocks.Widgets.Search()
			Element.ExpCol		=	App.Blocks.Widgets.IncDec()
			Element.Path 			= App.Blocks.Widgets.Path()
			Element.Key 			= App.Blocks.Widgets.EditProp('Key',ed=App.beta,fnset=print)
			Element.Val 			= App.Blocks.Widgets.EditProp('Val',ed=App.beta,fnset=print)
			Element.AppCtl		=	App.Blocks.Widgets.AppCtl()
			return Element

		def Modules():
			Module						= types.SimpleNamespace()
			Module.TreeCtl		=	App.Blocks.Layouts.siblings([Main.Element.ExpCol,Main.Element.Path],t='h',margin=[5,0,5,5])

			Module.WrpSearch	=	App.Blocks.Layouts.center(Main.Element.Search,w=0,margin=[5,0,5,5])
			Module.Edit				=	App.Blocks.Layouts.siblings([Main.Element.Key,Main.Element.Val],'v',margin=[25,0,25,5])
			# Module.wrpEdit	=	App.Blocks.Layouts.center(App.Main.Edit,w=25)
			Module.TrDisp			=	App.Blocks.Layouts.siblings([Main.Element.Tree,Module.TreeCtl],t='v')
			# Module.Tools			=	App.Blocks.Layouts.siblings([Module.WrpSearch,Module.Edit],'v',margin=[0,0,0,5])
			return Module

		def add():
			Main.lay.addWidget(Main.Module.TrDisp)
			Main.lay.addWidget(Main.Module.Edit)
			Main.lay.addWidget(Main.Module.WrpSearch)
			Main.lay.addWidget(Main.Element.AppCtl)
			return Main.lay
		Main=MainWgt()
		Main.Element	=	Elements()
		Main.Module 	=	Modules()
		Main.Layout		=	add()
		return Main

	def conn(App):
		conn=types.SimpleNamespace()
		elmt=App.Main.Element
		fnx=App.Fnx
		conn.fnSave = elmt.AppCtl.fnSave
		elmt.ExpCol.fnI(elmt.Tree.Tree.expandAll)
		elmt.ExpCol.fnD(elmt.Tree.Tree.collapseAll)
		elmt.Tree.Selected(fnx.OnSelect)
		elmt.Tree.FoundSel(fnx.Found)
		# elmt.AppCtl.fnSave(fnx.stdf)
		# elmt.AppCtl.fnPrint(fnx.stdo)
		elmt.Path.Copy(fnx.PathToClip)
		elmt.Search.Find(fnx.Searched)
		elmt.Search.Next(fnx.selNext)
		elmt.Search.Prev(fnx.selPrev)
		return conn

	App = QtApp()
	App.beta			= beta
	App.Main			= create(App)
	App.Fnx				= Fnx(App)
	App.Conn			=	conn(App)
	App.Clip			= App.QtWin.clipboard()
	return App

def browse(beta=False,**k):
	kv = k.popitem()
	QtApp = construct_Qt5Ui(kv[1],beta)
	trunk = QtApp.Fnx.makeTree(QtApp, name=kv[0], data=kv[1])
	QtApp.Main.Element.Tree.Tree.addTopLevelItem(trunk)
	QtApp.Conn.fnSave(QtApp.Fnx.stdf(dct=kv[1],name=kv[0]))
	QtApp.Main.show()
	QtApp.Fnx.allign(QtApp)
	QtApp.Main.Element.Tree.fittCols()
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
	browse(test=dct,beta=True)

# def saveDialog():
# 	Path, Type =QtWidgets.QFileDialog.getSaveFileName(QtWidgets.QWidget(),"Save As","","All Files (*)")
# 	return Path


# def skel(**k):
#
# 	def create(wgt):
# 		return wgt
# 	def layout(wgt):
# 		wgt.margin=k.get('margin')
# 		wgt = blk.Layouts.sPol(wgt, h='P', v='P')
# 		wgt.setContentsMargins(*wgt.margin)
# 		return wgt
# 	def add(wgt):
# 		wgt.lay.addWidget(wgt.)
# 		return wgt.lay
# 	def init(wgt):
# 		return wgt
# 	def fnx(wgt):
# 		wgt.fnx
# 		return wgt.fnx
# 	def conn(wgt):
# 		return wgt.conn
# 	wgt = blk.Elements.Wgt(n=f'wgt{n}',t='h')
# 	wgt=create(wgt)
# 	wgt.lay=add(wgt)
# 	wgt.fnx=fnx(wgt)
# 	wgt=layout(wgt)
# 	wgt.conn=conn(wgt)
# 	return wgt


				#
        # self.verticalLayout.addWidget(self.checkBox)
				#
        # MainWindow.setCentralWidget(self.centralwidget)
        # self.menubar = QMenuBar(MainWindow)
        # self.menubar.setObjectName(u"menubar")
        # self.menubar.setGeometry(QRect(0, 0, 220, 21))
        # MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QStatusBar(MainWindow)
        # self.statusbar.setObjectName(u"statusbar")
        # MainWindow.setStatusBar(self.statusbar)
