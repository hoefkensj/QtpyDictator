#!/usr/bin/env python
"""
	use:
		- import pyDictatorQT
		- from pyDictatorQt import browse

		pyDictatorQT.browse( [NAMEOFDICT] = [DICT]	)

		ex:
			from pyDictatorQt import browse
			mydict= { 'a' : 'B'}
			browse(mydict=mydict)
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import QtUser
import types ,sys

sPols 			= 	{
	'P'				: QtWidgets.QSizePolicy.Preferred,
	'M'				: QtWidgets.QSizePolicy.Maximum,
	'm'				: QtWidgets.QSizePolicy.Minimum,
	'E'				:	QtWidgets.QSizePolicy.Expanding,
	'mE'			:	QtWidgets.QSizePolicy.MinimumExpanding,
	'F'				:	QtWidgets.QSizePolicy.Fixed,
	}
ico					=		{
	'Search'	: [	b'PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXciIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KIDxwYXRoIGQ9Im02LjUgMWMzLjAzNzYgMCA1LjUgMi40NjI0IDUuNSA1LjUgMCAxLjMzODgtMC40NzgzIDIuNTY1OS0xLjI3MzQgMy41MTk2bDQuMTI3IDQuMTI2OGMwLjE5NTIgMC4xOTUzIDAuMTk1MiAwLjUxMTkgMCAwLjcwNzItMC4xNzM2IDAuMTczNS0wLjQ0MyAwLjE5MjgtMC42Mzc5IDAuMDU3OGwtMC4wNjkzLTAuMDU3OC00LjEyNjgtNC4xMjdjLTAuOTUzNyAwLjc5NTEtMi4xODA4IDEuMjczNC0zLjUxOTYgMS4yNzM0LTMuMDM3NiAwLTUuNS0yLjQ2MjQtNS41LTUuNSAwLTMuMDM3NiAyLjQ2MjQtNS41IDUuNS01LjV6bTAgMWMtMi40ODUzIDAtNC41IDIuMDE0Ny00LjUgNC41IDAgMi40ODUzIDIuMDE0NyA0LjUgNC41IDQuNSAyLjQ4NTMgMCA0LjUtMi4wMTQ3IDQuNS00LjUgMC0yLjQ4NTMtMi4wMTQ3LTQuNS00LjUtNC41eiIgZmlsbD0iIzM2MzYzNiIvPgo8L3N2Zz4K' ,
								b'PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXciIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KIDxwYXRoIGQ9Im02LjUgMWMzLjAzNzYgMCA1LjUgMi40NjI0IDUuNSA1LjUgMCAxLjMzODgtMC40NzgzIDIuNTY1OS0xLjI3MzQgMy41MTk2bDQuMTI3IDQuMTI2OGMwLjE5NTIgMC4xOTUzIDAuMTk1MiAwLjUxMTkgMCAwLjcwNzItMC4xNzM2IDAuMTczNS0wLjQ0MyAwLjE5MjgtMC42Mzc5IDAuMDU3OGwtMC4wNjkzLTAuMDU3OC00LjEyNjgtNC4xMjdjLTAuOTUzNyAwLjc5NTEtMi4xODA4IDEuMjczNC0zLjUxOTYgMS4yNzM0LTMuMDM3NiAwLTUuNS0yLjQ2MjQtNS41LTUuNSAwLTMuMDM3NiAyLjQ2MjQtNS41IDUuNS01LjV6bTAgMWMtMi40ODUzIDAtNC41IDIuMDE0Ny00LjUgNC41IDAgMi40ODUzIDIuMDE0NyA0LjUgNC41IDQuNSAyLjQ4NTMgMCA0LjUtMi4wMTQ3IDQuNS00LjUgMC0yLjQ4NTMtMi4wMTQ3LTQuNS00LjUtNC41eiIgZmlsbD0iI2RlZGVkZSIvPgo8L3N2Zz4K'] ,
	'Next'		:	[	b'PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZlcnNpb249IjEuMSI+CiA8ZGVmcz4KICA8c3R5bGUgaWQ9ImN1cnJlbnQtY29sb3Itc2NoZW1lIiB0eXBlPSJ0ZXh0L2NzcyI+LkNvbG9yU2NoZW1lLVRleHQgeyBjb2xvcjojMzYzNjM2OyB9PC9zdHlsZT4KIDwvZGVmcz4KIDxwYXRoIGNsYXNzPSJDb2xvclNjaGVtZS1UZXh0IiBkPSJNIDQuNjM2NywxLjYzNjcgMTEsOCA0LjYzNjcsMTQuMzYzMyAzLjkyOTY3LDEzLjY1NjI3IDkuNTg1ODcsOC4wMDAwNyAzLjkyOTY3LDIuMzQzODcgNC42MzY3LDEuNjM2ODQgWiIgZmlsbD0iY3VycmVudENvbG9yIi8+Cjwvc3ZnPgo=' ,
								b'PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZlcnNpb249IjEuMSI+CiA8ZGVmcz4KICA8c3R5bGUgaWQ9ImN1cnJlbnQtY29sb3Itc2NoZW1lIiB0eXBlPSJ0ZXh0L2NzcyI+LkNvbG9yU2NoZW1lLVRleHQgeyBjb2xvcjojZGVkZWRlOyB9PC9zdHlsZT4KIDwvZGVmcz4KIDxwYXRoIGNsYXNzPSJDb2xvclNjaGVtZS1UZXh0IiBkPSJNIDQuNjM2NywxLjYzNjcgMTEsOCA0LjYzNjcsMTQuMzYzMyAzLjkyOTY3LDEzLjY1NjI3IDkuNTg1ODcsOC4wMDAwNyAzLjkyOTY3LDIuMzQzODcgNC42MzY3LDEuNjM2ODQgWiIgZmlsbD0iY3VycmVudENvbG9yIi8+Cjwvc3ZnPgo='],
	'Prev'		:	[	b'PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZlcnNpb249IjEuMSI+CiA8ZGVmcz4KICA8c3R5bGUgaWQ9ImN1cnJlbnQtY29sb3Itc2NoZW1lIiB0eXBlPSJ0ZXh0L2NzcyI+LkNvbG9yU2NoZW1lLVRleHQgeyBjb2xvcjojMzYzNjM2OyB9PC9zdHlsZT4KIDwvZGVmcz4KIDxwYXRoIGQ9Im0xMC4zNjMgMS42MzY3LTYuMzYzMyA2LjM2MzMgNi4zNjMzIDYuMzYzMyAwLjcwNzAzLTAuNzA3MDMtNS42NTYyLTUuNjU2MiA1LjY1NjItNS42NTYyLTAuNzA3MDMtMC43MDcwM3oiIGNsYXNzPSJDb2xvclNjaGVtZS1UZXh0IiBzdHlsZT0iZmlsbDpjdXJyZW50Q29sb3IiLz4KPC9zdmc+Cg==',
								b'PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZlcnNpb249IjEuMSI+CiA8ZGVmcz4KICA8c3R5bGUgaWQ9ImN1cnJlbnQtY29sb3Itc2NoZW1lIiB0eXBlPSJ0ZXh0L2NzcyI+LkNvbG9yU2NoZW1lLVRleHQgeyBjb2xvcjojZGVkZWRlOyB9PC9zdHlsZT4KIDwvZGVmcz4KIDxwYXRoIGQ9Im0xMC4zNjMgMS42MzY3LTYuMzYzMyA2LjM2MzMgNi4zNjMzIDYuMzYzMyAwLjcwNzAzLTAuNzA3MDMtNS42NTYyLTUuNjU2MiA1LjY1NjItNS42NTYyLTAuNzA3MDMtMC43MDcwM3oiIGNsYXNzPSJDb2xvclNjaGVtZS1UZXh0IiBzdHlsZT0iZmlsbDpjdXJyZW50Q29sb3IiLz4KPC9zdmc+Cg=='],
	'Inc'			: [	b'PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXciIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KIDxyZWN0IHg9IjIiIHk9IjciIHdpZHRoPSIxMSIgaGVpZ2h0PSIxIiBmaWxsPSIjMzYzNjM2Ii8+Cjwvc3ZnPgo=',
								b'PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXciIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KIDxyZWN0IHg9IjIiIHk9IjciIHdpZHRoPSIxMSIgaGVpZ2h0PSIxIiBmaWxsPSIjZGVkZWRlIi8+CiA8cmVjdCB0cmFuc2Zvcm09InJvdGF0ZSg5MCkiIHg9IjIiIHk9Ii04IiB3aWR0aD0iMTEiIGhlaWdodD0iMSIgZmlsbD0iI2RlZGVkZSIvPgo8L3N2Zz4K'],
	'Dec'			:	[	b'PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXciIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KIDxwYXRoIGQ9Im0zIDhoMTB2MWgtMTB6IiBjb2xvcj0iIzM2MzYzNiIgZmlsbD0iIzM2MzYzNiIgb3ZlcmZsb3c9InZpc2libGUiIHN0cm9rZS13aWR0aD0iLjcwNzExIi8+Cjwvc3ZnPgo=',
								b'PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXciIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KIDxwYXRoIGQ9Im0zIDhoMTB2MWgtMTB6IiBjb2xvcj0iI2RlZGVkZSIgZmlsbD0iI2RlZGVkZSIgb3ZlcmZsb3c9InZpc2libGUiIHN0cm9rZS13aWR0aD0iLjcwNzExIi8+Cjwvc3ZnPgo='],
	'Edit'		:	[	b'PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KIDxwYXRoIGQ9Im0xMi4yMzggMS0wLjM1MyAwLjM2LTguOTY5IDkuMDk1LTAuMDMgMC4wNDVjLTAuMDYxIDAuMDk5LTAuMjcgMC40NS0wLjU4MyAxLjA4OC0wLjMxNCAwLjYzOC0wLjcgMS41MS0xLjAxMiAyLjQ5MmwtMC4yOTEgMC45MiAwLjkyLTAuMjkxYTE4LjE2MyAxOC4xNjMgMCAwIDAgMi40OTItMS4wMTJjMC42MzgtMC4zMTQgMC45ODctMC41MiAxLjA4OC0wLjU4NGwwLjA0NS0wLjAyOSA5LjQ1NS05LjMyMnptLTguMzQ3IDkuODkgMS4yMTggMS4yMi0wLjE3NyAwLjE3NWM3ZS0zIC01ZS0zIC0wLjM3OSAwLjIyNy0wLjk2MSAwLjUxNC0wLjIxNCAwLjEwNS0wLjUzNiAwLjIyMi0wLjgzNCAwLjMzOGwtMC4yNzQtMC4yNzRjMC4xMTYtMC4yOTggMC4yMzMtMC42MiAwLjMzOC0wLjgzNCAwLjI4Ny0wLjU4MiAwLjUxOC0wLjk2NiAwLjUxNC0wLjk2eiIgZmlsbD0iIzM2MzYzNiIgZm9udC1zaXplPSIxNSIgbGV0dGVyLXNwYWNpbmc9IjAiIHdvcmQtc3BhY2luZz0iMCIvPgo8L3N2Zz4K',
								b'PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KIDxwYXRoIGQ9Im0xMi4yMzggMS0wLjM1MyAwLjM2LTguOTY5IDkuMDk1LTAuMDMgMC4wNDVjLTAuMDYxIDAuMDk5LTAuMjcgMC40NS0wLjU4MyAxLjA4OC0wLjMxNCAwLjYzOC0wLjcgMS41MS0xLjAxMiAyLjQ5MmwtMC4yOTEgMC45MiAwLjkyLTAuMjkxYTE4LjE2MyAxOC4xNjMgMCAwIDAgMi40OTItMS4wMTJjMC42MzgtMC4zMTQgMC45ODctMC41MiAxLjA4OC0wLjU4NGwwLjA0NS0wLjAyOSA5LjQ1NS05LjMyMnptLTguMzQ3IDkuODkgMS4yMTggMS4yMi0wLjE3NyAwLjE3NWM3ZS0zIC01ZS0zIC0wLjM3OSAwLjIyNy0wLjk2MSAwLjUxNC0wLjIxNCAwLjEwNS0wLjUzNiAwLjIyMi0wLjgzNCAwLjMzOGwtMC4yNzQtMC4yNzRjMC4xMTYtMC4yOTggMC4yMzMtMC42MiAwLjMzOC0wLjgzNCAwLjI4Ny0wLjU4MiAwLjUxOC0wLjk2NiAwLjUxNC0wLjk2eiIgZmlsbD0iI2RlZGVkZSIgZm9udC1zaXplPSIxNSIgbGV0dGVyLXNwYWNpbmc9IjAiIHdvcmQtc3BhY2luZz0iMCIvPgo8L3N2Zz4K'],
	'Copy'		: [	b'PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXciIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KIDxwYXRoIGQ9Im02IDBjLTEuMTA0NiAwLTIgMC44OTU0My0yIDJ2MTBjMCAxLjEwNDYgMC44OTU0MyAyIDIgMmg2YzEuMTA0NiAwIDItMC44OTU0IDItMnYtMTBjMC0xLjEwNDYtMC44OTU0LTItMi0yem0tMSAyYzAtMC41NTIyOCAwLjQ0NzcyLTEgMS0xaDZjMC41NTIzIDAgMSAwLjQ0NzcyIDEgMXYxMGMwIDAuNTUyMy0wLjQ0NzcgMS0xIDFoLTZjLTAuNTUyMjggMC0xLTAuNDQ3Ny0xLTF6bS0zIDJjMC0wLjc0MDI4IDAuNDAyMi0xLjM4NjYgMS0xLjczMjR2MTAuMjMyYzAgMS4zODA3IDEuMTE5MyAyLjUgMi41IDIuNWg2LjIzMjRjLTAuMzQ1OCAwLjU5NzgtMC45OTIxIDEtMS43MzI0IDFoLTQuNWMtMS45MzMgMC0zLjUtMS41NjctMy41LTMuNXoiIGZpbGw9IiMzNjM2MzYiLz4KPC9zdmc+Cg==',
								b'PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXciIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KIDxwYXRoIGQ9Im02IDBjLTEuMTA0NiAwLTIgMC44OTU0My0yIDJ2MTBjMCAxLjEwNDYgMC44OTU0MyAyIDIgMmg2YzEuMTA0NiAwIDItMC44OTU0IDItMnYtMTBjMC0xLjEwNDYtMC44OTU0LTItMi0yem0tMSAyYzAtMC41NTIyOCAwLjQ0NzcyLTEgMS0xaDZjMC41NTIzIDAgMSAwLjQ0NzcyIDEgMXYxMGMwIDAuNTUyMy0wLjQ0NzcgMS0xIDFoLTZjLTAuNTUyMjggMC0xLTAuNDQ3Ny0xLTF6bS0zIDJjMC0wLjc0MDI4IDAuNDAyMi0xLjM4NjYgMS0xLjczMjR2MTAuMjMyYzAgMS4zODA3IDEuMTE5MyAyLjUgMi41IDIuNWg2LjIzMjRjLTAuMzQ1OCAwLjU5NzgtMC45OTIxIDEtMS43MzI0IDFoLTQuNWMtMS45MzMgMC0zLjUtMS41NjctMy41LTMuNXoiIGZpbGw9IiNkZWRlZGUiLz4KPC9zdmc+Cg=='],
	'RegEx'		:	[	b'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiI+PHBhdGggZD0iTTEwLjUgMWMtLjI3NyAwLS41LjIyMy0uNS41djEuNzkzTDguNzMyIDIuMDI1YS40OTkuNDk5IDAgMSAwLS43MDcuNzA4TDkuMjkzIDRINy41YS40OTkuNDk5IDAgMSAwIDAgMWgxLjc5M0w4LjAyNSA2LjI2OGEuNDk5LjQ5OSAwIDEgMCAuNzA3LjcwN0wxMCA1LjcwN1Y3LjVhLjQ5OS40OTkgMCAxIDAgMSAwVjUuNzA3bDEuMjY4IDEuMjY4YS40OTkuNDk5IDAgMSAwIC43MDctLjcwN0wxMS43MDcgNUgxMy41YS40OTkuNDk5IDAgMSAwIDAtMWgtMS43OTNsMS4yNjgtMS4yNjhhLjUuNSAwIDAgMC0uNzA3LS43MDdMMTEgMy4yOTNWMS41YzAtLjI3Ny0uMjIzLS41LS41LS41em0tOCAxMWExLjUgMS41IDAgMSAwIDAgMyAxLjUgMS41IDAgMCAwIDAtM3oiIGZpbGw9IiMzNjM2MzYiLz48L3N2Zz4=',
								b'PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiI+PHBhdGggZD0iTTEwLjUgMWMtLjI3NyAwLS41LjIyMy0uNS41djEuNzkzTDguNzMyIDIuMDI1YS40OTkuNDk5IDAgMSAwLS43MDcuNzA4TDkuMjkzIDRINy41YS40OTkuNDk5IDAgMSAwIDAgMWgxLjc5M0w4LjAyNSA2LjI2OGEuNDk5LjQ5OSAwIDEgMCAuNzA3LjcwN0wxMCA1LjcwN1Y3LjVhLjQ5OS40OTkgMCAxIDAgMSAwVjUuNzA3bDEuMjY4IDEuMjY4YS40OTkuNDk5IDAgMSAwIC43MDctLjcwN0wxMS43MDcgNUgxMy41YS40OTkuNDk5IDAgMSAwIDAtMWgtMS43OTNsMS4yNjgtMS4yNjhhLjUuNSAwIDAgMC0uNzA3LS43MDdMMTEgMy4yOTNWMS41YzAtLjI3Ny0uMjIzLS41LS41LS41em0tOCAxMWExLjUgMS41IDAgMSAwIDAgMyAxLjUgMS41IDAgMCAwIDAtM3oiIGZpbGw9IiNkZWRlZGUiLz48L3N2Zz4=']
	}
lays				=		{
	'H'				:	QtWidgets.QHBoxLayout,
	'V'				: QtWidgets.QVBoxLayout,
	'G'				:	QtWidgets.QGridLayout,
	'F'				:	QtWidgets.QFormLayout,
					}

def dummy(*a,**k):	pass

def QtBlocks():

	def Widgets():
		def Tree(*a,**k):
			def data():
				d = {}
				d['Name']		=k.get('n') or 'wgtTree'
				d['Margins']=k.get('margin') or  [0,0,0,0]
				return d
			def elements():
				e = {
						'Tree'	: 	blk['Elements']['Tree']['Wgt'](n=w['Data']['Name'],margin=w['Data']['Margins'])
						}
				return e
			def create(wgt):
				wgt.Tree 		= w['Elements']['Tree']
				return wgt
			def init(wgt):
				wgt.Tree.setContentsMargins(*w['Data']['Margins'])
				wgt.setContentsMargins(*w['Data']['Margins'])
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
							w = w + rel
						else:
							w	=	tot
						wgt.Tree.setColumnWidth(col,w)
					return setColWidth
				f = {}
				f['fittCols'] 		= resizeCols(wgt)
				f['colWidth']			=	colWidth(wgt)
				f['setColWidth'] 	= setColWidth(wgt)
				return f
			def conn(wgt):
				wgt.Selected=wgt.Tree.itemClicked.connect
				wgt.FoundSel	=	wgt.Tree.itemSelectionChanged.connect
				return wgt
			w = {}
			w['Data'] = data()
			w['Wgt'] 	=	blk['Base']['wgt'](n=w['Data']['Name'],t='h')
			w['Wgt'] 	=	blk['Base']['sPol'](w['Wgt'], h='E', v='mE')
			w['Elements']	=	elements()
			w['Wgt']			=	create(w['Wgt'])
			w['layout']		=	w['Wgt'].lay
			w['layout'] 	= add(w['Wgt'],w['layout'])
			w['Fnx'] 			= fnx(w['Wgt'])
			w['Conn']			=	conn(w['Wgt'])
			w['Wgt']			=	init(w['Wgt'])
			return w
		def IncDec(**k):
			def create(wgt):
				wgt.btnExp 		= blk['Elements']['iBtn']('Inc',h=15,w=15,icons=ico)
				wgt.btnCol 		= blk['Elements']['iBtn']('Dec',h=15,w=15,icons=ico)
				return wgt
			def layout(wgt):
				wgt = blk['Base']['sPol'](wgt, h='P', v='P')
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
			wgt =	 blk['Base']['Wgt'](n='wgtIncDec',t='h')
			wgt=create(wgt)
			wgt.lay=add(wgt,wgt.lay)
			wgt=layout(wgt)
			wgt=conn(wgt)
			wgt.setContentsMargins(*margin)
			return wgtcleeear
		def Search():
			def elements():
				e={}
				e['btnNext'] 			= blk['Elements']['iBtn']('Next', w=12,icons=ico)
				e['btnPrev'] 			= blk['Elements']['iBtn']('Prev', w=12,icons=ico)
				e['btnSearch'] 		= blk['Elements']['iBtn']('Search',icons=ico)
				e['chkRegEx']			=	blk['Elements']['chkBox']('RegEx',icons=ico)
				e['txt'] 					=	blk['Elements']['lEdit']('Search')
				e['wgtPN'] 				= blk['Layouts']['siblings']([e['btnPrev']['Wgt'],e['btnNext']['Wgt']],t='h',margin=[0,0,0,0])
				e['wgtCtl'] 			= blk['Layouts']['siblings']([e['wgtPN'],e['btnSearch']['Wgt']],t='h',margin=[0,0,0,0])
				e['wgtSearch']		= blk['Layouts']['siblings']([e['chkRegEx']['Wgt'],e['txt'],e['wgtCtl']],t='h',margin=[0,0,0,0])
				return e
			def add(wgt,lay):
				lay.addWidget(w['elements']['wgtSearch'])
			def init(wgt):
				w['elements']['btnPrev'].setHidden(True)
				w['elements']['btnNext'].setHidden(True)
				w['Wgt']	= blk['Base']['sPol'](wgt, h='E', v='F')
				w['Found'] = None

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
			w={}
			w['Wgt'] = blk['Base']['Wgt'](n='Search',t='h')
			w['Fnx']	= fnx()
			w['Conn']	=	conn()
			w['elements']	=	elements()
			w['layout'] 	= add(w['wgt'],w['layout'])
			init()
			return w
		def Path():
			def create(wgt):
				wgt.txt 		= blk['Elements']['lEdit'](n='Path',ro=True)
				wgt.btnCopy = blk['Elements']['iBtn']('Copy',icons=ico)
				return wgt
			def add(wgt,lay):
				lay.addWidget(wgt.txt)
				lay.addWidget(wgt.btnCopy)
				return lay
			def conn(wgt):
				wgt.Copy=wgt.btnCopy.clicked.connect
				return wgt
			Elmt = blk['Elements']
			wgt = blk['Base']['Wgt'](n='Path',t='h')
			wgt = create(wgt)
			wgt.lay = add(wgt,wgt.lay)
			wgt = conn(wgt)
			return wgt
		def EditProp(n,**k):
			fnSet=k.get('fnset') or dummy
			def elements():
				e = {}
				e['Lbl']		= blk['Elements']['Lbl'](f'{n}:')
				e['txt']		= blk['Elements']['lEdit'](n,ro=True)
				e['txtdup']	= blk['Elements']['lEdit'](n,ro=True)
				e['btnSet']	=	blk['Elements']['tBtn']('Set')
				e['btnEdit']=	blk['Elements']['iBtn']('Edit', bi=True,icons=ico)
				return e

			def add(w,lay):
				lay.addWidget(w['elements']['Lbl'])
				lay.addWidget(w['elements']['txt'])
				lay.addWidget(w['elements']['txtdup'])
				lay.addWidget(w['elements']['btnSet']['Wgt'] )
				lay.addWidget(w['elements']['btnEdit'])
				return lay
			def init(wgt):
				w['elements']['btnSet']['Fnx']['setHidden'](True)
				w['elements']['txt'].setReadOnly(True)
				w['elements']['txtdup'].setHidden(True)
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
						w['elements']['btnEdit'].setHidden(state)
					return editable
				f = {}
				f['Edit'] 		=	edit(wgt)
				f['txtText'] 	=	txtText(wgt)
				f['setText']	=	setText(wgt)
				f['Editable'] =	editable(wgt)
				return f
			def conn(wgt):
				c = {}
				c['btnEdit']= w['elements']['btnEdit'].clicked.connect
				c['btnSet']= w['elements']['btnSet']['Conn']['clicked']
				c['txt']	= {}
				c['txt']['returnPressed']= w['elements']['txt'].returnPressed.connect
				# wgt.btnEdit.clicked.connect(w['fnx']['Edit'])
				# wgt.btnSet.clicked.connect(w['fnx']['txtText'])
				# wgt.txt.returnPressed.connect(w['fnx']['txtText'])
				return c
			w ={}
			w['elements']	= elements()
			w['Wgt']		=	blk['Base']['Wgt'](n=n,t='h')
			w['Wgt']    = blk['Base']['sPol'](w['Wgt'], h='E', v='F')
			w['layout']	=	w['Wgt'].lay

			w['layout'] 	= add(w,w['layout'])
			w['fnx'] 			= fnx(w['Wgt'])
			w['conn']			=	conn(w['Wgt'])
			w['Wgt']			=	init(w['Wgt'])

			return w
		def AppCtl(**k):
			def elements():
				e={}
				e['hSpc']			=   	blk['Elements']['SpcEx']()
				e['btnExit']	=   	blk['Elements']['tBtn']('Exit')
				e['btnSave']	=	  	blk['Elements']['tBtn']('Save As')
				e['btnPrint']	=	  	blk['Elements']['tBtn']('Print')
				return e
			def add(w,lay):
				lay.addWidget(wgt['elements']['btnPrint']['Wgt'])
				lay.addWidget(wgt['elements']['btnSave']['Wgt'])
				lay.addWidget(wgt['elements']['hSpc'])
				lay.addWidget(wgt['elements']['btnExit']['Wgt'])
				return lay

			def init(w,d):
				w.setContentsMargins(*d['Margin'])
				w	= blk['Base']['sPol'](w,h='E',v='P')
				return w

			def data():
				d={}
				d['Name']		= 'wgtAppCtl'
				d['Margin']	= k.get('margin') or [0,0,0,0]
				d['Layout']	=	lays['H']
				return d

			def conn(w):
				c={}
				c['Print']	=	wgt['elements']['btnPrint']['Conn']['clicked']
				c['Save']		=	wgt['elements']['btnSave']['Conn']['clicked']
				c['Exit']		=	wgt['elements']['btnExit']['Conn']['clicked']
				return c

			wgt = {}
			wgt['wgt'] 			= blk['Base']['Wgt'](n='wgtAppCtl',t='h')
			wgt['layout']		=	wgt['wgt'].lay
			wgt['elements']	=	elements()
			wgt['layout'] 	= add(wgt['wgt'],wgt['layout'])
			wgt['data']			= data()

			wgt['wgt'] = init(wgt['wgt'],wgt['data'])
			wgt['conn'] = conn(wgt['wgt'])
			return wgt
		Wgt = {}

		Wgt['Tree']				=	Tree
		Wgt['Search']			= Search
		Wgt['Path']				=	Path
		Wgt['IncDec']			=	IncDec
		Wgt['EditProp']		= EditProp
		Wgt['AppCtl']			=	AppCtl
		return Wgt

	blk = {}
	blk['Elements'] = QtUser.Elements()
	blk['Base'] 		= QtUser.Base()
	blk['Layouts']	= QtUser.Layouts()
	blk['Widgets'] = Widgets()
	return blk

def construct_Qt5Ui(beta):

	def QtApp():
		app 						= {}
		app['QtWin'] 		= QtWidgets.QApplication(sys.argv)
		app['Blocks']		= QtBlocks()
		return app

	def Fnx(App):
		def search(App):
			# def find():
			# 	found=App.Main.Tree.Tree.findChild(str, App.Main.Search.txt.text(), QtCore.Qt.MatchFlag.MatchRecursive)
			# 	found2=App.Main.Tree.Tree.findChild(str , App.Main.Search.txt.text(), QtCore.Qt.MatchFlag.MatchContains)
			# 	print(App.Main.Search.txt.text(),found,found2)
			# return find
			def  searchTree():
				searchStr= App['Main']['Element']['Search'].txt.text()
				Opts =  (QtCore.Qt.MatchRecursive|QtCore.Qt.MatchWrap|QtCore.Qt.MatchContains|QtCore.Qt.CaseInsensitive)
				#QtCore.Qt.MatchRegExp
				findkeys	=	App['Main']['Element']['Tree'].Tree.findItems(searchStr,Opts, 0)
				findvals	=	App['Main']['Element']['Tree'].Tree.findItems(searchStr,Opts, 1)
				find			=	[*findkeys,*findvals]
				if len(find) > 1 :
					App['Main']['Element']['Search'].showPN(True)
					App['Main']['Element']['Tree'].Tree.setCurrentItem(find[0])
				elif len(find) == 1 :
					App['Main']['Element']['Search'].showPN(False)
					App['Main']['Element']['Tree'].Tree.setCurrentItem(find[0])
				else:
					App['Main']['Element']['Search'].showPN(False)
				App['Main']['Element']['Search'].Found=find
			return searchTree

		def searchSel(App):
			def searchSel():
				App['Main']['Element']['Tree'].Tree.currentItemChanged.connect(App['Fnx']['OnSelect'])
			return searchSel

		def select(*a,**k):
			Key=k.get('Key')
			Val=k.get('Val')
			Path=k.get('Path')
			txtBox = [Key['elements']['txt'], Val['elements']['txt'], Path.txt ]
			def select(data):
				for idx, txtbox in zip([0, 3, 2], txtBox):
					txtbox.setText(data.text(idx))
			return select

		def copytoclip(txt):
			def toclip():
				App['Clip'].setText(txt.text())
			return toclip

		def allign(App):
			maxwidth=max(App['Main']['Element']['Key']['elements']['Lbl'].width(),App['Main']['Element']['Val']['elements']['Lbl'].width())
			App['Main']['Element']['Key']['elements']['Lbl'].setMinimumWidth(maxwidth)
			App['Main']['Element']['Val']['elements']['Lbl'].setMinimumWidth(maxwidth)
			App['Allign'] 	=	allign
			App['Select'] 	=	select
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
						w = App['Main']['Element']['Tree']['Wgt'].Tree.columnWidth(1)
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

		fnx= {}
		fnx['select'] 			= select
		fnx['copytoclip']		=	copytoclip
		fnx['allign']				=	allign
		fnx['makeTree']			=	make_tree
		fnx['saveDialog']		=	saveDialog
		fnx['stdf']					=	stdf
		fnx['stdw']					= stdw
		fnx['OnSelect']			= select(Key=App['Main']['Element']['Key'],Val=App['Main']['Element']['Val'],Path=App['Main']['Element']['Path'])
		fnx['PathToClip']		=	copytoclip(App['Main']['Element']['Path'].txt)
		fnx['Searched']			=	search(App)
		fnx['Found']				=	searchSel(App)
		fnx['selNext']			= App['Main']['Element']['Search'].selNext(App['Main']['Element']['Tree']['Wgt'].Tree)
		fnx['selPrev']			= App['Main']['Element']['Search'].selPrev(App['Main']['Element']['Tree']['Wgt'].Tree)
		return fnx

	def create(App):
		def MainWgt():
			wgt = App['Blocks']['Base']['wgt'](n='Qt5',t='v')
			return wgt

		def Elements():
			Element							= {}
			Element['Tree']			=	App['Blocks']['Widgets']['Tree']()
			Element['Search']		= App['Blocks']['Widgets']['Search']()
			Element['ExpCol']		=	App['Blocks']['Widgets']['IncDec']()
			Element['Path'] 		= App['Blocks']['Widgets']['Path']()
			Element['Key'] 			= App['Blocks']['Widgets']['EditProp']('Key',ed=App['beta'],fnset=print)
			Element['Val'] 			= App['Blocks']['Widgets']['EditProp']('Val',ed=App['beta'],fnset=print)
			Element['AppCtl']		=	App['Blocks']['Widgets']['AppCtl']()
			return Element

		def Modules():
			Module								= {}
			Module['TreeCtl']			=	App['Blocks']['Layouts']['siblings']([Main['Element']['ExpCol'],Main['Element']['Path']],t='h',margin=[5,0,5,5])

			Module['WrpSearch']		=	App['Blocks']['Layouts']['center'](Main['Element']['Search'],w=0,margin=[5,0,5,5])
			Module['Edit']				=	App['Blocks']['Layouts']['siblings']([Main['Element']['Key']['Wgt'],Main['Element']['Val']['Wgt']],'v',margin=[25,0,25,5])
			# Module.wrpEdit	=	App['Blocks']['Layouts']['center'](App.Main.Edit,w=25)
			Module['TrDisp']			=	App['Blocks']['Layouts']['siblings']([Main['Element']['Tree']['Wgt'],Module['TreeCtl']],t='v')
			# Module.Tools			=	App['Blocks']['Layouts']['siblings']([Module.WrpSearch,Module.Edit],'v',margin=[0,0,0,5])
			return Module

		def add():
			Main['Wgt'].lay.addWidget(Main['Module']['TrDisp'])
			Main['Wgt'].lay.addWidget(Main['Module']['Edit'])
			Main['Wgt'].lay.addWidget(Main['Module']['WrpSearch'])
			Main['Wgt'].lay.addWidget(Main['Element']['AppCtl']['wgt'])
			return Main['Wgt'].lay


		Main={}
		Main['Wgt']				=	MainWgt()
		Main['Element']		=	Elements()
		Main['Module'] 		=	Modules()
		Main['Wgt'].lay		=	add()
		return Main

	def conn(App):
		conn={}

		conn['fnSave'] = App['Main']['Element']['AppCtl']['conn']['Save']
		App['Main']['Element']['ExpCol'].fnI(App['Main']['Element']['Tree']['Wgt'].Tree.expandAll)
		App['Main']['Element']['ExpCol'].fnD(App['Main']['Element']['Tree']['Wgt'].Tree.collapseAll)
		App['Main']['Element']['Tree']['Wgt'].Selected(	App['Fnx']['OnSelect'])
		App['Main']['Element']['Tree']['Wgt'].FoundSel(App['Fnx']['Found'])
		# elmt.AppCtl.fnSave(fnx.stdf)
		# elmt.AppCtl.fnPrint(fnx.stdo)
		App['Main']['Element']['Path'].Copy(App['Fnx']['PathToClip'])
		App['Main']['Element']['Search'].Find(App['Fnx']['Searched'])
		App['Main']['Element']['Search'].Next(App['Fnx']['selNext'])
		App['Main']['Element']['Search'].Prev(App['Fnx']['selPrev'])
		return conn

	App = QtApp()
	App['beta']			= beta
	App['Main']			= create(App)
	App['Fnx']			= Fnx(App)
	App['Conn']			=	conn(App)
	App['Clip']			= App['QtWin'].clipboard()
	return App

def browse(beta=False,**k):
	QtApp = construct_Qt5Ui(beta)
	kv = k.popitem() if k else ('QtApp', QtApp)
	trunk = QtApp['Fnx']['makeTree'](QtApp, name=kv[0], data=kv[1])
	QtApp['Main']['Element']['Tree']['Wgt'].Tree.addTopLevelItem(trunk)
	QtApp['Conn']['fnSave'](QtApp['Fnx']['stdf'](dct=kv[1],name=kv[0]))
	QtApp['Main']['Wgt'].show()
	QtApp['Fnx']['allign'](QtApp)
	QtApp['Main']['Element']['Tree']['Fnx']['fittCols']()
	sys.exit(QtApp['QtWin'].exec())

if __name__ == '__main__' :
	dct = {
		'a' : {
						'aa' : 'aa',
						'ab'  : 'ab'

		},
		'b'  : { 'ba'	: 'ba',
              'bb':  {	'bba'	: ['bba', 'ccc'],
												'bbb'	:	'ffff',}
		}}
	browse(beta=True)




















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
