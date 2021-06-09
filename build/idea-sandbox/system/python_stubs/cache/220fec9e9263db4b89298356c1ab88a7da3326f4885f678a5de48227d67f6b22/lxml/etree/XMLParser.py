# encoding: utf-8
# module lxml.etree
# from C:\Users\Doly\Anaconda3\lib\site-packages\lxml\etree.cp37-win_amd64.pyd
# by generator 1.147
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from ._FeedParser import _FeedParser

class XMLParser(_FeedParser):
    """
    XMLParser(self, encoding=None, attribute_defaults=False, dtd_validation=False, load_dtd=False, no_network=True, ns_clean=False, recover=False, schema: XMLSchema =None, huge_tree=False, remove_blank_text=False, resolve_entities=True, remove_comments=False, remove_pis=False, strip_cdata=True, collect_ids=True, target=None, compact=True)
    
        The XML parser.
    
        Parsers can be supplied as additional argument to various parse
        functions of the lxml API.  A default parser is always available
        and can be replaced by a call to the global function
        'set_default_parser'.  New parsers can be created at any time
        without a major run-time overhead.
    
        The keyword arguments in the constructor are mainly based on the
        libxml2 parser configuration.  A DTD will also be loaded if DTD
        validation or attribute default values are requested (unless you
        additionally provide an XMLSchema from which the default
        attributes can be read).
    
        Available boolean keyword arguments:
    
        - attribute_defaults - inject default attributes from DTD or XMLSchema
        - dtd_validation     - validate against a DTD referenced by the document
        - load_dtd           - use DTD for parsing
        - no_network         - prevent network access for related files (default: True)
        - ns_clean           - clean up redundant namespace declarations
        - recover            - try hard to parse through broken XML
        - remove_blank_text  - discard blank text nodes that appear ignorable
        - remove_comments    - discard comments
        - remove_pis         - discard processing instructions
        - strip_cdata        - replace CDATA sections by normal text content (default: True)
        - compact            - save memory for short text content (default: True)
        - collect_ids        - use a hash table of XML IDs for fast access (default: True, always True with DTD validation)
        - resolve_entities   - replace entities by their text value (default: True)
        - huge_tree          - disable security restrictions and support very deep trees
                               and very long text content (only affects libxml2 2.7+)
    
        Other keyword arguments:
    
        - encoding - override the document encoding
        - target   - a parser target object that will receive the parse events
        - schema   - an XMLSchema to validate against
    
        Note that you should avoid sharing parsers between threads.  While this is
        not harmful, it is more efficient to use separate parsers.  This does not
        apply to the default parser.
    """
    def __init__(self, encoding=None, attribute_defaults=False, dtd_validation=False, load_dtd=False, no_network=True, ns_clean=False, recover=False, schema=None, huge_tree=False, remove_blank_text=False, resolve_entities=True, remove_comments=False, remove_pis=False, strip_cdata=True, collect_ids=True, target=None, compact=True): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002467EEF8B40>'


