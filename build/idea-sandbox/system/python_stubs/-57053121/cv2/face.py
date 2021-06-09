# encoding: utf-8
# module cv2.face
# from C:\Users\Doly\Anaconda3\lib\site-packages\cv2\cv2.cp37-win_amd64.pyd
# by generator 1.147
# no doc
# no imports

# Variables with simple values

__loader__ = None

__spec__ = None

# functions

def BIF_create(num_bands=None, num_rotations=None): # real signature unknown; restored from __doc__
    """
    BIF_create([, num_bands[, num_rotations]]) -> retval
    .   * @param num_bands The number of filter bands (<=8) used for computing BIF.
    .        * @param num_rotations The number of image rotations for computing BIF.
    .        * @returns Object for computing BIF.
    """
    pass

def createFacemarkAAM(): # real signature unknown; restored from __doc__
    """
    createFacemarkAAM() -> retval
    .
    """
    pass

def createFacemarkKazemi(): # real signature unknown; restored from __doc__
    """
    createFacemarkKazemi() -> retval
    .
    """
    pass

def createFacemarkLBF(): # real signature unknown; restored from __doc__
    """
    createFacemarkLBF() -> retval
    .
    """
    pass

def drawFacemarks(image, points, color=None): # real signature unknown; restored from __doc__
    """
    drawFacemarks(image, points[, color]) -> image
    .   @brief Utility to draw the detected facial landmark points
    .   
    .   @param image The input image to be processed.
    .   @param points Contains the data of points which will be drawn.
    .   @param color The color of points in BGR format represented by cv::Scalar.
    .   
    .   <B>Example of usage</B>
    .   @code
    .   std::vector<Rect> faces;
    .   std::vector<std::vector<Point2f> > landmarks;
    .   facemark->getFaces(img, faces);
    .   facemark->fit(img, faces, landmarks);
    .   for(int j=0;j<rects.size();j++){
    .       face::drawFacemarks(frame, landmarks[j], Scalar(0,0,255));
    .   }
    .   @endcode
    """
    pass

def EigenFaceRecognizer_create(num_components=None, threshold=None): # real signature unknown; restored from __doc__
    """
    EigenFaceRecognizer_create([, num_components[, threshold]]) -> retval
    .   @param num_components The number of components (read: Eigenfaces) kept for this Principal
    .       Component Analysis. As a hint: There's no rule how many components (read: Eigenfaces) should be
    .       kept for good reconstruction capabilities. It is based on your input data, so experiment with the
    .       number. Keeping 80 components should almost always be sufficient.
    .       @param threshold The threshold applied in the prediction.
    .   
    .       ### Notes:
    .   
    .       -   Training and prediction must be done on grayscale images, use cvtColor to convert between the
    .           color spaces.
    .       -   **THE EIGENFACES METHOD MAKES THE ASSUMPTION, THAT THE TRAINING AND TEST IMAGES ARE OF EQUAL
    .           SIZE.** (caps-lock, because I got so many mails asking for this). You have to make sure your
    .           input data has the correct shape, else a meaningful exception is thrown. Use resize to resize
    .           the images.
    .       -   This model does not support updating.
    .   
    .       ### Model internal data:
    .   
    .       -   num_components see EigenFaceRecognizer::create.
    .       -   threshold see EigenFaceRecognizer::create.
    .       -   eigenvalues The eigenvalues for this Principal Component Analysis (ordered descending).
    .       -   eigenvectors The eigenvectors for this Principal Component Analysis (ordered by their
    .           eigenvalue).
    .       -   mean The sample mean calculated from the training data.
    .       -   projections The projections of the training data.
    .       -   labels The threshold applied in the prediction. If the distance to the nearest neighbor is
    .           larger than the threshold, this method returns -1.
    """
    pass

def FisherFaceRecognizer_create(num_components=None, threshold=None): # real signature unknown; restored from __doc__
    """
    FisherFaceRecognizer_create([, num_components[, threshold]]) -> retval
    .   @param num_components The number of components (read: Fisherfaces) kept for this Linear
    .       Discriminant Analysis with the Fisherfaces criterion. It's useful to keep all components, that
    .       means the number of your classes c (read: subjects, persons you want to recognize). If you leave
    .       this at the default (0) or set it to a value less-equal 0 or greater (c-1), it will be set to the
    .       correct number (c-1) automatically.
    .       @param threshold The threshold applied in the prediction. If the distance to the nearest neighbor
    .       is larger than the threshold, this method returns -1.
    .   
    .       ### Notes:
    .   
    .       -   Training and prediction must be done on grayscale images, use cvtColor to convert between the
    .           color spaces.
    .       -   **THE FISHERFACES METHOD MAKES THE ASSUMPTION, THAT THE TRAINING AND TEST IMAGES ARE OF EQUAL
    .           SIZE.** (caps-lock, because I got so many mails asking for this). You have to make sure your
    .           input data has the correct shape, else a meaningful exception is thrown. Use resize to resize
    .           the images.
    .       -   This model does not support updating.
    .   
    .       ### Model internal data:
    .   
    .       -   num_components see FisherFaceRecognizer::create.
    .       -   threshold see FisherFaceRecognizer::create.
    .       -   eigenvalues The eigenvalues for this Linear Discriminant Analysis (ordered descending).
    .       -   eigenvectors The eigenvectors for this Linear Discriminant Analysis (ordered by their
    .           eigenvalue).
    .       -   mean The sample mean calculated from the training data.
    .       -   projections The projections of the training data.
    .       -   labels The labels corresponding to the projections.
    """
    pass

def getFacesHAAR(image, face_cascade_name, faces=None): # real signature unknown; restored from __doc__
    """
    getFacesHAAR(image, face_cascade_name[, faces]) -> retval, faces
    .   @brief Default face detector
    .   This function is mainly utilized by the implementation of a Facemark Algorithm.
    .   End users are advised to use function Facemark::getFaces which can be manually defined
    .   and circumvented to the algorithm by Facemark::setFaceDetector.
    .   
    .   @param image The input image to be processed.
    .   @param faces Output of the function which represent region of interest of the detected faces.
    .   Each face is stored in cv::Rect container.
    .   @param params detector parameters
    .   
    .   <B>Example of usage</B>
    .   @code
    .   std::vector<cv::Rect> faces;
    .   CParams params("haarcascade_frontalface_alt.xml");
    .   cv::face::getFaces(frame, faces, &params);
    .   for(int j=0;j<faces.size();j++){
    .       cv::rectangle(frame, faces[j], cv::Scalar(255,0,255));
    .   }
    .   cv::imshow("detection", frame);
    .   @endcode
    """
    pass

def LBPHFaceRecognizer_create(radius=None, neighbors=None, grid_x=None, grid_y=None, threshold=None): # real signature unknown; restored from __doc__
    """
    LBPHFaceRecognizer_create([, radius[, neighbors[, grid_x[, grid_y[, threshold]]]]]) -> retval
    .   @param radius The radius used for building the Circular Local Binary Pattern. The greater the
    .       radius, the smoother the image but more spatial information you can get.
    .       @param neighbors The number of sample points to build a Circular Local Binary Pattern from. An
    .       appropriate value is to use `8` sample points. Keep in mind: the more sample points you include,
    .       the higher the computational cost.
    .       @param grid_x The number of cells in the horizontal direction, 8 is a common value used in
    .       publications. The more cells, the finer the grid, the higher the dimensionality of the resulting
    .       feature vector.
    .       @param grid_y The number of cells in the vertical direction, 8 is a common value used in
    .       publications. The more cells, the finer the grid, the higher the dimensionality of the resulting
    .       feature vector.
    .       @param threshold The threshold applied in the prediction. If the distance to the nearest neighbor
    .       is larger than the threshold, this method returns -1.
    .   
    .       ### Notes:
    .   
    .       -   The Circular Local Binary Patterns (used in training and prediction) expect the data given as
    .           grayscale images, use cvtColor to convert between the color spaces.
    .       -   This model supports updating.
    .   
    .       ### Model internal data:
    .   
    .       -   radius see LBPHFaceRecognizer::create.
    .       -   neighbors see LBPHFaceRecognizer::create.
    .       -   grid_x see LLBPHFaceRecognizer::create.
    .       -   grid_y see LBPHFaceRecognizer::create.
    .       -   threshold see LBPHFaceRecognizer::create.
    .       -   histograms Local Binary Patterns Histograms calculated from the given training data (empty if
    .           none was given).
    .       -   labels Labels corresponding to the calculated Local Binary Patterns Histograms.
    """
    pass

def loadDatasetList(imageList, annotationList, images, annotations): # real signature unknown; restored from __doc__
    """
    loadDatasetList(imageList, annotationList, images, annotations) -> retval
    .   @brief A utility to load list of paths to training image and annotation file.
    .   @param imageList The specified file contains paths to the training images.
    .   @param annotationList The specified file contains paths to the training annotations.
    .   @param images The loaded paths of training images.
    .   @param annotations The loaded paths of annotation files.
    .   
    .   Example of usage:
    .   @code
    .   String imageFiles = "images_path.txt";
    .   String ptsFiles = "annotations_path.txt";
    .   std::vector<String> images_train;
    .   std::vector<String> landmarks_train;
    .   loadDatasetList(imageFiles,ptsFiles,images_train,landmarks_train);
    .   @endcode
    """
    pass

def loadFacePoints(filename, points=None, offset=None): # real signature unknown; restored from __doc__
    """
    loadFacePoints(filename[, points[, offset]]) -> retval, points
    .   @brief A utility to load facial landmark information from a given file.
    .   
    .   @param filename The filename of file contains the facial landmarks data.
    .   @param points The loaded facial landmark points.
    .   @param offset An offset value to adjust the loaded points.
    .   
    .   <B>Example of usage</B>
    .   @code
    .   std::vector<Point2f> points;
    .   face::loadFacePoints("filename.txt", points, 0.0f);
    .   @endcode
    .   
    .   The annotation file should follow the default format which is
    .   @code
    .   version: 1
    .   n_points:  68
    .   {
    .   212.716603 499.771793
    .   230.232816 566.290071
    .   ...
    .   }
    .   @endcode
    .   where n_points is the number of points considered
    .   and each point is represented as its position in x and y.
    """
    pass

def loadTrainingData(filename, images, facePoints=None, delim=None, offset=None): # real signature unknown; restored from __doc__
    """
    loadTrainingData(filename, images[, facePoints[, delim[, offset]]]) -> retval, facePoints
    .   @brief A utility to load facial landmark dataset from a single file.
    .   
    .   @param filename The filename of a file that contains the dataset information.
    .   Each line contains the filename of an image followed by
    .   pairs of x and y values of facial landmarks points separated by a space.
    .   Example
    .   @code
    .   /home/user/ibug/image_003_1.jpg 336.820955 240.864510 334.238298 260.922709 335.266918 ...
    .   /home/user/ibug/image_005_1.jpg 376.158428 230.845712 376.736984 254.924635 383.265403 ...
    .   @endcode
    .   @param images A vector where each element represent the filename of image in the dataset.
    .   Images are not loaded by default to save the memory.
    .   @param facePoints The loaded landmark points for all training data.
    .   @param delim Delimiter between each element, the default value is a whitespace.
    .   @param offset An offset value to adjust the loaded points.
    .   
    .   <B>Example of usage</B>
    .   @code
    .   cv::String imageFiles = "../data/images_train.txt";
    .   cv::String ptsFiles = "../data/points_train.txt";
    .   std::vector<String> images;
    .   std::vector<std::vector<Point2f> > facePoints;
    .   loadTrainingData(imageFiles, ptsFiles, images, facePoints, 0.0f);
    .   @endcode
    
    
    
    loadTrainingData(imageList, groundTruth, images[, facePoints[, offset]]) -> retval, facePoints
    .   @brief A utility to load facial landmark information from the dataset.
    .   
    .   @param imageList A file contains the list of image filenames in the training dataset.
    .   @param groundTruth A file contains the list of filenames
    .   where the landmarks points information are stored.
    .   The content in each file should follow the standard format (see face::loadFacePoints).
    .   @param images A vector where each element represent the filename of image in the dataset.
    .   Images are not loaded by default to save the memory.
    .   @param facePoints The loaded landmark points for all training data.
    .   @param offset An offset value to adjust the loaded points.
    .   
    .   <B>Example of usage</B>
    .   @code
    .   cv::String imageFiles = "../data/images_train.txt";
    .   cv::String ptsFiles = "../data/points_train.txt";
    .   std::vector<String> images;
    .   std::vector<std::vector<Point2f> > facePoints;
    .   loadTrainingData(imageFiles, ptsFiles, images, facePoints, 0.0f);
    .   @endcode
    .   
    .   example of content in the images_train.txt
    .   @code
    .   /home/user/ibug/image_003_1.jpg
    .   /home/user/ibug/image_004_1.jpg
    .   /home/user/ibug/image_005_1.jpg
    .   /home/user/ibug/image_006.jpg
    .   @endcode
    .   
    .   example of content in the points_train.txt
    .   @code
    .   /home/user/ibug/image_003_1.pts
    .   /home/user/ibug/image_004_1.pts
    .   /home/user/ibug/image_005_1.pts
    .   /home/user/ibug/image_006.pts
    .   @endcode
    
    
    
    loadTrainingData(filename, trainlandmarks, trainimages) -> retval
    .   @brief This function extracts the data for training from .txt files which contains the corresponding image name and landmarks.
    .   *The first file in each file should give the path of the image whose
    .   *landmarks are being described in the file. Then in the subsequent
    .   *lines there should be coordinates of the landmarks in the image
    .   *i.e each line should be of the form x,y
    .   *where x represents the x coordinate of the landmark and y represents
    .   *the y coordinate of the landmark.
    .   *
    .   *For reference you can see the files as provided in the
    .   *<a href="http://www.ifp.illinois.edu/~vuongle2/helen/">HELEN dataset</a>
    .   *
    .   * @param filename A vector of type cv::String containing name of the .txt files.
    .   * @param trainlandmarks A vector of type cv::Point2f that would store shape or landmarks of all images.
    .   * @param trainimages A vector of type cv::String which stores the name of images whose landmarks are tracked
    .   * @returns A boolean value. It returns true when it reads the data successfully and false otherwise
    """
    pass

def MACE_create(IMGSIZE=None): # real signature unknown; restored from __doc__
    """
    MACE_create([, IMGSIZE]) -> retval
    .   @brief constructor
    .       @param IMGSIZE  images will get resized to this (should be an even number)
    """
    pass

def MACE_load(filename, objname=None): # real signature unknown; restored from __doc__
    """
    MACE_load(filename[, objname]) -> retval
    .   @brief constructor
    .       @param filename  build a new MACE instance from a pre-serialized FileStorage
    .       @param objname (optional) top-level node in the FileStorage
    """
    pass

def StandardCollector_create(threshold=None): # real signature unknown; restored from __doc__
    """
    StandardCollector_create([, threshold]) -> retval
    .   @brief Static constructor
    .       @param threshold set threshold
    """
    pass

# no classes
