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


class face_FaceRecognizer(__cv2.Algorithm):
    # no doc
    def getLabelInfo(self, label): # real signature unknown; restored from __doc__
        """
        getLabelInfo(label) -> retval
        .   @brief Gets string information by label.
        .   
        .       If an unknown label id is provided or there is no label information associated with the specified
        .       label id the method returns an empty string.
        """
        pass

    def getLabelsByString(self, p_str): # real signature unknown; restored from __doc__
        """
        getLabelsByString(str) -> retval
        .   @brief Gets vector of labels by string.
        .   
        .       The function searches for the labels containing the specified sub-string in the associated string
        .       info.
        """
        pass

    def predict(self, src): # real signature unknown; restored from __doc__
        """
        predict(src) -> label, confidence
        .   @brief Predicts a label and associated confidence (e.g. distance) for a given input image.
        .   
        .       @param src Sample image to get a prediction from.
        .       @param label The predicted label for the given image.
        .       @param confidence Associated confidence (e.g. distance) for the predicted label.
        .   
        .       The suffix const means that prediction does not affect the internal model state, so the method can
        .       be safely called from within different threads.
        .   
        .       The following example shows how to get a prediction from a trained model:
        .   
        .       @code
        .       using namespace cv;
        .       // Do your initialization here (create the cv::FaceRecognizer model) ...
        .       // ...
        .       // Read in a sample image:
        .       Mat img = imread("person1/3.jpg", IMREAD_GRAYSCALE);
        .       // And get a prediction from the cv::FaceRecognizer:
        .       int predicted = model->predict(img);
        .       @endcode
        .   
        .       Or to get a prediction and the associated confidence (e.g. distance):
        .   
        .       @code
        .       using namespace cv;
        .       // Do your initialization here (create the cv::FaceRecognizer model) ...
        .       // ...
        .       Mat img = imread("person1/3.jpg", IMREAD_GRAYSCALE);
        .       // Some variables for the predicted label and associated confidence (e.g. distance):
        .       int predicted_label = -1;
        .       double predicted_confidence = 0.0;
        .       // Get the prediction and associated confidence from the model
        .       model->predict(img, predicted_label, predicted_confidence);
        .       @endcode
        """
        pass

    def predict_collect(self, src, collector): # real signature unknown; restored from __doc__
        """
        predict_collect(src, collector) -> None
        .   @brief - if implemented - send all result of prediction to collector that can be used for somehow custom result handling
        .       @param src Sample image to get a prediction from.
        .       @param collector User-defined collector object that accepts all results
        .   
        .       To implement this method u just have to do same internal cycle as in predict(InputArray src, CV_OUT int &label, CV_OUT double &confidence) but
        .       not try to get "best@ result, just resend it to caller side with given collector
        """
        pass

    def predict_label(self, src): # real signature unknown; restored from __doc__
        """
        predict_label(src) -> retval
        .   @overload
        """
        pass

    def read(self, filename): # real signature unknown; restored from __doc__
        """
        read(filename) -> None
        .   @brief Loads a FaceRecognizer and its model state.
        .   
        .       Loads a persisted model and state from a given XML or YAML file . Every FaceRecognizer has to
        .       overwrite FaceRecognizer::load(FileStorage& fs) to enable loading the model state.
        .       FaceRecognizer::load(FileStorage& fs) in turn gets called by
        .       FaceRecognizer::load(const String& filename), to ease saving a model.
        """
        pass

    def setLabelInfo(self, label, strInfo): # real signature unknown; restored from __doc__
        """
        setLabelInfo(label, strInfo) -> None
        .   @brief Sets string info for the specified model's label.
        .   
        .       The string info is replaced by the provided value if it was set before for the specified label.
        """
        pass

    def train(self, src, labels): # real signature unknown; restored from __doc__
        """
        train(src, labels) -> None
        .   @brief Trains a FaceRecognizer with given data and associated labels.
        .   
        .       @param src The training images, that means the faces you want to learn. The data has to be
        .       given as a vector\<Mat\>.
        .       @param labels The labels corresponding to the images have to be given either as a vector\<int\>
        .       or a Mat of type CV_32SC1.
        .   
        .       The following source code snippet shows you how to learn a Fisherfaces model on a given set of
        .       images. The images are read with imread and pushed into a std::vector\<Mat\>. The labels of each
        .       image are stored within a std::vector\<int\> (you could also use a Mat of type CV_32SC1). Think of
        .       the label as the subject (the person) this image belongs to, so same subjects (persons) should have
        .       the same label. For the available FaceRecognizer you don't have to pay any attention to the order of
        .       the labels, just make sure same persons have the same label:
        .   
        .       @code
        .       // holds images and labels
        .       vector<Mat> images;
        .       vector<int> labels;
        .       // using Mat of type CV_32SC1
        .       // Mat labels(number_of_samples, 1, CV_32SC1);
        .       // images for first person
        .       images.push_back(imread("person0/0.jpg", IMREAD_GRAYSCALE)); labels.push_back(0);
        .       images.push_back(imread("person0/1.jpg", IMREAD_GRAYSCALE)); labels.push_back(0);
        .       images.push_back(imread("person0/2.jpg", IMREAD_GRAYSCALE)); labels.push_back(0);
        .       // images for second person
        .       images.push_back(imread("person1/0.jpg", IMREAD_GRAYSCALE)); labels.push_back(1);
        .       images.push_back(imread("person1/1.jpg", IMREAD_GRAYSCALE)); labels.push_back(1);
        .       images.push_back(imread("person1/2.jpg", IMREAD_GRAYSCALE)); labels.push_back(1);
        .       @endcode
        .   
        .       Now that you have read some images, we can create a new FaceRecognizer. In this example I'll create
        .       a Fisherfaces model and decide to keep all of the possible Fisherfaces:
        .   
        .       @code
        .       // Create a new Fisherfaces model and retain all available Fisherfaces,
        .       // this is the most common usage of this specific FaceRecognizer:
        .       //
        .       Ptr<FaceRecognizer> model =  FisherFaceRecognizer::create();
        .       @endcode
        .   
        .       And finally train it on the given dataset (the face images and labels):
        .   
        .       @code
        .       // This is the common interface to train all of the available cv::FaceRecognizer
        .       // implementations:
        .       //
        .       model->train(images, labels);
        .       @endcode
        """
        pass

    def update(self, src, labels): # real signature unknown; restored from __doc__
        """
        update(src, labels) -> None
        .   @brief Updates a FaceRecognizer with given data and associated labels.
        .   
        .       @param src The training images, that means the faces you want to learn. The data has to be given
        .       as a vector\<Mat\>.
        .       @param labels The labels corresponding to the images have to be given either as a vector\<int\> or
        .       a Mat of type CV_32SC1.
        .   
        .       This method updates a (probably trained) FaceRecognizer, but only if the algorithm supports it. The
        .       Local Binary Patterns Histograms (LBPH) recognizer (see createLBPHFaceRecognizer) can be updated.
        .       For the Eigenfaces and Fisherfaces method, this is algorithmically not possible and you have to
        .       re-estimate the model with FaceRecognizer::train. In any case, a call to train empties the existing
        .       model and learns a new model, while update does not delete any model data.
        .   
        .       @code
        .       // Create a new LBPH model (it can be updated) and use the default parameters,
        .       // this is the most common usage of this specific FaceRecognizer:
        .       //
        .       Ptr<FaceRecognizer> model =  LBPHFaceRecognizer::create();
        .       // This is the common interface to train all of the available cv::FaceRecognizer
        .       // implementations:
        .       //
        .       model->train(images, labels);
        .       // Some containers to hold new image:
        .       vector<Mat> newImages;
        .       vector<int> newLabels;
        .       // You should add some images to the containers:
        .       //
        .       // ...
        .       //
        .       // Now updating the model is as easy as calling:
        .       model->update(newImages,newLabels);
        .       // This will preserve the old model data and extend the existing model
        .       // with the new features extracted from newImages!
        .       @endcode
        .   
        .       Calling update on an Eigenfaces model (see EigenFaceRecognizer::create), which doesn't support
        .       updating, will throw an error similar to:
        .   
        .       @code
        .       OpenCV Error: The function/feature is not implemented (This FaceRecognizer (FaceRecognizer.Eigenfaces) does not support updating, you have to use FaceRecognizer::train to update it.) in update, file /home/philipp/git/opencv/modules/contrib/src/facerec.cpp, line 305
        .       terminate called after throwing an instance of 'cv::Exception'
        .       @endcode
        .   
        .       @note The FaceRecognizer does not store your training images, because this would be very
        .       memory intense and it's not the responsibility of te FaceRecognizer to do so. The caller is
        .       responsible for maintaining the dataset, he want to work with.
        """
        pass

    def write(self, filename): # real signature unknown; restored from __doc__
        """
        write(filename) -> None
        .   @brief Saves a FaceRecognizer and its model state.
        .   
        .       Saves this model to a given filename, either as XML or YAML.
        .       @param filename The filename to store this FaceRecognizer to (either XML/YAML).
        .   
        .       Every FaceRecognizer overwrites FaceRecognizer::save(FileStorage& fs) to save the internal model
        .       state. FaceRecognizer::save(const String& filename) saves the state of a model to the given
        .       filename.
        .   
        .       The suffix const means that prediction does not affect the internal model state, so the method can
        .       be safely called from within different threads.
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


