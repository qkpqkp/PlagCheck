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

class FileStorage(object):
    # no doc
    def getFirstTopLevelNode(self): # real signature unknown; restored from __doc__
        """
        getFirstTopLevelNode() -> retval
        .   @brief Returns the first element of the top-level mapping.
        .        @returns The first element of the top-level mapping.
        """
        pass

    def getFormat(self): # real signature unknown; restored from __doc__
        """
        getFormat() -> retval
        .   @brief Returns the current format.
        .        * @returns The current format, see FileStorage::Mode
        """
        pass

    def getNode(self, nodename): # real signature unknown; restored from __doc__
        """
        getNode(nodename) -> retval
        .   @overload
        """
        pass

    def isOpened(self): # real signature unknown; restored from __doc__
        """
        isOpened() -> retval
        .   @brief Checks whether the file is opened.
        .   
        .        @returns true if the object is associated with the current file and false otherwise. It is a
        .        good practice to call this method after you tried to open a file.
        """
        pass

    def open(self, filename, flags, encoding=None): # real signature unknown; restored from __doc__
        """
        open(filename, flags[, encoding]) -> retval
        .   @brief Opens a file.
        .   
        .        See description of parameters in FileStorage::FileStorage. The method calls FileStorage::release
        .        before opening the file.
        .        @param filename Name of the file to open or the text string to read the data from.
        .        Extension of the file (.xml, .yml/.yaml or .json) determines its format (XML, YAML or JSON
        .        respectively). Also you can append .gz to work with compressed files, for example myHugeMatrix.xml.gz. If both
        .        FileStorage::WRITE and FileStorage::MEMORY flags are specified, source is used just to specify
        .        the output file format (e.g. mydata.xml, .yml etc.). A file name can also contain parameters.
        .        You can use this format, "*?base64" (e.g. "file.json?base64" (case sensitive)), as an alternative to
        .        FileStorage::BASE64 flag.
        .        @param flags Mode of operation. One of FileStorage::Mode
        .        @param encoding Encoding of the file. Note that UTF-16 XML encoding is not supported currently and
        .        you should use 8-bit encoding instead of it.
        """
        pass

    def release(self): # real signature unknown; restored from __doc__
        """
        release() -> None
        .   @brief Closes the file and releases all the memory buffers.
        .   
        .        Call this method after all I/O operations with the storage are finished.
        """
        pass

    def releaseAndGetString(self): # real signature unknown; restored from __doc__
        """
        releaseAndGetString() -> retval
        .   @brief Closes the file and releases all the memory buffers.
        .   
        .        Call this method after all I/O operations with the storage are finished. If the storage was
        .        opened for writing data and FileStorage::WRITE was specified
        """
        pass

    def root(self, streamidx=None): # real signature unknown; restored from __doc__
        """
        root([, streamidx]) -> retval
        .   @brief Returns the top-level mapping
        .        @param streamidx Zero-based index of the stream. In most cases there is only one stream in the file.
        .        However, YAML supports multiple streams and so there can be several.
        .        @returns The top-level mapping.
        """
        pass

    def write(self, name, val): # real signature unknown; restored from __doc__
        """
        write(name, val) -> None
        .   * @brief Simplified writing API to use with bindings.
        .        * @param name Name of the written object
        .        * @param val Value of the written object
        """
        pass

    def writeComment(self, comment, append=None): # real signature unknown; restored from __doc__
        """
        writeComment(comment[, append]) -> None
        .   @brief Writes a comment.
        .   
        .        The function writes a comment into file storage. The comments are skipped when the storage is read.
        .        @param comment The written comment, single-line or multi-line
        .        @param append If true, the function tries to put the comment at the end of current line.
        .        Else if the comment is multi-line, or if it does not fit at the end of the current
        .        line, the comment starts a new line.
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


