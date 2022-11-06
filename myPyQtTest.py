#!/usr/bin/env python

from myPyQt.lib import QtWgt,tree,elements,gui


GUI=gui.Gui()

GUI['Elements'] |= elements.iBtn(n='Search')
GUI['Elements'] |= elements.iBtn(n='Edit')
GUI['Elements'] |= QtWgt.make(n='txt_Tree')
GUI['Elements'] |= elements.chkBox(n='RegEx')
GUI['Elements'] |= QtWgt.make(n='wgt_RegEx2')
GUI['Elements'] |= QtWgt.make(n='trw_Tree')
GUI['Run']()