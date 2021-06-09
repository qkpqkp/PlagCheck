# encoding: utf-8
# module lxml.sax
# from C:\Users\Doly\Anaconda3\lib\site-packages\lxml\sax.cp37-win_amd64.pyd
# by generator 1.147
"""
SAX-based adapter to copy trees from/to the Python standard library.

Use the `ElementTreeContentHandler` class to build an ElementTree from
SAX events.

Use the `ElementTreeProducer` class or the `saxify()` function to fire
the SAX events of an ElementTree against a SAX ContentHandler.

See http://codespeak.net/lxml/sax.html
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import lxml.etree as etree # C:\Users\Doly\Anaconda3\lib\site-packages\lxml\etree.cp37-win_amd64.pyd
from lxml.etree import (Comment, ElementTree, ProcessingInstruction, 
    SubElement)

import lxml.etree as __lxml_etree
import xml.sax.handler as __xml_sax_handler


# functions

def saxify(*args, **kwargs): # real signature unknown
    """
    One-shot helper to generate SAX events from an XML tree and fire
        them against a SAX ContentHandler.
    """
    pass

def __pyx_unpickle_ElementTreeProducer(*args, **kwargs): # real signature unknown
    pass

def __reduce_cython__(*args, **kwargs): # real signature unknown
    pass

def __setstate_cython__(*args, **kwargs): # real signature unknown
    pass

# classes

class ContentHandler(object):
    """
    Interface for receiving logical document content events.
    
        This is the main callback interface in SAX, and the one most
        important to applications. The order of events in this interface
        mirrors the order of the information in the document.
    """
    def characters(self, content): # reliably restored by inspect
        """
        Receive notification of character data.
        
                The Parser will call this method to report each chunk of
                character data. SAX parsers may return all contiguous
                character data in a single chunk, or they may split it into
                several chunks; however, all of the characters in any single
                event must come from the same external entity so that the
                Locator provides useful information.
        """
        pass

    def endDocument(self): # reliably restored by inspect
        """
        Receive notification of the end of a document.
        
                The SAX parser will invoke this method only once, and it will
                be the last method invoked during the parse. The parser shall
                not invoke this method until it has either abandoned parsing
                (because of an unrecoverable error) or reached the end of
                input.
        """
        pass

    def endElement(self, name): # reliably restored by inspect
        """
        Signals the end of an element in non-namespace mode.
        
                The name parameter contains the name of the element type, just
                as with the startElement event.
        """
        pass

    def endElementNS(self, name, qname): # reliably restored by inspect
        """
        Signals the end of an element in namespace mode.
        
                The name parameter contains the name of the element type, just
                as with the startElementNS event.
        """
        pass

    def endPrefixMapping(self, prefix): # reliably restored by inspect
        """
        End the scope of a prefix-URI mapping.
        
                See startPrefixMapping for details. This event will always
                occur after the corresponding endElement event, but the order
                of endPrefixMapping events is not otherwise guaranteed.
        """
        pass

    def ignorableWhitespace(self, whitespace): # reliably restored by inspect
        """
        Receive notification of ignorable whitespace in element content.
        
                Validating Parsers must use this method to report each chunk
                of ignorable whitespace (see the W3C XML 1.0 recommendation,
                section 2.10): non-validating parsers may also use this method
                if they are capable of parsing and using content models.
        
                SAX parsers may return all contiguous whitespace in a single
                chunk, or they may split it into several chunks; however, all
                of the characters in any single event must come from the same
                external entity, so that the Locator provides useful
                information.
        """
        pass

    def processingInstruction(self, target, data): # reliably restored by inspect
        """
        Receive notification of a processing instruction.
        
                The Parser will invoke this method once for each processing
                instruction found: note that processing instructions may occur
                before or after the main document element.
        
                A SAX parser should never report an XML declaration (XML 1.0,
                section 2.8) or a text declaration (XML 1.0, section 4.3.1)
                using this method.
        """
        pass

    def setDocumentLocator(self, locator): # reliably restored by inspect
        """
        Called by the parser to give the application a locator for
                locating the origin of document events.
        
                SAX parsers are strongly encouraged (though not absolutely
                required) to supply a locator: if it does so, it must supply
                the locator to the application by invoking this method before
                invoking any of the other methods in the DocumentHandler
                interface.
        
                The locator allows the application to determine the end
                position of any document-related event, even if the parser is
                not reporting an error. Typically, the application will use
                this information for reporting its own errors (such as
                character content that does not match an application's
                business rules). The information returned by the locator is
                probably not sufficient for use with a search engine.
        
                Note that the locator will return correct information only
                during the invocation of the events in this interface. The
                application should not attempt to use it at any other time.
        """
        pass

    def skippedEntity(self, name): # reliably restored by inspect
        """
        Receive notification of a skipped entity.
        
                The Parser will invoke this method once for each entity
                skipped. Non-validating processors may skip entities if they
                have not seen the declarations (because, for example, the
                entity was declared in an external DTD subset). All processors
                may skip external entities, depending on the values of the
                http://xml.org/sax/features/external-general-entities and the
                http://xml.org/sax/features/external-parameter-entities
                properties.
        """
        pass

    def startDocument(self): # reliably restored by inspect
        """
        Receive notification of the beginning of a document.
        
                The SAX parser will invoke this method only once, before any
                other methods in this interface or in DTDHandler (except for
                setDocumentLocator).
        """
        pass

    def startElement(self, name, attrs): # reliably restored by inspect
        """
        Signals the start of an element in non-namespace mode.
        
                The name parameter contains the raw XML 1.0 name of the
                element type as a string and the attrs parameter holds an
                instance of the Attributes class containing the attributes of
                the element.
        """
        pass

    def startElementNS(self, name, qname, attrs): # reliably restored by inspect
        """
        Signals the start of an element in namespace mode.
        
                The name parameter contains the name of the element type as a
                (uri, localname) tuple, the qname parameter the raw XML 1.0
                name used in the source document, and the attrs parameter
                holds an instance of the Attributes class containing the
                attributes of the element.
        
                The uri part of the name tuple is None for elements which have
                no namespace.
        """
        pass

    def startPrefixMapping(self, prefix, uri): # reliably restored by inspect
        """
        Begin the scope of a prefix-URI Namespace mapping.
        
                The information from this event is not necessary for normal
                Namespace processing: the SAX XML reader will automatically
                replace prefixes for element and attribute names when the
                http://xml.org/sax/features/namespaces feature is true (the
                default).
        
                There are cases, however, when applications need to use
                prefixes in character data or in attribute values, where they
                cannot safely be expanded automatically; the
                start/endPrefixMapping event supplies the information to the
                application to expand prefixes in those contexts itself, if
                necessary.
        
                Note that start/endPrefixMapping events are not guaranteed to
                be properly nested relative to each-other: all
                startPrefixMapping events will occur before the corresponding
                startElement event, and all endPrefixMapping events will occur
                after the corresponding endElement event, but their order is
                not guaranteed.
        """
        pass

    def __init__(self): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'xml.sax.handler', '__doc__': 'Interface for receiving logical document content events.\\n\\n    This is the main callback interface in SAX, and the one most\\n    important to applications. The order of events in this interface\\n    mirrors the order of the information in the document.', '__init__': <function ContentHandler.__init__ at 0x000001DD63D80378>, 'setDocumentLocator': <function ContentHandler.setDocumentLocator at 0x000001DD63D80400>, 'startDocument': <function ContentHandler.startDocument at 0x000001DD63D80488>, 'endDocument': <function ContentHandler.endDocument at 0x000001DD63D80510>, 'startPrefixMapping': <function ContentHandler.startPrefixMapping at 0x000001DD63D80598>, 'endPrefixMapping': <function ContentHandler.endPrefixMapping at 0x000001DD63D80620>, 'startElement': <function ContentHandler.startElement at 0x000001DD63D806A8>, 'endElement': <function ContentHandler.endElement at 0x000001DD63D80730>, 'startElementNS': <function ContentHandler.startElementNS at 0x000001DD63D807B8>, 'endElementNS': <function ContentHandler.endElementNS at 0x000001DD63D80840>, 'characters': <function ContentHandler.characters at 0x000001DD63D808C8>, 'ignorableWhitespace': <function ContentHandler.ignorableWhitespace at 0x000001DD63D80950>, 'processingInstruction': <function ContentHandler.processingInstruction at 0x000001DD63D809D8>, 'skippedEntity': <function ContentHandler.skippedEntity at 0x000001DD63D80A60>, '__dict__': <attribute '__dict__' of 'ContentHandler' objects>, '__weakref__': <attribute '__weakref__' of 'ContentHandler' objects>})"


class ElementTreeContentHandler(__xml_sax_handler.ContentHandler):
    """ Build an lxml ElementTree from SAX events. """
    def characters(self, *args, **kwargs): # real signature unknown
        pass

    def endDocument(self, *args, **kwargs): # real signature unknown
        pass

    def endElement(self, *args, **kwargs): # real signature unknown
        pass

    def endElementNS(self, *args, **kwargs): # real signature unknown
        pass

    def endPrefixMapping(self, *args, **kwargs): # real signature unknown
        pass

    def ignorableWhitespace(self, *args, **kwargs): # real signature unknown
        pass

    def processingInstruction(self, *args, **kwargs): # real signature unknown
        pass

    def setDocumentLocator(self, *args, **kwargs): # real signature unknown
        pass

    def startDocument(self, *args, **kwargs): # real signature unknown
        pass

    def startElement(self, *args, **kwargs): # real signature unknown
        pass

    def startElementNS(self, *args, **kwargs): # real signature unknown
        pass

    def startPrefixMapping(self, *args, **kwargs): # real signature unknown
        pass

    def _buildTag(self, *args, **kwargs): # real signature unknown
        pass

    def _get_etree(self, *args, **kwargs): # real signature unknown
        """ Contains the generated ElementTree after parsing is finished. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    etree = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Contains the generated ElementTree after parsing is finished."""



class ElementTreeProducer(object):
    """ Produces SAX events for an element and children. """
    def saxify(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001DD62469690>'


class SaxError(__lxml_etree.LxmlError):
    """ General SAX error. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001DD6248C438>'

__pyx_capi__ = {
    '_getNsTag': None, # (!) real value is '<capsule object "PyObject *(PyObject *)" at 0x000001DD62469660>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='lxml.sax', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001DD6248C438>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\lxml\\\\sax.cp37-win_amd64.pyd')"

__test__ = {}

