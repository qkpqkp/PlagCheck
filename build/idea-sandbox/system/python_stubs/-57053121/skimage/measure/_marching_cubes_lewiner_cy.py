# encoding: utf-8
# module skimage.measure._marching_cubes_lewiner_cy
# from C:\Users\Doly\Anaconda3\lib\site-packages\skimage\measure\_marching_cubes_lewiner_cy.cp37-win_amd64.pyd
# by generator 1.147
"""
This is an implementation of the marching cubes algorithm proposed in:

Efficient implementation of Marching Cubes' cases with topological guarantees.
Thomas Lewiner, Helio Lopes, Antonio Wilson Vieira and Geovan Tavares.
Journal of Graphics Tools 8(2): pp. 1-15 (december 2003)

This algorithm has the advantage that it provides topologically correct
results, and the algorithms implementation is relatively simple. Most
of the magic is in the lookup tables, which are provided as open source.

Originally implemented in C++ by Thomas Lewiner in 2002, ported to Cython
by Almar Klein in 2012. Adapted for scikit-image in 2016.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\Doly\Anaconda3\lib\site-packages\numpy\__init__.py

# functions

def marching_cubes(im, double_isovalue, LutProvider_luts, int_st=1, int_classic=0): # real signature unknown; restored from __doc__
    """
    marching_cubes(im, double isovalue, LutProvider luts, int st=1, int classic=0)
        This is the main entry to apply marching cubes.
        Returns (vertices, faces, normals, values)
    """
    pass

def remove_degenerate_faces(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_LutProvider(*args, **kwargs): # real signature unknown
    pass

# classes

class Cell(object):
    """
    Class to keep track of some stuff during the whole cube marching
        procedure.
    
        This "struct" keeps track of the current cell location, and the values
        of corners of the cube. Gradients for the cube corners are calculated
        when needed.
    
        Additionally, it keeps track of the array of vertices, faces and normals.
    
        Notes on vertices
        -----------------
        The vertices are stored in a C-array that is increased in size with
        factors of two if needed. The same applies to the faces and normals.
    
        Notes on faces
        --------------
        To keep track of the vertices already defined, this class maintains
        two faceLayer arrays. faceLayer1 is of the current layer (z-value)
        and faceLayer2 is of the next. Both face layers have 4 elements per
        cell in that layer, 1 for each unique edge per cell (see
        get_index_in_facelayer). These are initialized as -1, and set to the
        index in the vertex array when a new vertex is created.
        In summary, this allows us to keep track of the already created
        vertices without keeping a very big array.
    
        Notes on normals
        ----------------
        The normal is simply defined as the gradient. Each time that a face is
        created, we also add the gradient of that vertex position to the
        normals array. The gradients are all calculated from the differences between
        the 8 corners of the current cube, but because the final value of a normal
        was contributed from multiple cells, the normals are quite accurate.
    """
    def get_faces(self, *args, **kwargs): # real signature unknown
        pass

    def get_normals(self, *args, **kwargs): # real signature unknown
        """
        Get the final normals array.
                The normals are normalized to unit length.
        """
        pass

    def get_values(self, *args, **kwargs): # real signature unknown
        pass

    def get_vertices(self, *args, **kwargs): # real signature unknown
        """ Get the final vertex array. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001CBED406060>'


class Lut(object):
    """
    Representation of a lookup table.
        The tables are initially defined as numpy arrays. On initialization,
        this class converts them to a C array for fast access.
        This class defines functions to look up values using 1, 2 or 3 indices.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001CBED406090>'


class LutProvider(object):
    """
    Class that provides a common interface to the many lookup tables
        used by the algorithm.
        All the lists of lut names are autogenerated to prevent human error.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001CBED407518>'

__spec__ = None # (!) real value is "ModuleSpec(name='skimage.measure._marching_cubes_lewiner_cy', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001CBED407518>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\skimage\\\\measure\\\\_marching_cubes_lewiner_cy.cp37-win_amd64.pyd')"

__test__ = {}

