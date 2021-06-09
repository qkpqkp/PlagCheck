# encoding: utf-8
# module lxml.etree
# from C:\Users\Doly\Anaconda3\lib\site-packages\lxml\etree.cp37-win_amd64.pyd
# by generator 1.147
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from .object import object

class _XPathEvaluatorBase(object):
    # no doc
    def evaluate(self, _eval_arg, **_variables): # real signature unknown; restored from __doc__
        """
        evaluate(self, _eval_arg, **_variables)
        
                Evaluate an XPath expression.
        
                Instead of calling this method, you can also call the evaluator object
                itself.
        
                Variables may be provided as keyword arguments.  Note that namespaces
                are currently not supported for variables.
        
                :deprecated: call the object, not its method.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    error_log = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002467EEF8F00>'


