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

class VideoCapture(object):
    # no doc
    def get(self, propId): # real signature unknown; restored from __doc__
        """
        get(propId) -> retval
        .   @brief Returns the specified VideoCapture property
        .   
        .       @param propId Property identifier from cv::VideoCaptureProperties (eg. cv::CAP_PROP_POS_MSEC, cv::CAP_PROP_POS_FRAMES, ...)
        .       or one from @ref videoio_flags_others
        .       @return Value for the specified property. Value 0 is returned when querying a property that is
        .       not supported by the backend used by the VideoCapture instance.
        .   
        .       @note Reading / writing properties involves many layers. Some unexpected result might happens
        .       along this chain.
        .       @code{.txt}
        .       VideoCapture -> API Backend -> Operating System -> Device Driver -> Device Hardware
        .       @endcode
        .       The returned value might be different from what really used by the device or it could be encoded
        .       using device dependent rules (eg. steps or percentage). Effective behaviour depends from device
        .       driver and API Backend
        """
        pass

    def getBackendName(self): # real signature unknown; restored from __doc__
        """
        getBackendName() -> retval
        .   @brief Returns used backend API name
        .   
        .        @note Stream should be opened.
        """
        pass

    def getExceptionMode(self): # real signature unknown; restored from __doc__
        """
        getExceptionMode() -> retval
        .
        """
        pass

    def grab(self): # real signature unknown; restored from __doc__
        """
        grab() -> retval
        .   @brief Grabs the next frame from video file or capturing device.
        .   
        .       @return `true` (non-zero) in the case of success.
        .   
        .       The method/function grabs the next frame from video file or camera and returns true (non-zero) in
        .       the case of success.
        .   
        .       The primary use of the function is in multi-camera environments, especially when the cameras do not
        .       have hardware synchronization. That is, you call VideoCapture::grab() for each camera and after that
        .       call the slower method VideoCapture::retrieve() to decode and get frame from each camera. This way
        .       the overhead on demosaicing or motion jpeg decompression etc. is eliminated and the retrieved frames
        .       from different cameras will be closer in time.
        .   
        .       Also, when a connected camera is multi-head (for example, a stereo camera or a Kinect device), the
        .       correct way of retrieving data from it is to call VideoCapture::grab() first and then call
        .       VideoCapture::retrieve() one or more times with different values of the channel parameter.
        .   
        .       @ref tutorial_kinect_openni
        """
        pass

    def isOpened(self): # real signature unknown; restored from __doc__
        """
        isOpened() -> retval
        .   @brief Returns true if video capturing has been initialized already.
        .   
        .       If the previous call to VideoCapture constructor or VideoCapture::open() succeeded, the method returns
        .       true.
        """
        pass

    def open(self, filename, apiPreference=None): # real signature unknown; restored from __doc__
        """
        open(filename[, apiPreference]) -> retval
        .   @brief  Opens a video file or a capturing device or an IP video stream for video capturing.
        .   
        .       @overload
        .   
        .       Parameters are same as the constructor VideoCapture(const String& filename, int apiPreference = CAP_ANY)
        .       @return `true` if the file has been successfully opened
        .   
        .       The method first calls VideoCapture::release to close the already opened file or camera.
        
        
        
        open(index[, apiPreference]) -> retval
        .   @brief  Opens a camera for video capturing
        .   
        .       @overload
        .   
        .       Parameters are same as the constructor VideoCapture(int index, int apiPreference = CAP_ANY)
        .       @return `true` if the camera has been successfully opened.
        .   
        .       The method first calls VideoCapture::release to close the already opened file or camera.
        """
        pass

    def read(self, image=None): # real signature unknown; restored from __doc__
        """
        read([, image]) -> retval, image
        .   @brief Grabs, decodes and returns the next video frame.
        .   
        .       @param [out] image the video frame is returned here. If no frames has been grabbed the image will be empty.
        .       @return `false` if no frames has been grabbed
        .   
        .       The method/function combines VideoCapture::grab() and VideoCapture::retrieve() in one call. This is the
        .       most convenient method for reading video files or capturing data from decode and returns the just
        .       grabbed frame. If no frames has been grabbed (camera has been disconnected, or there are no more
        .       frames in video file), the method returns false and the function returns empty image (with %cv::Mat, test it with Mat::empty()).
        .   
        .       @note In @ref videoio_c "C API", functions cvRetrieveFrame() and cv.RetrieveFrame() return image stored inside the video
        .       capturing structure. It is not allowed to modify or release the image! You can copy the frame using
        .       cvCloneImage and then do whatever you want with the copy.
        """
        pass

    def release(self): # real signature unknown; restored from __doc__
        """
        release() -> None
        .   @brief Closes video file or capturing device.
        .   
        .       The method is automatically called by subsequent VideoCapture::open and by VideoCapture
        .       destructor.
        .   
        .       The C function also deallocates memory and clears \*capture pointer.
        """
        pass

    def retrieve(self, image=None, flag=None): # real signature unknown; restored from __doc__
        """
        retrieve([, image[, flag]]) -> retval, image
        .   @brief Decodes and returns the grabbed video frame.
        .   
        .       @param [out] image the video frame is returned here. If no frames has been grabbed the image will be empty.
        .       @param flag it could be a frame index or a driver specific flag
        .       @return `false` if no frames has been grabbed
        .   
        .       The method decodes and returns the just grabbed frame. If no frames has been grabbed
        .       (camera has been disconnected, or there are no more frames in video file), the method returns false
        .       and the function returns an empty image (with %cv::Mat, test it with Mat::empty()).
        .   
        .       @sa read()
        .   
        .       @note In @ref videoio_c "C API", functions cvRetrieveFrame() and cv.RetrieveFrame() return image stored inside the video
        .       capturing structure. It is not allowed to modify or release the image! You can copy the frame using
        .       cvCloneImage and then do whatever you want with the copy.
        """
        pass

    def set(self, propId, value): # real signature unknown; restored from __doc__
        """
        set(propId, value) -> retval
        .   @brief Sets a property in the VideoCapture.
        .   
        .       @param propId Property identifier from cv::VideoCaptureProperties (eg. cv::CAP_PROP_POS_MSEC, cv::CAP_PROP_POS_FRAMES, ...)
        .       or one from @ref videoio_flags_others
        .       @param value Value of the property.
        .       @return `true` if the property is supported by backend used by the VideoCapture instance.
        .       @note Even if it returns `true` this doesn't ensure that the property
        .       value has been accepted by the capture device. See note in VideoCapture::get()
        """
        pass

    def setExceptionMode(self, enable): # real signature unknown; restored from __doc__
        """
        setExceptionMode(enable) -> None
        .   Switches exceptions mode
        .        *
        .        * methods raise exceptions if not successful instead of returning an error code
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


