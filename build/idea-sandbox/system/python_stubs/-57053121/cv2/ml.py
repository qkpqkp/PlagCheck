# encoding: utf-8
# module cv2.ml
# from C:\Users\Doly\Anaconda3\lib\site-packages\cv2\cv2.cp37-win_amd64.pyd
# by generator 1.147
# no doc
# no imports

# Variables with simple values

ANN_MLP_ANNEAL = 2
ANN_MLP_BACKPROP = 0
ANN_MLP_GAUSSIAN = 2
ANN_MLP_IDENTITY = 0
ANN_MLP_LEAKYRELU = 4

ANN_MLP_NO_INPUT_SCALE = 2

ANN_MLP_NO_OUTPUT_SCALE = 4

ANN_MLP_RELU = 3
ANN_MLP_RPROP = 1

ANN_MLP_SIGMOID_SYM = 1

ANN_MLP_UPDATE_WEIGHTS = 1

Boost_DISCRETE = 0

BOOST_DISCRETE = 0

Boost_GENTLE = 3

BOOST_GENTLE = 3

Boost_LOGIT = 2

BOOST_LOGIT = 2

Boost_REAL = 1

BOOST_REAL = 1

COL_SAMPLE = 1

DTrees_PREDICT_AUTO = 0

DTREES_PREDICT_AUTO = 0

DTrees_PREDICT_MASK = 768

DTREES_PREDICT_MASK = 768

DTrees_PREDICT_MAX_VOTE = 512

DTREES_PREDICT_MAX_VOTE = 512

DTrees_PREDICT_SUM = 256

DTREES_PREDICT_SUM = 256

EM_COV_MAT_DEFAULT = 1
EM_COV_MAT_DIAGONAL = 1
EM_COV_MAT_GENERIC = 2
EM_COV_MAT_SPHERICAL = 0

EM_DEFAULT_MAX_ITERS = 100

EM_DEFAULT_NCLUSTERS = 5

EM_START_AUTO_STEP = 0

EM_START_E_STEP = 1

EM_START_M_STEP = 2

KNearest_BRUTE_FORCE = 1

KNEAREST_BRUTE_FORCE = 1

KNearest_KDTREE = 2

KNEAREST_KDTREE = 2

LogisticRegression_BATCH = 0

LogisticRegression_MINI_BATCH = 1

LogisticRegression_REG_DISABLE = -1
LogisticRegression_REG_L1 = 0
LogisticRegression_REG_L2 = 1

LOGISTIC_REGRESSION_BATCH = 0

LOGISTIC_REGRESSION_MINI_BATCH = 1

LOGISTIC_REGRESSION_REG_DISABLE = -1
LOGISTIC_REGRESSION_REG_L1 = 0
LOGISTIC_REGRESSION_REG_L2 = 1

ROW_SAMPLE = 0

StatModel_COMPRESSED_INPUT = 2

StatModel_PREPROCESSED_INPUT = 4

StatModel_RAW_OUTPUT = 1

StatModel_UPDATE_MODEL = 1

STAT_MODEL_COMPRESSED_INPUT = 2

STAT_MODEL_PREPROCESSED_INPUT = 4

STAT_MODEL_RAW_OUTPUT = 1

STAT_MODEL_UPDATE_MODEL = 1

SVMSGD_ASGD = 1

SVMSGD_HARD_MARGIN = 1

SVMSGD_SGD = 0

SVMSGD_SOFT_MARGIN = 0

SVM_C = 0
SVM_CHI2 = 4
SVM_COEF = 4
SVM_CUSTOM = -1

SVM_C_SVC = 100

SVM_DEGREE = 5

SVM_EPS_SVR = 103

SVM_GAMMA = 1
SVM_INTER = 5
SVM_LINEAR = 0
SVM_NU = 3

SVM_NU_SVC = 101
SVM_NU_SVR = 104

SVM_ONE_CLASS = 102

SVM_P = 2
SVM_POLY = 1
SVM_RBF = 2
SVM_SIGMOID = 3

TEST_ERROR = 0

TRAIN_ERROR = 1

VAR_CATEGORICAL = 1
VAR_NUMERICAL = 0
VAR_ORDERED = 0

__loader__ = None

__spec__ = None

# functions

def ANN_MLP_create(): # real signature unknown; restored from __doc__
    """
    ANN_MLP_create() -> retval
    .   @brief Creates empty model
    .   
    .       Use StatModel::train to train the model, Algorithm::load\<ANN_MLP\>(filename) to load the pre-trained model.
    .       Note that the train method has optional flags: ANN_MLP::TrainFlags.
    """
    pass

def ANN_MLP_load(filepath): # real signature unknown; restored from __doc__
    """
    ANN_MLP_load(filepath) -> retval
    .   @brief Loads and creates a serialized ANN from a file
    .        *
    .        * Use ANN::save to serialize and store an ANN to disk.
    .        * Load the ANN from this file again, by calling this function with the path to the file.
    .        *
    .        * @param filepath path to serialized ANN
    """
    pass

def Boost_create(): # real signature unknown; restored from __doc__
    """
    Boost_create() -> retval
    .   Creates the empty model.
    .   Use StatModel::train to train the model, Algorithm::load\<Boost\>(filename) to load the pre-trained model.
    """
    pass

def Boost_load(filepath, nodeName=None): # real signature unknown; restored from __doc__
    """
    Boost_load(filepath[, nodeName]) -> retval
    .   @brief Loads and creates a serialized Boost from a file
    .        *
    .        * Use Boost::save to serialize and store an RTree to disk.
    .        * Load the Boost from this file again, by calling this function with the path to the file.
    .        * Optionally specify the node for the file containing the classifier
    .        *
    .        * @param filepath path to serialized Boost
    .        * @param nodeName name of node containing the classifier
    """
    pass

def DTrees_create(): # real signature unknown; restored from __doc__
    """
    DTrees_create() -> retval
    .   @brief Creates the empty model
    .   
    .       The static method creates empty decision tree with the specified parameters. It should be then
    .       trained using train method (see StatModel::train). Alternatively, you can load the model from
    .       file using Algorithm::load\<DTrees\>(filename).
    """
    pass

def DTrees_load(filepath, nodeName=None): # real signature unknown; restored from __doc__
    """
    DTrees_load(filepath[, nodeName]) -> retval
    .   @brief Loads and creates a serialized DTrees from a file
    .        *
    .        * Use DTree::save to serialize and store an DTree to disk.
    .        * Load the DTree from this file again, by calling this function with the path to the file.
    .        * Optionally specify the node for the file containing the classifier
    .        *
    .        * @param filepath path to serialized DTree
    .        * @param nodeName name of node containing the classifier
    """
    pass

def EM_create(): # real signature unknown; restored from __doc__
    """
    EM_create() -> retval
    .   Creates empty %EM model.
    .       The model should be trained then using StatModel::train(traindata, flags) method. Alternatively, you
    .       can use one of the EM::train\* methods or load it from file using Algorithm::load\<EM\>(filename).
    """
    pass

def EM_load(filepath, nodeName=None): # real signature unknown; restored from __doc__
    """
    EM_load(filepath[, nodeName]) -> retval
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

def KNearest_create(): # real signature unknown; restored from __doc__
    """
    KNearest_create() -> retval
    .   @brief Creates the empty model
    .   
    .       The static method creates empty %KNearest classifier. It should be then trained using StatModel::train method.
    """
    pass

def KNearest_load(filepath): # real signature unknown; restored from __doc__
    """
    KNearest_load(filepath) -> retval
    .   @brief Loads and creates a serialized knearest from a file
    .        *
    .        * Use KNearest::save to serialize and store an KNearest to disk.
    .        * Load the KNearest from this file again, by calling this function with the path to the file.
    .        *
    .        * @param filepath path to serialized KNearest
    """
    pass

def LogisticRegression_create(): # real signature unknown; restored from __doc__
    """
    LogisticRegression_create() -> retval
    .   @brief Creates empty model.
    .   
    .       Creates Logistic Regression model with parameters given.
    """
    pass

def LogisticRegression_load(filepath, nodeName=None): # real signature unknown; restored from __doc__
    """
    LogisticRegression_load(filepath[, nodeName]) -> retval
    .   @brief Loads and creates a serialized LogisticRegression from a file
    .        *
    .        * Use LogisticRegression::save to serialize and store an LogisticRegression to disk.
    .        * Load the LogisticRegression from this file again, by calling this function with the path to the file.
    .        * Optionally specify the node for the file containing the classifier
    .        *
    .        * @param filepath path to serialized LogisticRegression
    .        * @param nodeName name of node containing the classifier
    """
    pass

def NormalBayesClassifier_create(): # real signature unknown; restored from __doc__
    """
    NormalBayesClassifier_create() -> retval
    .   Creates empty model
    .   Use StatModel::train to train the model after creation.
    """
    pass

def NormalBayesClassifier_load(filepath, nodeName=None): # real signature unknown; restored from __doc__
    """
    NormalBayesClassifier_load(filepath[, nodeName]) -> retval
    .   @brief Loads and creates a serialized NormalBayesClassifier from a file
    .        *
    .        * Use NormalBayesClassifier::save to serialize and store an NormalBayesClassifier to disk.
    .        * Load the NormalBayesClassifier from this file again, by calling this function with the path to the file.
    .        * Optionally specify the node for the file containing the classifier
    .        *
    .        * @param filepath path to serialized NormalBayesClassifier
    .        * @param nodeName name of node containing the classifier
    """
    pass

def ParamGrid_create(minVal=None, maxVal=None, logstep=None): # real signature unknown; restored from __doc__
    """
    ParamGrid_create([, minVal[, maxVal[, logstep]]]) -> retval
    .   @brief Creates a ParamGrid Ptr that can be given to the %SVM::trainAuto method
    .   
    .       @param minVal minimum value of the parameter grid
    .       @param maxVal maximum value of the parameter grid
    .       @param logstep Logarithmic step for iterating the statmodel parameter
    """
    pass

def RTrees_create(): # real signature unknown; restored from __doc__
    """
    RTrees_create() -> retval
    .   Creates the empty model.
    .       Use StatModel::train to train the model, StatModel::train to create and train the model,
    .       Algorithm::load to load the pre-trained model.
    """
    pass

def RTrees_load(filepath, nodeName=None): # real signature unknown; restored from __doc__
    """
    RTrees_load(filepath[, nodeName]) -> retval
    .   @brief Loads and creates a serialized RTree from a file
    .        *
    .        * Use RTree::save to serialize and store an RTree to disk.
    .        * Load the RTree from this file again, by calling this function with the path to the file.
    .        * Optionally specify the node for the file containing the classifier
    .        *
    .        * @param filepath path to serialized RTree
    .        * @param nodeName name of node containing the classifier
    """
    pass

def SVMSGD_create(): # real signature unknown; restored from __doc__
    """
    SVMSGD_create() -> retval
    .   @brief Creates empty model.
    .        * Use StatModel::train to train the model. Since %SVMSGD has several parameters, you may want to
    .        * find the best parameters for your problem or use setOptimalParameters() to set some default parameters.
    """
    pass

def SVMSGD_load(filepath, nodeName=None): # real signature unknown; restored from __doc__
    """
    SVMSGD_load(filepath[, nodeName]) -> retval
    .   @brief Loads and creates a serialized SVMSGD from a file
    .        *
    .        * Use SVMSGD::save to serialize and store an SVMSGD to disk.
    .        * Load the SVMSGD from this file again, by calling this function with the path to the file.
    .        * Optionally specify the node for the file containing the classifier
    .        *
    .        * @param filepath path to serialized SVMSGD
    .        * @param nodeName name of node containing the classifier
    """
    pass

def SVM_create(): # real signature unknown; restored from __doc__
    """
    SVM_create() -> retval
    .   Creates empty model.
    .       Use StatModel::train to train the model. Since %SVM has several parameters, you may want to
    .   find the best parameters for your problem, it can be done with SVM::trainAuto.
    """
    pass

def SVM_getDefaultGridPtr(param_id): # real signature unknown; restored from __doc__
    """
    SVM_getDefaultGridPtr(param_id) -> retval
    .   @brief Generates a grid for %SVM parameters.
    .   
    .       @param param_id %SVM parameters IDs that must be one of the SVM::ParamTypes. The grid is
    .       generated for the parameter with this ID.
    .   
    .       The function generates a grid pointer for the specified parameter of the %SVM algorithm.
    .       The grid may be passed to the function SVM::trainAuto.
    """
    pass

def SVM_load(filepath): # real signature unknown; restored from __doc__
    """
    SVM_load(filepath) -> retval
    .   @brief Loads and creates a serialized svm from a file
    .        *
    .        * Use SVM::save to serialize and store an SVM to disk.
    .        * Load the SVM from this file again, by calling this function with the path to the file.
    .        *
    .        * @param filepath path to serialized svm
    """
    pass

def TrainData_create(samples, layout, responses, varIdx=None, sampleIdx=None, sampleWeights=None, varType=None): # real signature unknown; restored from __doc__
    """
    TrainData_create(samples, layout, responses[, varIdx[, sampleIdx[, sampleWeights[, varType]]]]) -> retval
    .   @brief Creates training data from in-memory arrays.
    .   
    .       @param samples matrix of samples. It should have CV_32F type.
    .       @param layout see ml::SampleTypes.
    .       @param responses matrix of responses. If the responses are scalar, they should be stored as a
    .           single row or as a single column. The matrix should have type CV_32F or CV_32S (in the
    .           former case the responses are considered as ordered by default; in the latter case - as
    .           categorical)
    .       @param varIdx vector specifying which variables to use for training. It can be an integer vector
    .           (CV_32S) containing 0-based variable indices or byte vector (CV_8U) containing a mask of
    .           active variables.
    .       @param sampleIdx vector specifying which samples to use for training. It can be an integer
    .           vector (CV_32S) containing 0-based sample indices or byte vector (CV_8U) containing a mask
    .           of training samples.
    .       @param sampleWeights optional vector with weights for each sample. It should have CV_32F type.
    .       @param varType optional vector of type CV_8U and size `<number_of_variables_in_samples> +
    .           <number_of_variables_in_responses>`, containing types of each input and output variable. See
    .           ml::VariableTypes.
    """
    pass

def TrainData_getSubMatrix(matrix, idx, layout): # real signature unknown; restored from __doc__
    """
    TrainData_getSubMatrix(matrix, idx, layout) -> retval
    .   @brief Extract from matrix rows/cols specified by passed indexes.
    .       @param matrix input matrix (supported types: CV_32S, CV_32F, CV_64F)
    .       @param idx 1D index vector
    .       @param layout specifies to extract rows (cv::ml::ROW_SAMPLES) or to extract columns (cv::ml::COL_SAMPLES)
    """
    pass

def TrainData_getSubVector(vec, idx): # real signature unknown; restored from __doc__
    """
    TrainData_getSubVector(vec, idx) -> retval
    .   @brief Extract from 1D vector elements specified by passed indexes.
    .       @param vec input vector (supported types: CV_32S, CV_32F, CV_64F)
    .       @param idx 1D index vector
    """
    pass

# no classes
