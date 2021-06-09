# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QUndoStack(__PyQt5_QtCore.QObject):
    """ QUndoStack(parent: QObject = None) """
    def beginMacro(self, p_str): # real signature unknown; restored from __doc__
        """ beginMacro(self, str) """
        pass

    def canRedo(self): # real signature unknown; restored from __doc__
        """ canRedo(self) -> bool """
        return False

    def canRedoChanged(self, bool): # real signature unknown; restored from __doc__
        """ canRedoChanged(self, bool) [signal] """
        pass

    def canUndo(self): # real signature unknown; restored from __doc__
        """ canUndo(self) -> bool """
        return False

    def canUndoChanged(self, bool): # real signature unknown; restored from __doc__
        """ canUndoChanged(self, bool) [signal] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def cleanChanged(self, bool): # real signature unknown; restored from __doc__
        """ cleanChanged(self, bool) [signal] """
        pass

    def cleanIndex(self): # real signature unknown; restored from __doc__
        """ cleanIndex(self) -> int """
        return 0

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def command(self, p_int): # real signature unknown; restored from __doc__
        """ command(self, int) -> QUndoCommand """
        return QUndoCommand

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def createRedoAction(self, QObject, prefix=''): # real signature unknown; restored from __doc__
        """ createRedoAction(self, QObject, prefix: str = '') -> QAction """
        return QAction

    def createUndoAction(self, QObject, prefix=''): # real signature unknown; restored from __doc__
        """ createUndoAction(self, QObject, prefix: str = '') -> QAction """
        return QAction

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def endMacro(self): # real signature unknown; restored from __doc__
        """ endMacro(self) """
        pass

    def index(self): # real signature unknown; restored from __doc__
        """ index(self) -> int """
        return 0

    def indexChanged(self, p_int): # real signature unknown; restored from __doc__
        """ indexChanged(self, int) [signal] """
        pass

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def isClean(self): # real signature unknown; restored from __doc__
        """ isClean(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def push(self, QUndoCommand): # real signature unknown; restored from __doc__
        """ push(self, QUndoCommand) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def redo(self): # real signature unknown; restored from __doc__
        """ redo(self) """
        pass

    def redoText(self): # real signature unknown; restored from __doc__
        """ redoText(self) -> str """
        return ""

    def redoTextChanged(self, p_str): # real signature unknown; restored from __doc__
        """ redoTextChanged(self, str) [signal] """
        pass

    def resetClean(self): # real signature unknown; restored from __doc__
        """ resetClean(self) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setActive(self, active=True): # real signature unknown; restored from __doc__
        """ setActive(self, active: bool = True) """
        pass

    def setClean(self): # real signature unknown; restored from __doc__
        """ setClean(self) """
        pass

    def setIndex(self, p_int): # real signature unknown; restored from __doc__
        """ setIndex(self, int) """
        pass

    def setUndoLimit(self, p_int): # real signature unknown; restored from __doc__
        """ setUndoLimit(self, int) """
        pass

    def text(self, p_int): # real signature unknown; restored from __doc__
        """ text(self, int) -> str """
        return ""

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def undo(self): # real signature unknown; restored from __doc__
        """ undo(self) """
        pass

    def undoLimit(self): # real signature unknown; restored from __doc__
        """ undoLimit(self) -> int """
        return 0

    def undoText(self): # real signature unknown; restored from __doc__
        """ undoText(self) -> str """
        return ""

    def undoTextChanged(self, p_str): # real signature unknown; restored from __doc__
        """ undoTextChanged(self, str) [signal] """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass


