#!/usr/bin/env python
# Auth
from PyQt5 import QtCore, QtGui, QtWidgets
import QtUser
import sys

sPols 			= 	{
	'P'       : QtWidgets.QSizePolicy.Preferred,
	'M'       : QtWidgets.QSizePolicy.Maximum,
	'm'       : QtWidgets.QSizePolicy.Minimum,
	'E'       :	QtWidgets.QSizePolicy.Expanding,
	'mE'      :	QtWidgets.QSizePolicy.MinimumExpanding,
	'F'       :	QtWidgets.QSizePolicy.Fixed,
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
	'RegEx'   :	[ b'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiI+PHBhdGggZD0iTTEwLjUgMWMtLjI3NyAwLS41LjIyMy0uNS41djEuNzkzTDguNzMyIDIuMDI1YS40OTkuNDk5IDAgMSAwLS43MDcuNzA4TDkuMjkzIDRINy41YS40OTkuNDk5IDAgMSAwIDAgMWgxLjc5M0w4LjAyNSA2LjI2OGEuNDk5LjQ5OSAwIDEgMCAuNzA3LjcwN0wxMCA1LjcwN1Y3LjVhLjQ5OS40OTkgMCAxIDAgMSAwVjUuNzA3bDEuMjY4IDEuMjY4YS40OTkuNDk5IDAgMSAwIC43MDctLjcwN0wxMS43MDcgNUgxMy41YS40OTkuNDk5IDAgMSAwIDAtMWgtMS43OTNsMS4yNjgtMS4yNjhhLjUuNSAwIDAgMC0uNzA3LS43MDdMMTEgMy4yOTNWMS41YzAtLjI3Ny0uMjIzLS41LS41LS41em0tOCAxMWExLjUgMS41IDAgMSAwIDAgMyAxLjUgMS41IDAgMCAwIDAtM3oiIGZpbGw9IiMzNjM2MzYiLz48L3N2Zz4=',
                b'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiI+PHBhdGggZD0iTTEwLjUgMWMtLjI3NyAwLS41LjIyMy0uNS41djEuNzkzTDguNzMyIDIuMDI1YS40OTkuNDk5IDAgMSAwLS43MDcuNzA4TDkuMjkzIDRINy41YS40OTkuNDk5IDAgMSAwIDAgMWgxLjc5M0w4LjAyNSA2LjI2OGEuNDk5LjQ5OSAwIDEgMCAuNzA3LjcwN0wxMCA1LjcwN1Y3LjVhLjQ5OS40OTkgMCAxIDAgMSAwVjUuNzA3bDEuMjY4IDEuMjY4YS40OTkuNDk5IDAgMSAwIC43MDctLjcwN0wxMS43MDcgNUgxMy41YS40OTkuNDk5IDAgMSAwIDAtMWgtMS43OTNsMS4yNjgtMS4yNjhhLjUuNSAwIDAgMC0uNzA3LS43MDdMMTEgMy4yOTNWMS41YzAtLjI3Ny0uMjIzLS41LS41LS41em0tOCAxMWExLjUgMS41IDAgMSAwIDAgMyAxLjUgMS41IDAgMCAwIDAtM3oiIGZpbGw9IiNkZWRlZGUiLz48L3N2Zz4=']
	}
lays				=		{
	'H'       :	QtWidgets.QHBoxLayout,
	'V'       : QtWidgets.QVBoxLayout,
	'G'       :	QtWidgets.QGridLayout,
	'F'       :	QtWidgets.QFormLayout,
					}

def EditProp(n,**k):
			fnSet=k.get('fnset')
			def elements():
				e = {}
				e['Lbl']		= GUI['Elements']['Lbl'](n=f'{n}:')
				e['txt']		= GUI['Elements']['lEdit'](n=n,ro=True)
				e['txtdup']	= GUI['Elements']['lEdit'](n=n,ro=True)
				e['btnSet']	=	GUI['Elements']['tBtn'](n='Set')
				e['btnEdit']=	GUI['Elements']['iBtn'](n='Edit', bi=True,ico=ico)
				return e

			def add():
				w['Lay'].addWidget(w['elements']['Lbl']['Wgt'])
				w['Lay'].addWidget(w['elements']['txt']['Wgt'])
				w['Lay'].addWidget(w['elements']['txtdup']['Wgt'])
				w['Lay'].addWidget(w['elements']['btnSet']['Wgt'] )
				w['Lay'].addWidget(w['elements']['btnEdit']['Wgt'])
				return w['Lay']
			def init(wgt):
				w['elements']['btnSet']['Mtd']['setHidden'](True)
				w['elements']['txt']['Mtd']['setReadOnly'](True)
				w['elements']['txtdup']['Mtd']['setHidden'](True)
				w['fnx']['Editable'](not k.get('ed'))
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
						w['elements']['btnEdit']['Mtd']['setHidden'](state)
					return editable
				f = {}
				f['Edit'] 		=	edit(wgt)
				f['txtText'] 	=	txtText(wgt)
				f['setText']	=	setText(wgt)
				f['Editable'] =	editable(wgt)
				return f
			def conn(wgt):
				c = {}
				c['btnEdit']= w['elements']['btnEdit']['Wgt'].clicked.connect
				c['btnSet']= w['elements']['btnSet']['Conn']['clicked']
				c['txt']	= {}
				c['txt']['returnPressed']= w['elements']['txt']['Wgt'].returnPressed.connect
				# wgt.btnEdit.clicked.connect(w['fnx']['Edit'])
				# wgt.btnSet.clicked.connect(w['fnx']['txtText'])
				# wgt.txt.returnPressed.connect(w['fnx']['txtText'])
				return c
			w ={}

			w		=	GUI['Make']['Wgt'](n=n,t='h')
			w['elements']	= elements()
			w['Wgt']    = GUI['Make']['sPol'](w, h='E', v='F')
			w['layout'] 	= add()
			w['fnx'] 			= fnx(w['Wgt'])
			w['conn'] = conn(w['Wgt'])
			w['Wgt'] = init(w['Wgt'])

			return w

GUI 	= {}
GUI 	|= QtUser.QtUi
GUI['Elements']	= QtUser.Elements()
GUI|=	QtUser.App()


GUI['Main']	=	GUI['Make']['Wgt'](n='Qt5',t='v')
tmp=EditProp('test',ed=True,fnset=print, m=[0,5,0,5])
GUI['Main']['Lay'].addWidget(tmp['Wgt'])
GUI['Main']['Mtd']['show']()
sys.exit(GUI['QtApp'].exec())

