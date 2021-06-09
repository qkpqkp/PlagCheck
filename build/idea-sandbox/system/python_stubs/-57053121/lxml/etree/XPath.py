# encoding: utf-8
# module lxml.etree
# from C:\Users\Doly\Anaconda3\lib\site-packages\lxml\etree.cp37-win_amd64.pyd
# by generator 1.147
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from ._XPathEvaluatorBase import _XPathEvaluatorBase

class XPath(_XPathEvaluatorBase):
    """
    XPath(self, path, namespaces=None, extensions=None, regexp=True, smart_strings=True)
        A compiled XPath expression that can be called on Elements and ElementTrees.
    
        Besides the XPath expression, you can pass prefix-namespace
        mappings and extension functions to the constructor through the
        keyword arguments ``namespaces`` and ``extensions``.  EXSLT
        regular expression support can be disabled with the 'regexp'
        boolean keyword (defaults to True).  Smart strings will be
        returned for string results unless you pass
        ``smart_strings=False``.
    """
    def __call__(self, _etree_or_element, **_variables): # real signature unknown; restored from __doc__
        """ __call__(self, _etree_or_element, **_variables) """
        pass

    def __init__(self, path, namespaces=None, extensions=None, regexp=True, smart_strings=True): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The literal XPath expression.
        """


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002467EEF8F90>'


