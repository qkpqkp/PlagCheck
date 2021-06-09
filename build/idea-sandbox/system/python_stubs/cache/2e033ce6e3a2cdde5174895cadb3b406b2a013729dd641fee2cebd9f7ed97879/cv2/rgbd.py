# encoding: utf-8
# module cv2.rgbd
# from C:\Users\Doly\Anaconda3\lib\site-packages\cv2\cv2.cp37-win_amd64.pyd
# by generator 1.147
# no doc
# no imports

# Variables with simple values

DepthCleaner_DEPTH_CLEANER_NIL = 0

DEPTH_CLEANER_DEPTH_CLEANER_NIL = 0

OdometryFrame_CACHE_ALL = 3
OdometryFrame_CACHE_DST = 2
OdometryFrame_CACHE_SRC = 1

ODOMETRY_FRAME_CACHE_ALL = 3
ODOMETRY_FRAME_CACHE_DST = 2
ODOMETRY_FRAME_CACHE_SRC = 1

Odometry_RIGID_BODY_MOTION = 4

ODOMETRY_RIGID_BODY_MOTION = 4

Odometry_ROTATION = 1

ODOMETRY_ROTATION = 1

Odometry_TRANSLATION = 2

ODOMETRY_TRANSLATION = 2

RgbdNormals_RGBD_NORMALS_METHOD_FALS = 0
RgbdNormals_RGBD_NORMALS_METHOD_LINEMOD = 1
RgbdNormals_RGBD_NORMALS_METHOD_SRI = 2

RgbdPlane_RGBD_PLANE_METHOD_DEFAULT = 0

RGBD_NORMALS_RGBD_NORMALS_METHOD_FALS = 0
RGBD_NORMALS_RGBD_NORMALS_METHOD_LINEMOD = 1
RGBD_NORMALS_RGBD_NORMALS_METHOD_SRI = 2

RGBD_PLANE_RGBD_PLANE_METHOD_DEFAULT = 0

__loader__ = None

__spec__ = None

# functions

def DepthCleaner_create(depth, window_size=None, method=None): # real signature unknown; restored from __doc__
    """
    DepthCleaner_create(depth[, window_size[, method]]) -> retval
    .   Constructor
    .        * @param depth the depth of the normals (only CV_32F or CV_64F)
    .        * @param window_size the window size to compute the normals: can only be 1,3,5 or 7
    .        * @param method one of the methods to use: RGBD_NORMALS_METHOD_SRI, RGBD_NORMALS_METHOD_FALS
    """
    pass

def depthTo3d(depth, K, points3d=None, mask=None): # real signature unknown; restored from __doc__
    """
    depthTo3d(depth, K[, points3d[, mask]]) -> points3d
    .   Converts a depth image to an organized set of 3d points.
    .      * The coordinate system is x pointing left, y down and z away from the camera
    .      * @param depth the depth image (if given as short int CV_U, it is assumed to be the depth in millimeters
    .      *              (as done with the Microsoft Kinect), otherwise, if given as CV_32F or CV_64F, it is assumed in meters)
    .      * @param K The calibration matrix
    .      * @param points3d the resulting 3d points. They are of depth the same as `depth` if it is CV_32F or CV_64F, and the
    .      *        depth of `K` if `depth` is of depth CV_U
    .      * @param mask the mask of the points to consider (can be empty)
    """
    pass

def depthTo3dSparse(depth, in_K, in_points, points3d=None): # real signature unknown; restored from __doc__
    """
    depthTo3dSparse(depth, in_K, in_points[, points3d]) -> points3d
    .   * @param depth the depth image
    .      * @param in_K
    .      * @param in_points the list of xy coordinates
    .      * @param points3d the resulting 3d points
    """
    pass

def FastICPOdometry_create(cameraMatrix, maxDistDiff=None, angleThreshold=None, sigmaDepth=None, sigmaSpatial=None, kernelSize=None, iterCounts=None): # real signature unknown; restored from __doc__
    """
    FastICPOdometry_create(cameraMatrix[, maxDistDiff[, angleThreshold[, sigmaDepth[, sigmaSpatial[, kernelSize[, iterCounts]]]]]]) -> retval
    .   Constructor.
    .        * @param cameraMatrix Camera matrix
    .        * @param maxDistDiff Correspondences between pixels of two given frames will be filtered out
    .        *                     if their depth difference is larger than maxDepthDiff
    .        * @param angleThreshold Correspondence will be filtered out
    .        *                     if an angle between their normals is bigger than threshold
    .        * @param sigmaDepth Depth sigma in meters for bilateral smooth
    .        * @param sigmaSpatial Spatial sigma in pixels for bilateral smooth
    .        * @param kernelSize Kernel size in pixels for bilateral smooth
    .        * @param iterCounts Count of iterations on each pyramid level
    """
    pass

def ICPOdometry_create(cameraMatrix=None, minDepth=None, maxDepth=None, maxDepthDiff=None, maxPointsPart=None, iterCounts=None, transformType=None): # real signature unknown; restored from __doc__
    """
    ICPOdometry_create([, cameraMatrix[, minDepth[, maxDepth[, maxDepthDiff[, maxPointsPart[, iterCounts[, transformType]]]]]]]) -> retval
    .   Constructor.
    .        * @param cameraMatrix Camera matrix
    .        * @param minDepth Pixels with depth less than minDepth will not be used
    .        * @param maxDepth Pixels with depth larger than maxDepth will not be used
    .        * @param maxDepthDiff Correspondences between pixels of two given frames will be filtered out
    .        *                     if their depth difference is larger than maxDepthDiff
    .        * @param maxPointsPart The method uses a random pixels subset of size frameWidth x frameHeight x pointsPart
    .        * @param iterCounts Count of iterations on each pyramid level.
    .        * @param transformType Class of trasformation
    """
    pass

def OdometryFrame_create(image=None, depth=None, mask=None, normals=None, ID=None): # real signature unknown; restored from __doc__
    """
    OdometryFrame_create([, image[, depth[, mask[, normals[, ID]]]]]) -> retval
    .
    """
    pass

def Odometry_create(odometryType): # real signature unknown; restored from __doc__
    """
    Odometry_create(odometryType) -> retval
    .
    """
    pass

def registerDepth(unregisteredCameraMatrix, registeredCameraMatrix, registeredDistCoeffs, Rt, unregisteredDepth, outputImagePlaneSize, registeredDepth=None, depthDilation=None): # real signature unknown; restored from __doc__
    """
    registerDepth(unregisteredCameraMatrix, registeredCameraMatrix, registeredDistCoeffs, Rt, unregisteredDepth, outputImagePlaneSize[, registeredDepth[, depthDilation]]) -> registeredDepth
    .   Registers depth data to an external camera
    .      * Registration is performed by creating a depth cloud, transforming the cloud by
    .      * the rigid body transformation between the cameras, and then projecting the
    .      * transformed points into the RGB camera.
    .      *
    .      * uv_rgb = K_rgb * [R | t] * z * inv(K_ir) * uv_ir
    .      *
    .      * Currently does not check for negative depth values.
    .      *
    .      * @param unregisteredCameraMatrix the camera matrix of the depth camera
    .      * @param registeredCameraMatrix the camera matrix of the external camera
    .      * @param registeredDistCoeffs the distortion coefficients of the external camera
    .      * @param Rt the rigid body transform between the cameras. Transforms points from depth camera frame to external camera frame.
    .      * @param unregisteredDepth the input depth data
    .      * @param outputImagePlaneSize the image plane dimensions of the external camera (width, height)
    .      * @param registeredDepth the result of transforming the depth into the external camera
    .      * @param depthDilation whether or not the depth is dilated to avoid holes and occlusion errors (optional)
    """
    pass

def rescaleDepth(in_, depth, out=None): # real signature unknown; restored from __doc__
    """
    rescaleDepth(in, depth[, out]) -> out
    .   If the input image is of type CV_16UC1 (like the Kinect one), the image is converted to floats, divided
    .      * by 1000 to get a depth in meters, and the values 0 are converted to std::numeric_limits<float>::quiet_NaN()
    .      * Otherwise, the image is simply converted to floats
    .      * @param in the depth image (if given as short int CV_U, it is assumed to be the depth in millimeters
    .      *              (as done with the Microsoft Kinect), it is assumed in meters)
    .      * @param depth the desired output depth (floats or double)
    .      * @param out The rescaled float depth image
    """
    pass

def RgbdFrame_create(image=None, depth=None, mask=None, normals=None, ID=None): # real signature unknown; restored from __doc__
    """
    RgbdFrame_create([, image[, depth[, mask[, normals[, ID]]]]]) -> retval
    .
    """
    pass

def RgbdICPOdometry_create(cameraMatrix=None, minDepth=None, maxDepth=None, maxDepthDiff=None, maxPointsPart=None, iterCounts=None, minGradientMagnitudes=None, transformType=None): # real signature unknown; restored from __doc__
    """
    RgbdICPOdometry_create([, cameraMatrix[, minDepth[, maxDepth[, maxDepthDiff[, maxPointsPart[, iterCounts[, minGradientMagnitudes[, transformType]]]]]]]]) -> retval
    .   Constructor.
    .        * @param cameraMatrix Camera matrix
    .        * @param minDepth Pixels with depth less than minDepth will not be used
    .        * @param maxDepth Pixels with depth larger than maxDepth will not be used
    .        * @param maxDepthDiff Correspondences between pixels of two given frames will be filtered out
    .        *                     if their depth difference is larger than maxDepthDiff
    .        * @param maxPointsPart The method uses a random pixels subset of size frameWidth x frameHeight x pointsPart
    .        * @param iterCounts Count of iterations on each pyramid level.
    .        * @param minGradientMagnitudes For each pyramid level the pixels will be filtered out
    .        *                              if they have gradient magnitude less than minGradientMagnitudes[level].
    .        * @param transformType Class of trasformation
    """
    pass

def RgbdNormals_create(rows, cols, depth, K, window_size=None, method=None): # real signature unknown; restored from __doc__
    """
    RgbdNormals_create(rows, cols, depth, K[, window_size[, method]]) -> retval
    .   Constructor
    .        * @param rows the number of rows of the depth image normals will be computed on
    .        * @param cols the number of cols of the depth image normals will be computed on
    .        * @param depth the depth of the normals (only CV_32F or CV_64F)
    .        * @param K the calibration matrix to use
    .        * @param window_size the window size to compute the normals: can only be 1,3,5 or 7
    .        * @param method one of the methods to use: RGBD_NORMALS_METHOD_SRI, RGBD_NORMALS_METHOD_FALS
    """
    pass

def RgbdOdometry_create(cameraMatrix=None, minDepth=None, maxDepth=None, maxDepthDiff=None, iterCounts=None, minGradientMagnitudes=None, maxPointsPart=None, transformType=None): # real signature unknown; restored from __doc__
    """
    RgbdOdometry_create([, cameraMatrix[, minDepth[, maxDepth[, maxDepthDiff[, iterCounts[, minGradientMagnitudes[, maxPointsPart[, transformType]]]]]]]]) -> retval
    .   Constructor.
    .        * @param cameraMatrix Camera matrix
    .        * @param minDepth Pixels with depth less than minDepth will not be used (in meters)
    .        * @param maxDepth Pixels with depth larger than maxDepth will not be used (in meters)
    .        * @param maxDepthDiff Correspondences between pixels of two given frames will be filtered out
    .        *                     if their depth difference is larger than maxDepthDiff (in meters)
    .        * @param iterCounts Count of iterations on each pyramid level.
    .        * @param minGradientMagnitudes For each pyramid level the pixels will be filtered out
    .        *                              if they have gradient magnitude less than minGradientMagnitudes[level].
    .        * @param maxPointsPart The method uses a random pixels subset of size frameWidth x frameHeight x pointsPart
    .        * @param transformType Class of transformation
    """
    pass

def warpFrame(image, depth, mask, Rt, cameraMatrix, distCoeff, warpedImage=None, warpedDepth=None, warpedMask=None): # real signature unknown; restored from __doc__
    """
    warpFrame(image, depth, mask, Rt, cameraMatrix, distCoeff[, warpedImage[, warpedDepth[, warpedMask]]]) -> warpedImage, warpedDepth, warpedMask
    .   Warp the image: compute 3d points from the depth, transform them using given transformation,
    .      * then project color point cloud to an image plane.
    .      * This function can be used to visualize results of the Odometry algorithm.
    .      * @param image The image (of CV_8UC1 or CV_8UC3 type)
    .      * @param depth The depth (of type used in depthTo3d fuction)
    .      * @param mask The mask of used pixels (of CV_8UC1), it can be empty
    .      * @param Rt The transformation that will be applied to the 3d points computed from the depth
    .      * @param cameraMatrix Camera matrix
    .      * @param distCoeff Distortion coefficients
    .      * @param warpedImage The warped image.
    .      * @param warpedDepth The warped depth.
    .      * @param warpedMask The warped mask.
    """
    pass

# no classes
