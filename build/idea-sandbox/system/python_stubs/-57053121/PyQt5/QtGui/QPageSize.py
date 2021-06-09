# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QPageSize(__sip.simplewrapper):
    """
    QPageSize()
    QPageSize(QPageSize.PageSizeId)
    QPageSize(QSize, name: str = '', matchPolicy: QPageSize.SizeMatchPolicy = QPageSize.FuzzyMatch)
    QPageSize(QSizeF, QPageSize.Unit, name: str = '', matchPolicy: QPageSize.SizeMatchPolicy = QPageSize.FuzzyMatch)
    QPageSize(QPageSize)
    """
    def definitionSize(self, QPageSize_PageSizeId=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        definitionSize(self) -> QSizeF
        definitionSize(QPageSize.PageSizeId) -> QSizeF
        """
        pass

    def definitionUnits(self, QPageSize_PageSizeId=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        definitionUnits(self) -> QPageSize.Unit
        definitionUnits(QPageSize.PageSizeId) -> QPageSize.Unit
        """
        pass

    def id(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        id(self) -> QPageSize.PageSizeId
        id(QSize, matchPolicy: QPageSize.SizeMatchPolicy = QPageSize.FuzzyMatch) -> QPageSize.PageSizeId
        id(QSizeF, QPageSize.Unit, matchPolicy: QPageSize.SizeMatchPolicy = QPageSize.FuzzyMatch) -> QPageSize.PageSizeId
        id(int) -> QPageSize.PageSizeId
        """
        pass

    def isEquivalentTo(self, QPageSize): # real signature unknown; restored from __doc__
        """ isEquivalentTo(self, QPageSize) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def key(self, QPageSize_PageSizeId=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        key(self) -> str
        key(QPageSize.PageSizeId) -> str
        """
        return ""

    def name(self, QPageSize_PageSizeId=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        name(self) -> str
        name(QPageSize.PageSizeId) -> str
        """
        return ""

    def rect(self, QPageSize_Unit): # real signature unknown; restored from __doc__
        """ rect(self, QPageSize.Unit) -> QRectF """
        pass

    def rectPixels(self, p_int): # real signature unknown; restored from __doc__
        """ rectPixels(self, int) -> QRect """
        pass

    def rectPoints(self): # real signature unknown; restored from __doc__
        """ rectPoints(self) -> QRect """
        pass

    def size(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        size(self, QPageSize.Unit) -> QSizeF
        size(QPageSize.PageSizeId, QPageSize.Unit) -> QSizeF
        """
        pass

    def sizePixels(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        sizePixels(self, int) -> QSize
        sizePixels(QPageSize.PageSizeId, int) -> QSize
        """
        pass

    def sizePoints(self, QPageSize_PageSizeId=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        sizePoints(self) -> QSize
        sizePoints(QPageSize.PageSizeId) -> QSize
        """
        pass

    def swap(self, QPageSize): # real signature unknown; restored from __doc__
        """ swap(self, QPageSize) """
        pass

    def windowsId(self, QPageSize_PageSizeId=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        windowsId(self) -> int
        windowsId(QPageSize.PageSizeId) -> int
        """
        return 0

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    A0 = 5
    A1 = 6
    A10 = 31
    A2 = 7
    A3 = 8
    A3Extra = 32
    A4 = 0
    A4Extra = 33
    A4Plus = 34
    A4Small = 35
    A5 = 9
    A5Extra = 36
    A6 = 10
    A7 = 11
    A8 = 12
    A9 = 13
    AnsiA = 2
    AnsiB = 28
    AnsiC = 49
    AnsiD = 50
    AnsiE = 51
    ArchA = 57
    ArchB = 58
    ArchC = 59
    ArchD = 60
    ArchE = 61
    B0 = 14
    B1 = 15
    B10 = 16
    B2 = 17
    B3 = 18
    B4 = 19
    B5 = 1
    B5Extra = 37
    B6 = 20
    B7 = 21
    B8 = 22
    B9 = 23
    C5E = 24
    Cicero = 5
    Comm10E = 25
    Custom = 30
    Didot = 4
    DLE = 26
    DoublePostcard = 78
    Envelope10 = 25
    Envelope11 = 97
    Envelope12 = 98
    Envelope14 = 99
    Envelope9 = 96
    EnvelopeB4 = 85
    EnvelopeB5 = 86
    EnvelopeB6 = 87
    EnvelopeC0 = 88
    EnvelopeC1 = 89
    EnvelopeC2 = 90
    EnvelopeC3 = 91
    EnvelopeC4 = 92
    EnvelopeC5 = 24
    EnvelopeC6 = 93
    EnvelopeC65 = 94
    EnvelopeC7 = 95
    EnvelopeChou3 = 102
    EnvelopeChou4 = 103
    EnvelopeDL = 26
    EnvelopeInvite = 104
    EnvelopeItalian = 105
    EnvelopeKaku2 = 106
    EnvelopeKaku3 = 107
    EnvelopeMonarch = 100
    EnvelopePersonal = 101
    EnvelopePrc1 = 108
    EnvelopePrc10 = 117
    EnvelopePrc2 = 109
    EnvelopePrc3 = 110
    EnvelopePrc4 = 111
    EnvelopePrc5 = 112
    EnvelopePrc6 = 113
    EnvelopePrc7 = 114
    EnvelopePrc8 = 115
    EnvelopePrc9 = 116
    EnvelopeYou4 = 118
    ExactMatch = 2
    Executive = 4
    ExecutiveStandard = 71
    FanFoldGerman = 83
    FanFoldGermanLegal = 84
    FanFoldUS = 82
    Folio = 27
    FuzzyMatch = 0
    FuzzyOrientationMatch = 1
    Imperial10x11 = 66
    Imperial10x13 = 67
    Imperial10x14 = 68
    Imperial12x11 = 69
    Imperial15x11 = 70
    Imperial7x9 = 62
    Imperial8x10 = 63
    Imperial9x11 = 64
    Imperial9x12 = 65
    Inch = 2
    JisB0 = 38
    JisB1 = 39
    JisB10 = 48
    JisB2 = 40
    JisB3 = 41
    JisB4 = 42
    JisB5 = 43
    JisB6 = 44
    JisB7 = 45
    JisB8 = 46
    JisB9 = 47
    LastPageSize = 118
    Ledger = 28
    Legal = 3
    LegalExtra = 52
    Letter = 2
    LetterExtra = 53
    LetterPlus = 54
    LetterSmall = 55
    Millimeter = 0
    Note = 72
    NPageSize = 118
    NPaperSize = 118
    Pica = 3
    Point = 1
    Postcard = 77
    Prc16K = 79
    Prc32K = 80
    Prc32KBig = 81
    Quarto = 73
    Statement = 74
    SuperA = 75
    SuperB = 76
    Tabloid = 29
    TabloidExtra = 56
    __hash__ = None


