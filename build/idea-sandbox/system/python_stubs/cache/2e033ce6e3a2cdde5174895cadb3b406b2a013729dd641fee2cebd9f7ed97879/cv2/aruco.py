# encoding: utf-8
# module cv2.aruco
# from C:\Users\Doly\Anaconda3\lib\site-packages\cv2\cv2.cp37-win_amd64.pyd
# by generator 1.147
# no doc
# no imports

# Variables with simple values

CORNER_REFINE_APRILTAG = 3
CORNER_REFINE_CONTOUR = 2
CORNER_REFINE_NONE = 0
CORNER_REFINE_SUBPIX = 1

DICT_4X4_100 = 1
DICT_4X4_1000 = 3
DICT_4X4_250 = 2
DICT_4X4_50 = 0

DICT_5X5_100 = 5
DICT_5X5_1000 = 7
DICT_5X5_250 = 6
DICT_5X5_50 = 4

DICT_6X6_100 = 9
DICT_6X6_1000 = 11
DICT_6X6_250 = 10
DICT_6X6_50 = 8

DICT_7X7_100 = 13
DICT_7X7_1000 = 15
DICT_7X7_250 = 14
DICT_7X7_50 = 12

DICT_APRILTAG_16h5 = 17
DICT_APRILTAG_16H5 = 17
DICT_APRILTAG_25h9 = 18
DICT_APRILTAG_25H9 = 18
DICT_APRILTAG_36h10 = 19
DICT_APRILTAG_36H10 = 19
DICT_APRILTAG_36h11 = 20
DICT_APRILTAG_36H11 = 20

DICT_ARUCO_ORIGINAL = 16

__loader__ = None

__spec__ = None

# functions

def Board_create(objPoints, dictionary, ids): # real signature unknown; restored from __doc__
    """
    Board_create(objPoints, dictionary, ids) -> retval
    .   * @brief Provide way to create Board by passing necessary data. Specially needed in Python.
    .       *
    .       * @param objPoints array of object points of all the marker corners in the board
    .       * @param dictionary the dictionary of markers employed for this board
    .       * @param ids vector of the identifiers of the markers in the board
    .       *
    """
    pass

def calibrateCameraAruco(corners, ids, counter, board, imageSize, cameraMatrix, distCoeffs, rvecs=None, tvecs=None, flags=None, criteria=None): # real signature unknown; restored from __doc__
    """
    calibrateCameraAruco(corners, ids, counter, board, imageSize, cameraMatrix, distCoeffs[, rvecs[, tvecs[, flags[, criteria]]]]) -> retval, cameraMatrix, distCoeffs, rvecs, tvecs
    .   @brief It's the same function as #calibrateCameraAruco but without calibration error estimation.
    """
    pass

def calibrateCameraArucoExtended(corners, ids, counter, board, imageSize, cameraMatrix, distCoeffs, rvecs=None, tvecs=None, stdDeviationsIntrinsics=None, stdDeviationsExtrinsics=None, perViewErrors=None, flags=None, criteria=None): # real signature unknown; restored from __doc__
    """
    calibrateCameraArucoExtended(corners, ids, counter, board, imageSize, cameraMatrix, distCoeffs[, rvecs[, tvecs[, stdDeviationsIntrinsics[, stdDeviationsExtrinsics[, perViewErrors[, flags[, criteria]]]]]]]) -> retval, cameraMatrix, distCoeffs, rvecs, tvecs, stdDeviationsIntrinsics, stdDeviationsExtrinsics, perViewErrors
    .   * @brief Calibrate a camera using aruco markers
    .    *
    .    * @param corners vector of detected marker corners in all frames.
    .    * The corners should have the same format returned by detectMarkers (see #detectMarkers).
    .    * @param ids list of identifiers for each marker in corners
    .    * @param counter number of markers in each frame so that corners and ids can be split
    .    * @param board Marker Board layout
    .    * @param imageSize Size of the image used only to initialize the intrinsic camera matrix.
    .    * @param cameraMatrix Output 3x3 floating-point camera matrix
    .    * \f$A = \vecthreethree{f_x}{0}{c_x}{0}{f_y}{c_y}{0}{0}{1}\f$ . If CV\_CALIB\_USE\_INTRINSIC\_GUESS
    .    * and/or CV_CALIB_FIX_ASPECT_RATIO are specified, some or all of fx, fy, cx, cy must be
    .    * initialized before calling the function.
    .    * @param distCoeffs Output vector of distortion coefficients
    .    * \f$(k_1, k_2, p_1, p_2[, k_3[, k_4, k_5, k_6],[s_1, s_2, s_3, s_4]])\f$ of 4, 5, 8 or 12 elements
    .    * @param rvecs Output vector of rotation vectors (see Rodrigues ) estimated for each board view
    .    * (e.g. std::vector<cv::Mat>>). That is, each k-th rotation vector together with the corresponding
    .    * k-th translation vector (see the next output parameter description) brings the board pattern
    .    * from the model coordinate space (in which object points are specified) to the world coordinate
    .    * space, that is, a real position of the board pattern in the k-th pattern view (k=0.. *M* -1).
    .    * @param tvecs Output vector of translation vectors estimated for each pattern view.
    .    * @param stdDeviationsIntrinsics Output vector of standard deviations estimated for intrinsic parameters.
    .    * Order of deviations values:
    .    * \f$(f_x, f_y, c_x, c_y, k_1, k_2, p_1, p_2, k_3, k_4, k_5, k_6 , s_1, s_2, s_3,
    .    * s_4, \tau_x, \tau_y)\f$ If one of parameters is not estimated, it's deviation is equals to zero.
    .    * @param stdDeviationsExtrinsics Output vector of standard deviations estimated for extrinsic parameters.
    .    * Order of deviations values: \f$(R_1, T_1, \dotsc , R_M, T_M)\f$ where M is number of pattern views,
    .    * \f$R_i, T_i\f$ are concatenated 1x3 vectors.
    .    * @param perViewErrors Output vector of average re-projection errors estimated for each pattern view.
    .    * @param flags flags Different flags  for the calibration process (see #calibrateCamera for details).
    .    * @param criteria Termination criteria for the iterative optimization algorithm.
    .    *
    .    * This function calibrates a camera using an Aruco Board. The function receives a list of
    .    * detected markers from several views of the Board. The process is similar to the chessboard
    .    * calibration in calibrateCamera(). The function returns the final re-projection error.
    """
    pass

def calibrateCameraCharuco(charucoCorners, charucoIds, board, imageSize, cameraMatrix, distCoeffs, rvecs=None, tvecs=None, flags=None, criteria=None): # real signature unknown; restored from __doc__
    """
    calibrateCameraCharuco(charucoCorners, charucoIds, board, imageSize, cameraMatrix, distCoeffs[, rvecs[, tvecs[, flags[, criteria]]]]) -> retval, cameraMatrix, distCoeffs, rvecs, tvecs
    .   @brief It's the same function as #calibrateCameraCharuco but without calibration error estimation.
    """
    pass

def calibrateCameraCharucoExtended(charucoCorners, charucoIds, board, imageSize, cameraMatrix, distCoeffs, rvecs=None, tvecs=None, stdDeviationsIntrinsics=None, stdDeviationsExtrinsics=None, perViewErrors=None, flags=None, criteria=None): # real signature unknown; restored from __doc__
    """
    calibrateCameraCharucoExtended(charucoCorners, charucoIds, board, imageSize, cameraMatrix, distCoeffs[, rvecs[, tvecs[, stdDeviationsIntrinsics[, stdDeviationsExtrinsics[, perViewErrors[, flags[, criteria]]]]]]]) -> retval, cameraMatrix, distCoeffs, rvecs, tvecs, stdDeviationsIntrinsics, stdDeviationsExtrinsics, perViewErrors
    .   * @brief Calibrate a camera using Charuco corners
    .    *
    .    * @param charucoCorners vector of detected charuco corners per frame
    .    * @param charucoIds list of identifiers for each corner in charucoCorners per frame
    .    * @param board Marker Board layout
    .    * @param imageSize input image size
    .    * @param cameraMatrix Output 3x3 floating-point camera matrix
    .    * \f$A = \vecthreethree{f_x}{0}{c_x}{0}{f_y}{c_y}{0}{0}{1}\f$ . If CV\_CALIB\_USE\_INTRINSIC\_GUESS
    .    * and/or CV_CALIB_FIX_ASPECT_RATIO are specified, some or all of fx, fy, cx, cy must be
    .    * initialized before calling the function.
    .    * @param distCoeffs Output vector of distortion coefficients
    .    * \f$(k_1, k_2, p_1, p_2[, k_3[, k_4, k_5, k_6],[s_1, s_2, s_3, s_4]])\f$ of 4, 5, 8 or 12 elements
    .    * @param rvecs Output vector of rotation vectors (see Rodrigues ) estimated for each board view
    .    * (e.g. std::vector<cv::Mat>>). That is, each k-th rotation vector together with the corresponding
    .    * k-th translation vector (see the next output parameter description) brings the board pattern
    .    * from the model coordinate space (in which object points are specified) to the world coordinate
    .    * space, that is, a real position of the board pattern in the k-th pattern view (k=0.. *M* -1).
    .    * @param tvecs Output vector of translation vectors estimated for each pattern view.
    .    * @param stdDeviationsIntrinsics Output vector of standard deviations estimated for intrinsic parameters.
    .    * Order of deviations values:
    .    * \f$(f_x, f_y, c_x, c_y, k_1, k_2, p_1, p_2, k_3, k_4, k_5, k_6 , s_1, s_2, s_3,
    .    * s_4, \tau_x, \tau_y)\f$ If one of parameters is not estimated, it's deviation is equals to zero.
    .    * @param stdDeviationsExtrinsics Output vector of standard deviations estimated for extrinsic parameters.
    .    * Order of deviations values: \f$(R_1, T_1, \dotsc , R_M, T_M)\f$ where M is number of pattern views,
    .    * \f$R_i, T_i\f$ are concatenated 1x3 vectors.
    .    * @param perViewErrors Output vector of average re-projection errors estimated for each pattern view.
    .    * @param flags flags Different flags  for the calibration process (see #calibrateCamera for details).
    .    * @param criteria Termination criteria for the iterative optimization algorithm.
    .    *
    .    * This function calibrates a camera using a set of corners of a  Charuco Board. The function
    .    * receives a list of detected corners and its identifiers from several views of the Board.
    .    * The function returns the final re-projection error.
    """
    pass

def CharucoBoard_create(squaresX, squaresY, squareLength, markerLength, dictionary): # real signature unknown; restored from __doc__
    """
    CharucoBoard_create(squaresX, squaresY, squareLength, markerLength, dictionary) -> retval
    .   * @brief Create a CharucoBoard object
    .        *
    .        * @param squaresX number of chessboard squares in X direction
    .        * @param squaresY number of chessboard squares in Y direction
    .        * @param squareLength chessboard square side length (normally in meters)
    .        * @param markerLength marker side length (same unit than squareLength)
    .        * @param dictionary dictionary of markers indicating the type of markers.
    .        * The first markers in the dictionary are used to fill the white chessboard squares.
    .        * @return the output CharucoBoard object
    .        *
    .        * This functions creates a CharucoBoard object given the number of squares in each direction
    .        * and the size of the markers and chessboard squares.
    """
    pass

def custom_dictionary(nMarkers, markerSize, randomSeed=None): # real signature unknown; restored from __doc__
    """
    custom_dictionary(nMarkers, markerSize[, randomSeed]) -> retval
    .   * @see generateCustomDictionary
    """
    pass

def custom_dictionary_from(nMarkers, markerSize, baseDictionary, randomSeed=None): # real signature unknown; restored from __doc__
    """
    custom_dictionary_from(nMarkers, markerSize, baseDictionary[, randomSeed]) -> retval
    .   * @brief Generates a new customizable marker dictionary
    .     *
    .     * @param nMarkers number of markers in the dictionary
    .     * @param markerSize number of bits per dimension of each markers
    .     * @param baseDictionary Include the markers in this dictionary at the beginning (optional)
    .     * @param randomSeed a user supplied seed for theRNG()
    .     *
    .     * This function creates a new dictionary composed by nMarkers markers and each markers composed
    .     * by markerSize x markerSize bits. If baseDictionary is provided, its markers are directly
    .     * included and the rest are generated based on them. If the size of baseDictionary is higher
    .     * than nMarkers, only the first nMarkers in baseDictionary are taken and no new marker is added.
    """
    pass

def detectCharucoDiamond(image, markerCorners, markerIds, squareMarkerLengthRate, diamondCorners=None, diamondIds=None, cameraMatrix=None, distCoeffs=None): # real signature unknown; restored from __doc__
    """
    detectCharucoDiamond(image, markerCorners, markerIds, squareMarkerLengthRate[, diamondCorners[, diamondIds[, cameraMatrix[, distCoeffs]]]]) -> diamondCorners, diamondIds
    .   * @brief Detect ChArUco Diamond markers
    .    *
    .    * @param image input image necessary for corner subpixel.
    .    * @param markerCorners list of detected marker corners from detectMarkers function.
    .    * @param markerIds list of marker ids in markerCorners.
    .    * @param squareMarkerLengthRate rate between square and marker length:
    .    * squareMarkerLengthRate = squareLength/markerLength. The real units are not necessary.
    .    * @param diamondCorners output list of detected diamond corners (4 corners per diamond). The order
    .    * is the same than in marker corners: top left, top right, bottom right and bottom left. Similar
    .    * format than the corners returned by detectMarkers (e.g std::vector<std::vector<cv::Point2f> > ).
    .    * @param diamondIds ids of the diamonds in diamondCorners. The id of each diamond is in fact of
    .    * type Vec4i, so each diamond has 4 ids, which are the ids of the aruco markers composing the
    .    * diamond.
    .    * @param cameraMatrix Optional camera calibration matrix.
    .    * @param distCoeffs Optional camera distortion coefficients.
    .    *
    .    * This function detects Diamond markers from the previous detected ArUco markers. The diamonds
    .    * are returned in the diamondCorners and diamondIds parameters. If camera calibration parameters
    .    * are provided, the diamond search is based on reprojection. If not, diamond search is based on
    .    * homography. Homography is faster than reprojection but can slightly reduce the detection rate.
    """
    pass

def detectMarkers(image, dictionary, corners=None, ids=None, parameters=None, rejectedImgPoints=None, cameraMatrix=None, distCoeff=None): # real signature unknown; restored from __doc__
    """
    detectMarkers(image, dictionary[, corners[, ids[, parameters[, rejectedImgPoints[, cameraMatrix[, distCoeff]]]]]]) -> corners, ids, rejectedImgPoints
    .   * @brief Basic marker detection
    .    *
    .    * @param image input image
    .    * @param dictionary indicates the type of markers that will be searched
    .    * @param corners vector of detected marker corners. For each marker, its four corners
    .    * are provided, (e.g std::vector<std::vector<cv::Point2f> > ). For N detected markers,
    .    * the dimensions of this array is Nx4. The order of the corners is clockwise.
    .    * @param ids vector of identifiers of the detected markers. The identifier is of type int
    .    * (e.g. std::vector<int>). For N detected markers, the size of ids is also N.
    .    * The identifiers have the same order than the markers in the imgPoints array.
    .    * @param parameters marker detection parameters
    .    * @param rejectedImgPoints contains the imgPoints of those squares whose inner code has not a
    .    * correct codification. Useful for debugging purposes.
    .    * @param cameraMatrix optional input 3x3 floating-point camera matrix
    .    * \f$A = \vecthreethree{f_x}{0}{c_x}{0}{f_y}{c_y}{0}{0}{1}\f$
    .    * @param distCoeff optional vector of distortion coefficients
    .    * \f$(k_1, k_2, p_1, p_2[, k_3[, k_4, k_5, k_6],[s_1, s_2, s_3, s_4]])\f$ of 4, 5, 8 or 12 elements
    .    *
    .    * Performs marker detection in the input image. Only markers included in the specific dictionary
    .    * are searched. For each detected marker, it returns the 2D position of its corner in the image
    .    * and its corresponding identifier.
    .    * Note that this function does not perform pose estimation.
    .    * @sa estimatePoseSingleMarkers,  estimatePoseBoard
    .    *
    """
    pass

def DetectorParameters_create(): # real signature unknown; restored from __doc__
    """
    DetectorParameters_create() -> retval
    .
    """
    pass

def Dictionary_create(nMarkers, markerSize, randomSeed=None): # real signature unknown; restored from __doc__
    """
    Dictionary_create(nMarkers, markerSize[, randomSeed]) -> retval
    .   * @see generateCustomDictionary
    """
    pass

def Dictionary_create_from(nMarkers, markerSize, baseDictionary, randomSeed=None): # real signature unknown; restored from __doc__
    """
    Dictionary_create_from(nMarkers, markerSize, baseDictionary[, randomSeed]) -> retval
    .   * @see generateCustomDictionary
    """
    pass

def Dictionary_get(dict): # real signature unknown; restored from __doc__
    """
    Dictionary_get(dict) -> retval
    .   * @see getPredefinedDictionary
    """
    pass

def Dictionary_getBitsFromByteList(byteList, markerSize): # real signature unknown; restored from __doc__
    """
    Dictionary_getBitsFromByteList(byteList, markerSize) -> retval
    .   * @brief Transform list of bytes to matrix of bits
    """
    pass

def Dictionary_getByteListFromBits(bits): # real signature unknown; restored from __doc__
    """
    Dictionary_getByteListFromBits(bits) -> retval
    .   * @brief Transform matrix of bits to list of bytes in the 4 rotations
    """
    pass

def drawAxis(image, cameraMatrix, distCoeffs, rvec, tvec, length): # real signature unknown; restored from __doc__
    """
    drawAxis(image, cameraMatrix, distCoeffs, rvec, tvec, length) -> image
    .   * @brief Draw coordinate system axis from pose estimation
    .    *
    .    * @param image input/output image. It must have 1 or 3 channels. The number of channels is not
    .    * altered.
    .    * @param cameraMatrix input 3x3 floating-point camera matrix
    .    * \f$A = \vecthreethree{f_x}{0}{c_x}{0}{f_y}{c_y}{0}{0}{1}\f$
    .    * @param distCoeffs vector of distortion coefficients
    .    * \f$(k_1, k_2, p_1, p_2[, k_3[, k_4, k_5, k_6],[s_1, s_2, s_3, s_4]])\f$ of 4, 5, 8 or 12 elements
    .    * @param rvec rotation vector of the coordinate system that will be drawn. (@sa Rodrigues).
    .    * @param tvec translation vector of the coordinate system that will be drawn.
    .    * @param length length of the painted axis in the same unit than tvec (usually in meters)
    .    *
    .    * Given the pose estimation of a marker or board, this function draws the axis of the world
    .    * coordinate system, i.e. the system centered on the marker/board. Useful for debugging purposes.
    .    *
    .    * @deprecated use cv::drawFrameAxes
    """
    pass

def drawDetectedCornersCharuco(image, charucoCorners, charucoIds=None, cornerColor=None): # real signature unknown; restored from __doc__
    """
    drawDetectedCornersCharuco(image, charucoCorners[, charucoIds[, cornerColor]]) -> image
    .   * @brief Draws a set of Charuco corners
    .    * @param image input/output image. It must have 1 or 3 channels. The number of channels is not
    .    * altered.
    .    * @param charucoCorners vector of detected charuco corners
    .    * @param charucoIds list of identifiers for each corner in charucoCorners
    .    * @param cornerColor color of the square surrounding each corner
    .    *
    .    * This function draws a set of detected Charuco corners. If identifiers vector is provided, it also
    .    * draws the id of each corner.
    """
    pass

def drawDetectedDiamonds(image, diamondCorners, diamondIds=None, borderColor=None): # real signature unknown; restored from __doc__
    """
    drawDetectedDiamonds(image, diamondCorners[, diamondIds[, borderColor]]) -> image
    .   * @brief Draw a set of detected ChArUco Diamond markers
    .    *
    .    * @param image input/output image. It must have 1 or 3 channels. The number of channels is not
    .    * altered.
    .    * @param diamondCorners positions of diamond corners in the same format returned by
    .    * detectCharucoDiamond(). (e.g std::vector<std::vector<cv::Point2f> > ). For N detected markers,
    .    * the dimensions of this array should be Nx4. The order of the corners should be clockwise.
    .    * @param diamondIds vector of identifiers for diamonds in diamondCorners, in the same format
    .    * returned by detectCharucoDiamond() (e.g. std::vector<Vec4i>).
    .    * Optional, if not provided, ids are not painted.
    .    * @param borderColor color of marker borders. Rest of colors (text color and first corner color)
    .    * are calculated based on this one.
    .    *
    .    * Given an array of detected diamonds, this functions draws them in the image. The marker borders
    .    * are painted and the markers identifiers if provided.
    .    * Useful for debugging purposes.
    """
    pass

def drawDetectedMarkers(image, corners, ids=None, borderColor=None): # real signature unknown; restored from __doc__
    """
    drawDetectedMarkers(image, corners[, ids[, borderColor]]) -> image
    .   * @brief Draw detected markers in image
    .    *
    .    * @param image input/output image. It must have 1 or 3 channels. The number of channels is not
    .    * altered.
    .    * @param corners positions of marker corners on input image.
    .    * (e.g std::vector<std::vector<cv::Point2f> > ). For N detected markers, the dimensions of
    .    * this array should be Nx4. The order of the corners should be clockwise.
    .    * @param ids vector of identifiers for markers in markersCorners .
    .    * Optional, if not provided, ids are not painted.
    .    * @param borderColor color of marker borders. Rest of colors (text color and first corner color)
    .    * are calculated based on this one to improve visualization.
    .    *
    .    * Given an array of detected marker corners and its corresponding ids, this functions draws
    .    * the markers in the image. The marker borders are painted and the markers identifiers if provided.
    .    * Useful for debugging purposes.
    """
    pass

def drawMarker(dictionary, id, sidePixels, img=None, borderBits=None): # real signature unknown; restored from __doc__
    """
    drawMarker(dictionary, id, sidePixels[, img[, borderBits]]) -> img
    .   * @brief Draw a canonical marker image
    .    *
    .    * @param dictionary dictionary of markers indicating the type of markers
    .    * @param id identifier of the marker that will be returned. It has to be a valid id
    .    * in the specified dictionary.
    .    * @param sidePixels size of the image in pixels
    .    * @param img output image with the marker
    .    * @param borderBits width of the marker border.
    .    *
    .    * This function returns a marker image in its canonical form (i.e. ready to be printed)
    """
    pass

def drawPlanarBoard(board, outSize, img=None, marginSize=None, borderBits=None): # real signature unknown; restored from __doc__
    """
    drawPlanarBoard(board, outSize[, img[, marginSize[, borderBits]]]) -> img
    .   * @brief Draw a planar board
    .    * @sa _drawPlanarBoardImpl
    .    *
    .    * @param board layout of the board that will be drawn. The board should be planar,
    .    * z coordinate is ignored
    .    * @param outSize size of the output image in pixels.
    .    * @param img output image with the board. The size of this image will be outSize
    .    * and the board will be on the center, keeping the board proportions.
    .    * @param marginSize minimum margins (in pixels) of the board in the output image
    .    * @param borderBits width of the marker borders.
    .    *
    .    * This function return the image of a planar board, ready to be printed. It assumes
    .    * the Board layout specified is planar by ignoring the z coordinates of the object points.
    """
    pass

def estimatePoseBoard(corners, ids, board, cameraMatrix, distCoeffs, rvec, tvec, useExtrinsicGuess=None): # real signature unknown; restored from __doc__
    """
    estimatePoseBoard(corners, ids, board, cameraMatrix, distCoeffs, rvec, tvec[, useExtrinsicGuess]) -> retval, rvec, tvec
    .   * @brief Pose estimation for a board of markers
    .    *
    .    * @param corners vector of already detected markers corners. For each marker, its four corners
    .    * are provided, (e.g std::vector<std::vector<cv::Point2f> > ). For N detected markers, the
    .    * dimensions of this array should be Nx4. The order of the corners should be clockwise.
    .    * @param ids list of identifiers for each marker in corners
    .    * @param board layout of markers in the board. The layout is composed by the marker identifiers
    .    * and the positions of each marker corner in the board reference system.
    .    * @param cameraMatrix input 3x3 floating-point camera matrix
    .    * \f$A = \vecthreethree{f_x}{0}{c_x}{0}{f_y}{c_y}{0}{0}{1}\f$
    .    * @param distCoeffs vector of distortion coefficients
    .    * \f$(k_1, k_2, p_1, p_2[, k_3[, k_4, k_5, k_6],[s_1, s_2, s_3, s_4]])\f$ of 4, 5, 8 or 12 elements
    .    * @param rvec Output vector (e.g. cv::Mat) corresponding to the rotation vector of the board
    .    * (see cv::Rodrigues). Used as initial guess if not empty.
    .    * @param tvec Output vector (e.g. cv::Mat) corresponding to the translation vector of the board.
    .    * @param useExtrinsicGuess defines whether initial guess for \b rvec and \b tvec will be used or not.
    .    * Used as initial guess if not empty.
    .    *
    .    * This function receives the detected markers and returns the pose of a marker board composed
    .    * by those markers.
    .    * A Board of marker has a single world coordinate system which is defined by the board layout.
    .    * The returned transformation is the one that transforms points from the board coordinate system
    .    * to the camera coordinate system.
    .    * Input markers that are not included in the board layout are ignored.
    .    * The function returns the number of markers from the input employed for the board pose estimation.
    .    * Note that returning a 0 means the pose has not been estimated.
    """
    pass

def estimatePoseCharucoBoard(charucoCorners, charucoIds, board, cameraMatrix, distCoeffs, rvec, tvec, useExtrinsicGuess=None): # real signature unknown; restored from __doc__
    """
    estimatePoseCharucoBoard(charucoCorners, charucoIds, board, cameraMatrix, distCoeffs, rvec, tvec[, useExtrinsicGuess]) -> retval, rvec, tvec
    .   * @brief Pose estimation for a ChArUco board given some of their corners
    .    * @param charucoCorners vector of detected charuco corners
    .    * @param charucoIds list of identifiers for each corner in charucoCorners
    .    * @param board layout of ChArUco board.
    .    * @param cameraMatrix input 3x3 floating-point camera matrix
    .    * \f$A = \vecthreethree{f_x}{0}{c_x}{0}{f_y}{c_y}{0}{0}{1}\f$
    .    * @param distCoeffs vector of distortion coefficients
    .    * \f$(k_1, k_2, p_1, p_2[, k_3[, k_4, k_5, k_6],[s_1, s_2, s_3, s_4]])\f$ of 4, 5, 8 or 12 elements
    .    * @param rvec Output vector (e.g. cv::Mat) corresponding to the rotation vector of the board
    .    * (see cv::Rodrigues).
    .    * @param tvec Output vector (e.g. cv::Mat) corresponding to the translation vector of the board.
    .    * @param useExtrinsicGuess defines whether initial guess for \b rvec and \b tvec will be used or not.
    .    *
    .    * This function estimates a Charuco board pose from some detected corners.
    .    * The function checks if the input corners are enough and valid to perform pose estimation.
    .    * If pose estimation is valid, returns true, else returns false.
    """
    pass

def estimatePoseSingleMarkers(corners, markerLength, cameraMatrix, distCoeffs, rvecs=None, tvecs=None, _objPoints=None): # real signature unknown; restored from __doc__
    """
    estimatePoseSingleMarkers(corners, markerLength, cameraMatrix, distCoeffs[, rvecs[, tvecs[, _objPoints]]]) -> rvecs, tvecs, _objPoints
    .   * @brief Pose estimation for single markers
    .    *
    .    * @param corners vector of already detected markers corners. For each marker, its four corners
    .    * are provided, (e.g std::vector<std::vector<cv::Point2f> > ). For N detected markers,
    .    * the dimensions of this array should be Nx4. The order of the corners should be clockwise.
    .    * @sa detectMarkers
    .    * @param markerLength the length of the markers' side. The returning translation vectors will
    .    * be in the same unit. Normally, unit is meters.
    .    * @param cameraMatrix input 3x3 floating-point camera matrix
    .    * \f$A = \vecthreethree{f_x}{0}{c_x}{0}{f_y}{c_y}{0}{0}{1}\f$
    .    * @param distCoeffs vector of distortion coefficients
    .    * \f$(k_1, k_2, p_1, p_2[, k_3[, k_4, k_5, k_6],[s_1, s_2, s_3, s_4]])\f$ of 4, 5, 8 or 12 elements
    .    * @param rvecs array of output rotation vectors (@sa Rodrigues) (e.g. std::vector<cv::Vec3d>).
    .    * Each element in rvecs corresponds to the specific marker in imgPoints.
    .    * @param tvecs array of output translation vectors (e.g. std::vector<cv::Vec3d>).
    .    * Each element in tvecs corresponds to the specific marker in imgPoints.
    .    * @param _objPoints array of object points of all the marker corners
    .    *
    .    * This function receives the detected markers and returns their pose estimation respect to
    .    * the camera individually. So for each marker, one rotation and translation vector is returned.
    .    * The returned transformation is the one that transforms points from each marker coordinate system
    .    * to the camera coordinate system.
    .    * The marker corrdinate system is centered on the middle of the marker, with the Z axis
    .    * perpendicular to the marker plane.
    .    * The coordinates of the four corners of the marker in its own coordinate system are:
    .    * (-markerLength/2, markerLength/2, 0), (markerLength/2, markerLength/2, 0),
    .    * (markerLength/2, -markerLength/2, 0), (-markerLength/2, -markerLength/2, 0)
    """
    pass

def getBoardObjectAndImagePoints(board, detectedCorners, detectedIds, objPoints=None, imgPoints=None): # real signature unknown; restored from __doc__
    """
    getBoardObjectAndImagePoints(board, detectedCorners, detectedIds[, objPoints[, imgPoints]]) -> objPoints, imgPoints
    .   * @brief Given a board configuration and a set of detected markers, returns the corresponding
    .    * image points and object points to call solvePnP
    .    *
    .    * @param board Marker board layout.
    .    * @param detectedCorners List of detected marker corners of the board.
    .    * @param detectedIds List of identifiers for each marker.
    .    * @param objPoints Vector of vectors of board marker points in the board coordinate space.
    .    * @param imgPoints Vector of vectors of the projections of board marker corner points.
    """
    pass

def getPredefinedDictionary(dict): # real signature unknown; restored from __doc__
    """
    getPredefinedDictionary(dict) -> retval
    .   * @brief Returns one of the predefined dictionaries referenced by DICT_*.
    """
    pass

def GridBoard_create(markersX, markersY, markerLength, markerSeparation, dictionary, firstMarker=None): # real signature unknown; restored from __doc__
    """
    GridBoard_create(markersX, markersY, markerLength, markerSeparation, dictionary[, firstMarker]) -> retval
    .   * @brief Create a GridBoard object
    .        *
    .        * @param markersX number of markers in X direction
    .        * @param markersY number of markers in Y direction
    .        * @param markerLength marker side length (normally in meters)
    .        * @param markerSeparation separation between two markers (same unit as markerLength)
    .        * @param dictionary dictionary of markers indicating the type of markers
    .        * @param firstMarker id of first marker in dictionary to use on board.
    .        * @return the output GridBoard object
    .        *
    .        * This functions creates a GridBoard object given the number of markers in each direction and
    .        * the marker size and marker separation.
    """
    pass

def interpolateCornersCharuco(markerCorners, markerIds, image, board, charucoCorners=None, charucoIds=None, cameraMatrix=None, distCoeffs=None, minMarkers=None): # real signature unknown; restored from __doc__
    """
    interpolateCornersCharuco(markerCorners, markerIds, image, board[, charucoCorners[, charucoIds[, cameraMatrix[, distCoeffs[, minMarkers]]]]]) -> retval, charucoCorners, charucoIds
    .   * @brief Interpolate position of ChArUco board corners
    .    * @param markerCorners vector of already detected markers corners. For each marker, its four
    .    * corners are provided, (e.g std::vector<std::vector<cv::Point2f> > ). For N detected markers, the
    .    * dimensions of this array should be Nx4. The order of the corners should be clockwise.
    .    * @param markerIds list of identifiers for each marker in corners
    .    * @param image input image necesary for corner refinement. Note that markers are not detected and
    .    * should be sent in corners and ids parameters.
    .    * @param board layout of ChArUco board.
    .    * @param charucoCorners interpolated chessboard corners
    .    * @param charucoIds interpolated chessboard corners identifiers
    .    * @param cameraMatrix optional 3x3 floating-point camera matrix
    .    * \f$A = \vecthreethree{f_x}{0}{c_x}{0}{f_y}{c_y}{0}{0}{1}\f$
    .    * @param distCoeffs optional vector of distortion coefficients
    .    * \f$(k_1, k_2, p_1, p_2[, k_3[, k_4, k_5, k_6],[s_1, s_2, s_3, s_4]])\f$ of 4, 5, 8 or 12 elements
    .    * @param minMarkers number of adjacent markers that must be detected to return a charuco corner
    .    *
    .    * This function receives the detected markers and returns the 2D position of the chessboard corners
    .    * from a ChArUco board using the detected Aruco markers. If camera parameters are provided,
    .    * the process is based in an approximated pose estimation, else it is based on local homography.
    .    * Only visible corners are returned. For each corner, its corresponding identifier is
    .    * also returned in charucoIds.
    .    * The function returns the number of interpolated corners.
    """
    pass

def refineDetectedMarkers(image, board, detectedCorners, detectedIds, rejectedCorners, cameraMatrix=None, distCoeffs=None, minRepDistance=None, errorCorrectionRate=None, checkAllOrders=None, recoveredIdxs=None, parameters=None): # real signature unknown; restored from __doc__
    """
    refineDetectedMarkers(image, board, detectedCorners, detectedIds, rejectedCorners[, cameraMatrix[, distCoeffs[, minRepDistance[, errorCorrectionRate[, checkAllOrders[, recoveredIdxs[, parameters]]]]]]]) -> detectedCorners, detectedIds, rejectedCorners, recoveredIdxs
    .   * @brief Refind not detected markers based on the already detected and the board layout
    .    *
    .    * @param image input image
    .    * @param board layout of markers in the board.
    .    * @param detectedCorners vector of already detected marker corners.
    .    * @param detectedIds vector of already detected marker identifiers.
    .    * @param rejectedCorners vector of rejected candidates during the marker detection process.
    .    * @param cameraMatrix optional input 3x3 floating-point camera matrix
    .    * \f$A = \vecthreethree{f_x}{0}{c_x}{0}{f_y}{c_y}{0}{0}{1}\f$
    .    * @param distCoeffs optional vector of distortion coefficients
    .    * \f$(k_1, k_2, p_1, p_2[, k_3[, k_4, k_5, k_6],[s_1, s_2, s_3, s_4]])\f$ of 4, 5, 8 or 12 elements
    .    * @param minRepDistance minimum distance between the corners of the rejected candidate and the
    .    * reprojected marker in order to consider it as a correspondence.
    .    * @param errorCorrectionRate rate of allowed erroneous bits respect to the error correction
    .    * capability of the used dictionary. -1 ignores the error correction step.
    .    * @param checkAllOrders Consider the four posible corner orders in the rejectedCorners array.
    .    * If it set to false, only the provided corner order is considered (default true).
    .    * @param recoveredIdxs Optional array to returns the indexes of the recovered candidates in the
    .    * original rejectedCorners array.
    .    * @param parameters marker detection parameters
    .    *
    .    * This function tries to find markers that were not detected in the basic detecMarkers function.
    .    * First, based on the current detected marker and the board layout, the function interpolates
    .    * the position of the missing markers. Then it tries to find correspondence between the reprojected
    .    * markers and the rejected candidates based on the minRepDistance and errorCorrectionRate
    .    * parameters.
    .    * If camera parameters and distortion coefficients are provided, missing markers are reprojected
    .    * using projectPoint function. If not, missing marker projections are interpolated using global
    .    * homography, and all the marker corners in the board must have the same Z coordinate.
    """
    pass

# no classes
