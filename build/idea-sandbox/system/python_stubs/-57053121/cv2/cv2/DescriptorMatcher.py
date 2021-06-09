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


class DescriptorMatcher(__cv2.Algorithm):
    # no doc
    def add(self, descriptors): # real signature unknown; restored from __doc__
        """
        add(descriptors) -> None
        .   @brief Adds descriptors to train a CPU(trainDescCollectionis) or GPU(utrainDescCollectionis) descriptor
        .       collection.
        .   
        .       If the collection is not empty, the new descriptors are added to existing train descriptors.
        .   
        .       @param descriptors Descriptors to add. Each descriptors[i] is a set of descriptors from the same
        .       train image.
        """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """
        clear() -> None
        .   @brief Clears the train descriptor collections.
        """
        pass

    def clone(self, emptyTrainData=None): # real signature unknown; restored from __doc__
        """
        clone([, emptyTrainData]) -> retval
        .   @brief Clones the matcher.
        .   
        .       @param emptyTrainData If emptyTrainData is false, the method creates a deep copy of the object,
        .       that is, copies both parameters and train data. If emptyTrainData is true, the method creates an
        .       object copy with the current parameters but with empty train data.
        """
        pass

    def create(self, descriptorMatcherType): # real signature unknown; restored from __doc__
        """
        create(descriptorMatcherType) -> retval
        .   @brief Creates a descriptor matcher of a given type with the default parameters (using default
        .       constructor).
        .   
        .       @param descriptorMatcherType Descriptor matcher type. Now the following matcher types are
        .       supported:
        .       -   `BruteForce` (it uses L2 )
        .       -   `BruteForce-L1`
        .       -   `BruteForce-Hamming`
        .       -   `BruteForce-Hamming(2)`
        .       -   `FlannBased`
        
        
        
        create(matcherType) -> retval
        .
        """
        pass

    def empty(self): # real signature unknown; restored from __doc__
        """
        empty() -> retval
        .   @brief Returns true if there are no train descriptors in the both collections.
        """
        pass

    def getTrainDescriptors(self): # real signature unknown; restored from __doc__
        """
        getTrainDescriptors() -> retval
        .   @brief Returns a constant link to the train descriptor collection trainDescCollection .
        """
        pass

    def isMaskSupported(self): # real signature unknown; restored from __doc__
        """
        isMaskSupported() -> retval
        .   @brief Returns true if the descriptor matcher supports masking permissible matches.
        """
        pass

    def knnMatch(self, queryDescriptors, trainDescriptors, k, mask=None, compactResult=None): # real signature unknown; restored from __doc__
        """
        knnMatch(queryDescriptors, trainDescriptors, k[, mask[, compactResult]]) -> matches
        .   @brief Finds the k best matches for each descriptor from a query set.
        .   
        .       @param queryDescriptors Query set of descriptors.
        .       @param trainDescriptors Train set of descriptors. This set is not added to the train descriptors
        .       collection stored in the class object.
        .       @param mask Mask specifying permissible matches between an input query and train matrices of
        .       descriptors.
        .       @param matches Matches. Each matches[i] is k or less matches for the same query descriptor.
        .       @param k Count of best matches found per each query descriptor or less if a query descriptor has
        .       less than k possible matches in total.
        .       @param compactResult Parameter used when the mask (or masks) is not empty. If compactResult is
        .       false, the matches vector has the same size as queryDescriptors rows. If compactResult is true,
        .       the matches vector does not contain matches for fully masked-out query descriptors.
        .   
        .       These extended variants of DescriptorMatcher::match methods find several best matches for each query
        .       descriptor. The matches are returned in the distance increasing order. See DescriptorMatcher::match
        .       for the details about query and train descriptors.
        
        
        
        knnMatch(queryDescriptors, k[, masks[, compactResult]]) -> matches
        .   @overload
        .       @param queryDescriptors Query set of descriptors.
        .       @param matches Matches. Each matches[i] is k or less matches for the same query descriptor.
        .       @param k Count of best matches found per each query descriptor or less if a query descriptor has
        .       less than k possible matches in total.
        .       @param masks Set of masks. Each masks[i] specifies permissible matches between the input query
        .       descriptors and stored train descriptors from the i-th image trainDescCollection[i].
        .       @param compactResult Parameter used when the mask (or masks) is not empty. If compactResult is
        .       false, the matches vector has the same size as queryDescriptors rows. If compactResult is true,
        .       the matches vector does not contain matches for fully masked-out query descriptors.
        """
        pass

    def match(self, queryDescriptors, trainDescriptors, mask=None): # real signature unknown; restored from __doc__
        """
        match(queryDescriptors, trainDescriptors[, mask]) -> matches
        .   @brief Finds the best match for each descriptor from a query set.
        .   
        .       @param queryDescriptors Query set of descriptors.
        .       @param trainDescriptors Train set of descriptors. This set is not added to the train descriptors
        .       collection stored in the class object.
        .       @param matches Matches. If a query descriptor is masked out in mask , no match is added for this
        .       descriptor. So, matches size may be smaller than the query descriptors count.
        .       @param mask Mask specifying permissible matches between an input query and train matrices of
        .       descriptors.
        .   
        .       In the first variant of this method, the train descriptors are passed as an input argument. In the
        .       second variant of the method, train descriptors collection that was set by DescriptorMatcher::add is
        .       used. Optional mask (or masks) can be passed to specify which query and training descriptors can be
        .       matched. Namely, queryDescriptors[i] can be matched with trainDescriptors[j] only if
        .       mask.at\<uchar\>(i,j) is non-zero.
        
        
        
        match(queryDescriptors[, masks]) -> matches
        .   @overload
        .       @param queryDescriptors Query set of descriptors.
        .       @param matches Matches. If a query descriptor is masked out in mask , no match is added for this
        .       descriptor. So, matches size may be smaller than the query descriptors count.
        .       @param masks Set of masks. Each masks[i] specifies permissible matches between the input query
        .       descriptors and stored train descriptors from the i-th image trainDescCollection[i].
        """
        pass

    def radiusMatch(self, queryDescriptors, trainDescriptors, maxDistance, mask=None, compactResult=None): # real signature unknown; restored from __doc__
        """
        radiusMatch(queryDescriptors, trainDescriptors, maxDistance[, mask[, compactResult]]) -> matches
        .   @brief For each query descriptor, finds the training descriptors not farther than the specified distance.
        .   
        .       @param queryDescriptors Query set of descriptors.
        .       @param trainDescriptors Train set of descriptors. This set is not added to the train descriptors
        .       collection stored in the class object.
        .       @param matches Found matches.
        .       @param compactResult Parameter used when the mask (or masks) is not empty. If compactResult is
        .       false, the matches vector has the same size as queryDescriptors rows. If compactResult is true,
        .       the matches vector does not contain matches for fully masked-out query descriptors.
        .       @param maxDistance Threshold for the distance between matched descriptors. Distance means here
        .       metric distance (e.g. Hamming distance), not the distance between coordinates (which is measured
        .       in Pixels)!
        .       @param mask Mask specifying permissible matches between an input query and train matrices of
        .       descriptors.
        .   
        .       For each query descriptor, the methods find such training descriptors that the distance between the
        .       query descriptor and the training descriptor is equal or smaller than maxDistance. Found matches are
        .       returned in the distance increasing order.
        
        
        
        radiusMatch(queryDescriptors, maxDistance[, masks[, compactResult]]) -> matches
        .   @overload
        .       @param queryDescriptors Query set of descriptors.
        .       @param matches Found matches.
        .       @param maxDistance Threshold for the distance between matched descriptors. Distance means here
        .       metric distance (e.g. Hamming distance), not the distance between coordinates (which is measured
        .       in Pixels)!
        .       @param masks Set of masks. Each masks[i] specifies permissible matches between the input query
        .       descriptors and stored train descriptors from the i-th image trainDescCollection[i].
        .       @param compactResult Parameter used when the mask (or masks) is not empty. If compactResult is
        .       false, the matches vector has the same size as queryDescriptors rows. If compactResult is true,
        .       the matches vector does not contain matches for fully masked-out query descriptors.
        """
        pass

    def read(self, fileName): # real signature unknown; restored from __doc__
        """
        read(fileName) -> None
        .   
        
        
        
        read(arg1) -> None
        .
        """
        pass

    def train(self): # real signature unknown; restored from __doc__
        """
        train() -> None
        .   @brief Trains a descriptor matcher
        .   
        .       Trains a descriptor matcher (for example, the flann index). In all methods to match, the method
        .       train() is run every time before matching. Some descriptor matchers (for example, BruteForceMatcher)
        .       have an empty implementation of this method. Other matchers really train their inner structures (for
        .       example, FlannBasedMatcher trains flann::Index ).
        """
        pass

    def write(self, fileName): # real signature unknown; restored from __doc__
        """
        write(fileName) -> None
        .   
        
        
        
        write(fs[, name]) -> None
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


