# encoding: utf-8
# module lxml.etree
# from C:\Users\Doly\Anaconda3\lib\site-packages\lxml\etree.cp37-win_amd64.pyd
# by generator 1.147
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from .object import object

class CDATA(object):
    """
    CDATA(data)
    
        CDATA factory.  This factory creates an opaque data object that
        can be used to set Element text.  The usual way to use it is::
    
            >>> el = Element('content')
            >>> el.text = CDATA('a string')
    
            >>> print(el.text)
            a string
            >>> print(tostring(el, encoding="unicode"))
            <content><![CDATA[a string]]></content>
    """
    def __init__(self, data): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


