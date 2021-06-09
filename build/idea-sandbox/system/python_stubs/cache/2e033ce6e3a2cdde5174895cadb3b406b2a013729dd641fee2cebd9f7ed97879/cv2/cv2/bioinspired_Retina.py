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


class bioinspired_Retina(__cv2.Algorithm):
    # no doc
    def activateContoursProcessing(self, activate): # real signature unknown; restored from __doc__
        """
        activateContoursProcessing(activate) -> None
        .   @brief Activate/desactivate the Parvocellular pathway processing (contours information extraction), by
        .       default, it is activated
        .       @param activate true if Parvocellular (contours information extraction) output should be
        .       activated, false if not... if activated, the Parvocellular output can be retrieved using the
        .       Retina::getParvo methods
        """
        pass

    def activateMovingContoursProcessing(self, activate): # real signature unknown; restored from __doc__
        """
        activateMovingContoursProcessing(activate) -> None
        .   @brief Activate/desactivate the Magnocellular pathway processing (motion information extraction), by
        .       default, it is activated
        .       @param activate true if Magnocellular output should be activated, false if not... if activated,
        .       the Magnocellular output can be retrieved using the **getMagno** methods
        """
        pass

    def applyFastToneMapping(self, inputImage, outputToneMappedImage=None): # real signature unknown; restored from __doc__
        """
        applyFastToneMapping(inputImage[, outputToneMappedImage]) -> outputToneMappedImage
        .   @brief Method which processes an image in the aim to correct its luminance correct
        .       backlight problems, enhance details in shadows.
        .   
        .       This method is designed to perform High Dynamic Range image tone mapping (compress \>8bit/pixel
        .       images to 8bit/pixel). This is a simplified version of the Retina Parvocellular model
        .       (simplified version of the run/getParvo methods call) since it does not include the
        .       spatio-temporal filter modelling the Outer Plexiform Layer of the retina that performs spectral
        .       whitening and many other stuff. However, it works great for tone mapping and in a faster way.
        .   
        .       Check the demos and experiments section to see examples and the way to perform tone mapping
        .       using the original retina model and the method.
        .   
        .       @param inputImage the input image to process (should be coded in float format : CV_32F,
        .       CV_32FC1, CV_32F_C3, CV_32F_C4, the 4th channel won't be considered).
        .       @param outputToneMappedImage the output 8bit/channel tone mapped image (CV_8U or CV_8UC3 format).
        """
        pass

    def clearBuffers(self): # real signature unknown; restored from __doc__
        """
        clearBuffers() -> None
        .   @brief Clears all retina buffers
        .   
        .       (equivalent to opening the eyes after a long period of eye close ;o) whatchout the temporal
        .       transition occuring just after this method call.
        """
        pass

    def create(self, inputSize): # real signature unknown; restored from __doc__
        """
        create(inputSize) -> retval
        .   @overload
        
        
        
        create(inputSize, colorMode[, colorSamplingMethod[, useRetinaLogSampling[, reductionFactor[, samplingStrenght]]]]) -> retval
        .   @brief Constructors from standardized interfaces : retreive a smart pointer to a Retina instance
        .   
        .       @param inputSize the input frame size
        .       @param colorMode the chosen processing mode : with or without color processing
        .       @param colorSamplingMethod specifies which kind of color sampling will be used :
        .       -   cv::bioinspired::RETINA_COLOR_RANDOM: each pixel position is either R, G or B in a random choice
        .       -   cv::bioinspired::RETINA_COLOR_DIAGONAL: color sampling is RGBRGBRGB..., line 2 BRGBRGBRG..., line 3, GBRGBRGBR...
        .       -   cv::bioinspired::RETINA_COLOR_BAYER: standard bayer sampling
        .       @param useRetinaLogSampling activate retina log sampling, if true, the 2 following parameters can
        .       be used
        .       @param reductionFactor only usefull if param useRetinaLogSampling=true, specifies the reduction
        .       factor of the output frame (as the center (fovea) is high resolution and corners can be
        .       underscaled, then a reduction of the output is allowed without precision leak
        .       @param samplingStrenght only usefull if param useRetinaLogSampling=true, specifies the strenght of
        .       the log scale that is applied
        """
        pass

    def getInputSize(self): # real signature unknown; restored from __doc__
        """
        getInputSize() -> retval
        .   @brief Retreive retina input buffer size
        .       @return the retina input buffer size
        """
        pass

    def getMagno(self, retinaOutput_magno=None): # real signature unknown; restored from __doc__
        """
        getMagno([, retinaOutput_magno]) -> retinaOutput_magno
        .   @brief Accessor of the motion channel of the retina (models peripheral vision).
        .   
        .       Warning, getMagnoRAW methods return buffers that are not rescaled within range [0;255] while
        .       the non RAW method allows a normalized matrix to be retrieved.
        .       @param retinaOutput_magno the output buffer (reallocated if necessary), format can be :
        .       -   a Mat, this output is rescaled for standard 8bits image processing use in OpenCV
        .       -   RAW methods actually return a 1D matrix (encoding is M1, M2,... Mn), this output is the
        .       original retina filter model output, without any quantification or rescaling.
        .       @see getMagnoRAW
        """
        pass

    def getMagnoRAW(self, retinaOutput_magno=None): # real signature unknown; restored from __doc__
        """
        getMagnoRAW([, retinaOutput_magno]) -> retinaOutput_magno
        .   @brief Accessor of the motion channel of the retina (models peripheral vision).
        .       @see getMagno
        
        
        
        getMagnoRAW() -> retval
        .   @overload
        """
        pass

    def getOutputSize(self): # real signature unknown; restored from __doc__
        """
        getOutputSize() -> retval
        .   @brief Retreive retina output buffer size that can be different from the input if a spatial log
        .       transformation is applied
        .       @return the retina output buffer size
        """
        pass

    def getParvo(self, retinaOutput_parvo=None): # real signature unknown; restored from __doc__
        """
        getParvo([, retinaOutput_parvo]) -> retinaOutput_parvo
        .   @brief Accessor of the details channel of the retina (models foveal vision).
        .   
        .       Warning, getParvoRAW methods return buffers that are not rescaled within range [0;255] while
        .       the non RAW method allows a normalized matrix to be retrieved.
        .   
        .       @param retinaOutput_parvo the output buffer (reallocated if necessary), format can be :
        .       -   a Mat, this output is rescaled for standard 8bits image processing use in OpenCV
        .       -   RAW methods actually return a 1D matrix (encoding is R1, R2, ... Rn, G1, G2, ..., Gn, B1,
        .       B2, ...Bn), this output is the original retina filter model output, without any
        .       quantification or rescaling.
        .       @see getParvoRAW
        """
        pass

    def getParvoRAW(self, retinaOutput_parvo=None): # real signature unknown; restored from __doc__
        """
        getParvoRAW([, retinaOutput_parvo]) -> retinaOutput_parvo
        .   @brief Accessor of the details channel of the retina (models foveal vision).
        .       @see getParvo
        
        
        
        getParvoRAW() -> retval
        .   @overload
        """
        pass

    def printSetup(self): # real signature unknown; restored from __doc__
        """
        printSetup() -> retval
        .   @brief Outputs a string showing the used parameters setup
        .       @return a string which contains formated parameters information
        """
        pass

    def run(self, inputImage): # real signature unknown; restored from __doc__
        """
        run(inputImage) -> None
        .   @brief Method which allows retina to be applied on an input image,
        .   
        .       after run, encapsulated retina module is ready to deliver its outputs using dedicated
        .       acccessors, see getParvo and getMagno methods
        .       @param inputImage the input Mat image to be processed, can be gray level or BGR coded in any
        .       format (from 8bit to 16bits)
        """
        pass

    def setColorSaturation(self, saturateColors=None, colorSaturationValue=None): # real signature unknown; restored from __doc__
        """
        setColorSaturation([, saturateColors[, colorSaturationValue]]) -> None
        .   @brief Activate color saturation as the final step of the color demultiplexing process -\> this
        .       saturation is a sigmoide function applied to each channel of the demultiplexed image.
        .       @param saturateColors boolean that activates color saturation (if true) or desactivate (if false)
        .       @param colorSaturationValue the saturation factor : a simple factor applied on the chrominance
        .       buffers
        """
        pass

    def setup(self, retinaParameterFile=None, applyDefaultSetupOnFailure=None): # real signature unknown; restored from __doc__
        """
        setup([, retinaParameterFile[, applyDefaultSetupOnFailure]]) -> None
        .   @brief Try to open an XML retina parameters file to adjust current retina instance setup
        .   
        .       - if the xml file does not exist, then default setup is applied
        .       - warning, Exceptions are thrown if read XML file is not valid
        .       @param retinaParameterFile the parameters filename
        .       @param applyDefaultSetupOnFailure set to true if an error must be thrown on error
        .   
        .       You can retrieve the current parameters structure using the method Retina::getParameters and update
        .       it before running method Retina::setup.
        """
        pass

    def setupIPLMagnoChannel(self, normaliseOutput=None, parasolCells_beta=None, parasolCells_tau=None, parasolCells_k=None, amacrinCellsTemporalCutFrequency=None, V0CompressionParameter=None, localAdaptintegration_tau=None, localAdaptintegration_k=None): # real signature unknown; restored from __doc__
        """
        setupIPLMagnoChannel([, normaliseOutput[, parasolCells_beta[, parasolCells_tau[, parasolCells_k[, amacrinCellsTemporalCutFrequency[, V0CompressionParameter[, localAdaptintegration_tau[, localAdaptintegration_k]]]]]]]]) -> None
        .   @brief Set parameters values for the Inner Plexiform Layer (IPL) magnocellular channel
        .   
        .       this channel processes signals output from OPL processing stage in peripheral vision, it allows
        .       motion information enhancement. It is decorrelated from the details channel. See reference
        .       papers for more details.
        .   
        .       @param normaliseOutput specifies if (true) output is rescaled between 0 and 255 of not (false)
        .       @param parasolCells_beta the low pass filter gain used for local contrast adaptation at the
        .       IPL level of the retina (for ganglion cells local adaptation), typical value is 0
        .       @param parasolCells_tau the low pass filter time constant used for local contrast adaptation
        .       at the IPL level of the retina (for ganglion cells local adaptation), unit is frame, typical
        .       value is 0 (immediate response)
        .       @param parasolCells_k the low pass filter spatial constant used for local contrast adaptation
        .       at the IPL level of the retina (for ganglion cells local adaptation), unit is pixels, typical
        .       value is 5
        .       @param amacrinCellsTemporalCutFrequency the time constant of the first order high pass fiter of
        .       the magnocellular way (motion information channel), unit is frames, typical value is 1.2
        .       @param V0CompressionParameter the compression strengh of the ganglion cells local adaptation
        .       output, set a value between 0.6 and 1 for best results, a high value increases more the low
        .       value sensitivity... and the output saturates faster, recommended value: 0.95
        .       @param localAdaptintegration_tau specifies the temporal constant of the low pas filter
        .       involved in the computation of the local "motion mean" for the local adaptation computation
        .       @param localAdaptintegration_k specifies the spatial constant of the low pas filter involved
        .       in the computation of the local "motion mean" for the local adaptation computation
        """
        pass

    def setupOPLandIPLParvoChannel(self, colorMode=None, normaliseOutput=None, photoreceptorsLocalAdaptationSensitivity=None, photoreceptorsTemporalConstant=None, photoreceptorsSpatialConstant=None, horizontalCellsGain=None, HcellsTemporalConstant=None, HcellsSpatialConstant=None, ganglionCellsSensitivity=None): # real signature unknown; restored from __doc__
        """
        setupOPLandIPLParvoChannel([, colorMode[, normaliseOutput[, photoreceptorsLocalAdaptationSensitivity[, photoreceptorsTemporalConstant[, photoreceptorsSpatialConstant[, horizontalCellsGain[, HcellsTemporalConstant[, HcellsSpatialConstant[, ganglionCellsSensitivity]]]]]]]]]) -> None
        .   @brief Setup the OPL and IPL parvo channels (see biologocal model)
        .   
        .       OPL is referred as Outer Plexiform Layer of the retina, it allows the spatio-temporal filtering
        .       which withens the spectrum and reduces spatio-temporal noise while attenuating global luminance
        .       (low frequency energy) IPL parvo is the OPL next processing stage, it refers to a part of the
        .       Inner Plexiform layer of the retina, it allows high contours sensitivity in foveal vision. See
        .       reference papers for more informations.
        .       for more informations, please have a look at the paper Benoit A., Caplier A., Durette B., Herault, J., "USING HUMAN VISUAL SYSTEM MODELING FOR BIO-INSPIRED LOW LEVEL IMAGE PROCESSING", Elsevier, Computer Vision and Image Understanding 114 (2010), pp. 758-773, DOI: http://dx.doi.org/10.1016/j.cviu.2010.01.011
        .       @param colorMode specifies if (true) color is processed of not (false) to then processing gray
        .       level image
        .       @param normaliseOutput specifies if (true) output is rescaled between 0 and 255 of not (false)
        .       @param photoreceptorsLocalAdaptationSensitivity the photoreceptors sensitivity renage is 0-1
        .       (more log compression effect when value increases)
        .       @param photoreceptorsTemporalConstant the time constant of the first order low pass filter of
        .       the photoreceptors, use it to cut high temporal frequencies (noise or fast motion), unit is
        .       frames, typical value is 1 frame
        .       @param photoreceptorsSpatialConstant the spatial constant of the first order low pass filter of
        .       the photoreceptors, use it to cut high spatial frequencies (noise or thick contours), unit is
        .       pixels, typical value is 1 pixel
        .       @param horizontalCellsGain gain of the horizontal cells network, if 0, then the mean value of
        .       the output is zero, if the parameter is near 1, then, the luminance is not filtered and is
        .       still reachable at the output, typicall value is 0
        .       @param HcellsTemporalConstant the time constant of the first order low pass filter of the
        .       horizontal cells, use it to cut low temporal frequencies (local luminance variations), unit is
        .       frames, typical value is 1 frame, as the photoreceptors
        .       @param HcellsSpatialConstant the spatial constant of the first order low pass filter of the
        .       horizontal cells, use it to cut low spatial frequencies (local luminance), unit is pixels,
        .       typical value is 5 pixel, this value is also used for local contrast computing when computing
        .       the local contrast adaptation at the ganglion cells level (Inner Plexiform Layer parvocellular
        .       channel model)
        .       @param ganglionCellsSensitivity the compression strengh of the ganglion cells local adaptation
        .       output, set a value between 0.6 and 1 for best results, a high value increases more the low
        .       value sensitivity... and the output saturates faster, recommended value: 0.7
        """
        pass

    def write(self, fs): # real signature unknown; restored from __doc__
        """
        write(fs) -> None
        .   @brief Write xml/yml formated parameters information
        .       @param fs the filename of the xml file that will be open and writen with formatted parameters
        .       information
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


