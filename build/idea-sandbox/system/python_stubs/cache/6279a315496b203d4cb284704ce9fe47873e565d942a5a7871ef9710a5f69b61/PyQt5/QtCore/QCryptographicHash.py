# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QCryptographicHash(__sip.simplewrapper):
    """ QCryptographicHash(QCryptographicHash.Algorithm) """
    def addData(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        addData(self, bytes)
        addData(self, Union[QByteArray, bytes, bytearray])
        addData(self, QIODevice) -> bool
        """
        return False

    def hash(self, Union, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hash(Union[QByteArray, bytes, bytearray], QCryptographicHash.Algorithm) -> QByteArray """
        pass

    def hashLength(self, QCryptographicHash_Algorithm): # real signature unknown; restored from __doc__
        """ hashLength(QCryptographicHash.Algorithm) -> int """
        return 0

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) """
        pass

    def result(self): # real signature unknown; restored from __doc__
        """ result(self) -> QByteArray """
        return QByteArray

    def __init__(self, QCryptographicHash_Algorithm): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Keccak_224 = 7
    Keccak_256 = 8
    Keccak_384 = 9
    Keccak_512 = 10
    Md4 = 0
    Md5 = 1
    Sha1 = 2
    Sha224 = 3
    Sha256 = 4
    Sha384 = 5
    Sha3_224 = 11
    Sha3_256 = 12
    Sha3_384 = 13
    Sha3_512 = 14
    Sha512 = 6


