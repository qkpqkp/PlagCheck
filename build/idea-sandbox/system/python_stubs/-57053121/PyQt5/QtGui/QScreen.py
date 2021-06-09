# encoding: utf-8
# module PyQt5.QtGui
# from C:\Users\Doly\Anaconda3\lib\site-packages\PyQt5\QtGui.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


class QScreen(__PyQt5_QtCore.QObject):
    # no doc
    def angleBetween(self, Qt_ScreenOrientation, Qt_ScreenOrientation_1): # real signature unknown; restored from __doc__
        """ angleBetween(self, Qt.ScreenOrientation, Qt.ScreenOrientation) -> int """
        return 0

    def availableGeometry(self): # real signature unknown; restored from __doc__
        """ availableGeometry(self) -> QRect """
        pass

    def availableGeometryChanged(self, QRect): # real signature unknown; restored from __doc__
        """ availableGeometryChanged(self, QRect) [signal] """
        pass

    def availableSize(self): # real signature unknown; restored from __doc__
        """ availableSize(self) -> QSize """
        pass

    def availableVirtualGeometry(self): # real signature unknown; restored from __doc__
        """ availableVirtualGeometry(self) -> QRect """
        pass

    def availableVirtualSize(self): # real signature unknown; restored from __doc__
        """ availableVirtualSize(self) -> QSize """
        pass

    def depth(self): # real signature unknown; restored from __doc__
        """ depth(self) -> int """
        return 0

    def devicePixelRatio(self): # real signature unknown; restored from __doc__
        """ devicePixelRatio(self) -> float """
        return 0.0

    def geometry(self): # real signature unknown; restored from __doc__
        """ geometry(self) -> QRect """
        pass

    def geometryChanged(self, QRect): # real signature unknown; restored from __doc__
        """ geometryChanged(self, QRect) [signal] """
        pass

    def grabWindow(self, sip_voidptr, x=0, y=0, width=-1, height=-1): # real signature unknown; restored from __doc__
        """ grabWindow(self, sip.voidptr, x: int = 0, y: int = 0, width: int = -1, height: int = -1) -> QPixmap """
        return QPixmap

    def isLandscape(self, Qt_ScreenOrientation): # real signature unknown; restored from __doc__
        """ isLandscape(self, Qt.ScreenOrientation) -> bool """
        return False

    def isPortrait(self, Qt_ScreenOrientation): # real signature unknown; restored from __doc__
        """ isPortrait(self, Qt.ScreenOrientation) -> bool """
        return False

    def logicalDotsPerInch(self): # real signature unknown; restored from __doc__
        """ logicalDotsPerInch(self) -> float """
        return 0.0

    def logicalDotsPerInchChanged(self, p_float): # real signature unknown; restored from __doc__
        """ logicalDotsPerInchChanged(self, float) [signal] """
        pass

    def logicalDotsPerInchX(self): # real signature unknown; restored from __doc__
        """ logicalDotsPerInchX(self) -> float """
        return 0.0

    def logicalDotsPerInchY(self): # real signature unknown; restored from __doc__
        """ logicalDotsPerInchY(self) -> float """
        return 0.0

    def manufacturer(self): # real signature unknown; restored from __doc__
        """ manufacturer(self) -> str """
        return ""

    def mapBetween(self, Qt_ScreenOrientation, Qt_ScreenOrientation_1, QRect): # real signature unknown; restored from __doc__
        """ mapBetween(self, Qt.ScreenOrientation, Qt.ScreenOrientation, QRect) -> QRect """
        pass

    def model(self): # real signature unknown; restored from __doc__
        """ model(self) -> str """
        return ""

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def nativeOrientation(self): # real signature unknown; restored from __doc__
        """ nativeOrientation(self) -> Qt.ScreenOrientation """
        pass

    def orientation(self): # real signature unknown; restored from __doc__
        """ orientation(self) -> Qt.ScreenOrientation """
        pass

    def orientationChanged(self, Qt_ScreenOrientation): # real signature unknown; restored from __doc__
        """ orientationChanged(self, Qt.ScreenOrientation) [signal] """
        pass

    def orientationUpdateMask(self): # real signature unknown; restored from __doc__
        """ orientationUpdateMask(self) -> Qt.ScreenOrientations """
        pass

    def physicalDotsPerInch(self): # real signature unknown; restored from __doc__
        """ physicalDotsPerInch(self) -> float """
        return 0.0

    def physicalDotsPerInchChanged(self, p_float): # real signature unknown; restored from __doc__
        """ physicalDotsPerInchChanged(self, float) [signal] """
        pass

    def physicalDotsPerInchX(self): # real signature unknown; restored from __doc__
        """ physicalDotsPerInchX(self) -> float """
        return 0.0

    def physicalDotsPerInchY(self): # real signature unknown; restored from __doc__
        """ physicalDotsPerInchY(self) -> float """
        return 0.0

    def physicalSize(self): # real signature unknown; restored from __doc__
        """ physicalSize(self) -> QSizeF """
        pass

    def physicalSizeChanged(self, QSizeF): # real signature unknown; restored from __doc__
        """ physicalSizeChanged(self, QSizeF) [signal] """
        pass

    def primaryOrientation(self): # real signature unknown; restored from __doc__
        """ primaryOrientation(self) -> Qt.ScreenOrientation """
        pass

    def primaryOrientationChanged(self, Qt_ScreenOrientation): # real signature unknown; restored from __doc__
        """ primaryOrientationChanged(self, Qt.ScreenOrientation) [signal] """
        pass

    def refreshRate(self): # real signature unknown; restored from __doc__
        """ refreshRate(self) -> float """
        return 0.0

    def refreshRateChanged(self, p_float): # real signature unknown; restored from __doc__
        """ refreshRateChanged(self, float) [signal] """
        pass

    def serialNumber(self): # real signature unknown; restored from __doc__
        """ serialNumber(self) -> str """
        return ""

    def setOrientationUpdateMask(self, Union, Qt_ScreenOrientations=None, Qt_ScreenOrientation=None): # real signature unknown; restored from __doc__
        """ setOrientationUpdateMask(self, Union[Qt.ScreenOrientations, Qt.ScreenOrientation]) """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> QSize """
        pass

    def transformBetween(self, Qt_ScreenOrientation, Qt_ScreenOrientation_1, QRect): # real signature unknown; restored from __doc__
        """ transformBetween(self, Qt.ScreenOrientation, Qt.ScreenOrientation, QRect) -> QTransform """
        return QTransform

    def virtualGeometry(self): # real signature unknown; restored from __doc__
        """ virtualGeometry(self) -> QRect """
        pass

    def virtualGeometryChanged(self, QRect): # real signature unknown; restored from __doc__
        """ virtualGeometryChanged(self, QRect) [signal] """
        pass

    def virtualSiblings(self): # real signature unknown; restored from __doc__
        """ virtualSiblings(self) -> List[QScreen] """
        return []

    def virtualSize(self): # real signature unknown; restored from __doc__
        """ virtualSize(self) -> QSize """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


