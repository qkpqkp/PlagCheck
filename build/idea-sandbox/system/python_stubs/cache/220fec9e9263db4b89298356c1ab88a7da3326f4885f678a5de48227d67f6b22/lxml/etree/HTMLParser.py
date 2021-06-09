# encoding: utf-8
# module lxml.etree
# from C:\Users\Doly\Anaconda3\lib\site-packages\lxml\etree.cp37-win_amd64.pyd
# by generator 1.147
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from ._FeedParser import _FeedParser

class HTMLParser(_FeedParser):
    """
    HTMLParser(self, encoding=None, remove_blank_text=False,                    remove_comments=False, remove_pis=False, strip_cdata=True,                    no_network=True, target=None, schema: XMLSchema =None,                    recover=True, compact=True, collect_ids=True, huge_tree=False)
    
        The HTML parser.
    
        This parser allows reading HTML into a normal XML tree.  By
        default, it can read broken (non well-formed) HTML, depending on
        the capabilities of libxml2.  Use the 'recover' option to switch
        this off.
    
        Available boolean keyword arguments:
    
        - recover            - try hard to parse through broken HTML (default: True)
        - no_network         - prevent network access for related files (default: True)
        - remove_blank_text  - discard empty text nodes that are ignorable (i.e. not actual text content)
        - remove_comments    - discard comments
        - remove_pis         - discard processing instructions
        - strip_cdata        - replace CDATA sections by normal text content (default: True)
        - compact            - save memory for short text content (default: True)
        - default_doctype    - add a default doctype even if it is not found in the HTML (default: True)
        - collect_ids        - use a hash table of XML IDs for fast access (default: True)
        - huge_tree          - disable security restrictions and support very deep trees
                               and very long text content (only affects libxml2 2.7+)
    
        Other keyword arguments:
    
        - encoding - override the document encoding
        - target   - a parser target object that will receive the parse events
        - schema   - an XMLSchema to validate against
    
        Note that you should avoid sharing parsers between threads for performance
        reasons.
    """
    def __init__(self, encoding=None, remove_blank_text=False, remove_comments=False, remove_pis=False, strip_cdata=True, no_network=True, target=None, schema=None, recover=True, compact=True, collect_ids=True, huge_tree=False): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002467EEF8BD0>'


