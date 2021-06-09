# encoding: utf-8
# module cv2.omnidir
# from C:\Users\Doly\Anaconda3\lib\site-packages\cv2\cv2.cp37-win_amd64.pyd
# by generator 1.147
# no doc
# no imports

# Variables with simple values

CALIB_FIX_CENTER = 256
CALIB_FIX_GAMMA = 128
CALIB_FIX_K1 = 4
CALIB_FIX_K2 = 8
CALIB_FIX_P1 = 16
CALIB_FIX_P2 = 32
CALIB_FIX_SKEW = 2
CALIB_FIX_XI = 64

CALIB_USE_GUESS = 1

RECTIFY_CYLINDRICAL = 2
RECTIFY_LONGLATI = 3
RECTIFY_PERSPECTIVE = 1
RECTIFY_STEREOGRAPHIC = 4

XYZ = 2
XYZRGB = 1

__loader__ = None

__spec__ = None

# functions

def calibrate(objectPoints, imagePoints, size, K, xi, D, flags, criteria, rvecs=None, tvecs=None, idx=None): # real signature unknown; restored from __doc__
    """
    calibrate(objectPoints, imagePoints, size, K, xi, D, flags, criteria[, rvecs[, tvecs[, idx]]]) -> retval, K, xi, D, rvecs, tvecs, idx
    .   @brief Perform omnidirectional camera calibration, the default depth of outputs is CV_64F.
    .   
    .       @param objectPoints Vector of vector of Vec3f object points in world (pattern) coordinate.
    .       It also can be vector of Mat with size 1xN/Nx1 and type CV_32FC3. Data with depth of 64_F is also acceptable.
    .       @param imagePoints Vector of vector of Vec2f corresponding image points of objectPoints. It must be the same
    .       size and the same type with objectPoints.
    .       @param size Image size of calibration images.
    .       @param K Output calibrated camera matrix.
    .       @param xi Output parameter xi for CMei's model
    .       @param D Output distortion parameters \f$(k_1, k_2, p_1, p_2)\f$
    .       @param rvecs Output rotations for each calibration images
    .       @param tvecs Output translation for each calibration images
    .       @param flags The flags that control calibrate
    .       @param criteria Termination criteria for optimization
    .       @param idx Indices of images that pass initialization, which are really used in calibration. So the size of rvecs is the
    .       same as idx.total().
    """
    pass

def initUndistortRectifyMap(K, D, xi, R, P, size, mltype, flags, map1=None, map2=None): # real signature unknown; restored from __doc__
    """
    initUndistortRectifyMap(K, D, xi, R, P, size, mltype, flags[, map1[, map2]]) -> map1, map2
    .   @brief Computes undistortion and rectification maps for omnidirectional camera image transform by a rotation R.
    .       It output two maps that are used for cv::remap(). If D is empty then zero distortion is used,
    .       if R or P is empty then identity matrices are used.
    .   
    .       @param K Camera matrix \f$K = \vecthreethree{f_x}{s}{c_x}{0}{f_y}{c_y}{0}{0}{_1}\f$, with depth CV_32F or CV_64F
    .       @param D Input vector of distortion coefficients \f$(k_1, k_2, p_1, p_2)\f$, with depth CV_32F or CV_64F
    .       @param xi The parameter xi for CMei's model
    .       @param R Rotation transform between the original and object space : 3x3 1-channel, or vector: 3x1/1x3, with depth CV_32F or CV_64F
    .       @param P New camera matrix (3x3) or new projection matrix (3x4)
    .       @param size Undistorted image size.
    .       @param mltype Type of the first output map that can be CV_32FC1 or CV_16SC2 . See convertMaps()
    .       for details.
    .       @param map1 The first output map.
    .       @param map2 The second output map.
    .       @param flags Flags indicates the rectification type,  RECTIFY_PERSPECTIVE, RECTIFY_CYLINDRICAL, RECTIFY_LONGLATI and RECTIFY_STEREOGRAPHIC
    .       are supported.
    """
    pass

def projectPoints(objectPoints, rvec, tvec, K, xi, D, imagePoints=None, jacobian=None): # real signature unknown; restored from __doc__
    """
    projectPoints(objectPoints, rvec, tvec, K, xi, D[, imagePoints[, jacobian]]) -> imagePoints, jacobian
    .   @brief Projects points for omnidirectional camera using CMei's model
    .   
    .       @param objectPoints Object points in world coordinate, vector of vector of Vec3f or Mat of
    .       1xN/Nx1 3-channel of type CV_32F and N is the number of points. 64F is also acceptable.
    .       @param imagePoints Output array of image points, vector of vector of Vec2f or
    .       1xN/Nx1 2-channel of type CV_32F. 64F is also acceptable.
    .       @param rvec vector of rotation between world coordinate and camera coordinate, i.e., om
    .       @param tvec vector of translation between pattern coordinate and camera coordinate
    .       @param K Camera matrix \f$K = \vecthreethree{f_x}{s}{c_x}{0}{f_y}{c_y}{0}{0}{_1}\f$.
    .       @param D Input vector of distortion coefficients \f$(k_1, k_2, p_1, p_2)\f$.
    .       @param xi The parameter xi for CMei's model
    .       @param jacobian Optional output 2Nx16 of type CV_64F jacobian matrix, contains the derivatives of
    .       image pixel points wrt parameters including \f$om, T, f_x, f_y, s, c_x, c_y, xi, k_1, k_2, p_1, p_2\f$.
    .       This matrix will be used in calibration by optimization.
    .   
    .       The function projects object 3D points of world coordinate to image pixels, parameter by intrinsic
    .       and extrinsic parameters. Also, it optionally compute a by-product: the jacobian matrix containing
    .       contains the derivatives of image pixel points wrt intrinsic and extrinsic parameters.
    """
    pass

def stereoCalibrate(objectPoints, imagePoints1, imagePoints2, imageSize1, imageSize2, K1, xi1, D1, K2, xi2, D2, flags, criteria, rvec=None, tvec=None, rvecsL=None, tvecsL=None, idx=None): # real signature unknown; restored from __doc__
    """
    stereoCalibrate(objectPoints, imagePoints1, imagePoints2, imageSize1, imageSize2, K1, xi1, D1, K2, xi2, D2, flags, criteria[, rvec[, tvec[, rvecsL[, tvecsL[, idx]]]]]) -> retval, objectPoints, imagePoints1, imagePoints2, K1, xi1, D1, K2, xi2, D2, rvec, tvec, rvecsL, tvecsL, idx
    .   @brief Stereo calibration for omnidirectional camera model. It computes the intrinsic parameters for two
    .       cameras and the extrinsic parameters between two cameras. The default depth of outputs is CV_64F.
    .   
    .       @param objectPoints Object points in world (pattern) coordinate. Its type is vector<vector<Vec3f> >.
    .       It also can be vector of Mat with size 1xN/Nx1 and type CV_32FC3. Data with depth of 64_F is also acceptable.
    .       @param imagePoints1 The corresponding image points of the first camera, with type vector<vector<Vec2f> >.
    .       It must be the same size and the same type as objectPoints.
    .       @param imagePoints2 The corresponding image points of the second camera, with type vector<vector<Vec2f> >.
    .       It must be the same size and the same type as objectPoints.
    .       @param imageSize1 Image size of calibration images of the first camera.
    .       @param imageSize2 Image size of calibration images of the second camera.
    .       @param K1 Output camera matrix for the first camera.
    .       @param xi1 Output parameter xi of Mei's model for the first camera
    .       @param D1 Output distortion parameters \f$(k_1, k_2, p_1, p_2)\f$ for the first camera
    .       @param K2 Output camera matrix for the first camera.
    .       @param xi2 Output parameter xi of CMei's model for the second camera
    .       @param D2 Output distortion parameters \f$(k_1, k_2, p_1, p_2)\f$ for the second camera
    .       @param rvec Output rotation between the first and second camera
    .       @param tvec Output translation between the first and second camera
    .       @param rvecsL Output rotation for each image of the first camera
    .       @param tvecsL Output translation for each image of the first camera
    .       @param flags The flags that control stereoCalibrate
    .       @param criteria Termination criteria for optimization
    .       @param idx Indices of image pairs that pass initialization, which are really used in calibration. So the size of rvecs is the
    .       same as idx.total().
    .       @
    """
    pass

def stereoReconstruct(image1, image2, K1, D1, xi1, K2, D2, xi2, R, T, flag, numDisparities, SADWindowSize, disparity=None, image1Rec=None, image2Rec=None, newSize=None, Knew=None, pointCloud=None, pointType=None): # real signature unknown; restored from __doc__
    """
    stereoReconstruct(image1, image2, K1, D1, xi1, K2, D2, xi2, R, T, flag, numDisparities, SADWindowSize[, disparity[, image1Rec[, image2Rec[, newSize[, Knew[, pointCloud[, pointType]]]]]]]) -> disparity, image1Rec, image2Rec, pointCloud
    .   @brief Stereo 3D reconstruction from a pair of images
    .   
    .       @param image1 The first input image
    .       @param image2 The second input image
    .       @param K1 Input camera matrix of the first camera
    .       @param D1 Input distortion parameters \f$(k_1, k_2, p_1, p_2)\f$ for the first camera
    .       @param xi1 Input parameter xi for the first camera for CMei's model
    .       @param K2 Input camera matrix of the second camera
    .       @param D2 Input distortion parameters \f$(k_1, k_2, p_1, p_2)\f$ for the second camera
    .       @param xi2 Input parameter xi for the second camera for CMei's model
    .       @param R Rotation between the first and second camera
    .       @param T Translation between the first and second camera
    .       @param flag Flag of rectification type, RECTIFY_PERSPECTIVE or RECTIFY_LONGLATI
    .       @param numDisparities The parameter 'numDisparities' in StereoSGBM, see StereoSGBM for details.
    .       @param SADWindowSize The parameter 'SADWindowSize' in StereoSGBM, see StereoSGBM for details.
    .       @param disparity Disparity map generated by stereo matching
    .       @param image1Rec Rectified image of the first image
    .       @param image2Rec rectified image of the second image
    .       @param newSize Image size of rectified image, see omnidir::undistortImage
    .       @param Knew New camera matrix of rectified image, see omnidir::undistortImage
    .       @param pointCloud Point cloud of 3D reconstruction, with type CV_64FC3
    .       @param pointType Point cloud type, it can be XYZRGB or XYZ
    """
    pass

def stereoRectify(R, T, R1=None, R2=None): # real signature unknown; restored from __doc__
    """
    stereoRectify(R, T[, R1[, R2]]) -> R1, R2
    .   @brief Stereo rectification for omnidirectional camera model. It computes the rectification rotations for two cameras
    .   
    .       @param R Rotation between the first and second camera
    .       @param T Translation between the first and second camera
    .       @param R1 Output 3x3 rotation matrix for the first camera
    .       @param R2 Output 3x3 rotation matrix for the second camera
    """
    pass

def undistortImage(distorted, K, D, xi, flags, undistorted=None, Knew=None, new_size=None, R=None): # real signature unknown; restored from __doc__
    """
    undistortImage(distorted, K, D, xi, flags[, undistorted[, Knew[, new_size[, R]]]]) -> undistorted
    .   @brief Undistort omnidirectional images to perspective images
    .   
    .       @param distorted The input omnidirectional image.
    .       @param undistorted The output undistorted image.
    .       @param K Camera matrix \f$K = \vecthreethree{f_x}{s}{c_x}{0}{f_y}{c_y}{0}{0}{_1}\f$.
    .       @param D Input vector of distortion coefficients \f$(k_1, k_2, p_1, p_2)\f$.
    .       @param xi The parameter xi for CMei's model.
    .       @param flags Flags indicates the rectification type,  RECTIFY_PERSPECTIVE, RECTIFY_CYLINDRICAL, RECTIFY_LONGLATI and RECTIFY_STEREOGRAPHIC
    .       @param Knew Camera matrix of the distorted image. If it is not assigned, it is just K.
    .       @param new_size The new image size. By default, it is the size of distorted.
    .       @param R Rotation matrix between the input and output images. By default, it is identity matrix.
    """
    pass

def undistortPoints(distorted, K, D, xi, R, undistorted=None): # real signature unknown; restored from __doc__
    """
    undistortPoints(distorted, K, D, xi, R[, undistorted]) -> undistorted
    .   @brief Undistort 2D image points for omnidirectional camera using CMei's model
    .   
    .       @param distorted Array of distorted image points, vector of Vec2f
    .       or 1xN/Nx1 2-channel Mat of type CV_32F, 64F depth is also acceptable
    .       @param K Camera matrix \f$K = \vecthreethree{f_x}{s}{c_x}{0}{f_y}{c_y}{0}{0}{_1}\f$.
    .       @param D Distortion coefficients \f$(k_1, k_2, p_1, p_2)\f$.
    .       @param xi The parameter xi for CMei's model
    .       @param R Rotation trainsform between the original and object space : 3x3 1-channel, or vector: 3x1/1x3
    .       1-channel or 1x1 3-channel
    .       @param undistorted array of normalized object points, vector of Vec2f/Vec2d or 1xN/Nx1 2-channel Mat with the same
    .       depth of distorted points.
    """
    pass

# no classes
