# encoding: utf-8
# module cv2.samples
# from C:\Users\Doly\Anaconda3\lib\site-packages\cv2\cv2.cp37-win_amd64.pyd
# by generator 1.147
# no doc
# no imports

# Variables with simple values

__loader__ = None

__spec__ = None

# functions

def addSamplesDataSearchPath(path): # real signature unknown; restored from __doc__
    """
    addSamplesDataSearchPath(path) -> None
    .   @brief Override search data path by adding new search location
    .   
    .   Use this only to override default behavior
    .   Passed paths are used in LIFO order.
    .   
    .   @param path Path to used samples data
    """
    pass

def addSamplesDataSearchSubDirectory(subdir): # real signature unknown; restored from __doc__
    """
    addSamplesDataSearchSubDirectory(subdir) -> None
    .   @brief Append samples search data sub directory
    .   
    .   General usage is to add OpenCV modules name (`<opencv_contrib>/modules/<name>/samples/data` -> `<name>/samples/data` + `modules/<name>/samples/data`).
    .   Passed subdirectories are used in LIFO order.
    .   
    .   @param subdir samples data sub directory
    """
    pass

def findFile(relative_path, required=None, silentMode=None): # real signature unknown; restored from __doc__
    """
    findFile(relative_path[, required[, silentMode]]) -> retval
    .   @brief Try to find requested data file
    .   
    .   Search directories:
    .   
    .   1. Directories passed via `addSamplesDataSearchPath()`
    .   2. OPENCV_SAMPLES_DATA_PATH_HINT environment variable
    .   3. OPENCV_SAMPLES_DATA_PATH environment variable
    .      If parameter value is not empty and nothing is found then stop searching.
    .   4. Detects build/install path based on:
    .      a. current working directory (CWD)
    .      b. and/or binary module location (opencv_core/opencv_world, doesn't work with static linkage)
    .   5. Scan `<source>/{,data,samples/data}` directories if build directory is detected or the current directory is in source tree.
    .   6. Scan `<install>/share/OpenCV` directory if install directory is detected.
    .   
    .   @see cv::utils::findDataFile
    .   
    .   @param relative_path Relative path to data file
    .   @param required Specify "file not found" handling.
    .          If true, function prints information message and raises cv::Exception.
    .          If false, function returns empty result
    .   @param silentMode Disables messages
    .   @return Returns path (absolute or relative to the current directory) or empty string if file is not found
    """
    pass

def findFileOrKeep(relative_path, silentMode=None): # real signature unknown; restored from __doc__
    """
    findFileOrKeep(relative_path[, silentMode]) -> retval
    .
    """
    pass

# no classes
