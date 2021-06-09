# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QKeySequence(__sip.simplewrapper):
    """
    QKeySequence()
    QKeySequence(Union[QKeySequence, QKeySequence.StandardKey, str, int])
    QKeySequence(str, format: QKeySequence.SequenceFormat = QKeySequence.NativeText)
    QKeySequence(int, key2: int = 0, key3: int = 0, key4: int = 0)
    QKeySequence(Any)
    """
    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def fromString(self, p_str, format=None): # real signature unknown; restored from __doc__
        """ fromString(str, format: QKeySequence.SequenceFormat = QKeySequence.PortableText) -> QKeySequence """
        return QKeySequence

    def isDetached(self): # real signature unknown; restored from __doc__
        """ isDetached(self) -> bool """
        return False

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def keyBindings(self, QKeySequence_StandardKey): # real signature unknown; restored from __doc__
        """ keyBindings(QKeySequence.StandardKey) -> List[QKeySequence] """
        return []

    def listFromString(self, p_str, format=None): # real signature unknown; restored from __doc__
        """ listFromString(str, format: QKeySequence.SequenceFormat = QKeySequence.PortableText) -> List[QKeySequence] """
        return []

    def listToString(self, Iterable, Union=None, QKeySequence=None, QKeySequence_StandardKey=None, p_str=None, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ listToString(Iterable[Union[QKeySequence, QKeySequence.StandardKey, str, int]], format: QKeySequence.SequenceFormat = QKeySequence.PortableText) -> str """
        pass

    def matches(self, Union, QKeySequence=None, QKeySequence_StandardKey=None, p_str=None, p_int=None): # real signature unknown; restored from __doc__
        """ matches(self, Union[QKeySequence, QKeySequence.StandardKey, str, int]) -> QKeySequence.SequenceMatch """
        pass

    def mnemonic(self, p_str): # real signature unknown; restored from __doc__
        """ mnemonic(str) -> QKeySequence """
        return QKeySequence

    def swap(self, QKeySequence): # real signature unknown; restored from __doc__
        """ swap(self, QKeySequence) """
        pass

    def toString(self, format=None): # real signature unknown; restored from __doc__
        """ toString(self, format: QKeySequence.SequenceFormat = QKeySequence.PortableText) -> str """
        return ""

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
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

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AddTab = 19
    Back = 13
    Backspace = 69
    Bold = 27
    Cancel = 70
    Close = 4
    Copy = 9
    Cut = 8
    Delete = 7
    DeleteCompleteLine = 68
    DeleteEndOfLine = 60
    DeleteEndOfWord = 59
    DeleteStartOfWord = 58
    Deselect = 67
    ExactMatch = 2
    Find = 22
    FindNext = 23
    FindPrevious = 24
    Forward = 14
    FullScreen = 66
    HelpContents = 1
    InsertLineSeparator = 62
    InsertParagraphSeparator = 61
    Italic = 28
    MoveToEndOfBlock = 41
    MoveToEndOfDocument = 43
    MoveToEndOfLine = 39
    MoveToNextChar = 30
    MoveToNextLine = 34
    MoveToNextPage = 36
    MoveToNextWord = 32
    MoveToPreviousChar = 31
    MoveToPreviousLine = 35
    MoveToPreviousPage = 37
    MoveToPreviousWord = 33
    MoveToStartOfBlock = 40
    MoveToStartOfDocument = 42
    MoveToStartOfLine = 38
    NativeText = 0
    New = 6
    NextChild = 20
    NoMatch = 0
    Open = 3
    PartialMatch = 1
    Paste = 10
    PortableText = 1
    Preferences = 64
    PreviousChild = 21
    Print = 18
    Quit = 65
    Redo = 12
    Refresh = 15
    Replace = 25
    Save = 5
    SaveAs = 63
    SelectAll = 26
    SelectEndOfBlock = 55
    SelectEndOfDocument = 57
    SelectEndOfLine = 53
    SelectNextChar = 44
    SelectNextLine = 48
    SelectNextPage = 50
    SelectNextWord = 46
    SelectPreviousChar = 45
    SelectPreviousLine = 49
    SelectPreviousPage = 51
    SelectPreviousWord = 47
    SelectStartOfBlock = 54
    SelectStartOfDocument = 56
    SelectStartOfLine = 52
    Underline = 29
    Undo = 11
    UnknownKey = 0
    WhatsThis = 2
    ZoomIn = 16
    ZoomOut = 17


