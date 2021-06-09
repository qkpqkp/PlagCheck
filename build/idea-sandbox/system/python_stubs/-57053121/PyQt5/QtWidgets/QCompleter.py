# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QCompleter(__PyQt5_QtCore.QObject):
    """
    QCompleter(parent: QObject = None)
    QCompleter(QAbstractItemModel, parent: QObject = None)
    QCompleter(Iterable[str], parent: QObject = None)
    """
    def activated(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        activated(self, str) [signal]
        activated(self, QModelIndex) [signal]
        """
        pass

    def caseSensitivity(self): # real signature unknown; restored from __doc__
        """ caseSensitivity(self) -> Qt.CaseSensitivity """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def complete(self, rect=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ complete(self, rect: QRect = QRect()) """
        pass

    def completionColumn(self): # real signature unknown; restored from __doc__
        """ completionColumn(self) -> int """
        return 0

    def completionCount(self): # real signature unknown; restored from __doc__
        """ completionCount(self) -> int """
        return 0

    def completionMode(self): # real signature unknown; restored from __doc__
        """ completionMode(self) -> QCompleter.CompletionMode """
        pass

    def completionModel(self): # real signature unknown; restored from __doc__
        """ completionModel(self) -> QAbstractItemModel """
        pass

    def completionPrefix(self): # real signature unknown; restored from __doc__
        """ completionPrefix(self) -> str """
        return ""

    def completionRole(self): # real signature unknown; restored from __doc__
        """ completionRole(self) -> int """
        return 0

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def currentCompletion(self): # real signature unknown; restored from __doc__
        """ currentCompletion(self) -> str """
        return ""

    def currentIndex(self): # real signature unknown; restored from __doc__
        """ currentIndex(self) -> QModelIndex """
        pass

    def currentRow(self): # real signature unknown; restored from __doc__
        """ currentRow(self) -> int """
        return 0

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, QEvent): # real signature unknown; restored from __doc__
        """ event(self, QEvent) -> bool """
        return False

    def eventFilter(self, QObject, QEvent): # real signature unknown; restored from __doc__
        """ eventFilter(self, QObject, QEvent) -> bool """
        return False

    def filterMode(self): # real signature unknown; restored from __doc__
        """ filterMode(self) -> Qt.MatchFlags """
        pass

    def highlighted(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        highlighted(self, str) [signal]
        highlighted(self, QModelIndex) [signal]
        """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def maxVisibleItems(self): # real signature unknown; restored from __doc__
        """ maxVisibleItems(self) -> int """
        return 0

    def model(self): # real signature unknown; restored from __doc__
        """ model(self) -> QAbstractItemModel """
        pass

    def modelSorting(self): # real signature unknown; restored from __doc__
        """ modelSorting(self) -> QCompleter.ModelSorting """
        pass

    def pathFromIndex(self, QModelIndex): # real signature unknown; restored from __doc__
        """ pathFromIndex(self, QModelIndex) -> str """
        return ""

    def popup(self): # real signature unknown; restored from __doc__
        """ popup(self) -> QAbstractItemView """
        return QAbstractItemView

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setCaseSensitivity(self, Qt_CaseSensitivity): # real signature unknown; restored from __doc__
        """ setCaseSensitivity(self, Qt.CaseSensitivity) """
        pass

    def setCompletionColumn(self, p_int): # real signature unknown; restored from __doc__
        """ setCompletionColumn(self, int) """
        pass

    def setCompletionMode(self, QCompleter_CompletionMode): # real signature unknown; restored from __doc__
        """ setCompletionMode(self, QCompleter.CompletionMode) """
        pass

    def setCompletionPrefix(self, p_str): # real signature unknown; restored from __doc__
        """ setCompletionPrefix(self, str) """
        pass

    def setCompletionRole(self, p_int): # real signature unknown; restored from __doc__
        """ setCompletionRole(self, int) """
        pass

    def setCurrentRow(self, p_int): # real signature unknown; restored from __doc__
        """ setCurrentRow(self, int) -> bool """
        return False

    def setFilterMode(self, Union, Qt_MatchFlags=None, Qt_MatchFlag=None): # real signature unknown; restored from __doc__
        """ setFilterMode(self, Union[Qt.MatchFlags, Qt.MatchFlag]) """
        pass

    def setMaxVisibleItems(self, p_int): # real signature unknown; restored from __doc__
        """ setMaxVisibleItems(self, int) """
        pass

    def setModel(self, QAbstractItemModel): # real signature unknown; restored from __doc__
        """ setModel(self, QAbstractItemModel) """
        pass

    def setModelSorting(self, QCompleter_ModelSorting): # real signature unknown; restored from __doc__
        """ setModelSorting(self, QCompleter.ModelSorting) """
        pass

    def setPopup(self, QAbstractItemView): # real signature unknown; restored from __doc__
        """ setPopup(self, QAbstractItemView) """
        pass

    def setWidget(self, QWidget): # real signature unknown; restored from __doc__
        """ setWidget(self, QWidget) """
        pass

    def setWrapAround(self, bool): # real signature unknown; restored from __doc__
        """ setWrapAround(self, bool) """
        pass

    def splitPath(self, p_str): # real signature unknown; restored from __doc__
        """ splitPath(self, str) -> List[str] """
        return []

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def widget(self): # real signature unknown; restored from __doc__
        """ widget(self) -> QWidget """
        return QWidget

    def wrapAround(self): # real signature unknown; restored from __doc__
        """ wrapAround(self) -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    CaseInsensitivelySortedModel = 2
    CaseSensitivelySortedModel = 1
    InlineCompletion = 2
    PopupCompletion = 0
    UnfilteredPopupCompletion = 1
    UnsortedModel = 0


