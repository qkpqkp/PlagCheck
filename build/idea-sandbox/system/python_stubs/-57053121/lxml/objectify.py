# encoding: utf-8
# module lxml.objectify
# from C:\Users\Doly\Anaconda3\lib\site-packages\lxml\objectify.cp37-win_amd64.pyd
# by generator 1.147
"""
The ``lxml.objectify`` module implements a Python object API for XML.
It is based on `lxml.etree`.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
from lxml.etree import SubElement

import lxml.etree as __lxml_etree


# Variables with simple values

PYTYPE_ATTRIBUTE = '{http://codespeak.net/lxml/objectify/pytype}pytype'

__version__ = '4.3.4'

# functions

def annotate(element_or_tree, ignore_old=True, ignore_xsi=False, empty_pytype=None, empty_type=None, annotate_xsi=0, annotate_pytype=1): # real signature unknown; restored from __doc__
    """
    annotate(element_or_tree, ignore_old=True, ignore_xsi=False, empty_pytype=None, empty_type=None, annotate_xsi=0, annotate_pytype=1)
    
        Recursively annotates the elements of an XML tree with 'xsi:type'
        and/or 'py:pytype' attributes.
    
        If the 'ignore_old' keyword argument is True (the default), current
        'py:pytype' attributes will be ignored for the type annotation. Set to False
        if you want reuse existing 'py:pytype' information (iff appropriate for the
        element text value).
    
        If the 'ignore_xsi' keyword argument is False (the default), existing
        'xsi:type' attributes will be used for the type annotation, if they fit the
        element text values. 
        
        Note that the mapping from Python types to XSI types is usually ambiguous.
        Currently, only the first XSI type name in the corresponding PyType
        definition will be used for annotation.  Thus, you should consider naming
        the widest type first if you define additional types.
    
        The default 'py:pytype' annotation of empty elements can be set with the
        ``empty_pytype`` keyword argument. Pass 'str', for example, to make
        string values the default.
    
        The default 'xsi:type' annotation of empty elements can be set with the
        ``empty_type`` keyword argument.  The default is not to annotate empty
        elements.  Pass 'string', for example, to make string values the default.
    
        The keyword arguments 'annotate_xsi' (default: 0) and 'annotate_pytype'
        (default: 1) control which kind(s) of annotation to use.
    """
    pass

def DataElement(_value, attrib=None, nsmap=None, _pytype=None, _xsi=None, **_attributes): # real signature unknown; restored from __doc__
    """
    DataElement(_value, attrib=None, nsmap=None, _pytype=None, _xsi=None, **_attributes)
    
        Create a new element from a Python value and XML attributes taken from
        keyword arguments or a dictionary passed as second argument.
    
        Automatically adds a 'pytype' attribute for the Python type of the value,
        if the type can be identified.  If '_pytype' or '_xsi' are among the
        keyword arguments, they will be used instead.
    
        If the _value argument is an ObjectifiedDataElement instance, its py:pytype,
        xsi:type and other attributes and nsmap are reused unless they are redefined
        in attrib and/or keyword arguments.
    """
    pass

def deannotate(element_or_tree, pytype=True, xsi=True, xsi_nil=False, cleanup_namespaces=False): # real signature unknown; restored from __doc__
    """
    deannotate(element_or_tree, pytype=True, xsi=True, xsi_nil=False, cleanup_namespaces=False)
    
        Recursively de-annotate the elements of an XML tree by removing 'py:pytype'
        and/or 'xsi:type' attributes and/or 'xsi:nil' attributes.
    
        If the 'pytype' keyword argument is True (the default), 'py:pytype'
        attributes will be removed. If the 'xsi' keyword argument is True (the 
        default), 'xsi:type' attributes will be removed.
        If the 'xsi_nil' keyword argument is True (default: False), 'xsi:nil'
        attributes will be removed.
    
        Note that this does not touch the namespace declarations by
        default.  If you want to remove unused namespace declarations from
        the tree, pass the option ``cleanup_namespaces=True``.
    """
    pass

def dump(_Element_element_not_None): # real signature unknown; restored from __doc__
    """
    dump(_Element element not None)
    
        Return a recursively generated string representation of an element.
    """
    pass

def E(*args, **kwargs): # real signature unknown
    """
    ElementMaker(self, namespace=None, nsmap=None, annotate=True, makeelement=None)
    
        An ElementMaker that can be used for constructing trees.
    
        Example::
    
          >>> M = ElementMaker(annotate=False)
          >>> attributes = {'class': 'par'}
          >>> html = M.html( M.body( M.p('hello', attributes, M.br, 'objectify', style="font-weight: bold") ) )
    
          >>> from lxml.etree import tostring
          >>> print(tostring(html, method='html').decode('ascii'))
          <html><body><p style="font-weight: bold" class="par">hello<br>objectify</p></body></html>
    
        To create tags that are not valid Python identifiers, call the factory
        directly and pass the tag name as first argument::
    
          >>> root = M('tricky-tag', 'some text')
          >>> print(root.tag)
          tricky-tag
          >>> print(root.text)
          some text
    
        Note that this module has a predefined ElementMaker instance called ``E``.
    """
    pass

def Element(_tag, attrib=None, nsmap=None, _pytype=None, **_attributes): # real signature unknown; restored from __doc__
    """
    Element(_tag, attrib=None, nsmap=None, _pytype=None, **_attributes)
    
        Objectify specific version of the lxml.etree Element() factory that
        always creates a structural (tree) element.
    
        NOTE: requires parser based element class lookup activated in lxml.etree!
    """
    pass

def enable_recursive_str(on=True): # real signature unknown; restored from __doc__
    """
    enable_recursive_str(on=True)
    
        Enable a recursively generated tree representation for str(element),
        based on objectify.dump(element).
    """
    pass

def fromstring(xml, parser=None, base_url=None): # real signature unknown; restored from __doc__
    """
    fromstring(xml, parser=None, base_url=None)
    
        Objectify specific version of the lxml.etree fromstring() function
        that uses the objectify parser.
    
        You can pass a different parser as second argument.
    
        The ``base_url`` keyword argument allows to set the original base URL of
        the document to support relative Paths when looking up external entities
        (DTD, XInclude, ...).
    """
    pass

def getRegisteredTypes(): # real signature unknown; restored from __doc__
    """
    getRegisteredTypes()
    
        Returns a list of the currently registered PyType objects.
    
        To add a new type, retrieve this list and call unregister() for all
        entries.  Then add the new type at a suitable position (possibly replacing
        an existing one) and call register() for all entries.
    
        This is necessary if the new type interferes with the type check functions
        of existing ones (normally only int/float/bool) and must the tried before
        other types.  To add a type that is not yet parsable by the current type
        check functions, you can simply register() it, which will append it to the
        end of the type list.
    """
    pass

def makeparser(remove_blank_text=True, **kw): # real signature unknown; restored from __doc__
    """
    makeparser(remove_blank_text=True, **kw)
    
        Create a new XML parser for objectify trees.
    
        You can pass all keyword arguments that are supported by
        ``etree.XMLParser()``.  Note that this parser defaults to removing
        blank text.  You can disable this by passing the
        ``remove_blank_text`` boolean keyword option yourself.
    """
    pass

def parse(f, parser=None, base_url=None): # real signature unknown; restored from __doc__
    """
    parse(f, parser=None, base_url=None)
    
        Parse a file or file-like object with the objectify parser.
    
        You can pass a different parser as second argument.
    
        The ``base_url`` keyword allows setting a URL for the document
        when parsing from a file-like object.  This is needed when looking
        up external entities (DTD, XInclude, ...) with relative paths.
    """
    pass

def pyannotate(element_or_tree, ignore_old=False, ignore_xsi=False, empty_pytype=None): # real signature unknown; restored from __doc__
    """
    pyannotate(element_or_tree, ignore_old=False, ignore_xsi=False, empty_pytype=None)
    
        Recursively annotates the elements of an XML tree with 'pytype'
        attributes.
    
        If the 'ignore_old' keyword argument is True (the default), current 'pytype'
        attributes will be ignored and replaced.  Otherwise, they will be checked
        and only replaced if they no longer fit the current text value.
    
        Setting the keyword argument ``ignore_xsi`` to True makes the function
        additionally ignore existing ``xsi:type`` annotations.  The default is to
        use them as a type hint.
    
        The default annotation of empty elements can be set with the
        ``empty_pytype`` keyword argument.  The default is not to annotate empty
        elements.  Pass 'str', for example, to make string values the default.
    """
    pass

def pytypename(obj): # real signature unknown; restored from __doc__
    """
    pytypename(obj)
    
        Find the name of the corresponding PyType for a Python object.
    """
    pass

def set_default_parser(new_parser=None): # real signature unknown; restored from __doc__
    """
    set_default_parser(new_parser = None)
    
        Replace the default parser used by objectify's Element() and
        fromstring() functions.
    
        The new parser must be an etree.XMLParser.
    
        Call without arguments to reset to the original parser.
    """
    pass

def set_pytype_attribute_tag(attribute_tag=None): # real signature unknown; restored from __doc__
    """
    set_pytype_attribute_tag(attribute_tag=None)
        Change name and namespace of the XML attribute that holds Python type
        information.
    
        Do not use this unless you know what you are doing.
    
        Reset by calling without argument.
    
        Default: "{http://codespeak.net/lxml/objectify/pytype}pytype"
    """
    pass

def XML(xml, parser=None, base_url=None): # real signature unknown; restored from __doc__
    """
    XML(xml, parser=None, base_url=None)
    
        Objectify specific version of the lxml.etree XML() literal factory
        that uses the objectify parser.
    
        You can pass a different parser as second argument.
    
        The ``base_url`` keyword argument allows to set the original base URL of
        the document to support relative Paths when looking up external entities
        (DTD, XInclude, ...).
    """
    pass

def xsiannotate(element_or_tree, ignore_old=False, ignore_pytype=False, empty_type=None): # real signature unknown; restored from __doc__
    """
    xsiannotate(element_or_tree, ignore_old=False, ignore_pytype=False, empty_type=None)
    
        Recursively annotates the elements of an XML tree with 'xsi:type'
        attributes.
    
        If the 'ignore_old' keyword argument is True (the default), current
        'xsi:type' attributes will be ignored and replaced.  Otherwise, they will be
        checked and only replaced if they no longer fit the current text value.
    
        Note that the mapping from Python types to XSI types is usually ambiguous.
        Currently, only the first XSI type name in the corresponding PyType
        definition will be used for annotation.  Thus, you should consider naming
        the widest type first if you define additional types.
    
        Setting the keyword argument ``ignore_pytype`` to True makes the function
        additionally ignore existing ``pytype`` annotations.  The default is to
        use them as a type hint.
    
        The default annotation of empty elements can be set with the
        ``empty_type`` keyword argument.  The default is not to annotate empty
        elements.  Pass 'string', for example, to make string values the default.
    """
    pass

def __checkBool(*args, **kwargs): # real signature unknown
    pass

def __lower_bool(*args, **kwargs): # real signature unknown
    pass

def __parseBool(*args, **kwargs): # real signature unknown
    pass

def __unpickleElementTree(*args, **kwargs): # real signature unknown
    pass

# classes

class ObjectifiedElement(__lxml_etree.ElementBase):
    """
    Main XML Element class.
    
        Element children are accessed as object attributes.  Multiple children
        with the same name are available through a list index.  Example::
    
           >>> root = XML("<root><c1><c2>0</c2><c2>1</c2></c1></root>")
           >>> second_c2 = root.c1.c2[1]
           >>> print(second_c2.text)
           1
    
        Note that you cannot (and must not) instantiate this class or its
        subclasses.
    """
    def addattr(self, tag, value): # real signature unknown; restored from __doc__
        """
        addattr(self, tag, value)
        
                Add a child value to the element.
        
                As opposed to append(), it sets a data value, not an element.
        """
        pass

    def countchildren(self): # real signature unknown; restored from __doc__
        """
        countchildren(self)
        
                Return the number of children of this element, regardless of their
                name.
        """
        pass

    def descendantpaths(self, prefix=None): # real signature unknown; restored from __doc__
        """
        descendantpaths(self, prefix=None)
        
                Returns a list of object path expressions for all descendants.
        """
        pass

    def getchildren(self): # real signature unknown; restored from __doc__
        """
        getchildren(self)
        
                Returns a sequence of all direct children.  The elements are
                returned in document order.
        """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getattr__(self, *args, **kwargs): # real signature unknown
        """
        Return the (first) child with the given tag name.  If no namespace
                is provided, the child will be looked up in the same one as self.
        """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """
        Return a sibling, counting from the first child of the parent.  The
                method behaves like both a dict and a sequence.
        
                * If argument is an integer, returns the sibling at that position.
        
                * If argument is a string, does the same as getattr().  This can be
                  used to provide namespaces for element lookup, or to look up
                  children with special names (``text`` etc.).
        
                * If argument is a slice object, returns the matching slice.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """ ElementBase(*children, attrib=None, nsmap=None, **_extra) """
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Iterate over self and all siblings with the same tag. """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Count self and siblings with the same tag. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """
        Set the value of the (first) child with the given tag name.  If no
                namespace is provided, the child will be looked up in the same one as
                self.
        """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """
        Set the value of a sibling, counting from the first child of the
                parent.  Implements key assignment, item assignment and slice
                assignment.
        
                * If argument is an integer, sets the sibling at that position.
        
                * If argument is a string, does the same as setattr().  This is used
                  to provide namespaces for element lookup.
        
                * If argument is a sequence (list, tuple, etc.), assign the contained
                  items to the siblings.
        """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is 'mappingproxy({\'__str__\': <slot wrapper \'__str__\' of \'lxml.objectify.ObjectifiedElement\' objects>, \'__getattribute__\': <slot wrapper \'__getattribute__\' of \'lxml.objectify.ObjectifiedElement\' objects>, \'__setattr__\': <slot wrapper \'__setattr__\' of \'lxml.objectify.ObjectifiedElement\' objects>, \'__delattr__\': <slot wrapper \'__delattr__\' of \'lxml.objectify.ObjectifiedElement\' objects>, \'__iter__\': <slot wrapper \'__iter__\' of \'lxml.objectify.ObjectifiedElement\' objects>, \'__len__\': <slot wrapper \'__len__\' of \'lxml.objectify.ObjectifiedElement\' objects>, \'__getitem__\': <slot wrapper \'__getitem__\' of \'lxml.objectify.ObjectifiedElement\' objects>, \'__setitem__\': <slot wrapper \'__setitem__\' of \'lxml.objectify.ObjectifiedElement\' objects>, \'__delitem__\': <slot wrapper \'__delitem__\' of \'lxml.objectify.ObjectifiedElement\' objects>, \'__new__\': <built-in method __new__ of type object at 0x00007FFB24E58BD0>, \'__reduce__\': <cyfunction ObjectifiedElement.__reduce__ at 0x0000024E8CD7C550>, \'countchildren\': <cyfunction ObjectifiedElement.countchildren at 0x0000024E8CD7C608>, \'getchildren\': <cyfunction ObjectifiedElement.getchildren at 0x0000024E8CD7C6C0>, \'__getattr__\': <method \'__getattr__\' of \'lxml.objectify.ObjectifiedElement\' objects>, \'addattr\': <cyfunction ObjectifiedElement.addattr at 0x0000024E8CD7C778>, \'descendantpaths\': <cyfunction ObjectifiedElement.descendantpaths at 0x0000024E8CD7C830>, \'text\': <attribute \'text\' of \'lxml.objectify.ObjectifiedElement\' objects>, \'__dict__\': <attribute \'__dict__\' of \'lxml.objectify.ObjectifiedElement\' objects>, \'__doc__\': \'Main XML Element class.\\n\\n    Element children are accessed as object attributes.  Multiple children\\n    with the same name are available through a list index.  Example::\\n\\n       >>> root = XML("<root><c1><c2>0</c2><c2>1</c2></c1></root>")\\n       >>> second_c2 = root.c1.c2[1]\\n       >>> print(second_c2.text)\\n       1\\n\\n    Note that you cannot (and must not) instantiate this class or its\\n    subclasses.\\n    \'})'


class ObjectifiedDataElement(ObjectifiedElement):
    """
    This is the base class for all data type Elements.  Subclasses should
        override the 'pyval' property and possibly the __str__ method.
    """
    def _setText(self, *args, **kwargs): # real signature unknown
        """
        For use in subclasses only. Don't use unless you know what you are
                doing.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """ ElementBase(*children, attrib=None, nsmap=None, **_extra) """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    pyval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class NumberElement(ObjectifiedDataElement):
    # no doc
    def _setValueParser(self, *args, **kwargs): # real signature unknown
        """
        Set the function that parses the Python value from a string.
        
                Do not use this unless you know what you are doing.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __complex__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
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

    def __init__(self, *args, **kwargs): # real signature unknown
        """ ElementBase(*children, attrib=None, nsmap=None, **_extra) """
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    pyval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class IntElement(NumberElement):
    # no doc
    def _init(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """ ElementBase(*children, attrib=None, nsmap=None, **_extra) """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class BoolElement(IntElement):
    """
    Boolean type base on string values: 'true' or 'false'.
    
        Note that this inherits from IntElement to mimic the behaviour of
        Python's bool type.
    """
    def _init(self, *args, **kwargs): # real signature unknown
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

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

    def __init__(self, *args, **kwargs): # real signature unknown
        """ ElementBase(*children, attrib=None, nsmap=None, **_extra) """
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    pyval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class ElementMaker(object):
    """
    ElementMaker(self, namespace=None, nsmap=None, annotate=True, makeelement=None)
    
        An ElementMaker that can be used for constructing trees.
    
        Example::
    
          >>> M = ElementMaker(annotate=False)
          >>> attributes = {'class': 'par'}
          >>> html = M.html( M.body( M.p('hello', attributes, M.br, 'objectify', style="font-weight: bold") ) )
    
          >>> from lxml.etree import tostring
          >>> print(tostring(html, method='html').decode('ascii'))
          <html><body><p style="font-weight: bold" class="par">hello<br>objectify</p></body></html>
    
        To create tags that are not valid Python identifiers, call the factory
        directly and pass the tag name as first argument::
    
          >>> root = M('tricky-tag', 'some text')
          >>> print(root.tag)
          tricky-tag
          >>> print(root.text)
          some text
    
        Note that this module has a predefined ElementMaker instance called ``E``.
    """
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getattr__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, namespace=None, nsmap=None, annotate=True, makeelement=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000024E8CE4F720>'


class FloatElement(NumberElement):
    # no doc
    def _init(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """ ElementBase(*children, attrib=None, nsmap=None, **_extra) """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class LongElement(NumberElement):
    # no doc
    def _init(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """ ElementBase(*children, attrib=None, nsmap=None, **_extra) """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class NoneElement(ObjectifiedDataElement):
    # no doc
    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

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

    def __init__(self, *args, **kwargs): # real signature unknown
        """ ElementBase(*children, attrib=None, nsmap=None, **_extra) """
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    pyval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class ObjectifyElementClassLookup(__lxml_etree.ElementClassLookup):
    """
    ObjectifyElementClassLookup(self, tree_class=None, empty_data_class=None)
        Element class lookup method that uses the objectify classes.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        """
        Lookup mechanism for objectify.
        
                The default Element classes can be replaced by passing subclasses of
                ObjectifiedElement and ObjectifiedDataElement as keyword arguments.
                'tree_class' defines inner tree classes (defaults to
                ObjectifiedElement), 'empty_data_class' defines the default class for
                empty data elements (defaults to StringElement).
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class ObjectPath(object):
    """
    ObjectPath(path)
        Immutable object that represents a compiled object path.
    
        Example for a path: 'root.child[1].{other}child[25]'
    """
    def addattr(self, root, value): # real signature unknown; restored from __doc__
        """
        addattr(self, root, value)
        
                Append a value to the target element in a subtree.
        
                If any of the children on the path does not exist, it is created.
        """
        pass

    def hasattr(self, root): # real signature unknown; restored from __doc__
        """ hasattr(self, root) """
        pass

    def setattr(self, root, value): # real signature unknown; restored from __doc__
        """
        setattr(self, root, value)
        
                Set the value of the target element in a subtree.
        
                If any of the children on the path does not exist, it is created.
        """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """
        Follow the attribute path in the object structure and return the
                target attribute value.
        
                If it it not found, either returns a default value (if one was passed
                as second argument) or raises AttributeError.
        """
        pass

    def __init__(self, path): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    find = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class PyType(object):
    """
    PyType(self, name, type_check, type_class, stringify=None)
        User defined type.
    
        Named type that contains a type check function, a type class that
        inherits from ObjectifiedDataElement and an optional "stringification"
        function.  The type check must take a string as argument and raise
        ValueError or TypeError if it cannot handle the string value.  It may be
        None in which case it is not considered for type guessing.  For registered
        named types, the 'stringify' function (or unicode() if None) is used to
        convert a Python object with type name 'name' to the string representation
        stored in the XML tree.
    
        Example::
    
            PyType('int', int, MyIntClass).register()
    
        Note that the order in which types are registered matters.  The first
        matching type will be used.
    """
    def register(self, before=None, after=None): # real signature unknown; restored from __doc__
        """
        register(self, before=None, after=None)
        
                Register the type.
        
                The additional keyword arguments 'before' and 'after' accept a
                sequence of type names that must appear before/after the new type in
                the type list.  If any of them is not currently known, it is simply
                ignored.  Raises ValueError if the dependencies cannot be fulfilled.
        """
        pass

    def unregister(self): # real signature unknown; restored from __doc__
        """ unregister(self) """
        pass

    def __init__(self, name, type_check, type_class, stringify=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stringify = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type_check = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    xmlSchemaTypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The list of XML Schema datatypes this Python type maps to.

        Note that this must be set before registering the type!
        """



class StringElement(ObjectifiedDataElement):
    """
    String data class.
    
        Note that this class does *not* support the sequence protocol of strings:
        len(), iter(), str_attr[0], str_attr[0:1], etc. are *not* supported.
        Instead, use the .text attribute to get a 'real' string.
    """
    def strlen(self, *args, **kwargs): # real signature unknown
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __complex__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
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

    def __init__(self, *args, **kwargs): # real signature unknown
        """ ElementBase(*children, attrib=None, nsmap=None, **_extra) """
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    pyval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

__all__ = [
    'BoolElement',
    'DataElement',
    'E',
    'Element',
    'ElementMaker',
    'FloatElement',
    'IntElement',
    'LongElement',
    'NoneElement',
    'NumberElement',
    'ObjectPath',
    'ObjectifiedDataElement',
    'ObjectifiedElement',
    'ObjectifyElementClassLookup',
    'PYTYPE_ATTRIBUTE',
    'PyType',
    'StringElement',
    'SubElement',
    'XML',
    'annotate',
    'deannotate',
    'dump',
    'enable_recursive_str',
    'fromstring',
    'getRegisteredTypes',
    'makeparser',
    'parse',
    'pyannotate',
    'pytypename',
    'set_default_parser',
    'set_pytype_attribute_tag',
    'xsiannotate',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000024E8CCFBA58>'

__spec__ = None # (!) real value is "ModuleSpec(name='lxml.objectify', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000024E8CCFBA58>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\lxml\\\\objectify.cp37-win_amd64.pyd')"

__test__ = {}

