# encoding: utf-8
# module cv2.fisheye
# from C:\Users\Doly\Anaconda3\lib\site-packages\cv2\cv2.cp37-win_amd64.pyd
# by generator 1.147
# no doc
# no imports

# Variables with simple values

CALIB_CHECK_COND = 4

CALIB_FIX_INTRINSIC = 256
CALIB_FIX_K1 = 16
CALIB_FIX_K2 = 32
CALIB_FIX_K3 = 64
CALIB_FIX_K4 = 128

CALIB_FIX_PRINCIPAL_POINT = 512

CALIB_FIX_SKEW = 8

CALIB_RECOMPUTE_EXTRINSIC = 2

CALIB_USE_INTRINSIC_GUESS = 1

__loader__ = None

__spec__ = None

# functions

def calibrate(objectPoints, imagePoints, image_size, K, D, rvecs=None, tvecs=None, flags=None, criteria=None): # real signature unknown; restored from __doc__
    """
    calibrate(objectPoints, imagePoints, image_size, K, D[, rvecs[, tvecs[, flags[, criteria]]]]) -> retval, K, D, rvecs, tvecs
    .   @brief Performs camera calibaration
    .   
    .       @param objectPoints vector of vectors of calibration pattern points in the calibration pattern
    .       coordinate space.
    .       @param imagePoints vector of vectors of the projections of calibration pattern points.
    .       imagePoints.size() and objectPoints.size() and imagePoints[i].size() must be equal to
    .       objectPoints[i].size() for each i.
    .       @param image_size Size of the image used only to initialize the intrinsic camera matrix.
    .       @param K Output 3x3 floating-point camera matrix
    .       \f$A = \vecthreethree{f_x}{0}{c_x}{0}{f_y}{c_y}{0}{0}{1}\f$ . If
    .       fisheye::CALIB_USE_INTRINSIC_GUESS/ is specified, some or all of fx, fy, cx, cy must be
    .       initialized before calling the function.
    .       @param D Output vector of distortion coefficients \f$(k_1, k_2, k_3, k_4)\f$.
    .       @param rvecs Output vector of rotation vectors (see Rodrigues ) estimated for each pattern view.
    .       That is, each k-th rotation vector together with the corresponding k-th translation vector (see
    .       the next output parameter description) brings the calibration pattern from the model coordinate
    .       space (in which object points are specified) to the world coordinate space, that is, a real
    .       position of the calibration pattern in the k-th pattern view (k=0.. *M* -1).
    .       @param tvecs Output vector of translation vectors estimated for each pattern view.
    .       @param flags Different flags that may be zero or a combination of the following values:
    .       -   **fisheye::CALIB_USE_INTRINSIC_GUESS** cameraMatrix contains valid initial values of
    .       fx, fy, cx, cy that are optimized further. Otherwise, (cx, cy) is initially set to the image
    .       center ( imageSize is used), and focal distances are computed in a least-squares fashion.
    .       -   **fisheye::CALIB_RECOMPUTE_EXTRINSIC** Extrinsic will be recomputed after each iteration
    .       of intrinsic optimization.
    .       -   **fisheye::CALIB_CHECK_COND** The functions will check validity of condition number.
    .       -   **fisheye::CALIB_FIX_SKEW** Skew coefficient (alpha) is set to zero and stay zero.
    .       -   **fisheye::CALIB_FIX_K1..fisheye::CALIB_FIX_K4** Selected distortion coefficients
    .       are set to zeros and stay zero.
    .       -   **fisheye::CALIB_FIX_PRINCIPAL_POINT** The principal point is not changed during the global
    .   optimization. It stays at the center or at a different location specified when CALIB_USE_INTRINSIC_GUESS is set too.
    .       @param criteria Termination criteria for the iterative optimization algorithm.
    """
    pass

def distortPoints(undistorted, K, D, distorted=None, alpha=None): # real signature unknown; restored from __doc__
    """
    distortPoints(undistorted, K, D[, distorted[, alpha]]) -> distorted
    .   @brief Distorts 2D points using fisheye model.
    .   
    .       @param undistorted Array of object points, 1xN/Nx1 2-channel (or vector\<Point2f\> ), where N is
    .       the number of points in the view.
    .       @param K Camera matrix \f$K = \vecthreethree{f_x}{0}{c_x}{0}{f_y}{c_y}{0}{0}{_1}\f$.
    .       @param D Input vector of distortion coefficients \f$(k_1, k_2, k_3, k_4)\f$.
    .       @param alpha The skew coefficient.
    .       @param distorted Output array of image points, 1xN/Nx1 2-channel, or vector\<Point2f\> .
    .   
    .       Note that the function assumes the camera matrix of the undistorted points to be identity.
    .       This means if you want to transform back points undistorted with undistortPoints() you have to
    .       multiply them with \f$P^{-1}\f$.
    """
    pass

def estimateNewCameraMatrixForUndistortRectify(K, D, image_size, R, P=None, balance=None, new_size=None, fov_scale=None): # real signature unknown; restored from __doc__
    """
    estimateNewCameraMatrixForUndistortRectify(K, D, image_size, R[, P[, balance[, new_size[, fov_scale]]]]) -> P
    .   @brief Estimates new camera matrix for undistortion or rectification.
    .   
    .       @param K Camera matrix \f$K = \vecthreethree{f_x}{0}{c_x}{0}{f_y}{c_y}{0}{0}{_1}\f$.
    .       @param image_size Size of the image
    .       @param D Input vector of distortion coefficients \f$(k_1, k_2, k_3, k_4)\f$.
    .       @param R Rectification transformation in the object space: 3x3 1-channel, or vector: 3x1/1x3
    .       1-channel or 1x1 3-channel
    .       @param P New camera matrix (3x3) or new projection matrix (3x4)
    .       @param balance Sets the new focal length in range between the min focal length and the max focal
    .       length. Balance is in range of [0, 1].
    .       @param new_size the new size
    .       @param fov_scale Divisor for new focal length.
    """
    pass

def initUndistortRectifyMap(K, D, R, P, size, m1type, map1=None, map2=None): # real signature unknown; restored from __doc__
    """
    initUndistortRectifyMap(K, D, R, P, size, m1type[, map1[, map2]]) -> map1, map2
    .   @brief Computes undistortion and rectification maps for image transform by cv::remap(). If D is empty zero
    .       distortion is used, if R or P is empty identity matrixes are used.
    .   
    .       @param K Camera matrix \f$K = \vecthreethree{f_x}{0}{c_x}{0}{f_y}{c_y}{0}{0}{_1}\f$.
    .       @param D Input vector of distortion coefficients \f$(k_1, k_2, k_3, k_4)\f$.
    .       @param R Rectification transformation in the object space: 3x3 1-channel, or vector: 3x1/1x3
    .       1-channel or 1x1 3-channel
    .       @param P New camera matrix (3x3) or new projection matrix (3x4)
    .       @param size Undistorted image size.
    .       @param m1type Type of the first output map that can be CV_32FC1 or CV_16SC2 . See convertMaps()
    .       for details.
    .       @param map1 The first output map.
    .       @param map2 The second output map.
    """
    pass

def projectPoints(objectPoints, rvec, tvec, K, D, imagePoints=None, alpha=None, jacobian=None): # real signature unknown; restored from __doc__
    """
    projectPoints(objectPoints, rvec, tvec, K, D[, imagePoints[, alpha[, jacobian]]]) -> imagePoints, jacobian
    .   @overload
    """
    pass

def stereoCalibrate(objectPoints, imagePoints1, imagePoints2, K1, D1, K2, D2, imageSize, R=None, T=None, flags=None, criteria=None): # real signature unknown; restored from __doc__
    """
    stereoCalibrate(objectPoints, imagePoints1, imagePoints2, K1, D1, K2, D2, imageSize[, R[, T[, flags[, criteria]]]]) -> retval, K1, D1, K2, D2, R, T
    .   @brief Performs stereo calibration
    .   
    .       @param objectPoints Vector of vectors of the calibration pattern points.
    .       @param imagePoints1 Vector of vectors of the projections of the calibration pattern points,
    .       observed by the first camera.
    .       @param imagePoints2 Vector of vectors of the projections of the calibration pattern points,
    .       observed by the second camera.
    .       @param K1 Input/output first camera matrix:
    .       \f$\vecthreethree{f_x^{(j)}}{0}{c_x^{(j)}}{0}{f_y^{(j)}}{c_y^{(j)}}{0}{0}{1}\f$ , \f$j = 0,\, 1\f$ . If
    .       any of fisheye::CALIB_USE_INTRINSIC_GUESS , fisheye::CALIB_FIX_INTRINSIC are specified,
    .       some or all of the matrix components must be initialized.
    .       @param D1 Input/output vector of distortion coefficients \f$(k_1, k_2, k_3, k_4)\f$ of 4 elements.
    .       @param K2 Input/output second camera matrix. The parameter is similar to K1 .
    .       @param D2 Input/output lens distortion coefficients for the second camera. The parameter is
    .       similar to D1 .
    .       @param imageSize Size of the image used only to initialize intrinsic camera matrix.
    .       @param R Output rotation matrix between the 1st and the 2nd camera coordinate systems.
    .       @param T Output translation vector between the coordinate systems of the cameras.
    .       @param flags Different flags that may be zero or a combination of the following values:
    .       -   **fisheye::CALIB_FIX_INTRINSIC** Fix K1, K2? and D1, D2? so that only R, T matrices
    .       are estimated.
    .       -   **fisheye::CALIB_USE_INTRINSIC_GUESS** K1, K2 contains valid initial values of
    .       fx, fy, cx, cy that are optimized further. Otherwise, (cx, cy) is initially set to the image
    .       center (imageSize is used), and focal distances are computed in a least-squares fashion.
    .       -   **fisheye::CALIB_RECOMPUTE_EXTRINSIC** Extrinsic will be recomputed after each iteration
    .       of intrinsic optimization.
    .       -   **fisheye::CALIB_CHECK_COND** The functions will check validity of condition number.
    .       -   **fisheye::CALIB_FIX_SKEW** Skew coefficient (alpha) is set to zero and stay zero.
    .       -   **fisheye::CALIB_FIX_K1..4** Selected distortion coefficients are set to zeros and stay
    .       zero.
    .       @param criteria Termination criteria for the iterative optimization algorithm.
    """
    pass

def stereoRectify(K1, D1, K2, D2, imageSize, R, tvec, flags, R1=None, R2=None, P1=None, P2=None, Q=None, newImageSize=None, balance=None, fov_scale=None): # real signature unknown; restored from __doc__
    """
    stereoRectify(K1, D1, K2, D2, imageSize, R, tvec, flags[, R1[, R2[, P1[, P2[, Q[, newImageSize[, balance[, fov_scale]]]]]]]]) -> R1, R2, P1, P2, Q
    .   @brief Stereo rectification for fisheye camera model
    .   
    .       @param K1 First camera matrix.
    .       @param D1 First camera distortion parameters.
    .       @param K2 Second camera matrix.
    .       @param D2 Second camera distortion parameters.
    .       @param imageSize Size of the image used for stereo calibration.
    .       @param R Rotation matrix between the coordinate systems of the first and the second
    .       cameras.
    .       @param tvec Translation vector between coordinate systems of the cameras.
    .       @param R1 Output 3x3 rectification transform (rotation matrix) for the first camera.
    .       @param R2 Output 3x3 rectification transform (rotation matrix) for the second camera.
    .       @param P1 Output 3x4 projection matrix in the new (rectified) coordinate systems for the first
    .       camera.
    .       @param P2 Output 3x4 projection matrix in the new (rectified) coordinate systems for the second
    .       camera.
    .       @param Q Output \f$4 \times 4\f$ disparity-to-depth mapping matrix (see reprojectImageTo3D ).
    .       @param flags Operation flags that may be zero or CALIB_ZERO_DISPARITY . If the flag is set,
    .       the function makes the principal points of each camera have the same pixel coordinates in the
    .       rectified views. And if the flag is not set, the function may still shift the images in the
    .       horizontal or vertical direction (depending on the orientation of epipolar lines) to maximize the
    .       useful image area.
    .       @param newImageSize New image resolution after rectification. The same size should be passed to
    .       initUndistortRectifyMap (see the stereo_calib.cpp sample in OpenCV samples directory). When (0,0)
    .       is passed (default), it is set to the original imageSize . Setting it to larger value can help you
    .       preserve details in the original image, especially when there is a big radial distortion.
    .       @param balance Sets the new focal length in range between the min focal length and the max focal
    .       length. Balance is in range of [0, 1].
    .       @param fov_scale Divisor for new focal length.
    """
    pass

def undistortImage(distorted, K, D, undistorted=None, Knew=None, new_size=None): # real signature unknown; restored from __doc__
    """
    undistortImage(distorted, K, D[, undistorted[, Knew[, new_size]]]) -> undistorted
    .   @brief Transforms an image to compensate for fisheye lens distortion.
    .   
    .       @param distorted image with fisheye lens distortion.
    .       @param undistorted Output image with compensated fisheye lens distortion.
    .       @param K Camera matrix \f$K = \vecthreethree{f_x}{0}{c_x}{0}{f_y}{c_y}{0}{0}{_1}\f$.
    .       @param D Input vector of distortion coefficients \f$(k_1, k_2, k_3, k_4)\f$.
    .       @param Knew Camera matrix of the distorted image. By default, it is the identity matrix but you
    .       may additionally scale and shift the result by using a different matrix.
    .       @param new_size the new size
    .   
    .       The function transforms an image to compensate radial and tangential lens distortion.
    .   
    .       The function is simply a combination of fisheye::initUndistortRectifyMap (with unity R ) and remap
    .       (with bilinear interpolation). See the former function for details of the transformation being
    .       performed.
    .   
    .       See below the results of undistortImage.
    .          -   a\) result of undistort of perspective camera model (all possible coefficients (k_1, k_2, k_3,
    .               k_4, k_5, k_6) of distortion were optimized under calibration)
    .           -   b\) result of fisheye::undistortImage of fisheye camera model (all possible coefficients (k_1, k_2,
    .               k_3, k_4) of fisheye distortion were optimized under calibration)
    .           -   c\) original image was captured with fisheye lens
    .   
    .       Pictures a) and b) almost the same. But if we consider points of image located far from the center
    .       of image, we can notice that on image a) these points are distorted.
    .   
    .       ![image](pics/fisheye_undistorted.jpg)
    """
    pass

def undistortPoints(distorted, K, D, undistorted=None, R=None, P=None): # real signature unknown; restored from __doc__
    """
    undistortPoints(distorted, K, D[, undistorted[, R[, P]]]) -> undistorted
    .   @brief Undistorts 2D points using fisheye model
    .   
    .       @param distorted Array of object points, 1xN/Nx1 2-channel (or vector\<Point2f\> ), where N is the
    .       number of points in the view.
    .       @param K Camera matrix \f$K = \vecthreethree{f_x}{0}{c_x}{0}{f_y}{c_y}{0}{0}{_1}\f$.
    .       @param D Input vector of distortion coefficients \f$(k_1, k_2, k_3, k_4)\f$.
    .       @param R Rectification transformation in the object space: 3x3 1-channel, or vector: 3x1/1x3
    .       1-channel or 1x1 3-channel
    .       @param P New camera matrix (3x3) or new projection matrix (3x4)
    .       @param undistorted Output array of image points, 1xN/Nx1 2-channel, or vector\<Point2f\> .
    """
    pass

# no classes
