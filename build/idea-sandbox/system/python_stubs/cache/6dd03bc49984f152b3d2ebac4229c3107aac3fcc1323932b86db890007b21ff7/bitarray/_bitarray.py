# encoding: utf-8
# module bitarray._bitarray
# from C:\Users\Doly\Anaconda3\lib\site-packages\bitarray\_bitarray.cp37-win_amd64.pyd
# by generator 1.147
# no doc
# no imports

# functions

def bitdiff(a, b): # real signature unknown; restored from __doc__
    """
    bitdiff(a, b) -> int
    
    Return the difference between two bitarrays a and b.
    This is function does the same as (a ^ b).count(), but is more memory
    efficient, as no intermediate bitarray object gets created
    """
    return 0

def bits2bytes(n): # real signature unknown; restored from __doc__
    """
    bits2bytes(n) -> int
    
    Return the number of bytes necessary to store n bits.
    """
    return 0

def _sysinfo(): # real signature unknown; restored from __doc__
    """
    _sysinfo() -> tuple
    
    tuple(sizeof(void *),
          sizeof(size_t),
          sizeof(Py_ssize_t),
          sizeof(idx_t),
          PY_SSIZE_T_MAX)
    """
    return ()

# classes

class _bitarray(object):
    # no doc
    def all(self): # real signature unknown; restored from __doc__
        """
        all() -> bool
        
        Returns True when all bits in the array are True.
        """
        return False

    def any(self): # real signature unknown; restored from __doc__
        """
        any() -> bool
        
        Returns True when any bit in the array is True.
        """
        return False

    def append(self, item): # real signature unknown; restored from __doc__
        """
        append(item)
        
        Append the value bool(item) to the end of the bitarray.
        """
        pass

    def buffer_info(self): # real signature unknown; restored from __doc__
        """
        buffer_info() -> tuple
        
        Return a tuple (address, size, endianness, unused, allocated) giving the
        current memory address, the size (in bytes) used to hold the bitarray's
        contents, the bit endianness as a string, the number of unused bits
        (e.g. a bitarray of length 11 will have a buffer size of 2 bytes and
        5 unused bits), and the size (in bytes) of the allocated memory.
        """
        return ()

    def bytereverse(self): # real signature unknown; restored from __doc__
        """
        bytereverse()
        
        For all bytes representing the bitarray, reverse the bit order (in-place).
        Note: This method changes the actual machine values representing the
        bitarray; it does not change the endianness of the bitarray object.
        """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """
        copy() -> bitarray
        
        Return a copy of the bitarray.
        """
        pass

    def count(self, value=None): # real signature unknown; restored from __doc__
        """
        count([value]) -> int
        
        Return number of occurrences of value (defaults to True) in the bitarray.
        """
        return 0

    def decode(self, code): # real signature unknown; restored from __doc__
        """
        decode(code) -> list
        
        Given a prefix code (a dict mapping symbols to bitarrays),
        decode the content of the bitarray and return it as a list of symbols.
        """
        return []

    def encode(self, code, iterable): # real signature unknown; restored from __doc__
        """
        encode(code, iterable)
        
        Given a prefix code (a dict mapping symbols to bitarrays),
        iterate over the iterable object with symbols, and extend the bitarray
        with the corresponding bitarray for each symbols.
        """
        pass

    def endian(self): # real signature unknown; restored from __doc__
        """
        endian() -> string
        
        Return the bit endianness as a string (either 'little' or 'big').
        """
        return ""

    def extend(self, p_object): # real signature unknown; restored from __doc__
        """
        extend(object)
        
        Append bits to the end of the bitarray.  The objects which can be passed
        to this method are the same iterable objects which can given to a bitarray
        object upon initialization.
        """
        pass

    def fill(self): # real signature unknown; restored from __doc__
        """
        fill() -> int
        
        Adds zeros to the end of the bitarray, such that the length of the bitarray
        will be a multiple of 8.  Returns the number of bits added (0..7).
        """
        return 0

    def frombytes(self, bytes): # real signature unknown; restored from __doc__
        """
        frombytes(bytes)
        
        Append from a byte string, interpreted as machine values.
        """
        pass

    def fromfile(self, f, n=None): # real signature unknown; restored from __doc__
        """
        fromfile(f, [n])
        
        Read n bytes from the file object f and append them to the bitarray
        interpreted as machine values.  When n is omitted, as many bytes are
        read until EOF is reached.
        """
        pass

    def index(self, value, start=None, stop=None): # real signature unknown; restored from __doc__
        """
        index(value, [start, [stop]]) -> int
        
        Return index of the first occurrence of bool(value) in the bitarray.
        Raises ValueError if the value is not present.
        """
        return 0

    def insert(self, i, item): # real signature unknown; restored from __doc__
        """
        insert(i, item)
        
        Insert bool(item) into the bitarray before position i.
        """
        pass

    def invert(self): # real signature unknown; restored from __doc__
        """
        invert()
        
        Invert all bits in the array (in-place),
        i.e. convert each 1-bit into a 0-bit and vice versa.
        """
        pass

    def iterdecode(self, code): # real signature unknown; restored from __doc__
        """
        iterdecode(code) -> iterator
        
        Given a prefix code (a dict mapping symbols to bitarrays),
        decode the content of the bitarray and return an iterator over
        the symbols.
        """
        pass

    def itersearch(self, bitarray): # real signature unknown; restored from __doc__
        """
        itersearch(bitarray) -> iterator
        
        Searches for the given a bitarray in self, and return an iterator over
        the start positions where bitarray matches self.
        """
        pass

    def length(self): # real signature unknown; restored from __doc__
        """
        length() -> int
        
        Return the length, i.e. number of bits stored in the bitarray.
        This method is preferred over __len__ (used when typing ``len(a)``),
        since __len__ will fail for a bitarray object with 2^31 or more elements
        on a 32bit machine, whereas this method will return the correct value,
        on 32bit and 64bit machines.
        """
        return 0

    def pack(self, bytes): # real signature unknown; restored from __doc__
        """
        pack(bytes)
        
        Extend the bitarray from a byte string, where each characters corresponds to
        a single bit.  The character b'\x00' maps to bit 0 and all other characters
        map to bit 1.
        This method, as well as the unpack method, are meant for efficient
        transfer of data between bitarray objects to other python objects
        (for example NumPy's ndarray object) which have a different view of memory.
        """
        pass

    def pop(self, i=None): # real signature unknown; restored from __doc__
        """
        pop([i]) -> item
        
        Return the i-th (default last) element and delete it from the bitarray.
        Raises IndexError if bitarray is empty or index is out of range.
        """
        pass

    def remove(self, item): # real signature unknown; restored from __doc__
        """
        remove(item)
        
        Remove the first occurrence of bool(item) in the bitarray.
        Raises ValueError if item is not present.
        """
        pass

    def reverse(self): # real signature unknown; restored from __doc__
        """
        reverse()
        
        Reverse the order of bits in the array (in-place).
        """
        pass

    def search(self, bitarray, limit=None): # real signature unknown; restored from __doc__
        """
        search(bitarray, [limit]) -> list
        
        Searches for the given a bitarray in self, and returns the start positions
        where bitarray matches self as a list.
        The optional argument limits the number of search results to the integer
        specified.  By default, all search results are returned.
        """
        return []

    def setall(self, value): # real signature unknown; restored from __doc__
        """
        setall(value)
        
        Set all bits in the bitarray to bool(value).
        """
        pass

    def sort(self, reverse=False): # real signature unknown; restored from __doc__
        """
        sort(reverse=False)
        
        Sort the bits in the array (in-place).
        """
        pass

    def to01(self): # real signature unknown; restored from __doc__
        """
        to01() -> string
        
        Return a string containing '0's and '1's, representing the bits in the
        bitarray object.
        Note: To extend a bitarray from a string containing '0's and '1's,
        use the extend method.
        """
        return ""

    def tobytes(self): # real signature unknown; restored from __doc__
        """
        tobytes() -> bytes
        
        Return the byte representation of the bitarray.
        When the length of the bitarray is not a multiple of 8, the few remaining
        bits (1..7) are set to 0.
        """
        return b""

    def tofile(self, f): # real signature unknown; restored from __doc__
        """
        tofile(f)
        
        Write all bits (as machine values) to the file object f.
        When the length of the bitarray is not a multiple of 8,
        the remaining bits (1..7) are set to 0.
        """
        pass

    def tolist(self): # real signature unknown; restored from __doc__
        """
        tolist() -> list
        
        Return an ordinary list with the items in the bitarray.
        Note that the list object being created will require 32 or 64 times more
        memory than the bitarray object, which may cause a memory error if the
        bitarray is very large.
        Also note that to extend a bitarray with elements from a list,
        use the extend method.
        """
        return []

    def unpack(self, zero=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        unpack(zero=b'\x00', one=b'\xff') -> bytes
        
        Return a byte string containing one character for each bit in the bitarray,
        using the specified mapping.
        See also the pack method.
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        pass

    def __contains__(self, x): # real signature unknown; restored from __doc__
        """
        __contains__(x) -> bool
        
        Return True if bitarray contains x, False otherwise.
        The value x may be a boolean (or integer between 0 and 1), or a bitarray.
        """
        return False

    def __copy__(self, *args, **kwargs): # real signature unknown
        """
        copy() -> bitarray
        
        Return a copy of the bitarray.
        """
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        """
        copy() -> bitarray
        
        Return a copy of the bitarray.
        """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __iadd__(self, *args, **kwargs): # real signature unknown
        pass

    def __iand__(self, *args, **kwargs): # real signature unknown
        pass

    def __imul__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        pass

    def __ior__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __ixor__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """
        __len__() -> int
        
        Return the length, i.e. number of bits stored in the bitarray.
        This method will fail for a bitarray object with 2^31 or more elements
        on a 32bit machine.  Use bitarray.length() instead.
        """
        return 0

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ state information for pickling """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        pass

    __hash__ = None


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000002EBE8505F28>'

__spec__ = None # (!) real value is "ModuleSpec(name='bitarray._bitarray', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000002EBE8505F28>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\bitarray\\\\_bitarray.cp37-win_amd64.pyd')"

