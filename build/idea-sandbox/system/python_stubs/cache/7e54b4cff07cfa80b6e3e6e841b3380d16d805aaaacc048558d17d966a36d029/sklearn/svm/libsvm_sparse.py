# encoding: utf-8
# module sklearn.svm.libsvm_sparse
# from C:\Users\Doly\Anaconda3\lib\site-packages\sklearn\svm\libsvm_sparse.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import warnings as warnings # C:\Users\Doly\Anaconda3\lib\warnings.py
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py
import scipy.sparse as sparse # C:\Users\Doly\Anaconda3\lib\site-packages\scipy\sparse\__init__.py

# functions

def libsvm_sparse_decision_function(*args, **kwargs): # real signature unknown
    """
    Predict margin (libsvm name for this is predict_values)
    
        We have to reconstruct model and parameters to make sure we stay
        in sync with the python object.
    """
    pass

def libsvm_sparse_predict(*args, **kwargs): # real signature unknown
    """
    Predict values T given a model.
    
        For speed, all real work is done at the C level in function
        copy_predict (libsvm_helper.c).
    
        We have to reconstruct model and parameters to make sure we stay
        in sync with the python object.
    
        See sklearn.svm.predict for a complete list of parameters.
    
        Parameters
        ----------
        X : array-like, dtype=float
        Y : array
            target vector
    
        Returns
        -------
        dec_values : array
            predicted values.
    """
    pass

def libsvm_sparse_predict_proba(*args, **kwargs): # real signature unknown
    """ Predict values T given a model. """
    pass

def libsvm_sparse_train(*args, **kwargs): # real signature unknown
    """
    Wrap svm_train from libsvm using a scipy.sparse.csr matrix
    
        Work in progress.
    
        Parameters
        ----------
        n_features : number of features.
            XXX: can we retrieve this from any other parameter ?
    
        X : array-like, dtype=float, size=[N, D]
    
        Y : array, dtype=float, size=[N]
            target vector
    
        ...
    
        Notes
        -------------------
        See sklearn.svm.predict for a complete list of parameters.
    """
    pass

def set_verbosity_wrap(*args, **kwargs): # real signature unknown
    """ Control verbosity of libsvm library """
    pass

# classes

class ConvergenceWarning(UserWarning):
    """
    Custom warning to capture convergence problems
    
        .. versionchanged:: 0.18
           Moved from sklearn.utils.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000155DD8E59E8>'

__spec__ = None # (!) real value is "ModuleSpec(name='sklearn.svm.libsvm_sparse', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000155DD8E59E8>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\sklearn\\\\svm\\\\libsvm_sparse.cp37-win_amd64.pyd')"

__test__ = {}

