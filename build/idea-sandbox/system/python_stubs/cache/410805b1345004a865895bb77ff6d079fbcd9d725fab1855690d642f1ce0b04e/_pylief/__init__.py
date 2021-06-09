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


# Variables with simple values

__version__ = '0.9.0-'

# functions

def art_version(*args, **kwargs): # real signature unknown; restored from __doc__
    """
    art_version(*args, **kwargs)
    Overloaded function.
    
    1. art_version(filename: str) -> int
    
    Return the ART version of the given file
    
    2. art_version(raw: List[int]) -> int
    
    Return the ART version of the raw data
    """
    pass

def breakp(): # real signature unknown; restored from __doc__
    """
    breakp() -> object
    
    Trigger 'pdb.set_trace()'
    """
    return object()

def dex_version(*args, **kwargs): # real signature unknown; restored from __doc__
    """
    dex_version(*args, **kwargs)
    Overloaded function.
    
    1. dex_version(filename: str) -> int
    
    Return the OAT version of the given file
    
    2. dex_version(raw: List[int]) -> int
    
    Return the DEX version of the raw data
    """
    pass

def hash(*args, **kwargs): # real signature unknown; restored from __doc__
    """
    hash(*args, **kwargs)
    Overloaded function.
    
    1. hash(arg0: _pylief.Object) -> int
    
    2. hash(arg0: List[int]) -> int
    """
    pass

def is_art(*args, **kwargs): # real signature unknown; restored from __doc__
    """
    is_art(*args, **kwargs)
    Overloaded function.
    
    1. is_art(filename: str) -> bool
    
    Check if the given file is an ``ART`` (from filename)
    
    2. is_art(raw: List[int]) -> bool
    
    Check if the given raw data is an ``ART``
    """
    pass

def is_dex(*args, **kwargs): # real signature unknown; restored from __doc__
    """
    is_dex(*args, **kwargs)
    Overloaded function.
    
    1. is_dex(filename: str) -> bool
    
    Check if the given file is a ``DEX`` (from filename)
    
    2. is_dex(raw: List[int]) -> bool
    
    Check if the given raw data is a ``DEX``
    """
    pass

def is_elf(*args, **kwargs): # real signature unknown; restored from __doc__
    """
    is_elf(*args, **kwargs)
    Overloaded function.
    
    1. is_elf(filename: str) -> bool
    
    Check if the given file is an ``ELF``
    
    2. is_elf(raw: List[int]) -> bool
    
    Check if the given raw data is an ``ELF``
    """
    pass

def is_macho(*args, **kwargs): # real signature unknown; restored from __doc__
    """
    is_macho(*args, **kwargs)
    Overloaded function.
    
    1. is_macho(filename: str) -> bool
    
    Check if the given file is a ``MachO`` (from filename)
    
    2. is_macho(raw: List[int]) -> bool
    
    Check if the given raw data is a ``MachO``
    """
    pass

def is_oat(*args, **kwargs): # real signature unknown; restored from __doc__
    """
    is_oat(*args, **kwargs)
    Overloaded function.
    
    1. is_oat(filename: str) -> bool
    
    Check if the given file is an ``OAT`` (from filename)
    
    2. is_oat(raw: List[int]) -> bool
    
    Check if the given raw data is an ``OAT``
    
    3. is_oat(elf: _pylief.ELF.Binary) -> bool
    
    Check if the given :class:`~lief.ELF.Binary` is an ``OAT``
    """
    pass

def is_pe(*args, **kwargs): # real signature unknown; restored from __doc__
    """
    is_pe(*args, **kwargs)
    Overloaded function.
    
    1. is_pe(filename: str) -> bool
    
    Check if the given file is a ``PE`` (from filename)
    
    2. is_pe(raw: List[int]) -> bool
    
    Check if the given raw data is a ``PE``
    """
    pass

def is_vdex(*args, **kwargs): # real signature unknown; restored from __doc__
    """
    is_vdex(*args, **kwargs)
    Overloaded function.
    
    1. is_vdex(filename: str) -> bool
    
    Check if the given file is a ``VDEX`` (from filename)
    
    2. is_vdex(raw: List[int]) -> bool
    
    Check if the given raw data is a ``VDEX``
    """
    pass

def oat_version(*args, **kwargs): # real signature unknown; restored from __doc__
    """
    oat_version(*args, **kwargs)
    Overloaded function.
    
    1. oat_version(filename: str) -> int
    
    Return the OAT version of the given file
    
    2. oat_version(raw: List[int]) -> int
    
    Return the OAT version of the raw data
    
    3. oat_version(elf: _pylief.ELF.Binary) -> int
    
    Return the OAT version of the given :class:`~lief.ELF.Binary`
    """
    pass

def parse(*args, **kwargs): # real signature unknown; restored from __doc__
    """
    parse(*args, **kwargs)
    Overloaded function.
    
    1. parse(filepath: str) -> _pylief.Binary
    
    Parse the given binary and return a :class:`~lief.Binary` object
    
    2. parse(raw: List[int], name: str='') -> _pylief.Binary
    
    Parse the given binary and return a :class:`~lief.Binary` object
    
    3. parse(io: object, name: str='') -> _pylief.Binary
    """
    pass

def shell(): # real signature unknown; restored from __doc__
    """
    shell() -> object
    
    Drop into an IPython Interpreter
    """
    return object()

def to_json(arg0): # real signature unknown; restored from __doc__
    """ to_json(arg0: _pylief.Object) -> str """
    return ""

def to_json_from_abstract(arg0): # real signature unknown; restored from __doc__
    """ to_json_from_abstract(arg0: _pylief.Object) -> str """
    return ""

def vdex_version(*args, **kwargs): # real signature unknown; restored from __doc__
    """
    vdex_version(*args, **kwargs)
    Overloaded function.
    
    1. vdex_version(filename: str) -> int
    
    Return the VDEX version of the given file
    
    2. vdex_version(raw: List[int]) -> int
    
    Return the VDEX version of the raw data
    """
    pass

# classes

