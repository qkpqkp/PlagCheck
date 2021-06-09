# encoding: utf-8
# module cv2.cuda
# from C:\Users\Doly\Anaconda3\lib\site-packages\cv2\cv2.cp37-win_amd64.pyd
# by generator 1.147
# no doc
# no imports

# Variables with simple values

DeviceInfo_ComputeModeDefault = 0
DeviceInfo_ComputeModeExclusive = 1
DeviceInfo_ComputeModeExclusiveProcess = 3
DeviceInfo_ComputeModeProhibited = 2

DEVICE_INFO_COMPUTE_MODE_DEFAULT = 0
DEVICE_INFO_COMPUTE_MODE_EXCLUSIVE = 1

DEVICE_INFO_COMPUTE_MODE_EXCLUSIVE_PROCESS = 3

DEVICE_INFO_COMPUTE_MODE_PROHIBITED = 2

DYNAMIC_PARALLELISM = 35

Event_BLOCKING_SYNC = 1

EVENT_BLOCKING_SYNC = 1

Event_DEFAULT = 0

EVENT_DEFAULT = 0

Event_DISABLE_TIMING = 2

EVENT_DISABLE_TIMING = 2

Event_INTERPROCESS = 4

EVENT_INTERPROCESS = 4

FEATURE_SET_COMPUTE_10 = 10
FEATURE_SET_COMPUTE_11 = 11
FEATURE_SET_COMPUTE_12 = 12
FEATURE_SET_COMPUTE_13 = 13
FEATURE_SET_COMPUTE_20 = 20
FEATURE_SET_COMPUTE_21 = 21
FEATURE_SET_COMPUTE_30 = 30
FEATURE_SET_COMPUTE_32 = 32
FEATURE_SET_COMPUTE_35 = 35
FEATURE_SET_COMPUTE_50 = 50

GLOBAL_ATOMICS = 11

HostMem_PAGE_LOCKED = 1

HostMem_SHARED = 2

HostMem_WRITE_COMBINED = 4

HOST_MEM_PAGE_LOCKED = 1

HOST_MEM_SHARED = 2

HOST_MEM_WRITE_COMBINED = 4

NATIVE_DOUBLE = 13

SHARED_ATOMICS = 12

SURF_CUDA_ANGLE_ROW = 5

SURF_CUDA_HESSIAN_ROW = 6

SURF_CUDA_LAPLACIAN_ROW = 2

SURF_CUDA_OCTAVE_ROW = 3

SURF_CUDA_ROWS_COUNT = 7

SURF_CUDA_SIZE_ROW = 4

SURF_CUDA_X_ROW = 0

SURF_CUDA_Y_ROW = 1

WARP_SHUFFLE_FUNCTIONS = 30

__loader__ = None

__spec__ = None

# functions

def createContinuous(rows, cols, type, arr=None): # real signature unknown; restored from __doc__
    """
    createContinuous(rows, cols, type[, arr]) -> arr
    .   @brief Creates a continuous matrix.
    .   
    .   @param rows Row count.
    .   @param cols Column count.
    .   @param type Type of the matrix.
    .   @param arr Destination matrix. This parameter changes only if it has a proper type and area (
    .   \f$\texttt{rows} \times \texttt{cols}\f$ ).
    .   
    .   Matrix is called continuous if its elements are stored continuously, that is, without gaps at the
    .   end of each row.
    """
    pass

def ensureSizeIsEnough(rows, cols, type, arr=None): # real signature unknown; restored from __doc__
    """
    ensureSizeIsEnough(rows, cols, type[, arr]) -> arr
    .   @brief Ensures that the size of a matrix is big enough and the matrix has a proper type.
    .   
    .   @param rows Minimum desired number of rows.
    .   @param cols Minimum desired number of columns.
    .   @param type Desired matrix type.
    .   @param arr Destination matrix.
    .   
    .   The function does not reallocate memory if the matrix has proper attributes already.
    """
    pass

def Event_elapsedTime(start, end): # real signature unknown; restored from __doc__
    """
    Event_elapsedTime(start, end) -> retval
    .
    """
    pass

def getCudaEnabledDeviceCount(): # real signature unknown; restored from __doc__
    """
    getCudaEnabledDeviceCount() -> retval
    .   @brief Returns the number of installed CUDA-enabled devices.
    .   
    .   Use this function before any other CUDA functions calls. If OpenCV is compiled without CUDA support,
    .   this function returns 0. If the CUDA driver is not installed, or is incompatible, this function
    .   returns -1.
    """
    pass

def getDevice(): # real signature unknown; restored from __doc__
    """
    getDevice() -> retval
    .   @brief Returns the current device index set by cuda::setDevice or initialized by default.
    """
    pass

def GpuMat_defaultAllocator(): # real signature unknown; restored from __doc__
    """
    GpuMat_defaultAllocator() -> retval
    .
    """
    pass

def GpuMat_setDefaultAllocator(allocator): # real signature unknown; restored from __doc__
    """
    GpuMat_setDefaultAllocator(allocator) -> None
    .
    """
    pass

def printCudaDeviceInfo(device): # real signature unknown; restored from __doc__
    """
    printCudaDeviceInfo(device) -> None
    .
    """
    pass

def printShortCudaDeviceInfo(device): # real signature unknown; restored from __doc__
    """
    printShortCudaDeviceInfo(device) -> None
    .
    """
    pass

def registerPageLocked(m): # real signature unknown; restored from __doc__
    """
    registerPageLocked(m) -> None
    .   @brief Page-locks the memory of matrix and maps it for the device(s).
    .   
    .   @param m Input matrix.
    """
    pass

def resetDevice(): # real signature unknown; restored from __doc__
    """
    resetDevice() -> None
    .   @brief Explicitly destroys and cleans up all resources associated with the current device in the current
    .   process.
    .   
    .   Any subsequent API call to this device will reinitialize the device.
    """
    pass

def setBufferPoolConfig(deviceId, stackSize, stackCount): # real signature unknown; restored from __doc__
    """
    setBufferPoolConfig(deviceId, stackSize, stackCount) -> None
    .
    """
    pass

def setBufferPoolUsage(on): # real signature unknown; restored from __doc__
    """
    setBufferPoolUsage(on) -> None
    .
    """
    pass

def setDevice(device): # real signature unknown; restored from __doc__
    """
    setDevice(device) -> None
    .   @brief Sets a device and initializes it for the current thread.
    .   
    .   @param device System index of a CUDA device starting with 0.
    .   
    .   If the call of this function is omitted, a default device is initialized at the fist CUDA usage.
    """
    pass

def Stream_Null(): # real signature unknown; restored from __doc__
    """
    Stream_Null() -> retval
    .   @brief Adds a callback to be called on the host after all currently enqueued items in the stream have
    .       completed.
    .   
    .       @note Callbacks must not make any CUDA API calls. Callbacks must not perform any synchronization
    .       that may depend on outstanding device work or other callbacks that are not mandated to run earlier.
    .       Callbacks without a mandated order (in independent streams) execute in undefined order and may be
    .       serialized.
    """
    pass

def TargetArchs_has(major, minor): # real signature unknown; restored from __doc__
    """
    TargetArchs_has(major, minor) -> retval
    .   @brief There is a set of methods to check whether the module contains intermediate (PTX) or binary CUDA
    .       code for the given architecture(s):
    .   
    .       @param major Major compute capability version.
    .       @param minor Minor compute capability version.
    """
    pass

def TargetArchs_hasBin(major, minor): # real signature unknown; restored from __doc__
    """
    TargetArchs_hasBin(major, minor) -> retval
    .
    """
    pass

def TargetArchs_hasEqualOrGreater(major, minor): # real signature unknown; restored from __doc__
    """
    TargetArchs_hasEqualOrGreater(major, minor) -> retval
    .
    """
    pass

def TargetArchs_hasEqualOrGreaterBin(major, minor): # real signature unknown; restored from __doc__
    """
    TargetArchs_hasEqualOrGreaterBin(major, minor) -> retval
    .
    """
    pass

def TargetArchs_hasEqualOrGreaterPtx(major, minor): # real signature unknown; restored from __doc__
    """
    TargetArchs_hasEqualOrGreaterPtx(major, minor) -> retval
    .
    """
    pass

def TargetArchs_hasEqualOrLessPtx(major, minor): # real signature unknown; restored from __doc__
    """
    TargetArchs_hasEqualOrLessPtx(major, minor) -> retval
    .
    """
    pass

def TargetArchs_hasPtx(major, minor): # real signature unknown; restored from __doc__
    """
    TargetArchs_hasPtx(major, minor) -> retval
    .
    """
    pass

def unregisterPageLocked(m): # real signature unknown; restored from __doc__
    """
    unregisterPageLocked(m) -> None
    .   @brief Unmaps the memory of matrix and makes it pageable again.
    .   
    .   @param m Input matrix.
    """
    pass

# no classes
