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


class ml_EM(__cv2.ml_StatModel):
    # no doc
    def create(self): # real signature unknown; restored from __doc__
        """
        create() -> retval
        .   Creates empty %EM model.
        .       The model should be trained then using StatModel::train(traindata, flags) method. Alternatively, you
        .       can use one of the EM::train\* methods or load it from file using Algorithm::load\<EM\>(filename).
        """
        pass

    def getClustersNumber(self): # real signature unknown; restored from __doc__
        """
        getClustersNumber() -> retval
        .   @see setClustersNumber
        """
        pass

    def getCovarianceMatrixType(self): # real signature unknown; restored from __doc__
        """
        getCovarianceMatrixType() -> retval
        .   @see setCovarianceMatrixType
        """
        pass

    def getCovs(self, covs=None): # real signature unknown; restored from __doc__
        """
        getCovs([, covs]) -> covs
        .   @brief Returns covariation matrices
        .   
        .       Returns vector of covariation matrices. Number of matrices is the number of gaussian mixtures,
        .       each matrix is a square floating-point matrix NxN, where N is the space dimensionality.
        """
        pass

    def getMeans(self): # real signature unknown; restored from __doc__
        """
        getMeans() -> retval
        .   @brief Returns the cluster centers (means of the Gaussian mixture)
        .   
        .       Returns matrix with the number of rows equal to the number of mixtures and number of columns
        .       equal to the space dimensionality.
        """
        pass

    def getTermCriteria(self): # real signature unknown; restored from __doc__
        """
        getTermCriteria() -> retval
        .   @see setTermCriteria
        """
        pass

    def getWeights(self): # real signature unknown; restored from __doc__
        """
        getWeights() -> retval
        .   @brief Returns weights of the mixtures
        .   
        .       Returns vector with the number of elements equal to the number of mixtures.
        """
        pass

    def load(self, filepath, nodeName=None): # real signature unknown; restored from __doc__
        """
        load(filepath[, nodeName]) -> retval
        .   @brief Loads and creates a serialized EM from a file
        .        *
        .        * Use EM::save to serialize and store an EM to disk.
        .        * Load the EM from this file again, by calling this function with the path to the file.
        .        * Optionally specify the node for the file containing the classifier
        .        *
        .        * @param filepath path to serialized EM
        .        * @param nodeName name of node containing the classifier
        """
        pass

    def predict(self, samples, results=None, flags=None): # real signature unknown; restored from __doc__
        """
        predict(samples[, results[, flags]]) -> retval, results
        .   @brief Returns posterior probabilities for the provided samples
        .   
        .       @param samples The input samples, floating-point matrix
        .       @param results The optional output \f$ nSamples \times nClusters\f$ matrix of results. It contains
        .       posterior probabilities for each sample from the input
        .       @param flags This parameter will be ignored
        """
        pass

    def predict2(self, sample, probs=None): # real signature unknown; restored from __doc__
        """
        predict2(sample[, probs]) -> retval, probs
        .   @brief Returns a likelihood logarithm value and an index of the most probable mixture component
        .       for the given sample.
        .   
        .       @param sample A sample for classification. It should be a one-channel matrix of
        .           \f$1 \times dims\f$ or \f$dims \times 1\f$ size.
        .       @param probs Optional output matrix that contains posterior probabilities of each component
        .           given the sample. It has \f$1 \times nclusters\f$ size and CV_64FC1 type.
        .   
        .       The method returns a two-element double vector. Zero element is a likelihood logarithm value for
        .       the sample. First element is an index of the most probable mixture component for the given
        .       sample.
        """
        pass

    def setClustersNumber(self, val): # real signature unknown; restored from __doc__
        """
        setClustersNumber(val) -> None
        .   @copybrief getClustersNumber @see getClustersNumber
        """
        pass

    def setCovarianceMatrixType(self, val): # real signature unknown; restored from __doc__
        """
        setCovarianceMatrixType(val) -> None
        .   @copybrief getCovarianceMatrixType @see getCovarianceMatrixType
        """
        pass

    def setTermCriteria(self, val): # real signature unknown; restored from __doc__
        """
        setTermCriteria(val) -> None
        .   @copybrief getTermCriteria @see getTermCriteria
        """
        pass

    def trainE(self, samples, means0, covs0=None, weights0=None, logLikelihoods=None, labels=None, probs=None): # real signature unknown; restored from __doc__
        """
        trainE(samples, means0[, covs0[, weights0[, logLikelihoods[, labels[, probs]]]]]) -> retval, logLikelihoods, labels, probs
        .   @brief Estimate the Gaussian mixture parameters from a samples set.
        .   
        .       This variation starts with Expectation step. You need to provide initial means \f$a_k\f$ of
        .       mixture components. Optionally you can pass initial weights \f$\pi_k\f$ and covariance matrices
        .       \f$S_k\f$ of mixture components.
        .   
        .       @param samples Samples from which the Gaussian mixture model will be estimated. It should be a
        .           one-channel matrix, each row of which is a sample. If the matrix does not have CV_64F type
        .           it will be converted to the inner matrix of such type for the further computing.
        .       @param means0 Initial means \f$a_k\f$ of mixture components. It is a one-channel matrix of
        .           \f$nclusters \times dims\f$ size. If the matrix does not have CV_64F type it will be
        .           converted to the inner matrix of such type for the further computing.
        .       @param covs0 The vector of initial covariance matrices \f$S_k\f$ of mixture components. Each of
        .           covariance matrices is a one-channel matrix of \f$dims \times dims\f$ size. If the matrices
        .           do not have CV_64F type they will be converted to the inner matrices of such type for the
        .           further computing.
        .       @param weights0 Initial weights \f$\pi_k\f$ of mixture components. It should be a one-channel
        .           floating-point matrix with \f$1 \times nclusters\f$ or \f$nclusters \times 1\f$ size.
        .       @param logLikelihoods The optional output matrix that contains a likelihood logarithm value for
        .           each sample. It has \f$nsamples \times 1\f$ size and CV_64FC1 type.
        .       @param labels The optional output "class label" for each sample:
        .           \f$\texttt{labels}_i=\texttt{arg max}_k(p_{i,k}), i=1..N\f$ (indices of the most probable
        .           mixture component for each sample). It has \f$nsamples \times 1\f$ size and CV_32SC1 type.
        .       @param probs The optional output matrix that contains posterior probabilities of each Gaussian
        .           mixture component given the each sample. It has \f$nsamples \times nclusters\f$ size and
        .           CV_64FC1 type.
        """
        pass

    def trainEM(self, samples, logLikelihoods=None, labels=None, probs=None): # real signature unknown; restored from __doc__
        """
        trainEM(samples[, logLikelihoods[, labels[, probs]]]) -> retval, logLikelihoods, labels, probs
        .   @brief Estimate the Gaussian mixture parameters from a samples set.
        .   
        .       This variation starts with Expectation step. Initial values of the model parameters will be
        .       estimated by the k-means algorithm.
        .   
        .       Unlike many of the ML models, %EM is an unsupervised learning algorithm and it does not take
        .       responses (class labels or function values) as input. Instead, it computes the *Maximum
        .       Likelihood Estimate* of the Gaussian mixture parameters from an input sample set, stores all the
        .       parameters inside the structure: \f$p_{i,k}\f$ in probs, \f$a_k\f$ in means , \f$S_k\f$ in
        .       covs[k], \f$\pi_k\f$ in weights , and optionally computes the output "class label" for each
        .       sample: \f$\texttt{labels}_i=\texttt{arg max}_k(p_{i,k}), i=1..N\f$ (indices of the most
        .       probable mixture component for each sample).
        .   
        .       The trained model can be used further for prediction, just like any other classifier. The
        .       trained model is similar to the NormalBayesClassifier.
        .   
        .       @param samples Samples from which the Gaussian mixture model will be estimated. It should be a
        .           one-channel matrix, each row of which is a sample. If the matrix does not have CV_64F type
        .           it will be converted to the inner matrix of such type for the further computing.
        .       @param logLikelihoods The optional output matrix that contains a likelihood logarithm value for
        .           each sample. It has \f$nsamples \times 1\f$ size and CV_64FC1 type.
        .       @param labels The optional output "class label" for each sample:
        .           \f$\texttt{labels}_i=\texttt{arg max}_k(p_{i,k}), i=1..N\f$ (indices of the most probable
        .           mixture component for each sample). It has \f$nsamples \times 1\f$ size and CV_32SC1 type.
        .       @param probs The optional output matrix that contains posterior probabilities of each Gaussian
        .           mixture component given the each sample. It has \f$nsamples \times nclusters\f$ size and
        .           CV_64FC1 type.
        """
        pass

    def trainM(self, samples, probs0, logLikelihoods=None, labels=None, probs=None): # real signature unknown; restored from __doc__
        """
        trainM(samples, probs0[, logLikelihoods[, labels[, probs]]]) -> retval, logLikelihoods, labels, probs
        .   @brief Estimate the Gaussian mixture parameters from a samples set.
        .   
        .       This variation starts with Maximization step. You need to provide initial probabilities
        .       \f$p_{i,k}\f$ to use this option.
        .   
        .       @param samples Samples from which the Gaussian mixture model will be estimated. It should be a
        .           one-channel matrix, each row of which is a sample. If the matrix does not have CV_64F type
        .           it will be converted to the inner matrix of such type for the further computing.
        .       @param probs0 the probabilities
        .       @param logLikelihoods The optional output matrix that contains a likelihood logarithm value for
        .           each sample. It has \f$nsamples \times 1\f$ size and CV_64FC1 type.
        .       @param labels The optional output "class label" for each sample:
        .           \f$\texttt{labels}_i=\texttt{arg max}_k(p_{i,k}), i=1..N\f$ (indices of the most probable
        .           mixture component for each sample). It has \f$nsamples \times 1\f$ size and CV_32SC1 type.
        .       @param probs The optional output matrix that contains posterior probabilities of each Gaussian
        .           mixture component given the each sample. It has \f$nsamples \times nclusters\f$ size and
        .           CV_64FC1 type.
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


