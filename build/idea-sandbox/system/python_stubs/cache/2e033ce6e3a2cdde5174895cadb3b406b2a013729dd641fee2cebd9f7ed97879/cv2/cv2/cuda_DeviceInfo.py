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

class cuda_DeviceInfo(object):
    # no doc
    def asyncEngineCount(self): # real signature unknown; restored from __doc__
        """
        asyncEngineCount() -> retval
        .
        """
        pass

    def canMapHostMemory(self): # real signature unknown; restored from __doc__
        """
        canMapHostMemory() -> retval
        .
        """
        pass

    def clockRate(self): # real signature unknown; restored from __doc__
        """
        clockRate() -> retval
        .
        """
        pass

    def computeMode(self): # real signature unknown; restored from __doc__
        """
        computeMode() -> retval
        .
        """
        pass

    def concurrentKernels(self): # real signature unknown; restored from __doc__
        """
        concurrentKernels() -> retval
        .
        """
        pass

    def deviceID(self): # real signature unknown; restored from __doc__
        """
        deviceID() -> retval
        .   @brief Returns system index of the CUDA device starting with 0.
        """
        pass

    def ECCEnabled(self): # real signature unknown; restored from __doc__
        """
        ECCEnabled() -> retval
        .
        """
        pass

    def freeMemory(self): # real signature unknown; restored from __doc__
        """
        freeMemory() -> retval
        .
        """
        pass

    def integrated(self): # real signature unknown; restored from __doc__
        """
        integrated() -> retval
        .
        """
        pass

    def isCompatible(self): # real signature unknown; restored from __doc__
        """
        isCompatible() -> retval
        .   @brief Checks the CUDA module and device compatibility.
        .   
        .       This function returns true if the CUDA module can be run on the specified device. Otherwise, it
        .       returns false .
        """
        pass

    def kernelExecTimeoutEnabled(self): # real signature unknown; restored from __doc__
        """
        kernelExecTimeoutEnabled() -> retval
        .
        """
        pass

    def l2CacheSize(self): # real signature unknown; restored from __doc__
        """
        l2CacheSize() -> retval
        .
        """
        pass

    def majorVersion(self): # real signature unknown; restored from __doc__
        """
        majorVersion() -> retval
        .
        """
        pass

    def maxGridSize(self): # real signature unknown; restored from __doc__
        """
        maxGridSize() -> retval
        .
        """
        pass

    def maxSurface1D(self): # real signature unknown; restored from __doc__
        """
        maxSurface1D() -> retval
        .
        """
        pass

    def maxSurface1DLayered(self): # real signature unknown; restored from __doc__
        """
        maxSurface1DLayered() -> retval
        .
        """
        pass

    def maxSurface2D(self): # real signature unknown; restored from __doc__
        """
        maxSurface2D() -> retval
        .
        """
        pass

    def maxSurface2DLayered(self): # real signature unknown; restored from __doc__
        """
        maxSurface2DLayered() -> retval
        .
        """
        pass

    def maxSurface3D(self): # real signature unknown; restored from __doc__
        """
        maxSurface3D() -> retval
        .
        """
        pass

    def maxSurfaceCubemap(self): # real signature unknown; restored from __doc__
        """
        maxSurfaceCubemap() -> retval
        .
        """
        pass

    def maxSurfaceCubemapLayered(self): # real signature unknown; restored from __doc__
        """
        maxSurfaceCubemapLayered() -> retval
        .
        """
        pass

    def maxTexture1D(self): # real signature unknown; restored from __doc__
        """
        maxTexture1D() -> retval
        .
        """
        pass

    def maxTexture1DLayered(self): # real signature unknown; restored from __doc__
        """
        maxTexture1DLayered() -> retval
        .
        """
        pass

    def maxTexture1DLinear(self): # real signature unknown; restored from __doc__
        """
        maxTexture1DLinear() -> retval
        .
        """
        pass

    def maxTexture1DMipmap(self): # real signature unknown; restored from __doc__
        """
        maxTexture1DMipmap() -> retval
        .
        """
        pass

    def maxTexture2D(self): # real signature unknown; restored from __doc__
        """
        maxTexture2D() -> retval
        .
        """
        pass

    def maxTexture2DGather(self): # real signature unknown; restored from __doc__
        """
        maxTexture2DGather() -> retval
        .
        """
        pass

    def maxTexture2DLayered(self): # real signature unknown; restored from __doc__
        """
        maxTexture2DLayered() -> retval
        .
        """
        pass

    def maxTexture2DLinear(self): # real signature unknown; restored from __doc__
        """
        maxTexture2DLinear() -> retval
        .
        """
        pass

    def maxTexture2DMipmap(self): # real signature unknown; restored from __doc__
        """
        maxTexture2DMipmap() -> retval
        .
        """
        pass

    def maxTexture3D(self): # real signature unknown; restored from __doc__
        """
        maxTexture3D() -> retval
        .
        """
        pass

    def maxTextureCubemap(self): # real signature unknown; restored from __doc__
        """
        maxTextureCubemap() -> retval
        .
        """
        pass

    def maxTextureCubemapLayered(self): # real signature unknown; restored from __doc__
        """
        maxTextureCubemapLayered() -> retval
        .
        """
        pass

    def maxThreadsDim(self): # real signature unknown; restored from __doc__
        """
        maxThreadsDim() -> retval
        .
        """
        pass

    def maxThreadsPerBlock(self): # real signature unknown; restored from __doc__
        """
        maxThreadsPerBlock() -> retval
        .
        """
        pass

    def maxThreadsPerMultiProcessor(self): # real signature unknown; restored from __doc__
        """
        maxThreadsPerMultiProcessor() -> retval
        .
        """
        pass

    def memoryBusWidth(self): # real signature unknown; restored from __doc__
        """
        memoryBusWidth() -> retval
        .
        """
        pass

    def memoryClockRate(self): # real signature unknown; restored from __doc__
        """
        memoryClockRate() -> retval
        .
        """
        pass

    def memPitch(self): # real signature unknown; restored from __doc__
        """
        memPitch() -> retval
        .
        """
        pass

    def minorVersion(self): # real signature unknown; restored from __doc__
        """
        minorVersion() -> retval
        .
        """
        pass

    def multiProcessorCount(self): # real signature unknown; restored from __doc__
        """
        multiProcessorCount() -> retval
        .
        """
        pass

    def pciBusID(self): # real signature unknown; restored from __doc__
        """
        pciBusID() -> retval
        .
        """
        pass

    def pciDeviceID(self): # real signature unknown; restored from __doc__
        """
        pciDeviceID() -> retval
        .
        """
        pass

    def pciDomainID(self): # real signature unknown; restored from __doc__
        """
        pciDomainID() -> retval
        .
        """
        pass

    def queryMemory(self, totalMemory, freeMemory): # real signature unknown; restored from __doc__
        """
        queryMemory(totalMemory, freeMemory) -> None
        .
        """
        pass

    def regsPerBlock(self): # real signature unknown; restored from __doc__
        """
        regsPerBlock() -> retval
        .
        """
        pass

    def sharedMemPerBlock(self): # real signature unknown; restored from __doc__
        """
        sharedMemPerBlock() -> retval
        .
        """
        pass

    def surfaceAlignment(self): # real signature unknown; restored from __doc__
        """
        surfaceAlignment() -> retval
        .
        """
        pass

    def tccDriver(self): # real signature unknown; restored from __doc__
        """
        tccDriver() -> retval
        .
        """
        pass

    def textureAlignment(self): # real signature unknown; restored from __doc__
        """
        textureAlignment() -> retval
        .
        """
        pass

    def texturePitchAlignment(self): # real signature unknown; restored from __doc__
        """
        texturePitchAlignment() -> retval
        .
        """
        pass

    def totalConstMem(self): # real signature unknown; restored from __doc__
        """
        totalConstMem() -> retval
        .
        """
        pass

    def totalGlobalMem(self): # real signature unknown; restored from __doc__
        """
        totalGlobalMem() -> retval
        .
        """
        pass

    def totalMemory(self): # real signature unknown; restored from __doc__
        """
        totalMemory() -> retval
        .
        """
        pass

    def unifiedAddressing(self): # real signature unknown; restored from __doc__
        """
        unifiedAddressing() -> retval
        .
        """
        pass

    def warpSize(self): # real signature unknown; restored from __doc__
        """
        warpSize() -> retval
        .
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


