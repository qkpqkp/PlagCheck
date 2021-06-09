# encoding: utf-8
# module cv2.linemod
# from C:\Users\Doly\Anaconda3\lib\site-packages\cv2\cv2.cp37-win_amd64.pyd
# by generator 1.147
# no doc
# no imports

# Variables with simple values

__loader__ = None

__spec__ = None

# functions

def ColorGradient_create(weak_threshold, num_features, strong_threshold): # real signature unknown; restored from __doc__
    """
    ColorGradient_create(weak_threshold, num_features, strong_threshold) -> retval
    .   * \brief Constructor.
    .      *
    .      * \param weak_threshold   When quantizing, discard gradients with magnitude less than this.
    .      * \param num_features     How many features a template must contain.
    .      * \param strong_threshold Consider as candidate features only gradients whose norms are
    .      *                         larger than this.
    """
    pass

def colormap(quantized, dst=None): # real signature unknown; restored from __doc__
    """
    colormap(quantized[, dst]) -> dst
    .   * \brief Debug function to colormap a quantized image for viewing.
    """
    pass

def DepthNormal_create(distance_threshold, difference_threshold, num_features, extract_threshold): # real signature unknown; restored from __doc__
    """
    DepthNormal_create(distance_threshold, difference_threshold, num_features, extract_threshold) -> retval
    .   * \brief Constructor.
    .      *
    .      * \param distance_threshold   Ignore pixels beyond this distance.
    .      * \param difference_threshold When computing normals, ignore contributions of pixels whose
    .      *                             depth difference with the central pixel is above this threshold.
    .      * \param num_features         How many features a template must contain.
    .      * \param extract_threshold    Consider as candidate feature only if there are no differing
    .      *                             orientations within a distance of extract_threshold.
    """
    pass

def drawFeatures(img, templates, tl, size=None): # real signature unknown; restored from __doc__
    """
    drawFeatures(img, templates, tl[, size]) -> img
    .   * \brief Debug function to draw linemod features
    .    * @param img
    .    * @param templates see @ref Detector::addTemplate
    .    * @param tl template bbox top-left offset see @ref Detector::addTemplate
    .    * @param size marker size see @ref cv::drawMarker
    """
    pass

def getDefaultLINE(): # real signature unknown; restored from __doc__
    """
    getDefaultLINE() -> retval
    .   * \brief Factory function for detector using LINE algorithm with color gradients.
    .    *
    .    * Default parameter settings suitable for VGA images.
    """
    pass

def getDefaultLINEMOD(): # real signature unknown; restored from __doc__
    """
    getDefaultLINEMOD() -> retval
    .   * \brief Factory function for detector using LINE-MOD algorithm with color gradients
    .    * and depth normals.
    .    *
    .    * Default parameter settings suitable for VGA images.
    """
    pass

def Modality_create(modality_type): # real signature unknown; restored from __doc__
    """
    Modality_create(modality_type) -> retval
    .   * \brief Create modality by name.
    .      *
    .      * The following modality types are supported:
    .      * - "ColorGradient"
    .      * - "DepthNormal"
    
    
    
    Modality_create(fn) -> retval
    .   * \brief Load a modality from file.
    """
    pass

# no classes
