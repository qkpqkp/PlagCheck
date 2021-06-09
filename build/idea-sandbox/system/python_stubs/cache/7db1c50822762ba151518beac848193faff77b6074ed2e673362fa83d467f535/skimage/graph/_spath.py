# encoding: utf-8
# module skimage.graph._spath
# from C:\Users\Doly\Anaconda3\lib\site-packages\skimage\graph\_spath.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import skimage.graph._mcp as __skimage_graph__mcp


# functions

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_MCP_Diff(*args, **kwargs): # real signature unknown
    pass

# classes

class MCP_Diff(__skimage_graph__mcp.MCP):
    """
    MCP_Diff(costs, offsets=None, fully_connected=True)
    
        Find minimum-difference paths through an n-d costs array.
    
        See the documentation for MCP for full details. This class differs from
        MCP in that the cost of a path is not simply the sum of the costs along
        that path.
    
        This class instead assumes that the cost of moving from one point to
        another is the absolute value of the difference in the costs between the
        two points.
    """
    def __init__(self, costs, offsets=None, fully_connected=True): # real signature unknown; restored from __doc__
        """
        __init__(costs, offsets=None, fully_connected=True)
        
                See class documentation.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002166B6D0570>'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000002166B6C9BE0>'

__spec__ = None # (!) real value is "ModuleSpec(name='skimage.graph._spath', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000002166B6C9BE0>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\skimage\\\\graph\\\\_spath.cp37-win_amd64.pyd')"

__test__ = {}

