# encoding: utf-8
# module cv2.cv2
# from C:\Users\Doly\Anaconda3\lib\site-packages\cv2\cv2.cp37-win_amd64.pyd
# by generator 1.147
""" Python wrapper for OpenCV. """

# imports
import cv2.cv2 as  # C:\Users\Doly\Anaconda3\lib\site-packages\cv2\cv2.cp37-win_amd64.pyd
import cv2.Error as Error # <module 'cv2.Error'>
import cv2.aruco as aruco # <module 'cv2.aruco'>
import cv2.bgsegm as bgsegm # <module 'cv2.bgsegm'>
import cv2.bioinspired as bioinspired # <module 'cv2.bioinspired'>
import cv2.cuda as cuda # <module 'cv2.cuda'>
import cv2.datasets as datasets # <module 'cv2.datasets'>
import cv2.detail as detail # <module 'cv2.detail'>
import cv2.dnn as dnn # <module 'cv2.dnn'>
import cv2.face as face # <module 'cv2.face'>
import cv2.fisheye as fisheye # <module 'cv2.fisheye'>
import cv2.flann as flann # <module 'cv2.flann'>
import cv2.ft as ft # <module 'cv2.ft'>
import cv2.hfs as hfs # <module 'cv2.hfs'>
import cv2.img_hash as img_hash # <module 'cv2.img_hash'>
import cv2.instr as instr # <module 'cv2.instr'>
import cv2.ipp as ipp # <module 'cv2.ipp'>
import cv2.kinfu as kinfu # <module 'cv2.kinfu'>
import cv2.line_descriptor as line_descriptor # <module 'cv2.line_descriptor'>
import cv2.linemod as linemod # <module 'cv2.linemod'>
import cv2.ml as ml # <module 'cv2.ml'>
import cv2.motempl as motempl # <module 'cv2.motempl'>
import cv2.multicalib as multicalib # <module 'cv2.multicalib'>
import cv2.ocl as ocl # <module 'cv2.ocl'>
import cv2.ogl as ogl # <module 'cv2.ogl'>
import cv2.omnidir as omnidir # <module 'cv2.omnidir'>
import cv2.optflow as optflow # <module 'cv2.optflow'>
import cv2.plot as plot # <module 'cv2.plot'>
import cv2.ppf_match_3d as ppf_match_3d # <module 'cv2.ppf_match_3d'>
import cv2.quality as quality # <module 'cv2.quality'>
import cv2.reg as reg # <module 'cv2.reg'>
import cv2.rgbd as rgbd # <module 'cv2.rgbd'>
import cv2.saliency as saliency # <module 'cv2.saliency'>
import cv2.samples as samples # <module 'cv2.samples'>
import cv2.structured_light as structured_light # <module 'cv2.structured_light'>
import cv2.text as text # <module 'cv2.text'>
import cv2.utils as utils # <module 'cv2.utils'>
import cv2.videoio_registry as videoio_registry # <module 'cv2.videoio_registry'>
import cv2.videostab as videostab # <module 'cv2.videostab'>
import cv2.xfeatures2d as xfeatures2d # <module 'cv2.xfeatures2d'>
import cv2.ximgproc as ximgproc # <module 'cv2.ximgproc'>
import cv2.xphoto as xphoto # <module 'cv2.xphoto'>
import cv2 as __cv2


from .object import object

class cuda_GpuMat(object):
    # no doc
    def adjustROI(self, dtop, dbottom, dleft, dright): # real signature unknown; restored from __doc__
        """
        adjustROI(dtop, dbottom, dleft, dright) -> retval
        .
        """
        pass

    def assignTo(self, m, type=None): # real signature unknown; restored from __doc__
        """
        assignTo(m[, type]) -> None
        .
        """
        pass

    def channels(self): # real signature unknown; restored from __doc__
        """
        channels() -> retval
        .
        """
        pass

    def clone(self): # real signature unknown; restored from __doc__
        """
        clone() -> retval
        .
        """
        pass

    def col(self, x): # real signature unknown; restored from __doc__
        """
        col(x) -> retval
        .
        """
        pass

    def colRange(self, startcol, endcol): # real signature unknown; restored from __doc__
        """
        colRange(startcol, endcol) -> retval
        .   
        
        
        
        colRange(r) -> retval
        .
        """
        pass

    def convertTo(self, rtype, dst=None): # real signature unknown; restored from __doc__
        """
        convertTo(rtype[, dst]) -> dst
        .   
        
        
        
        convertTo(rtype, stream[, dst]) -> dst
        .   
        
        
        
        convertTo(rtype, alpha[, dst[, beta]]) -> dst
        .   
        
        
        
        convertTo(rtype, alpha, stream[, dst]) -> dst
        .   
        
        
        
        convertTo(rtype, alpha, beta, stream[, dst]) -> dst
        .
        """
        pass

    def copyTo(self, dst=None): # real signature unknown; restored from __doc__
        """
        copyTo([, dst]) -> dst
        .   
        
        
        
        copyTo(stream[, dst]) -> dst
        .   
        
        
        
        copyTo(mask[, dst]) -> dst
        .   
        
        
        
        copyTo(mask, stream[, dst]) -> dst
        .
        """
        pass

    def create(self, rows, cols, type): # real signature unknown; restored from __doc__
        """
        create(rows, cols, type) -> None
        .   
        
        
        
        create(size, type) -> None
        .
        """
        pass

    def defaultAllocator(self): # real signature unknown; restored from __doc__
        """
        defaultAllocator() -> retval
        .
        """
        pass

    def depth(self): # real signature unknown; restored from __doc__
        """
        depth() -> retval
        .
        """
        pass

    def download(self, dst=None): # real signature unknown; restored from __doc__
        """
        download([, dst]) -> dst
        .   @brief Performs data download from GpuMat (Blocking call)
        .   
        .       This function copies data from device memory to host memory. As being a blocking call, it is
        .       guaranteed that the copy operation is finished when this function returns.
        
        
        
        download(stream[, dst]) -> dst
        .   @brief Performs data download from GpuMat (Non-Blocking call)
        .   
        .       This function copies data from device memory to host memory. As being a non-blocking call, this
        .       function may return even if the copy operation is not finished.
        .   
        .       The copy operation may be overlapped with operations in other non-default streams if \p stream is
        .       not the default stream and \p dst is HostMem allocated with HostMem::PAGE_LOCKED option.
        """
        pass

    def elemSize(self): # real signature unknown; restored from __doc__
        """
        elemSize() -> retval
        .
        """
        pass

    def elemSize1(self): # real signature unknown; restored from __doc__
        """
        elemSize1() -> retval
        .
        """
        pass

    def empty(self): # real signature unknown; restored from __doc__
        """
        empty() -> retval
        .
        """
        pass

    def isContinuous(self): # real signature unknown; restored from __doc__
        """
        isContinuous() -> retval
        .
        """
        pass

    def locateROI(self, wholeSize, ofs): # real signature unknown; restored from __doc__
        """
        locateROI(wholeSize, ofs) -> None
        .
        """
        pass

    def reshape(self, cn, rows=None): # real signature unknown; restored from __doc__
        """
        reshape(cn[, rows]) -> retval
        .
        """
        pass

    def row(self, y): # real signature unknown; restored from __doc__
        """
        row(y) -> retval
        .
        """
        pass

    def rowRange(self, startrow, endrow): # real signature unknown; restored from __doc__
        """
        rowRange(startrow, endrow) -> retval
        .   
        
        
        
        rowRange(r) -> retval
        .
        """
        pass

    def setDefaultAllocator(self, allocator): # real signature unknown; restored from __doc__
        """
        setDefaultAllocator(allocator) -> None
        .
        """
        pass

    def setTo(self, s): # real signature unknown; restored from __doc__
        """
        setTo(s) -> retval
        .   
        
        
        
        setTo(s, stream) -> retval
        .   
        
        
        
        setTo(s, mask) -> retval
        .   
        
        
        
        setTo(s, mask, stream) -> retval
        .
        """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """
        size() -> retval
        .
        """
        pass

    def step1(self): # real signature unknown; restored from __doc__
        """
        step1() -> retval
        .
        """
        pass

    def swap(self, mat): # real signature unknown; restored from __doc__
        """
        swap(mat) -> None
        .
        """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """
        type() -> retval
        .
        """
        pass

    def updateContinuityFlag(self): # real signature unknown; restored from __doc__
        """
        updateContinuityFlag() -> None
        .
        """
        pass

    def upload(self, arr): # real signature unknown; restored from __doc__
        """
        upload(arr) -> None
        .   @brief Performs data upload to GpuMat (Blocking call)
        .   
        .       This function copies data from host memory to device memory. As being a blocking call, it is
        .       guaranteed that the copy operation is finished when this function returns.
        
        
        
        upload(arr, stream) -> None
        .   @brief Performs data upload to GpuMat (Non-Blocking call)
        .   
        .       This function copies data from host memory to device memory. As being a non-blocking call, this
        .       function may return even if the copy operation is not finished.
        .   
        .       The copy operation may be overlapped with operations in other non-default streams if \p stream is
        .       not the default stream and \p dst is HostMem allocated with HostMem::PAGE_LOCKED option.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    step = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """step"""



