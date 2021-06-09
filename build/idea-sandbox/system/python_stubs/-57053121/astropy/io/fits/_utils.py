# encoding: utf-8
# module astropy.io.fits._utils
# from C:\Users\Doly\Anaconda3\lib\site-packages\astropy\io\fits\_utils.cp37-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

# functions

def parse_header(*args, **kwargs): # real signature unknown
    """
    Fast (and incomplete) parser for FITS headers.
    
        This parser only reads the standard 8 character keywords, and ignores the
        CONTINUE, COMMENT, HISTORY and HIERARCH cards. The goal is to find quickly
        the structural keywords needed to build the HDU objects.
    
        The implementation is straightforward: first iterate on the 2880-bytes
        blocks, then iterate on the 80-bytes cards, find the value separator, and
        store the parsed (keyword, card image) in a dictionary.
    """
    pass

# classes

class OrderedDict(dict):
    """ Dictionary that remembers insertion order """
    def clear(self): # real signature unknown; restored from __doc__
        """ od.clear() -> None.  Remove all items from od. """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ od.copy() -> a shallow copy of od """
        pass

    @classmethod
    def fromkeys(cls, *args, **kwargs): # real signature unknown
        """ Create a new ordered dictionary with keys from iterable and values set to value. """
        pass

    def items(self, *args, **kwargs): # real signature unknown
        pass

    def keys(self, *args, **kwargs): # real signature unknown
        pass

    def move_to_end(self, *args, **kwargs): # real signature unknown
        """
        Move an existing element to the end (or beginning if last is false).
        
        Raise KeyError if the element does not exist.
        """
        pass

    def pop(self, k, d=None): # real signature unknown; restored from __doc__
        """
        od.pop(k[,d]) -> v, remove specified key and return the corresponding
                value.  If key is not found, d is returned if given, otherwise KeyError
                is raised.
        """
        pass

    def popitem(self, *args, **kwargs): # real signature unknown
        """
        Remove and return a (key, value) pair from the dictionary.
        
        Pairs are returned in LIFO order if last is true or FIFO order if false.
        """
        pass

    def setdefault(self, *args, **kwargs): # real signature unknown
        """
        Insert key with a value of default if key is not in the dictionary.
        
        Return the value for key if key is in the dictionary, else default.
        """
        pass

    def update(self, *args, **kwargs): # real signature unknown
        pass

    def values(self, *args, **kwargs): # real signature unknown
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Return state information for pickling """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __reversed__(self): # real signature unknown; restored from __doc__
        """ od.__reversed__() <==> reversed(od) """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        pass

    __dict__ = None # (!) real value is "mappingproxy({'__repr__': <slot wrapper '__repr__' of 'collections.OrderedDict' objects>, '__lt__': <slot wrapper '__lt__' of 'collections.OrderedDict' objects>, '__le__': <slot wrapper '__le__' of 'collections.OrderedDict' objects>, '__eq__': <slot wrapper '__eq__' of 'collections.OrderedDict' objects>, '__ne__': <slot wrapper '__ne__' of 'collections.OrderedDict' objects>, '__gt__': <slot wrapper '__gt__' of 'collections.OrderedDict' objects>, '__ge__': <slot wrapper '__ge__' of 'collections.OrderedDict' objects>, '__iter__': <slot wrapper '__iter__' of 'collections.OrderedDict' objects>, '__init__': <slot wrapper '__init__' of 'collections.OrderedDict' objects>, '__setitem__': <slot wrapper '__setitem__' of 'collections.OrderedDict' objects>, '__delitem__': <slot wrapper '__delitem__' of 'collections.OrderedDict' objects>, 'fromkeys': <method 'fromkeys' of 'collections.OrderedDict' objects>, '__sizeof__': <method '__sizeof__' of 'collections.OrderedDict' objects>, '__reduce__': <method '__reduce__' of 'collections.OrderedDict' objects>, 'setdefault': <method 'setdefault' of 'collections.OrderedDict' objects>, 'pop': <method 'pop' of 'collections.OrderedDict' objects>, 'popitem': <method 'popitem' of 'collections.OrderedDict' objects>, 'keys': <method 'keys' of 'collections.OrderedDict' objects>, 'values': <method 'values' of 'collections.OrderedDict' objects>, 'items': <method 'items' of 'collections.OrderedDict' objects>, 'update': <method 'update' of 'collections.OrderedDict' objects>, 'clear': <method 'clear' of 'collections.OrderedDict' objects>, 'copy': <method 'copy' of 'collections.OrderedDict' objects>, '__reversed__': <method '__reversed__' of 'collections.OrderedDict' objects>, 'move_to_end': <method 'move_to_end' of 'collections.OrderedDict' objects>, '__dict__': <attribute '__dict__' of 'collections.OrderedDict' objects>, '__doc__': 'Dictionary that remembers insertion order', '__hash__': None})"
    __hash__ = None


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001DD7F113518>'

__spec__ = None # (!) real value is "ModuleSpec(name='astropy.io.fits._utils', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001DD7F113518>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\astropy\\\\io\\\\fits\\\\_utils.cp37-win_amd64.pyd')"

__test__ = {}

