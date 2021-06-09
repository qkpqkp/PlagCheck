# encoding: utf-8
# module PyQt5.QtLocation
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtLocation.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QPlaceReply(__PyQt5_QtCore.QObject):
    """ QPlaceReply(parent: QObject = None) """
    def abort(self): # real signature unknown; restored from __doc__
        """ abort(self) """
        pass

    def aborted(self): # real signature unknown; restored from __doc__
        """ aborted(self) [signal] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contentUpdated(self): # real signature unknown; restored from __doc__
        """ contentUpdated(self) [signal] """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, QPlaceReply_Error=None, errorString=''): # real signature unknown; restored from __doc__ with multiple overloads
        """
        error(self) -> QPlaceReply.Error
        error(self, QPlaceReply.Error, errorString: str = '') [signal]
        """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def finished(self): # real signature unknown; restored from __doc__
        """ finished(self) [signal] """
        pass

    def isFinished(self): # real signature unknown; restored from __doc__
        """ isFinished(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setError(self, QPlaceReply_Error, p_str): # real signature unknown; restored from __doc__
        """ setError(self, QPlaceReply.Error, str) """
        pass

    def setFinished(self, bool): # real signature unknown; restored from __doc__
        """ setFinished(self, bool) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QPlaceReply.Type """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    BadArgumentError = 7
    CancelError = 8
    CategoryDoesNotExistError = 2
    CommunicationError = 3
    ContentReply = 4
    DetailsReply = 1
    IdReply = 5
    MatchReply = 6
    NoError = 0
    ParseError = 4
    PermissionsError = 5
    PlaceDoesNotExistError = 1
    Reply = 0
    SearchReply = 2
    SearchSuggestionReply = 3
    UnknownError = 9
    UnsupportedError = 6


