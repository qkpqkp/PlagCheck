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


class ARCHITECTURES(__pybind11_builtins.pybind11_object):
    # no doc
    def __eq__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __eq__(*args, **kwargs)
        Overloaded function.
        
        1. __eq__(self: _pylief.ARCHITECTURES, arg0: _pylief.ARCHITECTURES) -> bool
        
        2. __eq__(self: _pylief.ARCHITECTURES, arg0: int) -> bool
        """
        pass

    def __getstate__(self): # real signature unknown; restored from __doc__
        """ __getstate__(self: _pylief.ARCHITECTURES) -> tuple """
        return ()

    def __hash__(self): # real signature unknown; restored from __doc__
        """ __hash__(self: _pylief.ARCHITECTURES) -> int """
        return 0

    def __init__(self, arg0): # real signature unknown; restored from __doc__
        """ __init__(self: _pylief.ARCHITECTURES, arg0: int) -> None """
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ __int__(self: _pylief.ARCHITECTURES) -> int """
        return 0

    def __ne__(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        __ne__(*args, **kwargs)
        Overloaded function.
        
        1. __ne__(self: _pylief.ARCHITECTURES, arg0: _pylief.ARCHITECTURES) -> bool
        
        2. __ne__(self: _pylief.ARCHITECTURES, arg0: int) -> bool
        """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ __repr__(self: _pylief.ARCHITECTURES) -> str """
        return ""

    def __setstate__(self, arg0): # real signature unknown; restored from __doc__
        """ __setstate__(self: _pylief.ARCHITECTURES, arg0: tuple) -> None """
        pass

    ARM = ARCHITECTURES.ARM
    ARM64 = ARCHITECTURES.ARM64 # (!) forward: ARM64, real value is 'ARCHITECTURES.ARM64'
    INTEL = ARCHITECTURES.INTEL # (!) forward: INTEL, real value is 'ARCHITECTURES.INTEL'
    MIPS = ARCHITECTURES.MIPS # (!) forward: MIPS, real value is 'ARCHITECTURES.MIPS'
    NONE = ARCHITECTURES.NONE
    PPC = ARCHITECTURES.PPC # (!) forward: PPC, real value is 'ARCHITECTURES.PPC'
    SPARC = ARCHITECTURES.SPARC # (!) forward: SPARC, real value is 'ARCHITECTURES.SPARC'
    SYSZ = ARCHITECTURES.SYSZ # (!) forward: SYSZ, real value is 'ARCHITECTURES.SYSZ'
    X86 = ARCHITECTURES.X86 # (!) forward: X86, real value is 'ARCHITECTURES.X86'
    XCODE = ARCHITECTURES.XCODE # (!) forward: XCODE, real value is 'ARCHITECTURES.XCODE'
    __members__ = {
        'ARM': '<failed to retrieve the value>',
        'ARM64': '<failed to retrieve the value>',
        'INTEL': '<failed to retrieve the value>',
        'MIPS': '<failed to retrieve the value>',
        'NONE': '<failed to retrieve the value>',
        'PPC': '<failed to retrieve the value>',
        'SPARC': '<failed to retrieve the value>',
        'SYSZ': '<failed to retrieve the value>',
        'X86': '<failed to retrieve the value>',
        'XCODE': '<failed to retrieve the value>',
    }


