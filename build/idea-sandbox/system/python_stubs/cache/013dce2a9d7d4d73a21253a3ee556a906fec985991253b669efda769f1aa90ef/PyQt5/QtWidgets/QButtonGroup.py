# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QButtonGroup(__PyQt5_QtCore.QObject):
    """ QButtonGroup(parent: QObject = None) """
    def addButton(self, QAbstractButton, id=-1): # real signature unknown; restored from __doc__
        """ addButton(self, QAbstractButton, id: int = -1) """
        pass

    def button(self, p_int): # real signature unknown; restored from __doc__
        """ button(self, int) -> QAbstractButton """
        return QAbstractButton

    def buttonClicked(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        buttonClicked(self, QAbstractButton) [signal]
        buttonClicked(self, int) [signal]
        """
        pass

    def buttonPressed(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        buttonPressed(self, QAbstractButton) [signal]
        buttonPressed(self, int) [signal]
        """
        pass

    def buttonReleased(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        buttonReleased(self, QAbstractButton) [signal]
        buttonReleased(self, int) [signal]
        """
        pass

    def buttons(self): # real signature unknown; restored from __doc__
        """ buttons(self) -> List[QAbstractButton] """
        return []

    def buttonToggled(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        buttonToggled(self, QAbstractButton, bool) [signal]
        buttonToggled(self, int, bool) [signal]
        """
        pass

    def checkedButton(self): # real signature unknown; restored from __doc__
        """ checkedButton(self) -> QAbstractButton """
        return QAbstractButton

    def checkedId(self): # real signature unknown; restored from __doc__
        """ checkedId(self) -> int """
        return 0

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def exclusive(self): # real signature unknown; restored from __doc__
        """ exclusive(self) -> bool """
        return False

    def id(self, QAbstractButton): # real signature unknown; restored from __doc__
        """ id(self, QAbstractButton) -> int """
        return 0

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeButton(self, QAbstractButton): # real signature unknown; restored from __doc__
        """ removeButton(self, QAbstractButton) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setExclusive(self, bool): # real signature unknown; restored from __doc__
        """ setExclusive(self, bool) """
        pass

    def setId(self, QAbstractButton, p_int): # real signature unknown; restored from __doc__
        """ setId(self, QAbstractButton, int) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


