# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QLayout import QLayout

class QFormLayout(QLayout):
    """ QFormLayout(parent: QWidget = None) """
    def addChildLayout(self, *args, **kwargs): # real signature unknown
        pass

    def addChildWidget(self, *args, **kwargs): # real signature unknown
        pass

    def addItem(self, QLayoutItem): # real signature unknown; restored from __doc__
        """ addItem(self, QLayoutItem) """
        pass

    def addRow(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addRow(self, QWidget, QWidget)
        addRow(self, QWidget, QLayout)
        addRow(self, str, QWidget)
        addRow(self, str, QLayout)
        addRow(self, QWidget)
        addRow(self, QLayout)
        """
        pass

    def alignmentRect(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def expandingDirections(self): # real signature unknown; restored from __doc__
        """ expandingDirections(self) -> Qt.Orientations """
        pass

    def fieldGrowthPolicy(self): # real signature unknown; restored from __doc__
        """ fieldGrowthPolicy(self) -> QFormLayout.FieldGrowthPolicy """
        pass

    def formAlignment(self): # real signature unknown; restored from __doc__
        """ formAlignment(self) -> Qt.Alignment """
        pass

    def getItemPosition(self, p_int): # real signature unknown; restored from __doc__
        """ getItemPosition(self, int) -> Tuple[int, QFormLayout.ItemRole] """
        pass

    def getLayoutPosition(self, QLayout): # real signature unknown; restored from __doc__
        """ getLayoutPosition(self, QLayout) -> Tuple[int, QFormLayout.ItemRole] """
        pass

    def getWidgetPosition(self, QWidget): # real signature unknown; restored from __doc__
        """ getWidgetPosition(self, QWidget) -> Tuple[int, QFormLayout.ItemRole] """
        pass

    def hasHeightForWidth(self): # real signature unknown; restored from __doc__
        """ hasHeightForWidth(self) -> bool """
        return False

    def heightForWidth(self, p_int): # real signature unknown; restored from __doc__
        """ heightForWidth(self, int) -> int """
        return 0

    def horizontalSpacing(self): # real signature unknown; restored from __doc__
        """ horizontalSpacing(self) -> int """
        return 0

    def insertRow(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insertRow(self, int, QWidget, QWidget)
        insertRow(self, int, QWidget, QLayout)
        insertRow(self, int, str, QWidget)
        insertRow(self, int, str, QLayout)
        insertRow(self, int, QWidget)
        insertRow(self, int, QLayout)
        """
        pass

    def invalidate(self): # real signature unknown; restored from __doc__
        """ invalidate(self) """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def itemAt(self, p_int, QFormLayout_ItemRole=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        itemAt(self, int, QFormLayout.ItemRole) -> QLayoutItem
        itemAt(self, int) -> QLayoutItem
        """
        return QLayoutItem

    def labelAlignment(self): # real signature unknown; restored from __doc__
        """ labelAlignment(self) -> Qt.Alignment """
        pass

    def labelForField(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        labelForField(self, QWidget) -> QWidget
        labelForField(self, QLayout) -> QWidget
        """
        return QWidget

    def minimumSize(self): # real signature unknown; restored from __doc__
        """ minimumSize(self) -> QSize """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeRow(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        removeRow(self, int)
        removeRow(self, QWidget)
        removeRow(self, QLayout)
        """
        pass

    def rowCount(self): # real signature unknown; restored from __doc__
        """ rowCount(self) -> int """
        return 0

    def rowWrapPolicy(self): # real signature unknown; restored from __doc__
        """ rowWrapPolicy(self) -> QFormLayout.RowWrapPolicy """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setFieldGrowthPolicy(self, QFormLayout_FieldGrowthPolicy): # real signature unknown; restored from __doc__
        """ setFieldGrowthPolicy(self, QFormLayout.FieldGrowthPolicy) """
        pass

    def setFormAlignment(self, Union, Qt_Alignment=None, Qt_AlignmentFlag=None): # real signature unknown; restored from __doc__
        """ setFormAlignment(self, Union[Qt.Alignment, Qt.AlignmentFlag]) """
        pass

    def setGeometry(self, QRect): # real signature unknown; restored from __doc__
        """ setGeometry(self, QRect) """
        pass

    def setHorizontalSpacing(self, p_int): # real signature unknown; restored from __doc__
        """ setHorizontalSpacing(self, int) """
        pass

    def setItem(self, p_int, QFormLayout_ItemRole, QLayoutItem): # real signature unknown; restored from __doc__
        """ setItem(self, int, QFormLayout.ItemRole, QLayoutItem) """
        pass

    def setLabelAlignment(self, Union, Qt_Alignment=None, Qt_AlignmentFlag=None): # real signature unknown; restored from __doc__
        """ setLabelAlignment(self, Union[Qt.Alignment, Qt.AlignmentFlag]) """
        pass

    def setLayout(self, p_int, QFormLayout_ItemRole, QLayout): # real signature unknown; restored from __doc__
        """ setLayout(self, int, QFormLayout.ItemRole, QLayout) """
        pass

    def setRowWrapPolicy(self, QFormLayout_RowWrapPolicy): # real signature unknown; restored from __doc__
        """ setRowWrapPolicy(self, QFormLayout.RowWrapPolicy) """
        pass

    def setSpacing(self, p_int): # real signature unknown; restored from __doc__
        """ setSpacing(self, int) """
        pass

    def setVerticalSpacing(self, p_int): # real signature unknown; restored from __doc__
        """ setVerticalSpacing(self, int) """
        pass

    def setWidget(self, p_int, QFormLayout_ItemRole, QWidget): # real signature unknown; restored from __doc__
        """ setWidget(self, int, QFormLayout.ItemRole, QWidget) """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> QSize """
        pass

    def spacing(self): # real signature unknown; restored from __doc__
        """ spacing(self) -> int """
        return 0

    def takeAt(self, p_int): # real signature unknown; restored from __doc__
        """ takeAt(self, int) -> QLayoutItem """
        return QLayoutItem

    def takeRow(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        takeRow(self, int) -> QFormLayout.TakeRowResult
        takeRow(self, QWidget) -> QFormLayout.TakeRowResult
        takeRow(self, QLayout) -> QFormLayout.TakeRowResult
        """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def verticalSpacing(self): # real signature unknown; restored from __doc__
        """ verticalSpacing(self) -> int """
        return 0

    def widgetEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    AllNonFixedFieldsGrow = 2
    DontWrapRows = 0
    ExpandingFieldsGrow = 1
    FieldRole = 1
    FieldsStayAtSizeHint = 0
    LabelRole = 0
    SpanningRole = 2
    WrapAllRows = 2
    WrapLongRows = 1


