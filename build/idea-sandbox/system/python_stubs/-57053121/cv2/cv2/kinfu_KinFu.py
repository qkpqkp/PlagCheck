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

class kinfu_KinFu(object):
    # no doc
    def create(self, _params): # real signature unknown; restored from __doc__
        """
        create(_params) -> retval
        .
        """
        pass

    def getCloud(self, points=None, normals=None): # real signature unknown; restored from __doc__
        """
        getCloud([, points[, normals]]) -> points, normals
        .   @brief Gets points and normals of current 3d mesh
        .   
        .         The order of normals corresponds to order of points.
        .         The order of points is undefined.
        .   
        .           @param points vector of points which are 4-float vectors
        .           @param normals vector of normals which are 4-float vectors
        """
        pass

    def getNormals(self, points, normals=None): # real signature unknown; restored from __doc__
        """
        getNormals(points[, normals]) -> normals
        .   @brief Calculates normals for given points
        .           @param points input vector of points which are 4-float vectors
        .           @param normals output vector of corresponding normals which are 4-float vectors
        """
        pass

    def getPoints(self, points=None): # real signature unknown; restored from __doc__
        """
        getPoints([, points]) -> points
        .   @brief Gets points of current 3d mesh
        .   
        .        The order of points is undefined.
        .   
        .           @param points vector of points which are 4-float vectors
        """
        pass

    def render(self, image=None, cameraPose=None): # real signature unknown; restored from __doc__
        """
        render([, image[, cameraPose]]) -> image
        .   @brief Renders a volume into an image
        .   
        .         Renders a 0-surface of TSDF using Phong shading into a CV_8UC4 Mat.
        .         Light pose is fixed in KinFu params.
        .   
        .           @param image resulting image
        .           @param cameraPose pose of camera to render from. If empty then render from current pose
        .           which is a last frame camera pose.
        """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """
        reset() -> None
        .   @brief Resets the algorithm
        .   
        .       Clears current model and resets a pose.
        """
        pass

    def update(self, depth): # real signature unknown; restored from __doc__
        """
        update(depth) -> retval
        .   @brief Process next depth frame
        .   
        .         Integrates depth into voxel space with respect to its ICP-calculated pose.
        .         Input image is converted to CV_32F internally if has another type.
        .   
        .       @param depth one-channel image which size and depth scale is described in algorithm's parameters
        .       @return true if succeded to align new frame with current scene, false if opposite
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


