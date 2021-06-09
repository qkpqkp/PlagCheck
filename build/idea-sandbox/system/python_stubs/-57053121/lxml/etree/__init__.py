# encoding: utf-8
# module lxml.etree
# from C:\Users\Doly\Anaconda3\lib\site-packages\lxml\etree.cp37-win_amd64.pyd
# by generator 1.147
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

# Variables with simple values

DEBUG = 1

__docformat__ = 'restructuredtext en'

__version__ = '4.3.4'

# functions

def adopt_external_document(capsule, parser=None): # real signature unknown; restored from __doc__
    """
    adopt_external_document(capsule, parser=None)
    
        Unpack a libxml2 document pointer from a PyCapsule and wrap it in an
        lxml ElementTree object.
    
        This allows external libraries to build XML/HTML trees using libxml2
        and then pass them efficiently into lxml for further processing.
    
        If a ``parser`` is provided, it will be used for configuring the
        lxml document.  No parsing will be done.
    
        The capsule must have the name ``"libxml2:xmlDoc"`` and its pointer
        value must reference a correct libxml2 document of type ``xmlDoc*``.
        The creator of the capsule must take care to correctly clean up the
        document using an appropriate capsule destructor.  By default, the
        libxml2 document will be copied to let lxml safely own the memory
        of the internal tree that it uses.
    
        If the capsule context is non-NULL, it must point to a C string that
        can be compared using ``strcmp()``.  If the context string equals
        ``"destructor:xmlFreeDoc"``, the libxml2 document will not be copied
        but the capsule invalidated instead by clearing its destructor and
        name.  That way, lxml takes ownership of the libxml2 document in memory
        without creating a copy first, and the capsule destructor will not be
        called.  The document will then eventually be cleaned up by lxml using
        the libxml2 API function ``xmlFreeDoc()`` once it is no longer used.
    
        If no copy is made, later modifications of the tree outside of lxml
        should not be attempted after transferring the ownership.
    """
    pass

def cleanup_namespaces(tree_or_element, top_nsmap=None, keep_ns_prefixes=None): # real signature unknown; restored from __doc__
    """
    cleanup_namespaces(tree_or_element, top_nsmap=None, keep_ns_prefixes=None)
    
        Remove all namespace declarations from a subtree that are not used
        by any of the elements or attributes in that tree.
    
        If a 'top_nsmap' is provided, it must be a mapping from prefixes
        to namespace URIs.  These namespaces will be declared on the top
        element of the subtree before running the cleanup, which allows
        moving namespace declarations to the top of the tree.
    
        If a 'keep_ns_prefixes' is provided, it must be a list of prefixes.
        These prefixes will not be removed as part of the cleanup.
    """
    pass

def clear_error_log(): # real signature unknown; restored from __doc__
    """
    clear_error_log()
    
        Clear the global error log.  Note that this log is already bound to a
        fixed size.
    
        Note: since lxml 2.2, the global error log is local to a thread
        and this function will only clear the global error log of the
        current thread.
    """
    pass

def Comment(text=None): # real signature unknown; restored from __doc__
    """
    Comment(text=None)
    
        Comment element factory. This factory function creates a special element that will
        be serialized as an XML comment.
    """
    pass

def dump(elem, pretty_print=True, with_tail=True): # real signature unknown; restored from __doc__
    """
    dump(elem, pretty_print=True, with_tail=True)
    
        Writes an element tree or element structure to sys.stdout. This function
        should be used for debugging only.
    """
    pass

def Element(_tag, attrib=None, nsmap=None, **_extra): # real signature unknown; restored from __doc__
    """
    Element(_tag, attrib=None, nsmap=None, **_extra)
    
        Element factory.  This function returns an object implementing the
        Element interface.
    
        Also look at the `_Element.makeelement()` and
        `_BaseParser.makeelement()` methods, which provide a faster way to
        create an Element within a specific document or parser context.
    """
    pass

def ElementTree(element=None, file=None, parser=None): # real signature unknown; restored from __doc__
    """
    ElementTree(element=None, file=None, parser=None)
    
        ElementTree wrapper class.
    """
    pass

def Entity(name): # real signature unknown; restored from __doc__
    """
    Entity(name)
    
        Entity factory.  This factory function creates a special element
        that will be serialized as an XML entity reference or character
        reference.  Note, however, that entities will not be automatically
        declared in the document.  A document that uses entity references
        requires a DTD to define the entities.
    """
    pass

def Extension(module, function_mapping=None, ns=None): # real signature unknown; restored from __doc__
    """
    Extension(module, function_mapping=None, ns=None)
    
        Build a dictionary of extension functions from the functions
        defined in a module or the methods of an object.
    
        As second argument, you can pass an additional mapping of
        attribute names to XPath function names, or a list of function
        names that should be taken.
    
        The ``ns`` keyword argument accepts a namespace URI for the XPath
        functions.
    """
    pass

def fromstring(text, parser=None, base_url=None): # real signature unknown; restored from __doc__
    """
    fromstring(text, parser=None, base_url=None)
    
        Parses an XML document or fragment from a string.  Returns the
        root node (or the result returned by a parser target).
    
        To override the default parser with a different parser you can pass it to
        the ``parser`` keyword argument.
    
        The ``base_url`` keyword argument allows to set the original base URL of
        the document to support relative Paths when looking up external entities
        (DTD, XInclude, ...).
    """
    pass

def fromstringlist(strings, parser=None): # real signature unknown; restored from __doc__
    """
    fromstringlist(strings, parser=None)
    
        Parses an XML document from a sequence of strings.  Returns the
        root node (or the result returned by a parser target).
    
        To override the default parser with a different parser you can pass it to
        the ``parser`` keyword argument.
    """
    pass

def FunctionNamespace(ns_uri): # real signature unknown; restored from __doc__
    """
    FunctionNamespace(ns_uri)
    
        Retrieve the function namespace object associated with the given
        URI.
    
        Creates a new one if it does not yet exist. A function namespace
        can only be used to register extension functions.
    
        Usage:
    
        >>> ns_functions = FunctionNamespace("http://schema.org/Movie")
    
        >>> @ns_functions  # uses function name
        ... def add2(x):
        ...     return x + 2
    
        >>> @ns_functions("add3")  # uses explicit name
        ... def add_three(x):
        ...     return x + 3
    """
    pass

def get_default_parser(): # real signature unknown; restored from __doc__
    """ get_default_parser() """
    pass

def HTML(text, parser=None, base_url=None): # real signature unknown; restored from __doc__
    """
    HTML(text, parser=None, base_url=None)
    
        Parses an HTML document from a string constant.  Returns the root
        node (or the result returned by a parser target).  This function
        can be used to embed "HTML literals" in Python code.
    
        To override the parser with a different ``HTMLParser`` you can pass it to
        the ``parser`` keyword argument.
    
        The ``base_url`` keyword argument allows to set the original base URL of
        the document to support relative Paths when looking up external entities
        (DTD, XInclude, ...).
    """
    pass

def iselement(element): # real signature unknown; restored from __doc__
    """
    iselement(element)
    
        Checks if an object appears to be a valid element object.
    """
    pass

def parse(source, parser=None, base_url=None): # real signature unknown; restored from __doc__
    """
    parse(source, parser=None, base_url=None)
    
        Return an ElementTree object loaded with source elements.  If no parser
        is provided as second argument, the default parser is used.
    
        The ``source`` can be any of the following:
    
        - a file name/path
        - a file object
        - a file-like object
        - a URL using the HTTP or FTP protocol
    
        To parse from a string, use the ``fromstring()`` function instead.
    
        Note that it is generally faster to parse from a file path or URL
        than from an open file object or file-like object.  Transparent
        decompression from gzip compressed sources is supported (unless
        explicitly disabled in libxml2).
    
        The ``base_url`` keyword allows setting a URL for the document
        when parsing from a file-like object.  This is needed when looking
        up external entities (DTD, XInclude, ...) with relative paths.
    """
    pass

def parseid(source, parser=None): # real signature unknown; restored from __doc__
    """
    parseid(source, parser=None)
    
        Parses the source into a tuple containing an ElementTree object and an
        ID dictionary.  If no parser is provided as second argument, the default
        parser is used.
    
        Note that you must not modify the XML tree if you use the ID dictionary.
        The results are undefined.
    """
    pass

def PI(*args, **kwargs): # real signature unknown
    """
    ProcessingInstruction(target, text=None)
    
        ProcessingInstruction element factory. This factory function creates a
        special element that will be serialized as an XML processing instruction.
    """
    pass

def ProcessingInstruction(target, text=None): # real signature unknown; restored from __doc__
    """
    ProcessingInstruction(target, text=None)
    
        ProcessingInstruction element factory. This factory function creates a
        special element that will be serialized as an XML processing instruction.
    """
    pass

def register_namespace(*args, **kwargs): # real signature unknown
    """
    Registers a namespace prefix that newly created Elements in that
        namespace will use.  The registry is global, and any existing
        mapping for either the given prefix or the namespace URI will be
        removed.
    """
    pass

def set_default_parser(parser=None): # real signature unknown; restored from __doc__
    """
    set_default_parser(parser=None)
    
        Set a default parser for the current thread.  This parser is used
        globally whenever no parser is supplied to the various parse functions of
        the lxml API.  If this function is called without a parser (or if it is
        None), the default parser is reset to the original configuration.
    
        Note that the pre-installed default parser is not thread-safe.  Avoid the
        default parser in multi-threaded environments.  You can create a separate
        parser for each thread explicitly or use a parser pool.
    """
    pass

def set_element_class_lookup(lookup=None): # real signature unknown; restored from __doc__
    """
    set_element_class_lookup(lookup = None)
    
        Set the global default element class lookup method.
    """
    pass

def strip_attributes(tree_or_element, *attribute_names): # real signature unknown; restored from __doc__
    """
    strip_attributes(tree_or_element, *attribute_names)
    
        Delete all attributes with the provided attribute names from an
        Element (or ElementTree) and its descendants.
    
        Attribute names can contain wildcards as in `_Element.iter`.
    
        Example usage::
    
            strip_attributes(root_element,
                             'simpleattr',
                             '{http://some/ns}attrname',
                             '{http://other/ns}*')
    """
    pass

def strip_elements(tree_or_element, *tag_names, with_tail=True): # real signature unknown; restored from __doc__
    """
    strip_elements(tree_or_element, *tag_names, with_tail=True)
    
        Delete all elements with the provided tag names from a tree or
        subtree.  This will remove the elements and their entire subtree,
        including all their attributes, text content and descendants.  It
        will also remove the tail text of the element unless you
        explicitly set the ``with_tail`` keyword argument option to False.
    
        Tag names can contain wildcards as in `_Element.iter`.
    
        Note that this will not delete the element (or ElementTree root
        element) that you passed even if it matches.  It will only treat
        its descendants.  If you want to include the root element, check
        its tag name directly before even calling this function.
    
        Example usage::
    
            strip_elements(some_element,
                'simpletagname',             # non-namespaced tag
                '{http://some/ns}tagname',   # namespaced tag
                '{http://some/other/ns}*'    # any tag from a namespace
                lxml.etree.Comment           # comments
                )
    """
    pass

def strip_tags(tree_or_element, *tag_names): # real signature unknown; restored from __doc__
    """
    strip_tags(tree_or_element, *tag_names)
    
        Delete all elements with the provided tag names from a tree or
        subtree.  This will remove the elements and their attributes, but
        *not* their text/tail content or descendants.  Instead, it will
        merge the text content and children of the element into its
        parent.
    
        Tag names can contain wildcards as in `_Element.iter`.
    
        Note that this will not delete the element (or ElementTree root
        element) that you passed even if it matches.  It will only treat
        its descendants.
    
        Example usage::
    
            strip_tags(some_element,
                'simpletagname',             # non-namespaced tag
                '{http://some/ns}tagname',   # namespaced tag
                '{http://some/other/ns}*'    # any tag from a namespace
                Comment                      # comments (including their text!)
                )
    """
    pass

def SubElement(_parent, _tag, attrib=None, nsmap=None, **_extra): # real signature unknown; restored from __doc__
    """
    SubElement(_parent, _tag, attrib=None, nsmap=None, **_extra)
    
        Subelement factory.  This function creates an element instance, and
        appends it to an existing element.
    """
    pass

def tostring(element_or_tree, encoding=None, method="xml", xml_declaration=None, pretty_print=False, with_tail=True, standalone=None, doctype=None, exclusive=False, with_comments=True, inclusive_ns_prefixes=None): # real signature unknown; restored from __doc__
    """
    tostring(element_or_tree, encoding=None, method="xml",
                     xml_declaration=None, pretty_print=False, with_tail=True,
                     standalone=None, doctype=None,
                     exclusive=False, with_comments=True, inclusive_ns_prefixes=None)
    
        Serialize an element to an encoded string representation of its XML
        tree.
    
        Defaults to ASCII encoding without XML declaration.  This
        behaviour can be configured with the keyword arguments 'encoding'
        (string) and 'xml_declaration' (bool).  Note that changing the
        encoding to a non UTF-8 compatible encoding will enable a
        declaration by default.
    
        You can also serialise to a Unicode string without declaration by
        passing the name ``'unicode'`` as encoding (or the ``str`` function
        in Py3 or ``unicode`` in Py2).  This changes the return value from
        a byte string to an unencoded unicode string.
    
        The keyword argument 'pretty_print' (bool) enables formatted XML.
    
        The keyword argument 'method' selects the output method: 'xml',
        'html', plain 'text' (text content without tags) or 'c14n'.
        Default is 'xml'.
    
        The ``exclusive`` and ``with_comments`` arguments are only used
        with C14N output, where they request exclusive and uncommented
        C14N serialisation respectively.
    
        Passing a boolean value to the ``standalone`` option will output
        an XML declaration with the corresponding ``standalone`` flag.
    
        The ``doctype`` option allows passing in a plain string that will
        be serialised before the XML tree.  Note that passing in non
        well-formed content here will make the XML output non well-formed.
        Also, an existing doctype in the document tree will not be removed
        when serialising an ElementTree instance.
    
        You can prevent the tail text of the element from being serialised
        by passing the boolean ``with_tail`` option.  This has no impact
        on the tail text of children, which will always be serialised.
    """
    pass

def tostringlist(element_or_tree, *args, **kwargs): # real signature unknown; restored from __doc__
    """
    tostringlist(element_or_tree, *args, **kwargs)
    
        Serialize an element to an encoded string representation of its XML
        tree, stored in a list of partial strings.
    
        This is purely for ElementTree 1.3 compatibility.  The result is a
        single string wrapped in a list.
    """
    pass

def tounicode(element_or_tree, method="xml", pretty_print=False, with_tail=True, doctype=None): # real signature unknown; restored from __doc__
    """
    tounicode(element_or_tree, method="xml", pretty_print=False,
                      with_tail=True, doctype=None)
    
        Serialize an element to the Python unicode representation of its XML
        tree.
    
        :deprecated: use ``tostring(el, encoding='unicode')`` instead.
    
        Note that the result does not carry an XML encoding declaration and is
        therefore not necessarily suited for serialization to byte streams without
        further treatment.
    
        The boolean keyword argument 'pretty_print' enables formatted XML.
    
        The keyword argument 'method' selects the output method: 'xml',
        'html' or plain 'text'.
    
        You can prevent the tail text of the element from being serialised
        by passing the boolean ``with_tail`` option.  This has no impact
        on the tail text of children, which will always be serialised.
    """
    pass

def use_global_python_log(log): # real signature unknown; restored from __doc__
    """
    use_global_python_log(log)
    
        Replace the global error log by an etree.PyErrorLog that uses the
        standard Python logging package.
    
        Note that this disables access to the global error log from exceptions.
        Parsers, XSLT etc. will continue to provide their normal local error log.
    
        Note: prior to lxml 2.2, this changed the error log globally.
        Since lxml 2.2, the global error log is local to a thread and this
        function will only set the global error log of the current thread.
    """
    pass

def XML(text, parser=None, base_url=None): # real signature unknown; restored from __doc__
    """
    XML(text, parser=None, base_url=None)
    
        Parses an XML document or fragment from a string constant.
        Returns the root node (or the result returned by a parser target).
        This function can be used to embed "XML literals" in Python code,
        like in
    
           >>> root = XML("<root><test/></root>")
           >>> print(root.tag)
           root
    
        To override the parser with a different ``XMLParser`` you can pass it to
        the ``parser`` keyword argument.
    
        The ``base_url`` keyword argument allows to set the original base URL of
        the document to support relative Paths when looking up external entities
        (DTD, XInclude, ...).
    """
    pass

def XMLDTDID(text, parser=None, base_url=None): # real signature unknown; restored from __doc__
    """
    XMLDTDID(text, parser=None, base_url=None)
    
        Parse the text and return a tuple (root node, ID dictionary).  The root
        node is the same as returned by the XML() function.  The dictionary
        contains string-element pairs.  The dictionary keys are the values of ID
        attributes as defined by the DTD.  The elements referenced by the ID are
        stored as dictionary values.
    
        Note that you must not modify the XML tree if you use the ID dictionary.
        The results are undefined.
    """
    pass

def XMLID(text, parser=None, base_url=None): # real signature unknown; restored from __doc__
    """
    XMLID(text, parser=None, base_url=None)
    
        Parse the text and return a tuple (root node, ID dictionary).  The root
        node is the same as returned by the XML() function.  The dictionary
        contains string-element pairs.  The dictionary keys are the values of 'id'
        attributes.  The elements referenced by the ID are stored as dictionary
        values.
    """
    pass

def XPathEvaluator(etree_or_element, namespaces=None, extensions=None, regexp=True, smart_strings=True): # real signature unknown; restored from __doc__
    """
    XPathEvaluator(etree_or_element, namespaces=None, extensions=None, regexp=True, smart_strings=True)
    
        Creates an XPath evaluator for an ElementTree or an Element.
    
        The resulting object can be called with an XPath expression as argument
        and XPath variables provided as keyword arguments.
    
        Additional namespace declarations can be passed with the
        'namespace' keyword argument.  EXSLT regular expression support
        can be disabled with the 'regexp' boolean keyword (defaults to
        True).  Smart strings will be returned for string results unless
        you pass ``smart_strings=False``.
    """
    pass

# classes

from ._ElementMatchIterator import _ElementMatchIterator
from .AncestorsIterator import AncestorsIterator
from .ElementClassLookup import ElementClassLookup
from .FallbackElementClassLookup import FallbackElementClassLookup
from .AttributeBasedElementClassLookup import AttributeBasedElementClassLookup
from .Error import Error
from .LxmlError import LxmlError
from .C14NError import C14NError
from .CDATA import CDATA
from ._Element import _Element
from ._Comment import _Comment
from .CommentBase import CommentBase
from .CustomElementClassLookup import CustomElementClassLookup
from .DocInfo import DocInfo
from .DocumentInvalid import DocumentInvalid
from ._Validator import _Validator
from .DTD import DTD
from .DTDError import DTDError
from .DTDParseError import DTDParseError
from .DTDValidateError import DTDValidateError
from .ElementBase import ElementBase
from .ElementChildIterator import ElementChildIterator
from .ElementDefaultClassLookup import ElementDefaultClassLookup
from .ElementDepthFirstIterator import ElementDepthFirstIterator
from .ElementNamespaceClassLookup import ElementNamespaceClassLookup
from .ElementTextIterator import ElementTextIterator
from ._Entity import _Entity
from .EntityBase import EntityBase
from .ErrorDomains import ErrorDomains
from .ErrorLevels import ErrorLevels
from .ErrorTypes import ErrorTypes
from ._FeedParser import _FeedParser
from .XMLParser import XMLParser
from .XMLTreeBuilder import XMLTreeBuilder
from .ETCompatXMLParser import ETCompatXMLParser
from ._XPathEvaluatorBase import _XPathEvaluatorBase
from .XPath import XPath
from .ETXPath import ETXPath
from .xmlfile import xmlfile
from .htmlfile import htmlfile
from .HTMLParser import HTMLParser
from .HTMLPullParser import HTMLPullParser
from .iterparse import iterparse
from .iterwalk import iterwalk
from .LxmlRegistryError import LxmlRegistryError
from .LxmlSyntaxError import LxmlSyntaxError
from .NamespaceRegistryError import NamespaceRegistryError
from .ParseError import ParseError
from .ParserBasedElementClassLookup import ParserBasedElementClassLookup
from .ParserError import ParserError
from ._ProcessingInstruction import _ProcessingInstruction
from .PIBase import PIBase
from ._BaseErrorLog import _BaseErrorLog
from .PyErrorLog import PyErrorLog
from .PythonElementClassLookup import PythonElementClassLookup
from .QName import QName
from .RelaxNG import RelaxNG
from .RelaxNGError import RelaxNGError
from .RelaxNGErrorTypes import RelaxNGErrorTypes
from .RelaxNGParseError import RelaxNGParseError
from .RelaxNGValidateError import RelaxNGValidateError
from .Resolver import Resolver
from .Schematron import Schematron
from .SchematronError import SchematronError
from .SchematronParseError import SchematronParseError
from .SchematronValidateError import SchematronValidateError
from .SerialisationError import SerialisationError
from .SiblingsIterator import SiblingsIterator
from ._SaxParserTarget import _SaxParserTarget
from .TreeBuilder import TreeBuilder
from .XInclude import XInclude
from .XIncludeError import XIncludeError
from .XMLPullParser import XMLPullParser
from .XMLSchema import XMLSchema
from .XMLSchemaError import XMLSchemaError
from .XMLSchemaParseError import XMLSchemaParseError
from .XMLSchemaValidateError import XMLSchemaValidateError
from .XMLSyntaxError import XMLSyntaxError
from .XPathElementEvaluator import XPathElementEvaluator
from .XPathDocumentEvaluator import XPathDocumentEvaluator
from .XPathError import XPathError
from .XPathEvalError import XPathEvalError
from .XPathFunctionError import XPathFunctionError
from .XPathResultError import XPathResultError
from .XPathSyntaxError import XPathSyntaxError
from .XSLT import XSLT
from .XSLTAccessControl import XSLTAccessControl
from .XSLTError import XSLTError
from .XSLTApplyError import XSLTApplyError
from .XSLTExtension import XSLTExtension
from .XSLTExtensionError import XSLTExtensionError
from .XSLTParseError import XSLTParseError
from .XSLTSaveError import XSLTSaveError
from ._Attrib import _Attrib
from ._Document import _Document
from ._ListErrorLog import _ListErrorLog
from ._ErrorLog import _ErrorLog
from ._DomainErrorLog import _DomainErrorLog
from ._ElementTagMatcher import _ElementTagMatcher
from ._ElementIterator import _ElementIterator
from ._ElementStringResult import _ElementStringResult
from ._ElementTree import _ElementTree
from ._ElementUnicodeResult import _ElementUnicodeResult
from ._IDDict import _IDDict
from ._LogEntry import _LogEntry
from ._RotatingErrorLog import _RotatingErrorLog
from ._TargetParserResult import _TargetParserResult
from ._XSLTProcessingInstruction import _XSLTProcessingInstruction
from ._XSLTResultTree import _XSLTResultTree
# variables with complex values

LIBXML_COMPILED_VERSION = (
    2,
    9,
    9,
)

LIBXML_VERSION = (
    2,
    9,
    9,
)

LIBXSLT_COMPILED_VERSION = (
    1,
    1,
    33,
)

LIBXSLT_VERSION = (
    1,
    1,
    33,
)

LXML_VERSION = (
    4,
    3,
    4,
    0,
)

memory_debugger = None # (!) real value is '<lxml.etree._MemDebug object at 0x000002467DCAE390>'

__all__ = [
    'AttributeBasedElementClassLookup',
    'C14NError',
    'CDATA',
    'Comment',
    'CommentBase',
    'CustomElementClassLookup',
    'DEBUG',
    'DTD',
    'DTDError',
    'DTDParseError',
    'DTDValidateError',
    'DocumentInvalid',
    'ETCompatXMLParser',
    'ETXPath',
    'Element',
    'ElementBase',
    'ElementClassLookup',
    'ElementDefaultClassLookup',
    'ElementNamespaceClassLookup',
    'ElementTree',
    'Entity',
    'EntityBase',
    'Error',
    'ErrorDomains',
    'ErrorLevels',
    'ErrorTypes',
    'Extension',
    'FallbackElementClassLookup',
    'FunctionNamespace',
    'HTML',
    'HTMLParser',
    'LIBXML_COMPILED_VERSION',
    'LIBXML_VERSION',
    'LIBXSLT_COMPILED_VERSION',
    'LIBXSLT_VERSION',
    'LXML_VERSION',
    'LxmlError',
    'LxmlRegistryError',
    'LxmlSyntaxError',
    'NamespaceRegistryError',
    'PI',
    'PIBase',
    'ParseError',
    'ParserBasedElementClassLookup',
    'ParserError',
    'ProcessingInstruction',
    'PyErrorLog',
    'PythonElementClassLookup',
    'QName',
    'RelaxNG',
    'RelaxNGError',
    'RelaxNGErrorTypes',
    'RelaxNGParseError',
    'RelaxNGValidateError',
    'Resolver',
    'Schematron',
    'SchematronError',
    'SchematronParseError',
    'SchematronValidateError',
    'SerialisationError',
    'SubElement',
    'TreeBuilder',
    'XInclude',
    'XIncludeError',
    'XML',
    'XMLDTDID',
    'XMLID',
    'XMLParser',
    'XMLSchema',
    'XMLSchemaError',
    'XMLSchemaParseError',
    'XMLSchemaValidateError',
    'XMLSyntaxError',
    'XMLTreeBuilder',
    'XPath',
    'XPathDocumentEvaluator',
    'XPathError',
    'XPathEvalError',
    'XPathEvaluator',
    'XPathFunctionError',
    'XPathResultError',
    'XPathSyntaxError',
    'XSLT',
    'XSLTAccessControl',
    'XSLTApplyError',
    'XSLTError',
    'XSLTExtension',
    'XSLTExtensionError',
    'XSLTParseError',
    'XSLTSaveError',
    'cleanup_namespaces',
    'clear_error_log',
    'dump',
    'fromstring',
    'fromstringlist',
    'get_default_parser',
    'iselement',
    'iterparse',
    'iterwalk',
    'parse',
    'parseid',
    'register_namespace',
    'set_default_parser',
    'set_element_class_lookup',
    'strip_attributes',
    'strip_elements',
    'strip_tags',
    'tostring',
    'tostringlist',
    'tounicode',
    'use_global_python_log',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000002467EDCB3C8>'

__pyx_capi__ = {
    'adoptExternalDocument': None, # (!) real value is '<capsule object "struct LxmlElementTree *(xmlDoc *, PyObject *, int)" at 0x000002467EDA9900>'
    'appendChild': None, # (!) real value is '<capsule object "void (struct LxmlElement *, struct LxmlElement *)" at 0x000002467EDA9ED0>'
    'appendChildToElement': None, # (!) real value is '<capsule object "int (struct LxmlElement *, struct LxmlElement *)" at 0x000002467EDA9F00>'
    'attributeValue': None, # (!) real value is '<capsule object "PyObject *(xmlNode *, xmlAttr *)" at 0x000002467EDA9C30>'
    'attributeValueFromNsName': None, # (!) real value is '<capsule object "PyObject *(xmlNode *, const xmlChar *, const xmlChar *)" at 0x000002467EDA9C60>'
    'callLookupFallback': None, # (!) real value is '<capsule object "PyObject *(struct LxmlFallbackElementClassLookup *, struct LxmlDocument *, xmlNode *)" at 0x000002467EDA9A50>'
    'collectAttributes': None, # (!) real value is '<capsule object "PyObject *(xmlNode *, int)" at 0x000002467EDA9CF0>'
    'deepcopyNodeToDocument': None, # (!) real value is '<capsule object "struct LxmlElement *(struct LxmlDocument *, xmlNode *)" at 0x000002467EDA9870>'
    'delAttribute': None, # (!) real value is '<capsule object "int (struct LxmlElement *, PyObject *)" at 0x000002467EDA9D50>'
    'delAttributeFromNsName': None, # (!) real value is '<capsule object "int (xmlNode *, const xmlChar *, const xmlChar *)" at 0x000002467EDA9D80>'
    'documentOrRaise': None, # (!) real value is '<capsule object "struct LxmlDocument *(PyObject *)" at 0x000002467EDA9AB0>'
    'elementFactory': None, # (!) real value is '<capsule object "struct LxmlElement *(struct LxmlDocument *, xmlNode *)" at 0x000002467EDA9930>'
    'elementTreeFactory': None, # (!) real value is '<capsule object "struct LxmlElementTree *(struct LxmlElement *)" at 0x000002467EDA98A0>'
    'findChild': None, # (!) real value is '<capsule object "xmlNode *(xmlNode *, Py_ssize_t)" at 0x000002467EDA9DE0>'
    'findChildBackwards': None, # (!) real value is '<capsule object "xmlNode *(xmlNode *, Py_ssize_t)" at 0x000002467EDA9E40>'
    'findChildForwards': None, # (!) real value is '<capsule object "xmlNode *(xmlNode *, Py_ssize_t)" at 0x000002467EDA9E10>'
    'findOrBuildNodeNsPrefix': None, # (!) real value is '<capsule object "xmlNs *(struct LxmlDocument *, xmlNode *, const xmlChar *, const xmlChar *)" at 0x000002467EEF80F0>'
    'getAttributeValue': None, # (!) real value is '<capsule object "PyObject *(struct LxmlElement *, PyObject *, PyObject *)" at 0x000002467EDA9C90>'
    'getNsTag': None, # (!) real value is '<capsule object "PyObject *(PyObject *)" at 0x000002467EDA9F90>'
    'getNsTagWithEmptyNs': None, # (!) real value is '<capsule object "PyObject *(PyObject *)" at 0x000002467EDA9FC0>'
    'hasChild': None, # (!) real value is '<capsule object "int (xmlNode *)" at 0x000002467EDA9DB0>'
    'hasTail': None, # (!) real value is '<capsule object "int (xmlNode *)" at 0x000002467EDA9B40>'
    'hasText': None, # (!) real value is '<capsule object "int (xmlNode *)" at 0x000002467EDA9B10>'
    'initTagMatch': None, # (!) real value is '<capsule object "void (struct LxmlElementTagMatcher *, PyObject *)" at 0x000002467EEF80C0>'
    'iteratorStoreNext': None, # (!) real value is '<capsule object "void (struct LxmlElementIterator *, struct LxmlElement *)" at 0x000002467EEF8090>'
    'iterattributes': None, # (!) real value is '<capsule object "PyObject *(struct LxmlElement *, int)" at 0x000002467EDA9CC0>'
    'lookupDefaultElementClass': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *, xmlNode *)" at 0x000002467EDA99F0>'
    'lookupNamespaceElementClass': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *, xmlNode *)" at 0x000002467EDA9A20>'
    'makeElement': None, # (!) real value is '<capsule object "struct LxmlElement *(PyObject *, struct LxmlDocument *, PyObject *, PyObject *, PyObject *, PyObject *, PyObject *)" at 0x000002467EDA9960>'
    'makeSubElement': None, # (!) real value is '<capsule object "struct LxmlElement *(struct LxmlElement *, PyObject *, PyObject *, PyObject *, PyObject *, PyObject *)" at 0x000002467EDA9990>'
    'namespacedName': None, # (!) real value is '<capsule object "PyObject *(xmlNode *)" at 0x000002467EEF8030>'
    'namespacedNameFromNsName': None, # (!) real value is '<capsule object "PyObject *(const xmlChar *, const xmlChar *)" at 0x000002467EEF8060>'
    'newElementTree': None, # (!) real value is '<capsule object "struct LxmlElementTree *(struct LxmlElement *, PyObject *)" at 0x000002467EDA98D0>'
    'nextElement': None, # (!) real value is '<capsule object "xmlNode *(xmlNode *)" at 0x000002467EDA9E70>'
    'previousElement': None, # (!) real value is '<capsule object "xmlNode *(xmlNode *)" at 0x000002467EDA9EA0>'
    'pyunicode': None, # (!) real value is '<capsule object "PyObject *(const xmlChar *)" at 0x000002467EDA9F30>'
    'rootNodeOrRaise': None, # (!) real value is '<capsule object "struct LxmlElement *(PyObject *)" at 0x000002467EDA9AE0>'
    'setAttributeValue': None, # (!) real value is '<capsule object "int (struct LxmlElement *, PyObject *, PyObject *)" at 0x000002467EDA9D20>'
    'setElementClassLookupFunction': None, # (!) real value is '<capsule object "void (_element_class_lookup_function, PyObject *)" at 0x000002467EDA99C0>'
    'setNodeText': None, # (!) real value is '<capsule object "int (xmlNode *, PyObject *)" at 0x000002467EDA9BD0>'
    'setTailText': None, # (!) real value is '<capsule object "int (xmlNode *, PyObject *)" at 0x000002467EDA9C00>'
    'tagMatches': None, # (!) real value is '<capsule object "int (xmlNode *, const xmlChar *, const xmlChar *)" at 0x000002467EDA9A80>'
    'tailOf': None, # (!) real value is '<capsule object "PyObject *(xmlNode *)" at 0x000002467EDA9BA0>'
    'textOf': None, # (!) real value is '<capsule object "PyObject *(xmlNode *)" at 0x000002467EDA9B70>'
    'utf8': None, # (!) real value is '<capsule object "PyObject *(PyObject *)" at 0x000002467EDA9F60>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='lxml.etree', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000002467EDCB3C8>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\lxml\\\\etree.cp37-win_amd64.pyd')"

__test__ = {
    'FunctionNamespace (line 207)': 'FunctionNamespace(ns_uri)\n\n    Retrieve the function namespace object associated with the given\n    URI.\n\n    Creates a new one if it does not yet exist. A function namespace\n    can only be used to register extension functions.\n\n    Usage:\n\n    >>> ns_functions = FunctionNamespace("http://schema.org/Movie")\n\n    >>> @ns_functions  # uses function name\n    ... def add2(x):\n    ...     return x + 2\n\n    >>> @ns_functions("add3")  # uses explicit name\n    ... def add_three(x):\n    ...     return x + 3\n    ',
    'XML (line 3176)': 'XML(text, parser=None, base_url=None)\n\n    Parses an XML document or fragment from a string constant.\n    Returns the root node (or the result returned by a parser target).\n    This function can be used to embed "XML literals" in Python code,\n    like in\n\n       >>> root = XML("<root><test/></root>")\n       >>> print(root.tag)\n       root\n\n    To override the parser with a different ``XMLParser`` you can pass it to\n    the ``parser`` keyword argument.\n\n    The ``base_url`` keyword argument allows to set the original base URL of\n    the document to support relative Paths when looking up external entities\n    (DTD, XInclude, ...).\n    ',
}

