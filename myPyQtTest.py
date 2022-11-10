#!/usr/bin/env python

from myPyQt.lib import QtWgt,tree,elements,gui


GUI=gui.Gui()

GUI['Elements'] |= elements.iBtn('Search')
GUI['Elements'] |= elements.iBtn('Edit',lbl='test')
GUI['Elements'] |= QtWgt.make(n='txt_Tree')
# GUI['Elements'] |= elements.chkBox('RegEx')
GUI['Elements'] |= QtWgt.make(n='chk_RegEx',)
GUI['Elements'] |= QtWgt.make(n='trw_Tree')
GUI['Run']()