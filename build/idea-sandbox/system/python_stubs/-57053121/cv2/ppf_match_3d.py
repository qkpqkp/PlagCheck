# encoding: utf-8
# module cv2.ppf_match_3d
# from C:\Users\Doly\Anaconda3\lib\site-packages\cv2\cv2.cp37-win_amd64.pyd
# by generator 1.147
# no doc
# no imports

# Variables with simple values

__loader__ = None

__spec__ = None

# functions

def addNoisePC(pc, scale): # real signature unknown; restored from __doc__
    """
    addNoisePC(pc, scale) -> retval
    .   *  Adds a uniform noise in the given scale to the input point cloud
    .    *  @param [in] pc Input point cloud (CV_32F family).
    .    *  @param [in] scale Input scale of the noise. The larger the scale, the more noisy the output
    """
    pass

def computeNormalsPC3d(PC, NumNeighbors, FlipViewpoint, viewpoint, PCNormals=None): # real signature unknown; restored from __doc__
    """
    computeNormalsPC3d(PC, NumNeighbors, FlipViewpoint, viewpoint[, PCNormals]) -> retval, PCNormals
    .   *  @brief Compute the normals of an arbitrary point cloud
    .    *  computeNormalsPC3d uses a plane fitting approach to smoothly compute
    .    *  local normals. Normals are obtained through the eigenvector of the covariance
    .    *  matrix, corresponding to the smallest eigen value.
    .    *  If PCNormals is provided to be an Nx6 matrix, then no new allocation
    .    *  is made, instead the existing memory is overwritten.
    .    *  @param [in] PC Input point cloud to compute the normals for.
    .    *  @param [out] PCNormals Output point cloud
    .    *  @param [in] NumNeighbors Number of neighbors to take into account in a local region
    .    *  @param [in] FlipViewpoint Should normals be flipped to a viewing direction?
    .    *  @param [in] viewpoint
    .    *  @return Returns 0 on success
    """
    pass

def getRandomPose(Pose): # real signature unknown; restored from __doc__
    """
    getRandomPose(Pose) -> None
    .   *  Generate a random 4x4 pose matrix
    .    *  @param [out] Pose The random pose
    """
    pass

def loadPLYSimple(fileName, withNormals=None): # real signature unknown; restored from __doc__
    """
    loadPLYSimple(fileName[, withNormals]) -> retval
    .   *  @brief Load a PLY file
    .    *  @param [in] fileName The PLY model to read
    .    *  @param [in] withNormals Flag wheather the input PLY contains normal information,
    .    *  and whether it should be loaded or not
    .    *  @return Returns the matrix on successfull load
    """
    pass

def samplePCByQuantization(pc, xrange, yrange, zrange, sample_step_relative, weightByCenter=None): # real signature unknown; restored from __doc__
    """
    samplePCByQuantization(pc, xrange, yrange, zrange, sample_step_relative[, weightByCenter]) -> retval
    .   *  Sample a point cloud using uniform steps
    .    *  @param [in] pc Input point cloud
    .    *  @param [in] xrange X components (min and max) of the bounding box of the model
    .    *  @param [in] yrange Y components (min and max) of the bounding box of the model
    .    *  @param [in] zrange Z components (min and max) of the bounding box of the model
    .    *  @param [in] sample_step_relative The point cloud is sampled such that all points
    .    *  have a certain minimum distance. This minimum distance is determined relatively using
    .    *  the parameter sample_step_relative.
    .    *  @param [in] weightByCenter The contribution of the quantized data points can be weighted
    .    *  by the distance to the origin. This parameter enables/disables the use of weighting.
    .    *  @return Sampled point cloud
    """
    pass

def transformPCPose(pc, Pose): # real signature unknown; restored from __doc__
    """
    transformPCPose(pc, Pose) -> retval
    .   *  Transforms the point cloud with a given a homogeneous 4x4 pose matrix (in double precision)
    .    *  @param [in] pc Input point cloud (CV_32F family). Point clouds with 3 or 6 elements per
    .    *  row are expected. In the case where the normals are provided, they are also rotated to be
    .    *  compatible with the entire transformation
    .    *  @param [in] Pose 4x4 pose matrix, but linearized in row-major form.
    .    *  @return Transformed point cloud
    """
    pass

def writePLY(PC, fileName): # real signature unknown; restored from __doc__
    """
    writePLY(PC, fileName) -> None
    .   *  @brief Write a point cloud to PLY file
    .    *  @param [in] PC Input point cloud
    .    *  @param [in] fileName The PLY model file to write
    """
    pass

def writePLYVisibleNormals(PC, fileName): # real signature unknown; restored from __doc__
    """
    writePLYVisibleNormals(PC, fileName) -> None
    .   *  @brief Used for debbuging pruposes, writes a point cloud to a PLY file with the tip
    .   *  of the normal vectors as visible red points
    .   *  @param [in] PC Input point cloud
    .   *  @param [in] fileName The PLY model file to write
    """
    pass

# no classes
