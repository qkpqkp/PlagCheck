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

class linemod_Detector(object):
    # no doc
    def addSyntheticTemplate(self, templates, class_id): # real signature unknown; restored from __doc__
        """
        addSyntheticTemplate(templates, class_id) -> retval
        .   * \brief Add a new object template computed by external means.
        """
        pass

    def addTemplate(self, sources, class_id, object_mask): # real signature unknown; restored from __doc__
        """
        addTemplate(sources, class_id, object_mask) -> retval, bounding_box
        .   * \brief Add new object template.
        .      *
        .      * \param      sources      Source images, one for each modality.
        .      * \param      class_id     Object class ID.
        .      * \param      object_mask  Mask separating object from background.
        .      * \param[out] bounding_box Optionally return bounding box of the extracted features.
        .      *
        .      * \return Template ID, or -1 if failed to extract a valid template.
        """
        pass

    def classIds(self): # real signature unknown; restored from __doc__
        """
        classIds() -> retval
        .
        """
        pass

    def getModalities(self): # real signature unknown; restored from __doc__
        """
        getModalities() -> retval
        .   * \brief Get the modalities used by this detector.
        .      *
        .      * You are not permitted to add/remove modalities, but you may dynamic_cast them to
        .      * tweak parameters.
        """
        pass

    def getT(self, pyramid_level): # real signature unknown; restored from __doc__
        """
        getT(pyramid_level) -> retval
        .   * \brief Get sampling step T at pyramid_level.
        """
        pass

    def getTemplates(self, class_id, template_id): # real signature unknown; restored from __doc__
        """
        getTemplates(class_id, template_id) -> retval
        .   * \brief Get the template pyramid identified by template_id.
        .      *
        .      * For example, with 2 modalities (Gradient, Normal) and two pyramid levels
        .      * (L0, L1), the order is (GradientL0, NormalL0, GradientL1, NormalL1).
        """
        pass

    def match(self, sources, threshold, class_ids=None, quantized_images=None, masks=None): # real signature unknown; restored from __doc__
        """
        match(sources, threshold[, class_ids[, quantized_images[, masks]]]) -> matches, quantized_images
        .   * \brief Detect objects by template matching.
        .      *
        .      * Matches globally at the lowest pyramid level, then refines locally stepping up the pyramid.
        .      *
        .      * \param      sources   Source images, one for each modality.
        .      * \param      threshold Similarity threshold, a percentage between 0 and 100.
        .      * \param[out] matches   Template matches, sorted by similarity score.
        .      * \param      class_ids If non-empty, only search for the desired object classes.
        .      * \param[out] quantized_images Optionally return vector<Mat> of quantized images.
        .      * \param      masks     The masks for consideration during matching. The masks should be CV_8UC1
        .      *                       where 255 represents a valid pixel.  If non-empty, the vector must be
        .      *                       the same size as sources.  Each element must be
        .      *                       empty or the same size as its corresponding source.
        """
        pass

    def numClasses(self): # real signature unknown; restored from __doc__
        """
        numClasses() -> retval
        .
        """
        pass

    def numTemplates(self): # real signature unknown; restored from __doc__
        """
        numTemplates() -> retval
        .   
        
        
        
        numTemplates(class_id) -> retval
        .
        """
        pass

    def pyramidLevels(self): # real signature unknown; restored from __doc__
        """
        pyramidLevels() -> retval
        .   * \brief Get number of pyramid levels used by this detector.
        """
        pass

    def read(self, fn): # real signature unknown; restored from __doc__
        """
        read(fn) -> None
        .
        """
        pass

    def readClasses(self, class_ids, format=None): # real signature unknown; restored from __doc__
        """
        readClasses(class_ids[, format]) -> None
        .
        """
        pass

    def writeClasses(self, format=None): # real signature unknown; restored from __doc__
        """
        writeClasses([, format]) -> None
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


