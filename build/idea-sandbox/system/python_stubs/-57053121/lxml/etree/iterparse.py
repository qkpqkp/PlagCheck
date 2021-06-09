# encoding: utf-8
# module lxml.etree
# from C:\Users\Doly\Anaconda3\lib\site-packages\lxml\etree.cp37-win_amd64.pyd
# by generator 1.147
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from .object import object

class iterparse(object):
    """
    iterparse(self, source, events=("end",), tag=None,                   attribute_defaults=False, dtd_validation=False,                   load_dtd=False, no_network=True, remove_blank_text=False,                   remove_comments=False, remove_pis=False, encoding=None,                   html=False, recover=None, huge_tree=False, schema=None)
    
        Incremental parser.
    
        Parses XML into a tree and generates tuples (event, element) in a
        SAX-like fashion. ``event`` is any of 'start', 'end', 'start-ns',
        'end-ns'.
    
        For 'start' and 'end', ``element`` is the Element that the parser just
        found opening or closing.  For 'start-ns', it is a tuple (prefix, URI) of
        a new namespace declaration.  For 'end-ns', it is simply None.  Note that
        all start and end events are guaranteed to be properly nested.
    
        The keyword argument ``events`` specifies a sequence of event type names
        that should be generated.  By default, only 'end' events will be
        generated.
    
        The additional ``tag`` argument restricts the 'start' and 'end' events to
        those elements that match the given tag.  The ``tag`` argument can also be
        a sequence of tags to allow matching more than one tag.  By default,
        events are generated for all elements.  Note that the 'start-ns' and
        'end-ns' events are not impacted by this restriction.
    
        The other keyword arguments in the constructor are mainly based on the
        libxml2 parser configuration.  A DTD will also be loaded if validation or
        attribute default values are requested.
    
        Available boolean keyword arguments:
         - attribute_defaults: read default attributes from DTD
         - dtd_validation: validate (if DTD is available)
         - load_dtd: use DTD for parsing
         - no_network: prevent network access for related files
         - remove_blank_text: discard blank text nodes
         - remove_comments: discard comments
         - remove_pis: discard processing instructions
         - strip_cdata: replace CDATA sections by normal text content (default: True)
         - compact: safe memory for short text content (default: True)
         - resolve_entities: replace entities by their text value (default: True)
         - huge_tree: disable security restrictions and support very deep trees
                      and very long text content (only affects libxml2 2.7+)
         - html: parse input as HTML (default: XML)
         - recover: try hard to parse through broken input (default: True for HTML,
                    False otherwise)
    
        Other keyword arguments:
         - encoding: override the document encoding
         - schema: an XMLSchema to validate against
    """
    def makeelement(self, _tag, attrib=None, nsmap=None, **_extra): # real signature unknown; restored from __doc__
        """
        makeelement(self, _tag, attrib=None, nsmap=None, **_extra)
        
                Creates a new element associated with this parser.
        """
        pass

    def set_element_class_lookup(self, lookup=None): # real signature unknown; restored from __doc__
        """
        set_element_class_lookup(self, lookup = None)
        
                Set a lookup scheme for element classes generated from this parser.
        
                Reset it by passing None or nothing.
        """
        pass

    def __init__(self, source, events=None, tag=None, attribute_defaults=False, dtd_validation=False, load_dtd=False, no_network=True, remove_blank_text=False, remove_comments=False, remove_pis=False, encoding=None, html=False, recover=None, huge_tree=False, schema=None): # real signature unknown; restored from __doc__
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        pass

    error_log = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The error log of the last (or current) parser run.
        """

    resolvers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The custom resolver registry of the last (or current) parser run.
        """

    root = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The version of the underlying XML parser."""


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002467EEF8DE0>'


