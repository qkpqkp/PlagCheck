# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QItemEditorFactory(__sip.wrapper):
    """
    QItemEditorFactory()
    QItemEditorFactory(QItemEditorFactory)
    """
    def createEditor(self, p_int, QWidget): # real signature unknown; restored from __doc__
        """ createEditor(self, int, QWidget) -> QWidget """
        return QWidget

    def defaultFactory(self): # real signature unknown; restored from __doc__
        """ defaultFactory() -> QItemEditorFactory """
        return QItemEditorFactory

    def registerEditor(self, p_int, QItemEditorCreatorBase): # real signature unknown; restored from __doc__
        """ registerEditor(self, int, QItemEditorCreatorBase) """
        pass

    def setDefaultFactory(self, QItemEditorFactory): # real signature unknown; restored from __doc__
        """ setDefaultFactory(QItemEditorFactory) """
        pass

    def valuePropertyName(self, p_int): # real signature unknown; restored from __doc__
        """ valuePropertyName(self, int) -> QByteArray """
        pass

    def __init__(self, QItemEditorFactory=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



