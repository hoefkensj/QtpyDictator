#!/usr/bin/env python

from myPyQt.lib import gui
from myPyQt.lib.QModules import QHIncDec,QHSearch, QEditProp
from pyDictatorQt import browse
GUI=gui.make('TEST')
GUI['Elements'](QEditProp.make('Key'))
GUI['Elements'](QEditProp.make('Val'))
# GUI['Elements'](QHIncDec.make('ColEx'))


# GUI['Elements'](QSearch.make_QSearch('SearchTree'))
# GUI['Elements'](QSearch.make_QSearchCtl('Search'))
# GUI['Elements'](QHSearch.make('TrSearch'))
# GUI['Fnx']['Add'](  QtWgt.make('trw_RegEx',))
# GUI['Elements'](elements.make_iBtn('Search'))
# GUI['Elements'] |= elements.iBtn('Edit',lbl='test')
# GUI['Elements'] |= QtWgt.make(n='txt_EditProp')
# GUI['Elements'] |= elements.chkBox('RegEx')
# GUI['Elements'] |= QtWgt.make(n='chk_RegEx',)
# GUI['Elements'] |= QtWgt.make(n='trw_Tree')
# GUI['Elements'] |= QtWgt.make(n='lbl_Tree')
# GUI['Elements']['lbl_Tree']['Mtd']['setText']('Tree')

browse(UI=GUI)

GUI['Run']()
