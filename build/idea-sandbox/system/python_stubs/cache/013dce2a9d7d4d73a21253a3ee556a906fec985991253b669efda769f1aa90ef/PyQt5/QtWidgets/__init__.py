# encoding: utf-8
# module PyQt5.QtWidgets
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


# Variables with simple values

QWIDGETSIZE_MAX = 16777215

# functions

def qDrawBorderPixmap(QPainter, QRect, QMargins, QPixmap): # real signature unknown; restored from __doc__
    """ qDrawBorderPixmap(QPainter, QRect, QMargins, QPixmap) """
    pass

def qDrawPlainRect(QPainter, p_int, p_int_1, p_int_2, p_int_3, Union, QColor=None, Qt_GlobalColor=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    qDrawPlainRect(QPainter, int, int, int, int, Union[QColor, Qt.GlobalColor], lineWidth: int = 1, fill: Union[QBrush, QColor, Qt.GlobalColor, QGradient] = None)
    qDrawPlainRect(QPainter, QRect, Union[QColor, Qt.GlobalColor, QGradient], lineWidth: int = 1, fill: Union[QBrush, QColor, Qt.GlobalColor, QGradient] = None)
    """
    pass

def qDrawShadeLine(QPainter, p_int, p_int_1, p_int_2, p_int_3, QPalette, sunken=True, lineWidth=1, midLineWidth=0): # real signature unknown; restored from __doc__
    """
    qDrawShadeLine(QPainter, int, int, int, int, QPalette, sunken: bool = True, lineWidth: int = 1, midLineWidth: int = 0)
    qDrawShadeLine(QPainter, QPoint, QPoint, QPalette, sunken: bool = True, lineWidth: int = 1, midLineWidth: int = 0)
    """
    pass

def qDrawShadePanel(QPainter, p_int, p_int_1, p_int_2, p_int_3, QPalette, sunken=False, lineWidth=1, fill, QBrush=None, QColor=None, Qt_GlobalColor=None, QGradient=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    qDrawShadePanel(QPainter, int, int, int, int, QPalette, sunken: bool = False, lineWidth: int = 1, fill: Union[QBrush, QColor, Qt.GlobalColor, QGradient] = None)
    qDrawShadePanel(QPainter, QRect, QPalette, sunken: bool = False, lineWidth: int = 1, fill: Union[QBrush, QColor, Qt.GlobalColor, QGradient] = None)
    """
    pass

def qDrawShadeRect(QPainter, p_int, p_int_1, p_int_2, p_int_3, QPalette, sunken=False, lineWidth=1, midLineWidth=0, fill, QBrush=None, QColor=None, Qt_GlobalColor=None, QGradient=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    qDrawShadeRect(QPainter, int, int, int, int, QPalette, sunken: bool = False, lineWidth: int = 1, midLineWidth: int = 0, fill: Union[QBrush, QColor, Qt.GlobalColor, QGradient] = None)
    qDrawShadeRect(QPainter, QRect, QPalette, sunken: bool = False, lineWidth: int = 1, midLineWidth: int = 0, fill: Union[QBrush, QColor, Qt.GlobalColor, QGradient] = None)
    """
    pass

def qDrawWinButton(QPainter, p_int, p_int_1, p_int_2, p_int_3, QPalette, sunken=False, fill, QBrush=None, QColor=None, Qt_GlobalColor=None, QGradient=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    qDrawWinButton(QPainter, int, int, int, int, QPalette, sunken: bool = False, fill: Union[QBrush, QColor, Qt.GlobalColor, QGradient] = None)
    qDrawWinButton(QPainter, QRect, QPalette, sunken: bool = False, fill: Union[QBrush, QColor, Qt.GlobalColor, QGradient] = None)
    """
    pass

def qDrawWinPanel(QPainter, p_int, p_int_1, p_int_2, p_int_3, QPalette, sunken=False, fill, QBrush=None, QColor=None, Qt_GlobalColor=None, QGradient=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    qDrawWinPanel(QPainter, int, int, int, int, QPalette, sunken: bool = False, fill: Union[QBrush, QColor, Qt.GlobalColor, QGradient] = None)
    qDrawWinPanel(QPainter, QRect, QPalette, sunken: bool = False, fill: Union[QBrush, QColor, Qt.GlobalColor, QGradient] = None)
    """
    pass

# classes

from .QWidget import QWidget
from .QAbstractButton import QAbstractButton
from .QGraphicsItem import QGraphicsItem
from .QAbstractGraphicsShapeItem import QAbstractGraphicsShapeItem
from .QAbstractItemDelegate import QAbstractItemDelegate
from .QFrame import QFrame
from .QAbstractScrollArea import QAbstractScrollArea
from .QAbstractItemView import QAbstractItemView
from .QAbstractSlider import QAbstractSlider
from .QAbstractSpinBox import QAbstractSpinBox
from .QAction import QAction
from .QActionGroup import QActionGroup
from .QApplication import QApplication
from .QLayoutItem import QLayoutItem
from .QLayout import QLayout
from .QBoxLayout import QBoxLayout
from .QButtonGroup import QButtonGroup
from .QCalendarWidget import QCalendarWidget
from .QCheckBox import QCheckBox
from .QDialog import QDialog
from .QColorDialog import QColorDialog
from .QColumnView import QColumnView
from .QComboBox import QComboBox
from .QPushButton import QPushButton
from .QCommandLinkButton import QCommandLinkButton
from .QStyle import QStyle
from .QCommonStyle import QCommonStyle
from .QCompleter import QCompleter
from .QDataWidgetMapper import QDataWidgetMapper
from .QDateTimeEdit import QDateTimeEdit
from .QDateEdit import QDateEdit
from .QDesktopWidget import QDesktopWidget
from .QDial import QDial
from .QDialogButtonBox import QDialogButtonBox
from .QDirModel import QDirModel
from .QDockWidget import QDockWidget
from .QDoubleSpinBox import QDoubleSpinBox
from .QErrorMessage import QErrorMessage
from .QFileDialog import QFileDialog
from .QFileIconProvider import QFileIconProvider
from .QFileSystemModel import QFileSystemModel
from .QFocusFrame import QFocusFrame
from .QFontComboBox import QFontComboBox
from .QFontDialog import QFontDialog
from .QFormLayout import QFormLayout
from .QGesture import QGesture
from .QGestureEvent import QGestureEvent
from .QGestureRecognizer import QGestureRecognizer
from .QGraphicsAnchor import QGraphicsAnchor
from .QGraphicsLayoutItem import QGraphicsLayoutItem
from .QGraphicsLayout import QGraphicsLayout
from .QGraphicsAnchorLayout import QGraphicsAnchorLayout
from .QGraphicsEffect import QGraphicsEffect
from .QGraphicsBlurEffect import QGraphicsBlurEffect
from .QGraphicsColorizeEffect import QGraphicsColorizeEffect
from .QGraphicsDropShadowEffect import QGraphicsDropShadowEffect
from .QGraphicsEllipseItem import QGraphicsEllipseItem
from .QGraphicsGridLayout import QGraphicsGridLayout
from .QGraphicsItemGroup import QGraphicsItemGroup
from .QGraphicsLinearLayout import QGraphicsLinearLayout
from .QGraphicsLineItem import QGraphicsLineItem
from .QGraphicsObject import QGraphicsObject
from .QGraphicsOpacityEffect import QGraphicsOpacityEffect
from .QGraphicsPathItem import QGraphicsPathItem
from .QGraphicsPixmapItem import QGraphicsPixmapItem
from .QGraphicsPolygonItem import QGraphicsPolygonItem
from .QGraphicsWidget import QGraphicsWidget
from .QGraphicsProxyWidget import QGraphicsProxyWidget
from .QGraphicsRectItem import QGraphicsRectItem
from .QGraphicsTransform import QGraphicsTransform
from .QGraphicsRotation import QGraphicsRotation
from .QGraphicsScale import QGraphicsScale
from .QGraphicsScene import QGraphicsScene
from .QGraphicsSceneEvent import QGraphicsSceneEvent
from .QGraphicsSceneContextMenuEvent import QGraphicsSceneContextMenuEvent
from .QGraphicsSceneDragDropEvent import QGraphicsSceneDragDropEvent
from .QGraphicsSceneHelpEvent import QGraphicsSceneHelpEvent
from .QGraphicsSceneHoverEvent import QGraphicsSceneHoverEvent
from .QGraphicsSceneMouseEvent import QGraphicsSceneMouseEvent
from .QGraphicsSceneMoveEvent import QGraphicsSceneMoveEvent
from .QGraphicsSceneResizeEvent import QGraphicsSceneResizeEvent
from .QGraphicsSceneWheelEvent import QGraphicsSceneWheelEvent
from .QGraphicsSimpleTextItem import QGraphicsSimpleTextItem
from .QGraphicsTextItem import QGraphicsTextItem
from .QGraphicsView import QGraphicsView
from .QGridLayout import QGridLayout
from .QGroupBox import QGroupBox
from .QHBoxLayout import QHBoxLayout
from .QHeaderView import QHeaderView
from .QInputDialog import QInputDialog
from .QItemDelegate import QItemDelegate
from .QItemEditorCreatorBase import QItemEditorCreatorBase
from .QItemEditorFactory import QItemEditorFactory
from .QKeyEventTransition import QKeyEventTransition
from .QKeySequenceEdit import QKeySequenceEdit
from .QLabel import QLabel
from .QLCDNumber import QLCDNumber
from .QLineEdit import QLineEdit
from .QListView import QListView
from .QListWidget import QListWidget
from .QListWidgetItem import QListWidgetItem
from .QMainWindow import QMainWindow
from .QMdiArea import QMdiArea
from .QMdiSubWindow import QMdiSubWindow
from .QMenu import QMenu
from .QMenuBar import QMenuBar
from .QMessageBox import QMessageBox
from .QMouseEventTransition import QMouseEventTransition
from .QOpenGLWidget import QOpenGLWidget
from .QPanGesture import QPanGesture
from .QPinchGesture import QPinchGesture
from .QPlainTextDocumentLayout import QPlainTextDocumentLayout
from .QPlainTextEdit import QPlainTextEdit
from .QProgressBar import QProgressBar
from .QProgressDialog import QProgressDialog
from .QProxyStyle import QProxyStyle
from .QRadioButton import QRadioButton
from .QRubberBand import QRubberBand
from .QScrollArea import QScrollArea
from .QScrollBar import QScrollBar
from .QScroller import QScroller
from .QScrollerProperties import QScrollerProperties
from .QShortcut import QShortcut
from .QSizeGrip import QSizeGrip
from .QSizePolicy import QSizePolicy
from .QSlider import QSlider
from .QSpacerItem import QSpacerItem
from .QSpinBox import QSpinBox
from .QSplashScreen import QSplashScreen
from .QSplitter import QSplitter
from .QSplitterHandle import QSplitterHandle
from .QStackedLayout import QStackedLayout
from .QStackedWidget import QStackedWidget
from .QStatusBar import QStatusBar
from .QStyledItemDelegate import QStyledItemDelegate
from .QStyleFactory import QStyleFactory
from .QStyleHintReturn import QStyleHintReturn
from .QStyleHintReturnMask import QStyleHintReturnMask
from .QStyleHintReturnVariant import QStyleHintReturnVariant
from .QStyleOption import QStyleOption
from .QStyleOptionButton import QStyleOptionButton
from .QStyleOptionComplex import QStyleOptionComplex
from .QStyleOptionComboBox import QStyleOptionComboBox
from .QStyleOptionDockWidget import QStyleOptionDockWidget
from .QStyleOptionFocusRect import QStyleOptionFocusRect
from .QStyleOptionFrame import QStyleOptionFrame
from .QStyleOptionGraphicsItem import QStyleOptionGraphicsItem
from .QStyleOptionGroupBox import QStyleOptionGroupBox
from .QStyleOptionHeader import QStyleOptionHeader
from .QStyleOptionMenuItem import QStyleOptionMenuItem
from .QStyleOptionProgressBar import QStyleOptionProgressBar
from .QStyleOptionRubberBand import QStyleOptionRubberBand
from .QStyleOptionSizeGrip import QStyleOptionSizeGrip
from .QStyleOptionSlider import QStyleOptionSlider
from .QStyleOptionSpinBox import QStyleOptionSpinBox
from .QStyleOptionTab import QStyleOptionTab
from .QStyleOptionTabBarBase import QStyleOptionTabBarBase
from .QStyleOptionTabWidgetFrame import QStyleOptionTabWidgetFrame
from .QStyleOptionTitleBar import QStyleOptionTitleBar
from .QStyleOptionToolBar import QStyleOptionToolBar
from .QStyleOptionToolBox import QStyleOptionToolBox
from .QStyleOptionToolButton import QStyleOptionToolButton
from .QStyleOptionViewItem import QStyleOptionViewItem
from .QStylePainter import QStylePainter
from .QSwipeGesture import QSwipeGesture
from .QSystemTrayIcon import QSystemTrayIcon
from .QTabBar import QTabBar
from .QTableView import QTableView
from .QTableWidget import QTableWidget
from .QTableWidgetItem import QTableWidgetItem
from .QTableWidgetSelectionRange import QTableWidgetSelectionRange
from .QTabWidget import QTabWidget
from .QTapAndHoldGesture import QTapAndHoldGesture
from .QTapGesture import QTapGesture
from .QTextEdit import QTextEdit
from .QTextBrowser import QTextBrowser
from .QTimeEdit import QTimeEdit
from .QToolBar import QToolBar
from .QToolBox import QToolBox
from .QToolButton import QToolButton
from .QToolTip import QToolTip
from .QTreeView import QTreeView
from .QTreeWidget import QTreeWidget
from .QTreeWidgetItem import QTreeWidgetItem
from .QTreeWidgetItemIterator import QTreeWidgetItemIterator
from .QUndoCommand import QUndoCommand
from .QUndoGroup import QUndoGroup
from .QUndoStack import QUndoStack
from .QUndoView import QUndoView
from .QVBoxLayout import QVBoxLayout
from .QWhatsThis import QWhatsThis
from .QWidgetAction import QWidgetAction
from .QWidgetItem import QWidgetItem
from .QWizard import QWizard
from .QWizardPage import QWizardPage
# variables with complex values

qApp = QApplication() # real value of type <class 'PyQt5.QtWidgets.QApplication'> replaced



