# encoding: utf-8
# module lxml.etree
# from C:\Users\Doly\Anaconda3\lib\site-packages\lxml\etree.cp37-win_amd64.pyd
# by generator 1.147
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from ._ElementTree import _ElementTree

class _XSLTResultTree(_ElementTree):
    """
    The result of an XSLT evaluation.
    
        Use ``str()`` or ``bytes()`` (or ``unicode()`` in Python 2.x) to serialise to a string,
        and the ``.write_output()`` method to write serialise to a file.
    """
    def write_output(self, file, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        write_output(self, file, *, compression=0)
        
                Serialise the XSLT output to a file or file-like object.
        
                As opposed to the generic ``.write()`` method, ``.write_output()`` serialises
                the result as defined by the ``<xsl:output>`` tag.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __unicode__(self, *args, **kwargs): # real signature unknown
        pass

    xslt_profile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return an ElementTree with profiling data for the stylesheet run.
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002467EF170F0>'


