# encoding: utf-8
# module PyQt5.QtPrintSupport
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtPrintSupport.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtGui as __PyQt5_QtGui
import PyQt5.QtWidgets as __PyQt5_QtWidgets
import sip as __sip


# no functions
# classes

class QAbstractPrintDialog(__PyQt5_QtWidgets.QDialog):
    """ QAbstractPrintDialog(QPrinter, parent: QWidget = None) """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def enabledOptions(self): # real signature unknown; restored from __doc__
        """ enabledOptions(self) -> QAbstractPrintDialog.PrintDialogOptions """
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def eventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def exec(self): # real signature unknown; restored from __doc__
        """ exec(self) -> int """
        return 0

    def exec_(self): # real signature unknown; restored from __doc__
        """ exec_(self) -> int """
        return 0

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def fromPage(self): # real signature unknown; restored from __doc__
        """ fromPage(self) -> int """
        return 0

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def maxPage(self): # real signature unknown; restored from __doc__
        """ maxPage(self) -> int """
        return 0

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def minPage(self): # real signature unknown; restored from __doc__
        """ minPage(self) -> int """
        return 0

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def printer(self): # real signature unknown; restored from __doc__
        """ printer(self) -> QPrinter """
        return QPrinter

    def printRange(self): # real signature unknown; restored from __doc__
        """ printRange(self) -> QAbstractPrintDialog.PrintRange """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setEnabledOptions(self, Union, QAbstractPrintDialog_PrintDialogOptions=None, QAbstractPrintDialog_PrintDialogOption=None): # real signature unknown; restored from __doc__
        """ setEnabledOptions(self, Union[QAbstractPrintDialog.PrintDialogOptions, QAbstractPrintDialog.PrintDialogOption]) """
        pass

    def setFromTo(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ setFromTo(self, int, int) """
        pass

    def setMinMax(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ setMinMax(self, int, int) """
        pass

    def setOptionTabs(self, Iterable, QWidget=None): # real signature unknown; restored from __doc__
        """ setOptionTabs(self, Iterable[QWidget]) """
        pass

    def setPrintRange(self, QAbstractPrintDialog_PrintRange): # real signature unknown; restored from __doc__
        """ setPrintRange(self, QAbstractPrintDialog.PrintRange) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def toPage(self): # real signature unknown; restored from __doc__
        """ toPage(self) -> int """
        return 0

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, QPrinter, parent=None): # real signature unknown; restored from __doc__
        pass

    AllPages = 0
    CurrentPage = 3
    None_ = 0
    PageRange = 2
    PrintCollateCopies = 16
    PrintCurrentPage = 64
    PrintPageRange = 4
    PrintSelection = 2
    PrintShowPageSize = 8
    PrintToFile = 1
    Selection = 1


class QPageSetupDialog(__PyQt5_QtWidgets.QDialog):
    """
    QPageSetupDialog(QPrinter, parent: QWidget = None)
    QPageSetupDialog(parent: QWidget = None)
    """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def done(self, p_int): # real signature unknown; restored from __doc__
        """ done(self, int) """
        pass

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def eventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def exec(self): # real signature unknown; restored from __doc__
        """ exec(self) -> int """
        return 0

    def exec_(self): # real signature unknown; restored from __doc__
        """ exec_(self) -> int """
        return 0

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def open(self, PYQT_SLOT=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        open(self)
        open(self, PYQT_SLOT)
        """
        pass

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def printer(self): # real signature unknown; restored from __doc__
        """ printer(self) -> QPrinter """
        return QPrinter

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ setVisible(self, bool) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QPrintDialog(QAbstractPrintDialog):
    """
    QPrintDialog(QPrinter, parent: QWidget = None)
    QPrintDialog(parent: QWidget = None)
    """
    def accepted(self, QPrinter=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        accepted(self) [signal]
        accepted(self, QPrinter) [signal]
        """
        pass

    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def done(self, p_int): # real signature unknown; restored from __doc__
        """ done(self, int) """
        pass

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def eventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def exec(self): # real signature unknown; restored from __doc__
        """ exec(self) -> int """
        return 0

    def exec_(self): # real signature unknown; restored from __doc__
        """ exec_(self) -> int """
        return 0

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def open(self, PYQT_SLOT=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        open(self)
        open(self, PYQT_SLOT)
        """
        pass

    def options(self): # real signature unknown; restored from __doc__
        """ options(self) -> QAbstractPrintDialog.PrintDialogOptions """
        pass

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setOption(self, QAbstractPrintDialog_PrintDialogOption, on=True): # real signature unknown; restored from __doc__
        """ setOption(self, QAbstractPrintDialog.PrintDialogOption, on: bool = True) """
        pass

    def setOptions(self, Union, QAbstractPrintDialog_PrintDialogOptions=None, QAbstractPrintDialog_PrintDialogOption=None): # real signature unknown; restored from __doc__
        """ setOptions(self, Union[QAbstractPrintDialog.PrintDialogOptions, QAbstractPrintDialog.PrintDialogOption]) """
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ setVisible(self, bool) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def testOption(self, QAbstractPrintDialog_PrintDialogOption): # real signature unknown; restored from __doc__
        """ testOption(self, QAbstractPrintDialog.PrintDialogOption) -> bool """
        return False

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QPrintEngine(__sip.simplewrapper):
    """
    QPrintEngine()
    QPrintEngine(QPrintEngine)
    """
    def abort(self): # real signature unknown; restored from __doc__
        """ abort(self) -> bool """
        return False

    def metric(self, QPaintDevice_PaintDeviceMetric): # real signature unknown; restored from __doc__
        """ metric(self, QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def newPage(self): # real signature unknown; restored from __doc__
        """ newPage(self) -> bool """
        return False

    def printerState(self): # real signature unknown; restored from __doc__
        """ printerState(self) -> QPrinter.PrinterState """
        pass

    def property(self, QPrintEngine_PrintEnginePropertyKey): # real signature unknown; restored from __doc__
        """ property(self, QPrintEngine.PrintEnginePropertyKey) -> Any """
        pass

    def setProperty(self, QPrintEngine_PrintEnginePropertyKey, Any): # real signature unknown; restored from __doc__
        """ setProperty(self, QPrintEngine.PrintEnginePropertyKey, Any) """
        pass

    def __init__(self, QPrintEngine=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    PPK_CollateCopies = 0
    PPK_ColorMode = 1
    PPK_CopyCount = 24
    PPK_Creator = 2
    PPK_CustomBase = 65280
    PPK_CustomPaperSize = 22
    PPK_DocumentName = 3
    PPK_Duplex = 20
    PPK_FontEmbedding = 19
    PPK_FullPage = 4
    PPK_NumberOfCopies = 5
    PPK_Orientation = 6
    PPK_OutputFileName = 7
    PPK_PageMargins = 23
    PPK_PageOrder = 8
    PPK_PageRect = 9
    PPK_PageSize = 10
    PPK_PaperName = 26
    PPK_PaperRect = 11
    PPK_PaperSize = 10
    PPK_PaperSource = 12
    PPK_PaperSources = 21
    PPK_PrinterName = 13
    PPK_PrinterProgram = 14
    PPK_QPageLayout = 29
    PPK_QPageMargins = 28
    PPK_QPageSize = 27
    PPK_Resolution = 15
    PPK_SelectionOption = 16
    PPK_SupportedResolutions = 17
    PPK_SupportsMultipleCopies = 25
    PPK_WindowsPageSize = 18


class QPrinter(__PyQt5_QtGui.QPagedPaintDevice):
    """
    QPrinter(mode: QPrinter.PrinterMode = QPrinter.ScreenResolution)
    QPrinter(QPrinterInfo, mode: QPrinter.PrinterMode = QPrinter.ScreenResolution)
    """
    def abort(self): # real signature unknown; restored from __doc__
        """ abort(self) -> bool """
        return False

    def collateCopies(self): # real signature unknown; restored from __doc__
        """ collateCopies(self) -> bool """
        return False

    def colorMode(self): # real signature unknown; restored from __doc__
        """ colorMode(self) -> QPrinter.ColorMode """
        pass

    def copyCount(self): # real signature unknown; restored from __doc__
        """ copyCount(self) -> int """
        return 0

    def creator(self): # real signature unknown; restored from __doc__
        """ creator(self) -> str """
        return ""

    def docName(self): # real signature unknown; restored from __doc__
        """ docName(self) -> str """
        return ""

    def doubleSidedPrinting(self): # real signature unknown; restored from __doc__
        """ doubleSidedPrinting(self) -> bool """
        return False

    def duplex(self): # real signature unknown; restored from __doc__
        """ duplex(self) -> QPrinter.DuplexMode """
        pass

    def fontEmbeddingEnabled(self): # real signature unknown; restored from __doc__
        """ fontEmbeddingEnabled(self) -> bool """
        return False

    def fromPage(self): # real signature unknown; restored from __doc__
        """ fromPage(self) -> int """
        return 0

    def fullPage(self): # real signature unknown; restored from __doc__
        """ fullPage(self) -> bool """
        return False

    def getPageMargins(self, QPrinter_Unit): # real signature unknown; restored from __doc__
        """ getPageMargins(self, QPrinter.Unit) -> Tuple[float, float, float, float] """
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def metric(self, QPaintDevice_PaintDeviceMetric): # real signature unknown; restored from __doc__
        """ metric(self, QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def newPage(self): # real signature unknown; restored from __doc__
        """ newPage(self) -> bool """
        return False

    def orientation(self): # real signature unknown; restored from __doc__
        """ orientation(self) -> QPrinter.Orientation """
        pass

    def outputFileName(self): # real signature unknown; restored from __doc__
        """ outputFileName(self) -> str """
        return ""

    def outputFormat(self): # real signature unknown; restored from __doc__
        """ outputFormat(self) -> QPrinter.OutputFormat """
        pass

    def pageOrder(self): # real signature unknown; restored from __doc__
        """ pageOrder(self) -> QPrinter.PageOrder """
        pass

    def pageRect(self, QPrinter_Unit=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        pageRect(self) -> QRect
        pageRect(self, QPrinter.Unit) -> QRectF
        """
        pass

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ paintEngine(self) -> QPaintEngine """
        pass

    def paperName(self): # real signature unknown; restored from __doc__
        """ paperName(self) -> str """
        return ""

    def paperRect(self, QPrinter_Unit=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        paperRect(self) -> QRect
        paperRect(self, QPrinter.Unit) -> QRectF
        """
        pass

    def paperSize(self, QPrinter_Unit=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        paperSize(self) -> QPagedPaintDevice.PageSize
        paperSize(self, QPrinter.Unit) -> QSizeF
        """
        pass

    def paperSource(self): # real signature unknown; restored from __doc__
        """ paperSource(self) -> QPrinter.PaperSource """
        pass

    def pdfVersion(self): # real signature unknown; restored from __doc__
        """ pdfVersion(self) -> QPagedPaintDevice.PdfVersion """
        pass

    def printEngine(self): # real signature unknown; restored from __doc__
        """ printEngine(self) -> QPrintEngine """
        return QPrintEngine

    def printerName(self): # real signature unknown; restored from __doc__
        """ printerName(self) -> str """
        return ""

    def printerState(self): # real signature unknown; restored from __doc__
        """ printerState(self) -> QPrinter.PrinterState """
        pass

    def printProgram(self): # real signature unknown; restored from __doc__
        """ printProgram(self) -> str """
        return ""

    def printRange(self): # real signature unknown; restored from __doc__
        """ printRange(self) -> QPrinter.PrintRange """
        pass

    def resolution(self): # real signature unknown; restored from __doc__
        """ resolution(self) -> int """
        return 0

    def setCollateCopies(self, bool): # real signature unknown; restored from __doc__
        """ setCollateCopies(self, bool) """
        pass

    def setColorMode(self, QPrinter_ColorMode): # real signature unknown; restored from __doc__
        """ setColorMode(self, QPrinter.ColorMode) """
        pass

    def setCopyCount(self, p_int): # real signature unknown; restored from __doc__
        """ setCopyCount(self, int) """
        pass

    def setCreator(self, p_str): # real signature unknown; restored from __doc__
        """ setCreator(self, str) """
        pass

    def setDocName(self, p_str): # real signature unknown; restored from __doc__
        """ setDocName(self, str) """
        pass

    def setDoubleSidedPrinting(self, bool): # real signature unknown; restored from __doc__
        """ setDoubleSidedPrinting(self, bool) """
        pass

    def setDuplex(self, QPrinter_DuplexMode): # real signature unknown; restored from __doc__
        """ setDuplex(self, QPrinter.DuplexMode) """
        pass

    def setEngines(self, QPrintEngine, QPaintEngine): # real signature unknown; restored from __doc__
        """ setEngines(self, QPrintEngine, QPaintEngine) """
        pass

    def setFontEmbeddingEnabled(self, bool): # real signature unknown; restored from __doc__
        """ setFontEmbeddingEnabled(self, bool) """
        pass

    def setFromTo(self, p_int, p_int_1): # real signature unknown; restored from __doc__
        """ setFromTo(self, int, int) """
        pass

    def setFullPage(self, bool): # real signature unknown; restored from __doc__
        """ setFullPage(self, bool) """
        pass

    def setMargins(self, QPagedPaintDevice_Margins): # real signature unknown; restored from __doc__
        """ setMargins(self, QPagedPaintDevice.Margins) """
        pass

    def setOrientation(self, QPrinter_Orientation): # real signature unknown; restored from __doc__
        """ setOrientation(self, QPrinter.Orientation) """
        pass

    def setOutputFileName(self, p_str): # real signature unknown; restored from __doc__
        """ setOutputFileName(self, str) """
        pass

    def setOutputFormat(self, QPrinter_OutputFormat): # real signature unknown; restored from __doc__
        """ setOutputFormat(self, QPrinter.OutputFormat) """
        pass

    def setPageMargins(self, p_float, p_float_1, p_float_2, p_float_3, QPrinter_Unit): # real signature unknown; restored from __doc__
        """ setPageMargins(self, float, float, float, float, QPrinter.Unit) """
        pass

    def setPageOrder(self, QPrinter_PageOrder): # real signature unknown; restored from __doc__
        """ setPageOrder(self, QPrinter.PageOrder) """
        pass

    def setPageSizeMM(self, QSizeF): # real signature unknown; restored from __doc__
        """ setPageSizeMM(self, QSizeF) """
        pass

    def setPaperName(self, p_str): # real signature unknown; restored from __doc__
        """ setPaperName(self, str) """
        pass

    def setPaperSize(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setPaperSize(self, QPagedPaintDevice.PageSize)
        setPaperSize(self, QSizeF, QPrinter.Unit)
        """
        pass

    def setPaperSource(self, QPrinter_PaperSource): # real signature unknown; restored from __doc__
        """ setPaperSource(self, QPrinter.PaperSource) """
        pass

    def setPdfVersion(self, QPagedPaintDevice_PdfVersion): # real signature unknown; restored from __doc__
        """ setPdfVersion(self, QPagedPaintDevice.PdfVersion) """
        pass

    def setPrinterName(self, p_str): # real signature unknown; restored from __doc__
        """ setPrinterName(self, str) """
        pass

    def setPrintProgram(self, p_str): # real signature unknown; restored from __doc__
        """ setPrintProgram(self, str) """
        pass

    def setPrintRange(self, QPrinter_PrintRange): # real signature unknown; restored from __doc__
        """ setPrintRange(self, QPrinter.PrintRange) """
        pass

    def setResolution(self, p_int): # real signature unknown; restored from __doc__
        """ setResolution(self, int) """
        pass

    def supportedResolutions(self): # real signature unknown; restored from __doc__
        """ supportedResolutions(self) -> List[int] """
        return []

    def supportsMultipleCopies(self): # real signature unknown; restored from __doc__
        """ supportsMultipleCopies(self) -> bool """
        return False

    def toPage(self): # real signature unknown; restored from __doc__
        """ toPage(self) -> int """
        return 0

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Aborted = 2
    Active = 1
    AllPages = 0
    Auto = 6
    Cassette = 11
    Cicero = 5
    Color = 1
    CurrentPage = 3
    CustomSource = 14
    DevicePixel = 6
    Didot = 4
    DuplexAuto = 1
    DuplexLongSide = 2
    DuplexNone = 0
    DuplexShortSide = 3
    Envelope = 4
    EnvelopeManual = 5
    Error = 3
    FirstPageFirst = 0
    FormSource = 12
    GrayScale = 0
    HighResolution = 2
    Idle = 0
    Inch = 2
    Landscape = 1
    LargeCapacity = 10
    LargeFormat = 9
    LastPageFirst = 1
    LastPaperSource = 14
    Lower = 1
    Manual = 3
    MaxPageSource = 13
    Middle = 2
    Millimeter = 0
    NativeFormat = 0
    OnlyOne = 0
    PageRange = 2
    PdfFormat = 1
    Pica = 3
    Point = 1
    Portrait = 0
    PrinterResolution = 1
    ScreenResolution = 0
    Selection = 1
    SmallFormat = 8
    Tractor = 7
    Upper = 0


class QPrinterInfo(__sip.simplewrapper):
    """
    QPrinterInfo()
    QPrinterInfo(QPrinterInfo)
    QPrinterInfo(QPrinter)
    """
    def availablePrinterNames(self): # real signature unknown; restored from __doc__
        """ availablePrinterNames() -> List[str] """
        return []

    def availablePrinters(self): # real signature unknown; restored from __doc__
        """ availablePrinters() -> List[QPrinterInfo] """
        return []

    def defaultDuplexMode(self): # real signature unknown; restored from __doc__
        """ defaultDuplexMode(self) -> QPrinter.DuplexMode """
        pass

    def defaultPageSize(self): # real signature unknown; restored from __doc__
        """ defaultPageSize(self) -> QPageSize """
        pass

    def defaultPrinter(self): # real signature unknown; restored from __doc__
        """ defaultPrinter() -> QPrinterInfo """
        return QPrinterInfo

    def defaultPrinterName(self): # real signature unknown; restored from __doc__
        """ defaultPrinterName() -> str """
        return ""

    def description(self): # real signature unknown; restored from __doc__
        """ description(self) -> str """
        return ""

    def isDefault(self): # real signature unknown; restored from __doc__
        """ isDefault(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isRemote(self): # real signature unknown; restored from __doc__
        """ isRemote(self) -> bool """
        return False

    def location(self): # real signature unknown; restored from __doc__
        """ location(self) -> str """
        return ""

    def makeAndModel(self): # real signature unknown; restored from __doc__
        """ makeAndModel(self) -> str """
        return ""

    def maximumPhysicalPageSize(self): # real signature unknown; restored from __doc__
        """ maximumPhysicalPageSize(self) -> QPageSize """
        pass

    def minimumPhysicalPageSize(self): # real signature unknown; restored from __doc__
        """ minimumPhysicalPageSize(self) -> QPageSize """
        pass

    def printerInfo(self, p_str): # real signature unknown; restored from __doc__
        """ printerInfo(str) -> QPrinterInfo """
        return QPrinterInfo

    def printerName(self): # real signature unknown; restored from __doc__
        """ printerName(self) -> str """
        return ""

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> QPrinter.PrinterState """
        pass

    def supportedDuplexModes(self): # real signature unknown; restored from __doc__
        """ supportedDuplexModes(self) -> List[QPrinter.DuplexMode] """
        return []

    def supportedPageSizes(self): # real signature unknown; restored from __doc__
        """ supportedPageSizes(self) -> List[QPageSize] """
        return []

    def supportedPaperSizes(self): # real signature unknown; restored from __doc__
        """ supportedPaperSizes(self) -> List[QPagedPaintDevice.PageSize] """
        return []

    def supportedResolutions(self): # real signature unknown; restored from __doc__
        """ supportedResolutions(self) -> List[int] """
        return []

    def supportedSizesWithNames(self): # real signature unknown; restored from __doc__
        """ supportedSizesWithNames(self) -> List[Tuple[str, QSizeF]] """
        return []

    def supportsCustomPageSizes(self): # real signature unknown; restored from __doc__
        """ supportsCustomPageSizes(self) -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QPrintPreviewDialog(__PyQt5_QtWidgets.QDialog):
    """
    QPrintPreviewDialog(parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
    QPrintPreviewDialog(QPrinter, parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
    """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def done(self, p_int): # real signature unknown; restored from __doc__
        """ done(self, int) """
        pass

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def eventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def open(self, PYQT_SLOT=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        open(self)
        open(self, PYQT_SLOT)
        """
        pass

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paintRequested(self, QPrinter): # real signature unknown; restored from __doc__
        """ paintRequested(self, QPrinter) [signal] """
        pass

    def printer(self): # real signature unknown; restored from __doc__
        """ printer(self) -> QPrinter """
        return QPrinter

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ setVisible(self, bool) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QPrintPreviewWidget(__PyQt5_QtWidgets.QWidget):
    """
    QPrintPreviewWidget(QPrinter, parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
    QPrintPreviewWidget(parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
    """
    def actionEvent(self, *args, **kwargs): # real signature unknown
        pass

    def changeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenuEvent(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def currentPage(self): # real signature unknown; restored from __doc__
        """ currentPage(self) -> int """
        return 0

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def destroy(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def dragEnterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragLeaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dragMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dropEvent(self, *args, **kwargs): # real signature unknown
        pass

    def enterEvent(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def fitInView(self): # real signature unknown; restored from __doc__
        """ fitInView(self) """
        pass

    def fitToWidth(self): # real signature unknown; restored from __doc__
        """ fitToWidth(self) """
        pass

    def focusInEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusNextPrevChild(self, *args, **kwargs): # real signature unknown
        pass

    def focusOutEvent(self, *args, **kwargs): # real signature unknown
        pass

    def focusPreviousChild(self, *args, **kwargs): # real signature unknown
        pass

    def hideEvent(self, *args, **kwargs): # real signature unknown
        pass

    def initPainter(self, *args, **kwargs): # real signature unknown
        pass

    def inputMethodEvent(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyPressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def keyReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def leaveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def mouseDoubleClickEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseMoveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, *args, **kwargs): # real signature unknown
        pass

    def mouseReleaseEvent(self, *args, **kwargs): # real signature unknown
        pass

    def moveEvent(self, *args, **kwargs): # real signature unknown
        pass

    def nativeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def orientation(self): # real signature unknown; restored from __doc__
        """ orientation(self) -> QPrinter.Orientation """
        pass

    def pageCount(self): # real signature unknown; restored from __doc__
        """ pageCount(self) -> int """
        return 0

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paintRequested(self, QPrinter): # real signature unknown; restored from __doc__
        """ paintRequested(self, QPrinter) [signal] """
        pass

    def previewChanged(self): # real signature unknown; restored from __doc__
        """ previewChanged(self) [signal] """
        pass

    def print(self): # real signature unknown; restored from __doc__
        """ print(self) """
        pass

    def print_(self): # real signature unknown; restored from __doc__
        """ print_(self) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAllPagesViewMode(self): # real signature unknown; restored from __doc__
        """ setAllPagesViewMode(self) """
        pass

    def setCurrentPage(self, p_int): # real signature unknown; restored from __doc__
        """ setCurrentPage(self, int) """
        pass

    def setFacingPagesViewMode(self): # real signature unknown; restored from __doc__
        """ setFacingPagesViewMode(self) """
        pass

    def setLandscapeOrientation(self): # real signature unknown; restored from __doc__
        """ setLandscapeOrientation(self) """
        pass

    def setOrientation(self, QPrinter_Orientation): # real signature unknown; restored from __doc__
        """ setOrientation(self, QPrinter.Orientation) """
        pass

    def setPortraitOrientation(self): # real signature unknown; restored from __doc__
        """ setPortraitOrientation(self) """
        pass

    def setSinglePageViewMode(self): # real signature unknown; restored from __doc__
        """ setSinglePageViewMode(self) """
        pass

    def setViewMode(self, QPrintPreviewWidget_ViewMode): # real signature unknown; restored from __doc__
        """ setViewMode(self, QPrintPreviewWidget.ViewMode) """
        pass

    def setVisible(self, bool): # real signature unknown; restored from __doc__
        """ setVisible(self, bool) """
        pass

    def setZoomFactor(self, p_float): # real signature unknown; restored from __doc__
        """ setZoomFactor(self, float) """
        pass

    def setZoomMode(self, QPrintPreviewWidget_ZoomMode): # real signature unknown; restored from __doc__
        """ setZoomMode(self, QPrintPreviewWidget.ZoomMode) """
        pass

    def sharedPainter(self, *args, **kwargs): # real signature unknown
        pass

    def showEvent(self, *args, **kwargs): # real signature unknown
        pass

    def tabletEvent(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateMicroFocus(self, *args, **kwargs): # real signature unknown
        pass

    def updatePreview(self): # real signature unknown; restored from __doc__
        """ updatePreview(self) """
        pass

    def viewMode(self): # real signature unknown; restored from __doc__
        """ viewMode(self) -> QPrintPreviewWidget.ViewMode """
        pass

    def wheelEvent(self, *args, **kwargs): # real signature unknown
        pass

    def zoomFactor(self): # real signature unknown; restored from __doc__
        """ zoomFactor(self) -> float """
        return 0.0

    def zoomIn(self, factor=1.1): # real signature unknown; restored from __doc__
        """ zoomIn(self, factor: float = 1.1) """
        pass

    def zoomMode(self): # real signature unknown; restored from __doc__
        """ zoomMode(self) -> QPrintPreviewWidget.ZoomMode """
        pass

    def zoomOut(self, factor=1.1): # real signature unknown; restored from __doc__
        """ zoomOut(self, factor: float = 1.1) """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AllPagesView = 2
    CustomZoom = 0
    FacingPagesView = 1
    FitInView = 2
    FitToWidth = 1
    SinglePageView = 0


# variables with complex values



