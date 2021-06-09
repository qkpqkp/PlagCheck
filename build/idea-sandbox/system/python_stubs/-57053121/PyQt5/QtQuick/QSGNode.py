# encoding: utf-8
# module PyQt5.QtQuick
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtQuick.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import PyQt5.QtQml as __PyQt5_QtQml
import sip as __sip


class QSGNode(__sip.wrapper):
    """ QSGNode() """
    def appendChildNode(self, QSGNode): # real signature unknown; restored from __doc__
        """ appendChildNode(self, QSGNode) """
        pass

    def childAtIndex(self, p_int): # real signature unknown; restored from __doc__
        """ childAtIndex(self, int) -> QSGNode """
        return QSGNode

    def childCount(self): # real signature unknown; restored from __doc__
        """ childCount(self) -> int """
        return 0

    def firstChild(self): # real signature unknown; restored from __doc__
        """ firstChild(self) -> QSGNode """
        return QSGNode

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> QSGNode.Flags """
        pass

    def insertChildNodeAfter(self, QSGNode, QSGNode_1): # real signature unknown; restored from __doc__
        """ insertChildNodeAfter(self, QSGNode, QSGNode) """
        pass

    def insertChildNodeBefore(self, QSGNode, QSGNode_1): # real signature unknown; restored from __doc__
        """ insertChildNodeBefore(self, QSGNode, QSGNode) """
        pass

    def isSubtreeBlocked(self): # real signature unknown; restored from __doc__
        """ isSubtreeBlocked(self) -> bool """
        return False

    def lastChild(self): # real signature unknown; restored from __doc__
        """ lastChild(self) -> QSGNode """
        return QSGNode

    def markDirty(self, Union, QSGNode_DirtyState=None, QSGNode_DirtyStateBit=None): # real signature unknown; restored from __doc__
        """ markDirty(self, Union[QSGNode.DirtyState, QSGNode.DirtyStateBit]) """
        pass

    def nextSibling(self): # real signature unknown; restored from __doc__
        """ nextSibling(self) -> QSGNode """
        return QSGNode

    def parent(self): # real signature unknown; restored from __doc__
        """ parent(self) -> QSGNode """
        return QSGNode

    def prependChildNode(self, QSGNode): # real signature unknown; restored from __doc__
        """ prependChildNode(self, QSGNode) """
        pass

    def preprocess(self): # real signature unknown; restored from __doc__
        """ preprocess(self) """
        pass

    def previousSibling(self): # real signature unknown; restored from __doc__
        """ previousSibling(self) -> QSGNode """
        return QSGNode

    def removeAllChildNodes(self): # real signature unknown; restored from __doc__
        """ removeAllChildNodes(self) """
        pass

    def removeChildNode(self, QSGNode): # real signature unknown; restored from __doc__
        """ removeChildNode(self, QSGNode) """
        pass

    def setFlag(self, QSGNode_Flag, enabled=True): # real signature unknown; restored from __doc__
        """ setFlag(self, QSGNode.Flag, enabled: bool = True) """
        pass

    def setFlags(self, Union, QSGNode_Flags=None, QSGNode_Flag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setFlags(self, Union[QSGNode.Flags, QSGNode.Flag], enabled: bool = True) """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QSGNode.NodeType """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    BasicNodeType = 0
    ClipNodeType = 3
    DirtyGeometry = 4096
    DirtyMaterial = 8192
    DirtyMatrix = 256
    DirtyNodeAdded = 1024
    DirtyNodeRemoved = 2048
    DirtyOpacity = 16384
    GeometryNodeType = 1
    OpacityNodeType = 4
    OwnedByParent = 1
    OwnsGeometry = 65536
    OwnsMaterial = 131072
    OwnsOpaqueMaterial = 262144
    TransformNodeType = 2
    UsePreprocess = 2


