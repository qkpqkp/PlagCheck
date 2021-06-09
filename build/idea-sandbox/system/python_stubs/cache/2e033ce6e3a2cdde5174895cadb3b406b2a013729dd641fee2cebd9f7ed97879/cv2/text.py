# encoding: utf-8
# module cv2.text
# from C:\Users\Doly\Anaconda3\lib\site-packages\cv2\cv2.cp37-win_amd64.pyd
# by generator 1.147
# no doc
# no imports

# Variables with simple values

ERFILTER_NM_IHSGrad = 1
ERFILTER_NM_IHSGRAD = 1
ERFILTER_NM_RGBLGrad = 0
ERFILTER_NM_RGBLGRAD = 0

ERGROUPING_ORIENTATION_ANY = 1
ERGROUPING_ORIENTATION_HORIZ = 0

OCR_CNN_CLASSIFIER = 1

OCR_DECODER_VITERBI = 0

OCR_KNN_CLASSIFIER = 0

OCR_LEVEL_TEXTLINE = 1
OCR_LEVEL_WORD = 0

OEM_CUBE_ONLY = 1

OEM_DEFAULT = 3

OEM_TESSERACT_CUBE_COMBINED = 2

OEM_TESSERACT_ONLY = 0

PSM_AUTO = 3

PSM_AUTO_ONLY = 2
PSM_AUTO_OSD = 1

PSM_CIRCLE_WORD = 9

PSM_OSD_ONLY = 0

PSM_SINGLE_BLOCK = 6

PSM_SINGLE_BLOCK_VERT_TEXT = 5

PSM_SINGLE_CHAR = 10
PSM_SINGLE_COLUMN = 4
PSM_SINGLE_LINE = 7
PSM_SINGLE_WORD = 8

__loader__ = None

__spec__ = None

# functions

def computeNMChannels(_src, _channels=None, _mode=None): # real signature unknown; restored from __doc__
    """
    computeNMChannels(_src[, _channels[, _mode]]) -> _channels
    .   @brief Compute the different channels to be processed independently in the N&M algorithm @cite Neumann12.
    .   
    .   @param _src Source image. Must be RGB CV_8UC3.
    .   
    .   @param _channels Output vector\<Mat\> where computed channels are stored.
    .   
    .   @param _mode Mode of operation. Currently the only available options are:
    .   **ERFILTER_NM_RGBLGrad** (used by default) and **ERFILTER_NM_IHSGrad**.
    .   
    .   In N&M algorithm, the combination of intensity (I), hue (H), saturation (S), and gradient magnitude
    .   channels (Grad) are used in order to obtain high localization recall. This implementation also
    .   provides an alternative combination of red (R), green (G), blue (B), lightness (L), and gradient
    .   magnitude (Grad).
    """
    pass

def createERFilterNM1(cb, thresholdDelta=None, minArea=None, maxArea=None, minProbability=None, nonMaxSuppression=None, minProbabilityDiff=None): # real signature unknown; restored from __doc__
    """
    createERFilterNM1(cb[, thresholdDelta[, minArea[, maxArea[, minProbability[, nonMaxSuppression[, minProbabilityDiff]]]]]]) -> retval
    .   @brief Create an Extremal Region Filter for the 1st stage classifier of N&M algorithm @cite Neumann12.
    .   
    .   @param  cb :   Callback with the classifier. Default classifier can be implicitly load with function
    .   loadClassifierNM1, e.g. from file in samples/cpp/trained_classifierNM1.xml
    .   @param  thresholdDelta :   Threshold step in subsequent thresholds when extracting the component tree
    .   @param  minArea :   The minimum area (% of image size) allowed for retreived ER's
    .   @param  maxArea :   The maximum area (% of image size) allowed for retreived ER's
    .   @param  minProbability :   The minimum probability P(er|character) allowed for retreived ER's
    .   @param  nonMaxSuppression :   Whenever non-maximum suppression is done over the branch probabilities
    .   @param  minProbabilityDiff :   The minimum probability difference between local maxima and local minima ERs
    .   
    .   The component tree of the image is extracted by a threshold increased step by step from 0 to 255,
    .   incrementally computable descriptors (aspect_ratio, compactness, number of holes, and number of
    .   horizontal crossings) are computed for each ER and used as features for a classifier which estimates
    .   the class-conditional probability P(er|character). The value of P(er|character) is tracked using the
    .   inclusion relation of ER across all thresholds and only the ERs which correspond to local maximum of
    .   the probability P(er|character) are selected (if the local maximum of the probability is above a
    .   global limit pmin and the difference between local maximum and local minimum is greater than
    .   minProbabilityDiff).
    
    
    
    createERFilterNM1(filename[, thresholdDelta[, minArea[, maxArea[, minProbability[, nonMaxSuppression[, minProbabilityDiff]]]]]]) -> retval
    .   @brief Reads an Extremal Region Filter for the 1st stage classifier of N&M algorithm
    .       from the provided path e.g. /path/to/cpp/trained_classifierNM1.xml
    .   
    .   @overload
    """
    pass

def createERFilterNM2(cb, minProbability=None): # real signature unknown; restored from __doc__
    """
    createERFilterNM2(cb[, minProbability]) -> retval
    .   @brief Create an Extremal Region Filter for the 2nd stage classifier of N&M algorithm @cite Neumann12.
    .   
    .   @param  cb :   Callback with the classifier. Default classifier can be implicitly load with function
    .   loadClassifierNM2, e.g. from file in samples/cpp/trained_classifierNM2.xml
    .   @param  minProbability :   The minimum probability P(er|character) allowed for retreived ER's
    .   
    .   In the second stage, the ERs that passed the first stage are classified into character and
    .   non-character classes using more informative but also more computationally expensive features. The
    .   classifier uses all the features calculated in the first stage and the following additional
    .   features: hole area ratio, convex hull ratio, and number of outer inflexion points.
    
    
    
    createERFilterNM2(filename[, minProbability]) -> retval
    .   @brief Reads an Extremal Region Filter for the 2nd stage classifier of N&M algorithm
    .       from the provided path e.g. /path/to/cpp/trained_classifierNM2.xml
    .   
    .   @overload
    """
    pass

def createOCRHMMTransitionsTable(vocabulary, lexicon): # real signature unknown; restored from __doc__
    """
    createOCRHMMTransitionsTable(vocabulary, lexicon) -> retval
    .   @brief Utility function to create a tailored language model transitions table from a given list of words (lexicon).
    .    *
    .    * @param vocabulary The language vocabulary (chars when ASCII English text).
    .    *
    .    * @param lexicon The list of words that are expected to be found in a particular image.
    .    *
    .    * @param transition_probabilities_table Output table with transition probabilities between character pairs. cols == rows == vocabulary.size().
    .    *
    .    * The function calculate frequency statistics of character pairs from the given lexicon and fills the output transition_probabilities_table with them. The transition_probabilities_table can be used as input in the OCRHMMDecoder::create() and OCRBeamSearchDecoder::create() methods.
    .    * @note
    .    *    -   (C++) An alternative would be to load the default generic language transition table provided in the text module samples folder (created from ispell 42869 english words list) :
    .    *            <https://github.com/opencv/opencv_contrib/blob/master/modules/text/samples/OCRHMM_transitions_table.xml>
    .   *
    """
    pass

def detectRegions(image, er_filter1, er_filter2): # real signature unknown; restored from __doc__
    """
    detectRegions(image, er_filter1, er_filter2) -> regions
    .   @brief Converts MSER contours (vector\<Point\>) to ERStat regions.
    .   
    .   @param image Source image CV_8UC1 from which the MSERs where extracted.
    .   
    .   @param contours Input vector with all the contours (vector\<Point\>).
    .   
    .   @param regions Output where the ERStat regions are stored.
    .   
    .   It takes as input the contours provided by the OpenCV MSER feature detector and returns as output
    .   two vectors of ERStats. This is because MSER() output contains both MSER+ and MSER- regions in a
    .   single vector\<Point\>, the function separates them in two different vectors (this is as if the
    .   ERStats where extracted from two different channels).
    .   
    .   An example of MSERsToERStats in use can be found in the text detection webcam_demo:
    .   <https://github.com/opencv/opencv_contrib/blob/master/modules/text/samples/webcam_demo.cpp>
    
    
    
    detectRegions(image, er_filter1, er_filter2[, method[, filename[, minProbability]]]) -> groups_rects
    .   @brief Extracts text regions from image.
    .   
    .   @param image Source image where text blocks needs to be extracted from.  Should be CV_8UC3 (color).
    .   @param er_filter1 Extremal Region Filter for the 1st stage classifier of N&M algorithm @cite Neumann12
    .   @param er_filter2 Extremal Region Filter for the 2nd stage classifier of N&M algorithm @cite Neumann12
    .   @param groups_rects Output list of rectangle blocks with text
    .   @param method Grouping method (see text::erGrouping_Modes). Can be one of ERGROUPING_ORIENTATION_HORIZ, ERGROUPING_ORIENTATION_ANY.
    .   @param filename The XML or YAML file with the classifier model (e.g. samples/trained_classifier_erGrouping.xml). Only to use when grouping method is ERGROUPING_ORIENTATION_ANY.
    .   @param minProbability The minimum probability for accepting a group. Only to use when grouping method is ERGROUPING_ORIENTATION_ANY.
    """
    pass

def erGrouping(image, channel, regions, method=None, filename=None, minProbablity=None): # real signature unknown; restored from __doc__
    """
    erGrouping(image, channel, regions[, method[, filename[, minProbablity]]]) -> groups_rects
    .   @brief Find groups of Extremal Regions that are organized as text blocks.
    .   
    .   @param img Original RGB or Greyscale image from wich the regions were extracted.
    .   
    .   @param channels Vector of single channel images CV_8UC1 from wich the regions were extracted.
    .   
    .   @param regions Vector of ER's retrieved from the ERFilter algorithm from each channel.
    .   
    .   @param groups The output of the algorithm is stored in this parameter as set of lists of indexes to
    .   provided regions.
    .   
    .   @param groups_rects The output of the algorithm are stored in this parameter as list of rectangles.
    .   
    .   @param method Grouping method (see text::erGrouping_Modes). Can be one of ERGROUPING_ORIENTATION_HORIZ,
    .   ERGROUPING_ORIENTATION_ANY.
    .   
    .   @param filename The XML or YAML file with the classifier model (e.g.
    .   samples/trained_classifier_erGrouping.xml). Only to use when grouping method is
    .   ERGROUPING_ORIENTATION_ANY.
    .   
    .   @param minProbablity The minimum probability for accepting a group. Only to use when grouping
    .   method is ERGROUPING_ORIENTATION_ANY.
    """
    pass

def loadClassifierNM1(filename): # real signature unknown; restored from __doc__
    """
    loadClassifierNM1(filename) -> retval
    .   @brief Allow to implicitly load the default classifier when creating an ERFilter object.
    .   
    .   @param filename The XML or YAML file with the classifier model (e.g. trained_classifierNM1.xml)
    .   
    .   returns a pointer to ERFilter::Callback.
    """
    pass

def loadClassifierNM2(filename): # real signature unknown; restored from __doc__
    """
    loadClassifierNM2(filename) -> retval
    .   @brief Allow to implicitly load the default classifier when creating an ERFilter object.
    .   
    .   @param filename The XML or YAML file with the classifier model (e.g. trained_classifierNM2.xml)
    .   
    .   returns a pointer to ERFilter::Callback.
    """
    pass

def loadOCRBeamSearchClassifierCNN(filename): # real signature unknown; restored from __doc__
    """
    loadOCRBeamSearchClassifierCNN(filename) -> retval
    .   @brief Allow to implicitly load the default character classifier when creating an OCRBeamSearchDecoder object.
    .   
    .   @param filename The XML or YAML file with the classifier model (e.g. OCRBeamSearch_CNN_model_data.xml.gz)
    .   
    .   The CNN default classifier is based in the scene text recognition method proposed by Adam Coates &
    .   Andrew NG in [Coates11a]. The character classifier consists in a Single Layer Convolutional Neural Network and
    .   a linear classifier. It is applied to the input image in a sliding window fashion, providing a set of recognitions
    .   at each window location.
    """
    pass

def loadOCRHMMClassifier(filename, classifier): # real signature unknown; restored from __doc__
    """
    loadOCRHMMClassifier(filename, classifier) -> retval
    .   @brief Allow to implicitly load the default character classifier when creating an OCRHMMDecoder object.
    .   
    .    @param filename The XML or YAML file with the classifier model (e.g. OCRBeamSearch_CNN_model_data.xml.gz)
    .   
    .    @param classifier Can be one of classifier_type enum values.
    """
    pass

def loadOCRHMMClassifierCNN(filename): # real signature unknown; restored from __doc__
    """
    loadOCRHMMClassifierCNN(filename) -> retval
    .   @brief Allow to implicitly load the default character classifier when creating an OCRHMMDecoder object.
    .   
    .   @param filename The XML or YAML file with the classifier model (e.g. OCRBeamSearch_CNN_model_data.xml.gz)
    .   
    .   The CNN default classifier is based in the scene text recognition method proposed by Adam Coates &
    .   Andrew NG in [Coates11a]. The character classifier consists in a Single Layer Convolutional Neural Network and
    .   a linear classifier. It is applied to the input image in a sliding window fashion, providing a set of recognitions
    .   at each window location.
    .   
    .   @deprecated use loadOCRHMMClassifier instead
    """
    pass

def loadOCRHMMClassifierNM(filename): # real signature unknown; restored from __doc__
    """
    loadOCRHMMClassifierNM(filename) -> retval
    .   @brief Allow to implicitly load the default character classifier when creating an OCRHMMDecoder object.
    .   
    .   @param filename The XML or YAML file with the classifier model (e.g. OCRHMM_knn_model_data.xml)
    .   
    .   The KNN default classifier is based in the scene text recognition method proposed by Luk&#225;s Neumann &
    .   Jiri Matas in [Neumann11b]. Basically, the region (contour) in the input image is normalized to a
    .   fixed size, while retaining the centroid and aspect ratio, in order to extract a feature vector
    .   based on gradient orientations along the chain-code of its perimeter. Then, the region is classified
    .   using a KNN model trained with synthetic data of rendered characters with different standard font
    .   types.
    .   
    .   @deprecated loadOCRHMMClassifier instead
    """
    pass

def OCRBeamSearchDecoder_create(classifier, vocabulary, transition_probabilities_table, emission_probabilities_table, mode=None, beam_size=None): # real signature unknown; restored from __doc__
    """
    OCRBeamSearchDecoder_create(classifier, vocabulary, transition_probabilities_table, emission_probabilities_table[, mode[, beam_size]]) -> retval
    .   @brief Creates an instance of the OCRBeamSearchDecoder class. Initializes HMMDecoder.
    .   
    .       @param classifier The character classifier with built in feature extractor.
    .   
    .       @param vocabulary The language vocabulary (chars when ASCII English text). vocabulary.size()
    .       must be equal to the number of classes of the classifier.
    .   
    .       @param transition_probabilities_table Table with transition probabilities between character
    .       pairs. cols == rows == vocabulary.size().
    .   
    .       @param emission_probabilities_table Table with observation emission probabilities. cols ==
    .       rows == vocabulary.size().
    .   
    .       @param mode HMM Decoding algorithm. Only OCR_DECODER_VITERBI is available for the moment
    .       (<http://en.wikipedia.org/wiki/Viterbi_algorithm>).
    .   
    .       @param beam_size Size of the beam in Beam Search algorithm.
    
    
    
    OCRBeamSearchDecoder_create(filename, vocabulary, transition_probabilities_table, emission_probabilities_table[, mode[, beam_size]]) -> retval
    .   @brief Creates an instance of the OCRBeamSearchDecoder class. Initializes HMMDecoder from the specified path.
    .   
    .       @overload
    """
    pass

def OCRHMMDecoder_create(classifier, vocabulary, transition_probabilities_table, emission_probabilities_table, mode=None): # real signature unknown; restored from __doc__
    """
    OCRHMMDecoder_create(classifier, vocabulary, transition_probabilities_table, emission_probabilities_table[, mode]) -> retval
    .   @brief Creates an instance of the OCRHMMDecoder class. Initializes HMMDecoder.
    .   
    .       @param classifier The character classifier with built in feature extractor.
    .   
    .       @param vocabulary The language vocabulary (chars when ascii english text). vocabulary.size()
    .       must be equal to the number of classes of the classifier.
    .   
    .       @param transition_probabilities_table Table with transition probabilities between character
    .       pairs. cols == rows == vocabulary.size().
    .   
    .       @param emission_probabilities_table Table with observation emission probabilities. cols ==
    .       rows == vocabulary.size().
    .   
    .       @param mode HMM Decoding algorithm. Only OCR_DECODER_VITERBI is available for the moment
    .       (<http://en.wikipedia.org/wiki/Viterbi_algorithm>).
    
    
    
    OCRHMMDecoder_create(filename, vocabulary, transition_probabilities_table, emission_probabilities_table[, mode[, classifier]]) -> retval
    .   @brief Creates an instance of the OCRHMMDecoder class. Loads and initializes HMMDecoder from the specified path
    .   
    .        @overload
    """
    pass

def OCRTesseract_create(datapath=None, language=None, char_whitelist=None, oem=None, psmode=None): # real signature unknown; restored from __doc__
    """
    OCRTesseract_create([, datapath[, language[, char_whitelist[, oem[, psmode]]]]]) -> retval
    .   @brief Creates an instance of the OCRTesseract class. Initializes Tesseract.
    .   
    .       @param datapath the name of the parent directory of tessdata ended with "/", or NULL to use the
    .       system's default directory.
    .       @param language an ISO 639-3 code or NULL will default to "eng".
    .       @param char_whitelist specifies the list of characters used for recognition. NULL defaults to
    .       "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".
    .       @param oem tesseract-ocr offers different OCR Engine Modes (OEM), by default
    .       tesseract::OEM_DEFAULT is used. See the tesseract-ocr API documentation for other possible
    .       values.
    .       @param psmode tesseract-ocr offers different Page Segmentation Modes (PSM) tesseract::PSM_AUTO
    .       (fully automatic layout analysis) is used. See the tesseract-ocr API documentation for other
    .       possible values.
    """
    pass

def TextDetectorCNN_create(modelArchFilename, modelWeightsFilename): # real signature unknown; restored from __doc__
    """
    TextDetectorCNN_create(modelArchFilename, modelWeightsFilename) -> retval
    .   @overload
    """
    pass

# no classes
