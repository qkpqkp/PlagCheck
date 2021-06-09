# encoding: utf-8
# module lxml.etree
# from C:\Users\Doly\Anaconda3\lib\site-packages\lxml\etree.cp37-win_amd64.pyd
# by generator 1.147
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from ._XPathEvaluatorBase import _XPathEvaluatorBase

class XPathElementEvaluator(_XPathEvaluatorBase):
    """
    XPathElementEvaluator(self, element, namespaces=None, extensions=None, regexp=True, smart_strings=True)
        Create an XPath evaluator for an element.
    
        Absolute XPath expressions (starting with '/') will be evaluated against
        the ElementTree as returned by getroottree().
    
        Additional namespace declarations can be passed with the
        'namespace' keyword argument.  EXSLT regular expression support
        can be disabled with the 'regexp' boolean keyword (defaults to
        True).  Smart strings will be returned for string results unless
        you pass ``smart_strings=False``.
    """
    def register_namespace(self, *args, **kwargs): # real signature unknown
        """ Register a namespace with the XPath context. """
        pass

    def register_namespaces(self, *args, **kwargs): # real signature unknown
        """ Register a prefix -> uri dict. """
        pass

    def __call__(self, _path, **_variables): # real signature unknown; restored from __doc__
        """
        __call__(self, _path, **_variables)
        
                Evaluate an XPath expression on the document.
        
                Variables may be provided as keyword arguments.  Note that namespaces
                are currently not supported for variables.
        
                Absolute XPath expressions (starting with '/') will be evaluated
                against the ElementTree as returned by getroottree().
        """
        pass

    def __init__(self, element, namespaces=None, extensions=None, regexp=True, smart_strings=True): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002467EEF8F30>'


