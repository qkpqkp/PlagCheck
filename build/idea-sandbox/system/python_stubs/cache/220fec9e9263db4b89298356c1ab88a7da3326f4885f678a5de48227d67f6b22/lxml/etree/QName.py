# encoding: utf-8
# module lxml.etree
# from C:\Users\Doly\Anaconda3\lib\site-packages\lxml\etree.cp37-win_amd64.pyd
# by generator 1.147
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from .object import object

class QName(object):
    """
    QName(text_or_uri_or_element, tag=None)
    
        QName wrapper for qualified XML names.
    
        Pass a tag name by itself or a namespace URI and a tag name to
        create a qualified name.  Alternatively, pass an Element to
        extract its tag name.  ``None`` as first argument is ignored in
        order to allow for generic 2-argument usage.
    
        The ``text`` property holds the qualified name in
        ``{namespace}tagname`` notation.  The ``namespace`` and
        ``localname`` properties hold the respective parts of the tag
        name.
    
        You can pass QName objects wherever a tag name is expected.  Also,
        setting Element text from a QName will resolve the namespace prefix
        on assignment and set a qualified text value.  This is helpful in XML
        languages like SOAP or XML-Schema that use prefixed tag names in
        their text content.
    """
    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, text_or_uri_or_element, tag=None): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    localname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    namespace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



