# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QInputMethod(__PyQt5_QtCore.QObject):
    # no doc
    def anchorRectangle(self): # real signature unknown; restored from __doc__
        """ anchorRectangle(self) -> QRectF """
        pass

    def anchorRectangleChanged(self): # real signature unknown; restored from __doc__
        """ anchorRectangleChanged(self) [signal] """
        pass

    def animatingChanged(self): # real signature unknown; restored from __doc__
        """ animatingChanged(self) [signal] """
        pass

    def commit(self): # real signature unknown; restored from __doc__
        """ commit(self) """
        pass

    def cursorRectangle(self): # real signature unknown; restored from __doc__
        """ cursorRectangle(self) -> QRectF """
        pass

    def cursorRectangleChanged(self): # real signature unknown; restored from __doc__
        """ cursorRectangleChanged(self) [signal] """
        pass

    def hide(self): # real signature unknown; restored from __doc__
        """ hide(self) """
        pass

    def inputDirection(self): # real signature unknown; restored from __doc__
        """ inputDirection(self) -> Qt.LayoutDirection """
        pass

    def inputDirectionChanged(self, Qt_LayoutDirection): # real signature unknown; restored from __doc__
        """ inputDirectionChanged(self, Qt.LayoutDirection) [signal] """
        pass

    def inputItemClipRectangle(self): # real signature unknown; restored from __doc__
        """ inputItemClipRectangle(self) -> QRectF """
        pass

    def inputItemClipRectangleChanged(self): # real signature unknown; restored from __doc__
        """ inputItemClipRectangleChanged(self) [signal] """
        pass

    def inputItemRectangle(self): # real signature unknown; restored from __doc__
        """ inputItemRectangle(self) -> QRectF """
        pass

    def inputItemTransform(self): # real signature unknown; restored from __doc__
        """ inputItemTransform(self) -> QTransform """
        return QTransform

    def invokeAction(self, QInputMethod_Action, p_int): # real signature unknown; restored from __doc__
        """ invokeAction(self, QInputMethod.Action, int) """
        pass

    def isAnimating(self): # real signature unknown; restored from __doc__
        """ isAnimating(self) -> bool """
        return False

    def isVisible(self): # real signature unknown; restored from __doc__
        """ isVisible(self) -> bool """
        return False

    def keyboardRectangle(self): # real signature unknown; restored from __doc__
        """ keyboardRectangle(self) -> QRectF """
        pass

    def keyboardRectangleChanged(self): # real signature unknown; restored from __doc__
        """ keyboardRectangleChanged(self) [signal] """
        pass

    def locale(self): # real signature unknown; restored from __doc__
        """ locale(self) -> QLocale """
        pass

    def localeChanged(self): # real signature unknown; restored from __doc__
        """ localeChanged(self) [signal] """
        pass

    def queryFocusObject(self, Qt_InputMethodQuery, Any): # real signature unknown; restored from __doc__
        """ queryFocusObject(Qt.InputMethodQuery, Any) -> Any """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def setInputItemRectangle(self, QRectF): # real signature unknown; restored from __doc__
        """ setInputItemRectangle(self, QRectF) """
        pass

    def setInputItemTransform(self, QTransform): # real signature unknown; restored from __doc__
        """ setInputItemTransform(self, QTransform) """
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ setVisible(self, bool) """
        pass

    def show(self): # real signature unknown; restored from __doc__
        """ show(self) """
        pass

    def update(self, Union, Qt_InputMethodQueries=None, Qt_InputMethodQuery=None): # real signature unknown; restored from __doc__
        """ update(self, Union[Qt.InputMethodQueries, Qt.InputMethodQuery]) """
        pass

    def visibleChanged(self): # real signature unknown; restored from __doc__
        """ visibleChanged(self) [signal] """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    Click = 0
    ContextMenu = 1


