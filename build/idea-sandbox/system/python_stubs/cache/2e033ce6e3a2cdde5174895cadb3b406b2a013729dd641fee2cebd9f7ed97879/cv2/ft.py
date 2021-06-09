# encoding: utf-8
# module cv2.ft
# from C:\Users\Doly\Anaconda3\lib\site-packages\cv2\cv2.cp37-win_amd64.pyd
# by generator 1.147
# no doc
# no imports

# Variables with simple values

ITERATIVE = 3

LINEAR = 1

MULTI_STEP = 2

ONE_STEP = 1

SINUS = 2

__loader__ = None

__spec__ = None

# functions

def createKernel(function, radius, chn, kernel=None): # real signature unknown; restored from __doc__
    """
    createKernel(function, radius, chn[, kernel]) -> kernel
    .   @brief Creates kernel from general functions.
    .       @param function Function type could be one of the following:
    .           -   **LINEAR** Linear basic function.
    .       @param radius Radius of the basic function.
    .       @param kernel Final 32-bit kernel.
    .       @param chn Number of kernel channels.
    .   
    .       The function creates kernel from predefined functions.
    """
    pass

def createKernel1(A, B, chn, kernel=None): # real signature unknown; restored from __doc__
    """
    createKernel1(A, B, chn[, kernel]) -> kernel
    .   @brief Creates kernel from basic functions.
    .       @param A Basic function used in axis **x**.
    .       @param B Basic function used in axis **y**.
    .       @param kernel Final 32-bit kernel derived from **A** and **B**.
    .       @param chn Number of kernel channels.
    .   
    .       The function creates kernel usable for latter fuzzy image processing.
    """
    pass

def filter(image, kernel, output=None): # real signature unknown; restored from __doc__
    """
    filter(image, kernel[, output]) -> output
    .   @brief Image filtering
    .       @param image Input image.
    .       @param kernel Final 32-bit kernel.
    .       @param output Output 32-bit image.
    .   
    .       Filtering of the input image by means of F-transform.
    """
    pass

def FT02D_components(matrix, kernel, components=None, mask=None): # real signature unknown; restored from __doc__
    """
    FT02D_components(matrix, kernel[, components[, mask]]) -> components
    .   @brief Computes components of the array using direct \f$F^0\f$-transform.
    .       @param matrix Input array.
    .       @param kernel Kernel used for processing. Function `ft::createKernel` can be used.
    .       @param components Output 32-bit float array for the components.
    .       @param mask Mask can be used for unwanted area marking.
    .   
    .       The function computes components using predefined kernel and mask.
    """
    pass

def FT02D_FL_process(matrix, radius, output=None): # real signature unknown; restored from __doc__
    """
    FT02D_FL_process(matrix, radius[, output]) -> output
    .   @brief Sligtly less accurate version of \f$F^0\f$-transfrom computation optimized for higher speed. The methods counts with linear basic function.
    .       @param matrix Input 3 channels matrix.
    .       @param radius Radius of the `ft::LINEAR` basic function.
    .       @param output Output array.
    .   
    .       This function computes F-transfrom and inverse F-transfotm using linear basic function in one step. It is ~10 times faster than `ft::FT02D_process` method.
    """
    pass

def FT02D_FL_process_float(matrix, radius, output=None): # real signature unknown; restored from __doc__
    """
    FT02D_FL_process_float(matrix, radius[, output]) -> output
    .   @brief Sligtly less accurate version of \f$F^0\f$-transfrom computation optimized for higher speed. The methods counts with linear basic function.
    .       @param matrix Input 3 channels matrix.
    .       @param radius Radius of the `ft::LINEAR` basic function.
    .       @param output Output array.
    .   
    .       This function computes F-transfrom and inverse F-transfotm using linear basic function in one step. It is ~9 times faster then `ft::FT02D_process` method and more accurate than `ft::FT02D_FL_process` method.
    """
    pass

def FT02D_inverseFT(components, kernel, width, height, output=None): # real signature unknown; restored from __doc__
    """
    FT02D_inverseFT(components, kernel, width, height[, output]) -> output
    .   @brief Computes inverse \f$F^0\f$-transfrom.
    .       @param components Input 32-bit float single channel array for the components.
    .       @param kernel Kernel used for processing. Function `ft::createKernel` can be used.
    .       @param output Output 32-bit float array.
    .       @param width Width of the output array.
    .       @param height Height of the output array.
    .   
    .       Computation of inverse F-transform.
    """
    pass

def FT02D_iteration(matrix, kernel, mask, firstStop, output=None, maskOutput=None): # real signature unknown; restored from __doc__
    """
    FT02D_iteration(matrix, kernel, mask, firstStop[, output[, maskOutput]]) -> retval, output, maskOutput
    .   @brief Computes \f$F^0\f$-transfrom and inverse \f$F^0\f$-transfrom at once and return state.
    .       @param matrix Input matrix.
    .       @param kernel Kernel used for processing. Function `ft::createKernel` can be used.
    .       @param output Output 32-bit float array.
    .       @param mask Mask used for unwanted area marking.
    .       @param maskOutput Mask after one iteration.
    .       @param firstStop If **true** function returns -1 when first problem appears. In case of `false` the process is completed and summation of all problems returned.
    .   
    .       This function computes iteration of F-transfrom and inverse F-transfotm and handle image and mask change. The function is used in `ft::inpaint` function.
    """
    pass

def FT02D_process(matrix, kernel, output=None, mask=None): # real signature unknown; restored from __doc__
    """
    FT02D_process(matrix, kernel[, output[, mask]]) -> output
    .   @brief Computes \f$F^0\f$-transfrom and inverse \f$F^0\f$-transfrom at once.
    .       @param matrix Input matrix.
    .       @param kernel Kernel used for processing. Function `ft::createKernel` can be used.
    .       @param output Output 32-bit float array.
    .       @param mask Mask used for unwanted area marking.
    .   
    .       This function computes F-transfrom and inverse F-transfotm in one step. It is fully sufficient and optimized for `cv::Mat`.
    """
    pass

def FT12D_components(matrix, kernel, components=None): # real signature unknown; restored from __doc__
    """
    FT12D_components(matrix, kernel[, components]) -> components
    .   @brief Computes components of the array using direct \f$F^1\f$-transform.
    .       @param matrix Input array.
    .       @param kernel Kernel used for processing. Function `ft::createKernel` can be used.
    .       @param components Output 32-bit float array for the components.
    .   
    .       The function computes linear components using predefined kernel.
    """
    pass

def FT12D_createPolynomMatrixHorizontal(radius, chn, matrix=None): # real signature unknown; restored from __doc__
    """
    FT12D_createPolynomMatrixHorizontal(radius, chn[, matrix]) -> matrix
    .   @brief Creates horizontal matrix for \f$F^1\f$-transform computation.
    .       @param radius Radius of the basic function.
    .       @param matrix The horizontal matrix.
    .       @param chn Number of channels.
    .   
    .       The function creates helper horizontal matrix for \f$F^1\f$-transfrom processing. It is used for gradient computation.
    """
    pass

def FT12D_createPolynomMatrixVertical(radius, chn, matrix=None): # real signature unknown; restored from __doc__
    """
    FT12D_createPolynomMatrixVertical(radius, chn[, matrix]) -> matrix
    .   @brief Creates vertical matrix for \f$F^1\f$-transform computation.
    .       @param radius Radius of the basic function.
    .       @param matrix The vertical matrix.
    .       @param chn Number of channels.
    .   
    .       The function creates helper vertical matrix for \f$F^1\f$-transfrom processing. It is used for gradient computation.
    """
    pass

def FT12D_inverseFT(components, kernel, width, height, output=None): # real signature unknown; restored from __doc__
    """
    FT12D_inverseFT(components, kernel, width, height[, output]) -> output
    .   @brief Computes inverse \f$F^1\f$-transfrom.
    .       @param components Input 32-bit float single channel array for the components.
    .       @param kernel Kernel used for processing. The same kernel as for components computation must be used.
    .       @param output Output 32-bit float array.
    .       @param width Width of the output array.
    .       @param height Height of the output array.
    .   
    .       Computation of inverse \f$F^1\f$-transform.
    """
    pass

def FT12D_polynomial(matrix, kernel, c00=None, c10=None, c01=None, components=None, mask=None): # real signature unknown; restored from __doc__
    """
    FT12D_polynomial(matrix, kernel[, c00[, c10[, c01[, components[, mask]]]]]) -> c00, c10, c01, components
    .   @brief Computes elements of \f$F^1\f$-transform components.
    .       @param matrix Input array.
    .       @param kernel Kernel used for processing. Function `ft::createKernel` can be used.
    .       @param c00 Elements represent average color.
    .       @param c10 Elements represent average vertical gradient.
    .       @param c01 Elements represent average horizontal gradient.
    .       @param components Output 32-bit float array for the components.
    .       @param mask Mask can be used for unwanted area marking.
    .   
    .       The function computes components and its elements using predefined kernel and mask.
    """
    pass

def FT12D_process(matrix, kernel, output=None, mask=None): # real signature unknown; restored from __doc__
    """
    FT12D_process(matrix, kernel[, output[, mask]]) -> output
    .   @brief Computes \f$F^1\f$-transfrom and inverse \f$F^1\f$-transfrom at once.
    .       @param matrix Input matrix.
    .       @param kernel Kernel used for processing. Function `ft::createKernel` can be used.
    .       @param output Output 32-bit float array.
    .       @param mask Mask used for unwanted area marking.
    .   
    .       This function computes \f$F^1\f$-transfrom and inverse \f$F^1\f$-transfotm in one step. It is fully sufficient and optimized for `cv::Mat`.
    .   
    .       @note
    .           F-transform technique of first degreee is described in paper @cite Vlas:FT.
    """
    pass

def inpaint(image, mask, radius, function, algorithm, output=None): # real signature unknown; restored from __doc__
    """
    inpaint(image, mask, radius, function, algorithm[, output]) -> output
    .   @brief Image inpainting
    .       @param image Input image.
    .       @param mask Mask used for unwanted area marking.
    .       @param output Output 32-bit image.
    .       @param radius Radius of the basic function.
    .       @param function Function type could be one of the following:
    .           -   `ft::LINEAR` Linear basic function.
    .       @param algorithm Algorithm could be one of the following:
    .           -   `ft::ONE_STEP` One step algorithm.
    .           -   `ft::MULTI_STEP` This algorithm automaticaly increases radius of the basic function.
    .           -   `ft::ITERATIVE` Iterative algorithm running in more steps using partial computations.
    .   
    .       This function provides inpainting technique based on the fuzzy mathematic.
    .   
    .       @note
    .           The algorithms are described in paper @cite Perf:rec.
    """
    pass

# no classes
