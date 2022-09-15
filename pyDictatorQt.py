#!/usr/bin/env python
from PyQt5 import QtCore, QtGui, QtWidgets
import os, types

def Wgt(n=None, t='h'):
	wgt=None
	lay=None
	def create(wgt,lay):
		wgt = QtWidgets.QWidget()
		if t == 'h':
			lay = QtWidgets.QHBoxLayout(wgt)
		elif t == 'v':
			lay = QtWidgets.QVBoxLayout(wgt)
		return wgt,lay
	def init(wgt,lay):
		wgt.setObjectName(f'wgt{n}')
		lay.setObjectName(f'lay{n}')
		wgt.setContentsMargins(0, 0, 0, 0)
		lay.setContentsMargins(0, 0, 0, 0)
		lay.setSpacing(0)
		return wgt,lay
	wgt, lay = create(wgt,lay)
	wgt, lay = init(wgt, lay)
	return wgt,lay

def make_icon(n=None, set='Fluent'):
	icon = QtGui.QIcon()
	lset = f'/home/hoefkens/.local/share/icons/{set}/symbolic/actions/{n}.svg'
	dset = f'/home/hoefkens/.local/share/icons/{set}-dark/symbolic/actions/{n}.svg'
	icon.addPixmap(QtGui.QPixmap(dset), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	icon.addPixmap(QtGui.QPixmap(lset), QtGui.QIcon.Normal, QtGui.QIcon.On)
	return icon



class QtGui(object):
	def GreateUi(self,Ui):
