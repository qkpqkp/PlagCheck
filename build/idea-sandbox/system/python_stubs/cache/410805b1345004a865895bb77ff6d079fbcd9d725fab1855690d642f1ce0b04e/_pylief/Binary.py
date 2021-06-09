# encoding: utf-8
# module _pylief
# from C:\Users\Doly\Anaconda3\lib\site-packages\_pylief.pyd
# by generator 1.147
# no doc

# imports
import _pylief.ELF as ELF # <module '_pylief.ELF'>
import _pylief.PE as PE # <module '_pylief.PE'>
import _pylief.MachO as MachO # <module '_pylief.MachO'>
import _pylief.OAT as OAT # <module '_pylief.OAT'>
import _pylief.VDEX as VDEX # <module '_pylief.VDEX'>
import _pylief.DEX as DEX # <module '_pylief.DEX'>
import _pylief.ART as ART # <module '_pylief.ART'>
import _pylief.Android as Android # <module '_pylief.Android'>
import pybind11_builtins as __pybind11_builtins


from .Object import Object

class Binary(Object):
    # no doc
    def get_content_from_virtual_address(self, virtual_address, size, va_type=None): # real signature unknown; restored from __doc__
        """
        get_content_from_virtual_address(self: _pylief.Binary, virtual_address: int, size: int, va_type: _pylief.VA_TYPES=VA_TYPES.AUTO) -> List[int]
        
        Return the content located at virtual address.
        
        Virtual address is specified in the first argument and size to read (in bytes) in the second.
        If the underlying binary is a PE, one can specify if the virtual address is a :attr:`~lief.Binary.VA_TYPES.RVA` or a :attr:`~lief.Binary.VA_TYPES.VA`. By default it is set to :attr:`~lief.Binary.VA_TYPES.AUTO`
        """
        return []

    def get_function_address(self, function_name): # real signature unknown; restored from __doc__
        """
        get_function_address(self: _pylief.Binary, function_name: str) -> int
        
        Return the address of the given function name
        """
        return 0

    def get_symbol(self, symbol_name): # real signature unknown; restored from __doc__
        """
        get_symbol(self: _pylief.Binary, symbol_name: str) -> LIEF::Symbol
        
        Return the :class:`~lief.Symbol` with the given ``name``
        """
        pass

    def has_symbol(self, symbol_name): # real signature unknown; restored from __doc__
        """
        has_symbol(self: _pylief.Binary, symbol_name: str) -> bool
        
        Check if a :class:`~lief.Symbol` with the given name exists
        """
        return False

    def patch_address(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        patch_address(*args, **kwargs)
        Overloaded function.
        
        1. patch_address(self: _pylief.Binary, address: int, patch_value: List[int], va_type: _pylief.VA_TYPES=VA_TYPES.AUTO) -> None
        
        Virtual address is specified in the first argument and the content in the second (as a list of bytes).
        If the underlying binary is a PE, one can specify if the virtual address is a :attr:`~lief.Binary.VA_TYPES.RVA` or a :attr:`~lief.Binary.VA_TYPES.VA`. By default it is set to :attr:`~lief.Binary.VA_TYPES.AUTO`
        
        2. patch_address(self: _pylief.Binary, address: int, patch_value: int, size: int=8, va_type: _pylief.VA_TYPES=VA_TYPES.AUTO) -> None
        
        Virtual address is specified in the first argument, integer in the second and sizeof the integer in third one.
        If the underlying binary is a PE, one can specify if the virtual address is a :attr:`~lief.Binary.VA_TYPES.RVA` or a :attr:`~lief.Binary.VA_TYPES.VA`. By default it is set to :attr:`~lief.Binary.VA_TYPES.AUTO`
        """
        pass

    def xref(self, Return_all, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ xref(self: _pylief.Binary, Return all **virtual address** that *use* the ``address`` given in parametervirtual_address: int) -> List[int] """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ __str__(self: _pylief.Binary) -> str """
        return ""

    abstract = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the :class:`~lief.Binary` object

.. warning::

	Getting this property modifies the ``__class__`` attribute so that the current binary looks like a :class:`~lief.Binary`.

	Use the :attr:`~lief.Binary.concrete` to get back to the original binary."""

    concrete = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return either :class:`lief.ELF.Binary`, :class:`lief.PE.Binary`, :class:`lief.MachO.Binary` object

"""

    entrypoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Binary's entrypoint"""

    exported_functions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return binary's exported functions (name)"""

    format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """File format :class:`~lief.EXE_FORMATS` of the underlying binary."""

    has_nx = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Check if the binary uses ``NX`` protection"""

    header = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Binary's header"""

    imported_functions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return binary's imported functions (name)"""

    is_pie = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Check if the binary is position independent"""

    libraries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return binary's imported libraries (name)"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Binary's name"""

    relocations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return an iterator over abstract :class:`~lief.Relocation`"""

    sections = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return a list in **read only** of binary's abstract :class:`~lief.Section`"""

    symbols = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return a list in **read only** of binary's abstract :class:`~lief.Symbol`"""


    VA_TYPES = None # (!) real value is "<class '_pylief.Binary.VA_TYPES'>"


