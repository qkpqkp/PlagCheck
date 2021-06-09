# encoding: utf-8
# module cv2.line_descriptor
# from C:\Users\Doly\Anaconda3\lib\site-packages\cv2\cv2.cp37-win_amd64.pyd
# by generator 1.147
# no doc
# no imports

# Variables with simple values

__loader__ = None

__spec__ = None

# functions

def BinaryDescriptor_createBinaryDescriptor(): # real signature unknown; restored from __doc__
    """
    BinaryDescriptor_createBinaryDescriptor() -> retval
    .   @brief Create a BinaryDescriptor object with default parameters (or with the ones provided)
    .     and return a smart pointer to it
    """
    pass

def drawKeylines(image, keylines, outImage=None, color=None, flags=None): # real signature unknown; restored from __doc__
    """
    drawKeylines(image, keylines[, outImage[, color[, flags]]]) -> outImage
    .   @brief Draws keylines.
    .   
    .   @param image input image
    .   @param keylines keylines to be drawn
    .   @param outImage output image to draw on
    .   @param color color of lines to be drawn (if set to defaul value, color is chosen randomly)
    .   @param flags drawing flags
    """
    pass

def drawLineMatches(img1, keylines1, img2, keylines2, matches1to2, outImg=None, matchColor=None, singleLineColor=None, matchesMask=None, flags=None): # real signature unknown; restored from __doc__
    """
    drawLineMatches(img1, keylines1, img2, keylines2, matches1to2[, outImg[, matchColor[, singleLineColor[, matchesMask[, flags]]]]]) -> outImg
    .   @brief Draws the found matches of keylines from two images.
    .   
    .   @param img1 first image
    .   @param keylines1 keylines extracted from first image
    .   @param img2 second image
    .   @param keylines2 keylines extracted from second image
    .   @param matches1to2 vector of matches
    .   @param outImg output matrix to draw on
    .   @param matchColor drawing color for matches (chosen randomly in case of default value)
    .   @param singleLineColor drawing color for keylines (chosen randomly in case of default value)
    .   @param matchesMask mask to indicate which matches must be drawn
    .   @param flags drawing flags, see DrawLinesMatchesFlags
    .   
    .   @note If both *matchColor* and *singleLineColor* are set to their default values, function draws
    .   matched lines and line connecting them with same color
    """
    pass

def LSDDetector_createLSDDetector(): # real signature unknown; restored from __doc__
    """
    LSDDetector_createLSDDetector() -> retval
    .   @brief Creates ad LSDDetector object, using smart pointers.
    """
    pass

def LSDDetector_createLSDDetectorWithParams(params): # real signature unknown; restored from __doc__
    """
    LSDDetector_createLSDDetectorWithParams(params) -> retval
    .
    """
    pass

# no classes
