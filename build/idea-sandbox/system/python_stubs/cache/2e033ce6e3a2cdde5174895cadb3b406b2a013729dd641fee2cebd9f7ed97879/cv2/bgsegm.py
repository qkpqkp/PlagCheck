# encoding: utf-8
# module cv2.bgsegm
# from C:\Users\Doly\Anaconda3\lib\site-packages\cv2\cv2.cp37-win_amd64.pyd
# by generator 1.147
# no doc
# no imports

# Variables with simple values

LSBP_CAMERA_MOTION_COMPENSATION_LK = 1
LSBP_CAMERA_MOTION_COMPENSATION_NONE = 0

__loader__ = None

__spec__ = None

# functions

def createBackgroundSubtractorCNT(minPixelStability=None, useHistory=None, maxPixelStability=None, isParallel=None): # real signature unknown; restored from __doc__
    """
    createBackgroundSubtractorCNT([, minPixelStability[, useHistory[, maxPixelStability[, isParallel]]]]) -> retval
    .   @brief Creates a CNT Background Subtractor
    .   
    .   @param minPixelStability number of frames with same pixel color to consider stable
    .   @param useHistory determines if we're giving a pixel credit for being stable for a long time
    .   @param maxPixelStability maximum allowed credit for a pixel in history
    .   @param isParallel determines if we're parallelizing the algorithm
    """
    pass

def createBackgroundSubtractorGMG(initializationFrames=None, decisionThreshold=None): # real signature unknown; restored from __doc__
    """
    createBackgroundSubtractorGMG([, initializationFrames[, decisionThreshold]]) -> retval
    .   @brief Creates a GMG Background Subtractor
    .   
    .   @param initializationFrames number of frames used to initialize the background models.
    .   @param decisionThreshold Threshold value, above which it is marked foreground, else background.
    """
    pass

def createBackgroundSubtractorGSOC(mc=None, nSamples=None, replaceRate=None, propagationRate=None, hitsThreshold=None, alpha=None, beta=None, blinkingSupressionDecay=None, blinkingSupressionMultiplier=None, noiseRemovalThresholdFacBG=None, noiseRemovalThresholdFacFG=None): # real signature unknown; restored from __doc__
    """
    createBackgroundSubtractorGSOC([, mc[, nSamples[, replaceRate[, propagationRate[, hitsThreshold[, alpha[, beta[, blinkingSupressionDecay[, blinkingSupressionMultiplier[, noiseRemovalThresholdFacBG[, noiseRemovalThresholdFacFG]]]]]]]]]]]) -> retval
    .   @brief Creates an instance of BackgroundSubtractorGSOC algorithm.
    .   
    .   Implementation of the different yet better algorithm which is called GSOC, as it was implemented during GSOC and was not originated from any paper.
    .   
    .   @param mc Whether to use camera motion compensation.
    .   @param nSamples Number of samples to maintain at each point of the frame.
    .   @param replaceRate Probability of replacing the old sample - how fast the model will update itself.
    .   @param propagationRate Probability of propagating to neighbors.
    .   @param hitsThreshold How many positives the sample must get before it will be considered as a possible replacement.
    .   @param alpha Scale coefficient for threshold.
    .   @param beta Bias coefficient for threshold.
    .   @param blinkingSupressionDecay Blinking supression decay factor.
    .   @param blinkingSupressionMultiplier Blinking supression multiplier.
    .   @param noiseRemovalThresholdFacBG Strength of the noise removal for background points.
    .   @param noiseRemovalThresholdFacFG Strength of the noise removal for foreground points.
    """
    pass

def createBackgroundSubtractorLSBP(mc=None, nSamples=None, LSBPRadius=None, Tlower=None, Tupper=None, Tinc=None, Tdec=None, Rscale=None, Rincdec=None, noiseRemovalThresholdFacBG=None, noiseRemovalThresholdFacFG=None, LSBPthreshold=None, minCount=None): # real signature unknown; restored from __doc__
    """
    createBackgroundSubtractorLSBP([, mc[, nSamples[, LSBPRadius[, Tlower[, Tupper[, Tinc[, Tdec[, Rscale[, Rincdec[, noiseRemovalThresholdFacBG[, noiseRemovalThresholdFacFG[, LSBPthreshold[, minCount]]]]]]]]]]]]]) -> retval
    .   @brief Creates an instance of BackgroundSubtractorLSBP algorithm.
    .   
    .   Background Subtraction using Local SVD Binary Pattern. More details about the algorithm can be found at @cite LGuo2016
    .   
    .   @param mc Whether to use camera motion compensation.
    .   @param nSamples Number of samples to maintain at each point of the frame.
    .   @param LSBPRadius LSBP descriptor radius.
    .   @param Tlower Lower bound for T-values. See @cite LGuo2016 for details.
    .   @param Tupper Upper bound for T-values. See @cite LGuo2016 for details.
    .   @param Tinc Increase step for T-values. See @cite LGuo2016 for details.
    .   @param Tdec Decrease step for T-values. See @cite LGuo2016 for details.
    .   @param Rscale Scale coefficient for threshold values.
    .   @param Rincdec Increase/Decrease step for threshold values.
    .   @param noiseRemovalThresholdFacBG Strength of the noise removal for background points.
    .   @param noiseRemovalThresholdFacFG Strength of the noise removal for foreground points.
    .   @param LSBPthreshold Threshold for LSBP binary string.
    .   @param minCount Minimal number of matches for sample to be considered as foreground.
    """
    pass

def createBackgroundSubtractorMOG(history=None, nmixtures=None, backgroundRatio=None, noiseSigma=None): # real signature unknown; restored from __doc__
    """
    createBackgroundSubtractorMOG([, history[, nmixtures[, backgroundRatio[, noiseSigma]]]]) -> retval
    .   @brief Creates mixture-of-gaussian background subtractor
    .   
    .   @param history Length of the history.
    .   @param nmixtures Number of Gaussian mixtures.
    .   @param backgroundRatio Background ratio.
    .   @param noiseSigma Noise strength (standard deviation of the brightness or each color channel). 0
    .   means some automatic value.
    """
    pass

def createSyntheticSequenceGenerator(background, p_object, amplitude=None, wavelength=None, wavespeed=None, objspeed=None): # real signature unknown; restored from __doc__
    """
    createSyntheticSequenceGenerator(background, object[, amplitude[, wavelength[, wavespeed[, objspeed]]]]) -> retval
    .   @brief Creates an instance of SyntheticSequenceGenerator.
    .   
    .   @param background Background image for object.
    .   @param object Object image which will move slowly over the background.
    .   @param amplitude Amplitude of wave distortion applied to background.
    .   @param wavelength Length of waves in distortion applied to background.
    .   @param wavespeed How fast waves will move.
    .   @param objspeed How fast object will fly over background.
    """
    pass

# no classes
