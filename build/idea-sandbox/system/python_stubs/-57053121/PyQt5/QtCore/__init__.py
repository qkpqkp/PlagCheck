# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


# Variables with simple values

PYQT_VERSION = 330755

PYQT_VERSION_STR = '5.12.3'

QtCriticalMsg = 2
QtDebugMsg = 0
QtFatalMsg = 3
QtInfoMsg = 4
QtSystemMsg = 2
QtWarningMsg = 1

QT_VERSION = 330760

QT_VERSION_STR = '5.12.8'

# functions

def bin_(QTextStream): # real signature unknown; restored from __doc__
    """ bin_(QTextStream) -> QTextStream """
    return QTextStream

def bom(QTextStream): # real signature unknown; restored from __doc__
    """ bom(QTextStream) -> QTextStream """
    return QTextStream

def center(QTextStream): # real signature unknown; restored from __doc__
    """ center(QTextStream) -> QTextStream """
    return QTextStream

def dec(QTextStream): # real signature unknown; restored from __doc__
    """ dec(QTextStream) -> QTextStream """
    return QTextStream

def endl(QTextStream): # real signature unknown; restored from __doc__
    """ endl(QTextStream) -> QTextStream """
    return QTextStream

def fixed(QTextStream): # real signature unknown; restored from __doc__
    """ fixed(QTextStream) -> QTextStream """
    return QTextStream

def flush(QTextStream): # real signature unknown; restored from __doc__
    """ flush(QTextStream) -> QTextStream """
    return QTextStream

def forcepoint(QTextStream): # real signature unknown; restored from __doc__
    """ forcepoint(QTextStream) -> QTextStream """
    return QTextStream

def forcesign(QTextStream): # real signature unknown; restored from __doc__
    """ forcesign(QTextStream) -> QTextStream """
    return QTextStream

def hex_(QTextStream): # real signature unknown; restored from __doc__
    """ hex_(QTextStream) -> QTextStream """
    return QTextStream

def left(QTextStream): # real signature unknown; restored from __doc__
    """ left(QTextStream) -> QTextStream """
    return QTextStream

def lowercasebase(QTextStream): # real signature unknown; restored from __doc__
    """ lowercasebase(QTextStream) -> QTextStream """
    return QTextStream

def lowercasedigits(QTextStream): # real signature unknown; restored from __doc__
    """ lowercasedigits(QTextStream) -> QTextStream """
    return QTextStream

def noforcepoint(QTextStream): # real signature unknown; restored from __doc__
    """ noforcepoint(QTextStream) -> QTextStream """
    return QTextStream

def noforcesign(QTextStream): # real signature unknown; restored from __doc__
    """ noforcesign(QTextStream) -> QTextStream """
    return QTextStream

def noshowbase(QTextStream): # real signature unknown; restored from __doc__
    """ noshowbase(QTextStream) -> QTextStream """
    return QTextStream

def oct_(QTextStream): # real signature unknown; restored from __doc__
    """ oct_(QTextStream) -> QTextStream """
    return QTextStream

def pyqtPickleProtocol(): # real signature unknown; restored from __doc__
    """ pyqtPickleProtocol() -> Optional[int] """
    pass

def pyqtRemoveInputHook(): # real signature unknown; restored from __doc__
    """ pyqtRemoveInputHook() """
    pass

def pyqtRestoreInputHook(): # real signature unknown; restored from __doc__
    """ pyqtRestoreInputHook() """
    pass

def pyqtSetPickleProtocol(Optional, p_int=None): # real signature unknown; restored from __doc__
    """ pyqtSetPickleProtocol(Optional[int]) """
    pass

def pyqtSlot(*types, name, p_str=None, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    @pyqtSlot(*types, name: Optional[str], result: Optional[str])
    
    This is a decorator applied to Python methods of a QObject that marks them
    as Qt slots.
    The non-keyword arguments are the types of the slot arguments and each may
    be a Python type object or a string specifying a C++ type.
    name is the name of the slot and defaults to the name of the method.
    result is type of the value returned by the slot.
    """
    pass

def qAbs(p_float): # real signature unknown; restored from __doc__
    """ qAbs(float) -> float """
    return 0.0

def qAddPostRoutine(Callable, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ qAddPostRoutine(Callable[..., None]) """
    pass

def qAddPreRoutine(Callable, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ qAddPreRoutine(Callable[[], None]) """
    pass

def qChecksum(bytes): # real signature unknown; restored from __doc__
    """
    qChecksum(bytes) -> int
    qChecksum(bytes, Qt.ChecksumType) -> int
    """
    return 0

def qCompress(Union, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ qCompress(Union[QByteArray, bytes, bytearray], compressionLevel: int = -1) -> QByteArray """
    pass

def qCritical(p_str): # real signature unknown; restored from __doc__
    """ qCritical(str) """
    pass

def qDebug(p_str): # real signature unknown; restored from __doc__
    """ qDebug(str) """
    pass

def qEnvironmentVariable(p_str): # real signature unknown; restored from __doc__
    """
    qEnvironmentVariable(str) -> str
    qEnvironmentVariable(str, str) -> str
    """
    return ""

def qErrnoWarning(p_int, p_str): # real signature unknown; restored from __doc__
    """
    qErrnoWarning(int, str)
    qErrnoWarning(str)
    """
    pass

def qFatal(p_str): # real signature unknown; restored from __doc__
    """ qFatal(str) """
    pass

def qFloatDistance(p_float, p_float_1): # real signature unknown; restored from __doc__
    """ qFloatDistance(float, float) -> int """
    return 0

def qFormatLogMessage(QtMsgType, QMessageLogContext, p_str): # real signature unknown; restored from __doc__
    """ qFormatLogMessage(QtMsgType, QMessageLogContext, str) -> str """
    return ""

def qFuzzyCompare(p_float, p_float_1): # real signature unknown; restored from __doc__
    """ qFuzzyCompare(float, float) -> bool """
    return False

def qInf(): # real signature unknown; restored from __doc__
    """ qInf() -> float """
    return 0.0

def qInfo(p_str): # real signature unknown; restored from __doc__
    """ qInfo(str) """
    pass

def qInstallMessageHandler(Optional, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ qInstallMessageHandler(Optional[Callable[[QtMsgType, QMessageLogContext, str], None]]) -> Optional[Callable[[QtMsgType, QMessageLogContext, str], None]] """
    pass

def qIsFinite(p_float): # real signature unknown; restored from __doc__
    """ qIsFinite(float) -> bool """
    return False

def qIsInf(p_float): # real signature unknown; restored from __doc__
    """ qIsInf(float) -> bool """
    return False

def qIsNaN(p_float): # real signature unknown; restored from __doc__
    """ qIsNaN(float) -> bool """
    return False

def qIsNull(p_float): # real signature unknown; restored from __doc__
    """ qIsNull(float) -> bool """
    return False

def qQNaN(): # real signature unknown; restored from __doc__
    """ qQNaN() -> float """
    return 0.0

def qrand(): # real signature unknown; restored from __doc__
    """ qrand() -> int """
    return 0

def qRegisterResourceData(p_int, bytes, bytes_1, bytes_2): # real signature unknown; restored from __doc__
    """ qRegisterResourceData(int, bytes, bytes, bytes) -> bool """
    return False

def qRemovePostRoutine(Callable, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ qRemovePostRoutine(Callable[..., None]) """
    pass

def qRound(p_float): # real signature unknown; restored from __doc__
    """ qRound(float) -> int """
    return 0

def qRound64(p_float): # real signature unknown; restored from __doc__
    """ qRound64(float) -> int """
    return 0

def qSetFieldWidth(p_int): # real signature unknown; restored from __doc__
    """ qSetFieldWidth(int) -> QTextStreamManipulator """
    return QTextStreamManipulator

def qSetMessagePattern(p_str): # real signature unknown; restored from __doc__
    """ qSetMessagePattern(str) """
    pass

def qSetPadChar(p_str): # real signature unknown; restored from __doc__
    """ qSetPadChar(str) -> QTextStreamManipulator """
    return QTextStreamManipulator

def qSetRealNumberPrecision(p_int): # real signature unknown; restored from __doc__
    """ qSetRealNumberPrecision(int) -> QTextStreamManipulator """
    return QTextStreamManipulator

def qSharedBuild(): # real signature unknown; restored from __doc__
    """ qSharedBuild() -> bool """
    return False

def qSNaN(): # real signature unknown; restored from __doc__
    """ qSNaN() -> float """
    return 0.0

def qsrand(p_int): # real signature unknown; restored from __doc__
    """ qsrand(int) """
    pass

def QT_TRANSLATE_NOOP(p_str, p_str_1): # real signature unknown; restored from __doc__
    """ QT_TRANSLATE_NOOP(str, str) -> str """
    return ""

def QT_TR_NOOP(p_str): # real signature unknown; restored from __doc__
    """ QT_TR_NOOP(str) -> str """
    return ""

def QT_TR_NOOP_UTF8(p_str): # real signature unknown; restored from __doc__
    """ QT_TR_NOOP_UTF8(str) -> str """
    return ""

def qUncompress(Union, QByteArray=None, bytes=None, bytearray=None): # real signature unknown; restored from __doc__
    """ qUncompress(Union[QByteArray, bytes, bytearray]) -> QByteArray """
    return QByteArray

def qUnregisterResourceData(p_int, bytes, bytes_1, bytes_2): # real signature unknown; restored from __doc__
    """ qUnregisterResourceData(int, bytes, bytes, bytes) -> bool """
    return False

def qVersion(): # real signature unknown; restored from __doc__
    """ qVersion() -> str """
    return ""

def qWarning(p_str): # real signature unknown; restored from __doc__
    """ qWarning(str) """
    pass

def Q_ARG(p_object, p_object_1): # real signature unknown; restored from __doc__
    """ Q_ARG(object, object) -> QGenericArgument """
    return QGenericArgument

def Q_CLASSINFO(p_str, p_str_1): # real signature unknown; restored from __doc__
    """ Q_CLASSINFO(str, str) """
    pass

def Q_ENUM(Union, type=None, enum_Enum=None): # real signature unknown; restored from __doc__
    """ Q_ENUM(Union[type, enum.Enum]) """
    pass

def Q_ENUMS(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ Q_ENUMS(*) """
    pass

def Q_FLAG(Union, type=None, enum_Enum=None): # real signature unknown; restored from __doc__
    """ Q_FLAG(Union[type, enum.Enum]) """
    pass

def Q_FLAGS(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ Q_FLAGS(*) """
    pass

def Q_RETURN_ARG(p_object): # real signature unknown; restored from __doc__
    """ Q_RETURN_ARG(object) -> QGenericReturnArgument """
    return QGenericReturnArgument

def reset(QTextStream): # real signature unknown; restored from __doc__
    """ reset(QTextStream) -> QTextStream """
    return QTextStream

def right(QTextStream): # real signature unknown; restored from __doc__
    """ right(QTextStream) -> QTextStream """
    return QTextStream

def scientific(QTextStream): # real signature unknown; restored from __doc__
    """ scientific(QTextStream) -> QTextStream """
    return QTextStream

def showbase(QTextStream): # real signature unknown; restored from __doc__
    """ showbase(QTextStream) -> QTextStream """
    return QTextStream

def uppercasebase(QTextStream): # real signature unknown; restored from __doc__
    """ uppercasebase(QTextStream) -> QTextStream """
    return QTextStream

def uppercasedigits(QTextStream): # real signature unknown; restored from __doc__
    """ uppercasedigits(QTextStream) -> QTextStream """
    return QTextStream

def ws(QTextStream): # real signature unknown; restored from __doc__
    """ ws(QTextStream) -> QTextStream """
    return QTextStream

# classes

from .pyqtBoundSignal import pyqtBoundSignal
from .pyqtProperty import pyqtProperty
from .pyqtSignal import pyqtSignal
from .QObject import QObject
from .QAbstractAnimation import QAbstractAnimation
from .QAbstractEventDispatcher import QAbstractEventDispatcher
from .QAbstractItemModel import QAbstractItemModel
from .QAbstractListModel import QAbstractListModel
from .QAbstractNativeEventFilter import QAbstractNativeEventFilter
from .QAbstractProxyModel import QAbstractProxyModel
from .QAbstractState import QAbstractState
from .QAbstractTableModel import QAbstractTableModel
from .QAbstractTransition import QAbstractTransition
from .QAnimationGroup import QAnimationGroup
from .QBasicTimer import QBasicTimer
from .QBitArray import QBitArray
from .QIODevice import QIODevice
from .QBuffer import QBuffer
from .QByteArray import QByteArray
from .QByteArrayMatcher import QByteArrayMatcher
from .QCborError import QCborError
from .QCborKnownTags import QCborKnownTags
from .QCborSimpleType import QCborSimpleType
from .QCborStreamReader import QCborStreamReader
from .QCborStreamWriter import QCborStreamWriter
from .QEvent import QEvent
from .QChildEvent import QChildEvent
from .QCollator import QCollator
from .QCollatorSortKey import QCollatorSortKey
from .QCommandLineOption import QCommandLineOption
from .QCommandLineParser import QCommandLineParser
from .QCoreApplication import QCoreApplication
from .QCryptographicHash import QCryptographicHash
from .QDataStream import QDataStream
from .QDate import QDate
from .QDateTime import QDateTime
from .QDeadlineTimer import QDeadlineTimer
from .QDir import QDir
from .QDirIterator import QDirIterator
from .QDynamicPropertyChangeEvent import QDynamicPropertyChangeEvent
from .QEasingCurve import QEasingCurve
from .QElapsedTimer import QElapsedTimer
from .QEventLoop import QEventLoop
from .QEventLoopLocker import QEventLoopLocker
from .QEventTransition import QEventTransition
from .QFileDevice import QFileDevice
from .QFile import QFile
from .QFileInfo import QFileInfo
from .QFileSelector import QFileSelector
from .QFileSystemWatcher import QFileSystemWatcher
from .QFinalState import QFinalState
from .QGenericArgument import QGenericArgument
from .QGenericReturnArgument import QGenericReturnArgument
from .QHistoryState import QHistoryState
from .QIdentityProxyModel import QIdentityProxyModel
from .QItemSelection import QItemSelection
from .QItemSelectionModel import QItemSelectionModel
from .QItemSelectionRange import QItemSelectionRange
from .QJsonDocument import QJsonDocument
from .QJsonParseError import QJsonParseError
from .QJsonValue import QJsonValue
from .QLibrary import QLibrary
from .QLibraryInfo import QLibraryInfo
from .QLine import QLine
from .QLineF import QLineF
from .QLocale import QLocale
from .QLockFile import QLockFile
from .QLoggingCategory import QLoggingCategory
from .QMargins import QMargins
from .QMarginsF import QMarginsF
from .QMessageAuthenticationCode import QMessageAuthenticationCode
from .QMessageLogContext import QMessageLogContext
from .QMessageLogger import QMessageLogger
from .QMetaClassInfo import QMetaClassInfo
from .QMetaEnum import QMetaEnum
from .QMetaMethod import QMetaMethod
from .QMetaObject import QMetaObject
from .QMetaProperty import QMetaProperty
from .QMetaType import QMetaType
from .QMimeData import QMimeData
from .QMimeDatabase import QMimeDatabase
from .QMimeType import QMimeType
from .QModelIndex import QModelIndex
from .QMutex import QMutex
from .QMutexLocker import QMutexLocker
from .QObjectCleanupHandler import QObjectCleanupHandler
from .QOperatingSystemVersion import QOperatingSystemVersion
from .QParallelAnimationGroup import QParallelAnimationGroup
from .QPauseAnimation import QPauseAnimation
from .QPersistentModelIndex import QPersistentModelIndex
from .QPluginLoader import QPluginLoader
from .QPoint import QPoint
from .QPointF import QPointF
from .QProcess import QProcess
from .QProcessEnvironment import QProcessEnvironment
from .QVariantAnimation import QVariantAnimation
from .QPropertyAnimation import QPropertyAnimation
from .QRandomGenerator import QRandomGenerator
from .QReadLocker import QReadLocker
from .QReadWriteLock import QReadWriteLock
from .QRect import QRect
from .QRectF import QRectF
from .QRegExp import QRegExp
from .QRegularExpression import QRegularExpression
from .QRegularExpressionMatch import QRegularExpressionMatch
from .QRegularExpressionMatchIterator import QRegularExpressionMatchIterator
from .QResource import QResource
from .QRunnable import QRunnable
from .QSaveFile import QSaveFile
from .QSemaphore import QSemaphore
from .QSemaphoreReleaser import QSemaphoreReleaser
from .QSequentialAnimationGroup import QSequentialAnimationGroup
from .QSettings import QSettings
from .QSharedMemory import QSharedMemory
from .QSignalBlocker import QSignalBlocker
from .QSignalMapper import QSignalMapper
from .QSignalTransition import QSignalTransition
from .QSize import QSize
from .QSizeF import QSizeF
from .QSocketNotifier import QSocketNotifier
from .QSortFilterProxyModel import QSortFilterProxyModel
from .QStandardPaths import QStandardPaths
from .QState import QState
from .QStateMachine import QStateMachine
from .QStorageInfo import QStorageInfo
from .QStringListModel import QStringListModel
from .QSysInfo import QSysInfo
from .QSystemSemaphore import QSystemSemaphore
from .Qt import Qt
from .QTemporaryDir import QTemporaryDir
from .QTemporaryFile import QTemporaryFile
from .QTextBoundaryFinder import QTextBoundaryFinder
from .QTextCodec import QTextCodec
from .QTextDecoder import QTextDecoder
from .QTextEncoder import QTextEncoder
from .QTextStream import QTextStream
from .QTextStreamManipulator import QTextStreamManipulator
from .QThread import QThread
from .QThreadPool import QThreadPool
from .QTime import QTime
from .QTimeLine import QTimeLine
from .QTimer import QTimer
from .QTimerEvent import QTimerEvent
from .QTimeZone import QTimeZone
from .QtMsgType import QtMsgType
from .QTranslator import QTranslator
from .QUrl import QUrl
from .QUrlQuery import QUrlQuery
from .QUuid import QUuid
from .QVariant import QVariant
from .QVersionNumber import QVersionNumber
from .QWaitCondition import QWaitCondition
from .QWinEventNotifier import QWinEventNotifier
from .QWriteLocker import QWriteLocker
from .QXmlStreamAttribute import QXmlStreamAttribute
from .QXmlStreamAttributes import QXmlStreamAttributes
from .QXmlStreamEntityDeclaration import QXmlStreamEntityDeclaration
from .QXmlStreamEntityResolver import QXmlStreamEntityResolver
from .QXmlStreamNamespaceDeclaration import QXmlStreamNamespaceDeclaration
from .QXmlStreamNotationDeclaration import QXmlStreamNotationDeclaration
from .QXmlStreamReader import QXmlStreamReader
from .QXmlStreamWriter import QXmlStreamWriter
# variables with complex values

PYQT_CONFIGURATION = {
    'sip_flags': '-n PyQt5.sip -t WS_WIN -t Qt_5_12_8',
}




