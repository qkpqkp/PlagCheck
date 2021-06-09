# encoding: utf-8
# module lxml.builder
# from C:\Users\Doly\Anaconda3\lib\site-packages\lxml\builder.cp37-win_amd64.pyd
# by generator 1.147
""" The ``E`` Element factory for generating XML documents. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

# functions

def E(tag): # real signature unknown; restored from __doc__
    """
    Element generator factory.
    
        Unlike the ordinary Element factory, the E factory allows you to pass in
        more than just a tag and some optional attributes; you can also pass in
        text and other elements.  The text is added as either text or tail
        attributes, and elements are inserted at the right spot.  Some small
        examples::
    
            >>> from lxml import etree as ET
            >>> from lxml.builder import E
    
            >>> ET.tostring(E("tag"))
            '<tag/>'
            >>> ET.tostring(E("tag", "text"))
            '<tag>text</tag>'
            >>> ET.tostring(E("tag", "text", key="value"))
            '<tag key="value">text</tag>'
            >>> ET.tostring(E("tag", E("subtag", "text"), "tail"))
            '<tag><subtag>text</subtag>tail</tag>'
    
        For simple tags, the factory also allows you to write ``E.tag(...)`` instead
        of ``E('tag', ...)``::
    
            >>> ET.tostring(E.tag())
            '<tag/>'
            >>> ET.tostring(E.tag("text"))
            '<tag>text</tag>'
            >>> ET.tostring(E.tag(E.subtag("text"), "tail"))
            '<tag><subtag>text</subtag>tail</tag>'
    
        Here's a somewhat larger example; this shows how to generate HTML
        documents, using a mix of prepared factory functions for inline elements,
        nested ``E.tag`` calls, and embedded XHTML fragments::
    
            # some common inline elements
            A = E.a
            I = E.i
            B = E.b
    
            def CLASS(v):
                # helper function, 'class' is a reserved word
                return {'class': v}
    
            page = (
                E.html(
                    E.head(
                        E.title("This is a sample document")
                    ),
                    E.body(
                        E.h1("Hello!", CLASS("title")),
                        E.p("This is a paragraph with ", B("bold"), " text in it!"),
                        E.p("This is another paragraph, with a ",
                            A("link", href="http://www.python.org"), "."),
                        E.p("Here are some reserved characters: <spam&egg>."),
                        ET.XML("<p>And finally, here is an embedded XHTML fragment.</p>"),
                    )
                )
            )
    
            print ET.tostring(page)
    
        Here's a prettyprinted version of the output from the above script::
    
            <html>
              <head>
                <title>This is a sample document</title>
              </head>
              <body>
                <h1 class="title">Hello!</h1>
                <p>This is a paragraph with <b>bold</b> text in it!</p>
                <p>This is another paragraph, with <a href="http://www.python.org">link</a>.</p>
                <p>Here are some reserved characters: &lt;spam&amp;egg&gt;.</p>
                <p>And finally, here is an embedded XHTML fragment.</p>
              </body>
            </html>
    
        For namespace support, you can pass a namespace map (``nsmap``)
        and/or a specific target ``namespace`` to the ElementMaker class::
    
            >>> E = ElementMaker(namespace="http://my.ns/")
            >>> print(ET.tostring( E.test ))
            <test xmlns="http://my.ns/"/>
    
            >>> E = ElementMaker(namespace="http://my.ns/", nsmap={'p':'http://my.ns/'})
            >>> print(ET.tostring( E.test ))
            <p:test xmlns:p="http://my.ns/"/>
    """
    pass

def __pyx_unpickle_ElementMaker(*args, **kwargs): # real signature unknown
    pass

def __reduce_cython__(*args, **kwargs): # real signature unknown
    pass

def __setstate_cython__(*args, **kwargs): # real signature unknown
    pass

# classes

class unicode(object):
    """
    str(object='') -> str
    str(bytes_or_buffer[, encoding[, errors]]) -> str
    
    Create a new string object from the given object. If encoding or
    errors is specified, then the object must expose a data buffer
    that will be decoded using the given encoding and error handler.
    Otherwise, returns the result of object.__str__() (if defined)
    or repr(object).
    encoding defaults to sys.getdefaultencoding().
    errors defaults to 'strict'.
    """
    def capitalize(self, *args, **kwargs): # real signature unknown
        """
        Return a capitalized version of the string.
        
        More specifically, make the first character have upper case and the rest lower
        case.
        """
        pass

    def casefold(self, *args, **kwargs): # real signature unknown
        """ Return a version of the string suitable for caseless comparisons. """
        pass

    def center(self, *args, **kwargs): # real signature unknown
        """
        Return a centered string of length width.
        
        Padding is done using the specified fill character (default is a space).
        """
        pass

    def count(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.count(sub[, start[, end]]) -> int
        
        Return the number of non-overlapping occurrences of substring sub in
        string S[start:end].  Optional arguments start and end are
        interpreted as in slice notation.
        """
        return 0

    def encode(self, *args, **kwargs): # real signature unknown
        """
        Encode the string using the codec registered for encoding.
        
          encoding
            The encoding in which to encode the string.
          errors
            The error handling scheme to use for encoding errors.
            The default is 'strict' meaning that encoding errors raise a
            UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
            'xmlcharrefreplace' as well as any other name registered with
            codecs.register_error that can handle UnicodeEncodeErrors.
        """
        pass

    def endswith(self, suffix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.endswith(suffix[, start[, end]]) -> bool
        
        Return True if S ends with the specified suffix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        suffix can also be a tuple of strings to try.
        """
        return False

    def expandtabs(self, *args, **kwargs): # real signature unknown
        """
        Return a copy where all tab characters are expanded using spaces.
        
        If tabsize is not given, a tab size of 8 characters is assumed.
        """
        pass

    def find(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.find(sub[, start[, end]]) -> int
        
        Return the lowest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    def format(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        S.format(*args, **kwargs) -> str
        
        Return a formatted version of S, using substitutions from args and kwargs.
        The substitutions are identified by braces ('{' and '}').
        """
        return ""

    def format_map(self, mapping): # real signature unknown; restored from __doc__
        """
        S.format_map(mapping) -> str
        
        Return a formatted version of S, using substitutions from mapping.
        The substitutions are identified by braces ('{' and '}').
        """
        return ""

    def index(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.index(sub[, start[, end]]) -> int
        
        Return the lowest index in S where substring sub is found, 
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Raises ValueError when the substring is not found.
        """
        return 0

    def isalnum(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is an alpha-numeric string, False otherwise.
        
        A string is alpha-numeric if all characters in the string are alpha-numeric and
        there is at least one character in the string.
        """
        pass

    def isalpha(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is an alphabetic string, False otherwise.
        
        A string is alphabetic if all characters in the string are alphabetic and there
        is at least one character in the string.
        """
        pass

    def isascii(self, *args, **kwargs): # real signature unknown
        """
        Return True if all characters in the string are ASCII, False otherwise.
        
        ASCII characters have code points in the range U+0000-U+007F.
        Empty string is ASCII too.
        """
        pass

    def isdecimal(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a decimal string, False otherwise.
        
        A string is a decimal string if all characters in the string are decimal and
        there is at least one character in the string.
        """
        pass

    def isdigit(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a digit string, False otherwise.
        
        A string is a digit string if all characters in the string are digits and there
        is at least one character in the string.
        """
        pass

    def isidentifier(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a valid Python identifier, False otherwise.
        
        Use keyword.iskeyword() to test for reserved identifiers such as "def" and
        "class".
        """
        pass

    def islower(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a lowercase string, False otherwise.
        
        A string is lowercase if all cased characters in the string are lowercase and
        there is at least one cased character in the string.
        """
        pass

    def isnumeric(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a numeric string, False otherwise.
        
        A string is numeric if all characters in the string are numeric and there is at
        least one character in the string.
        """
        pass

    def isprintable(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is printable, False otherwise.
        
        A string is printable if all of its characters are considered printable in
        repr() or if it is empty.
        """
        pass

    def isspace(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a whitespace string, False otherwise.
        
        A string is whitespace if all characters in the string are whitespace and there
        is at least one character in the string.
        """
        pass

    def istitle(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is a title-cased string, False otherwise.
        
        In a title-cased string, upper- and title-case characters may only
        follow uncased characters and lowercase characters only cased ones.
        """
        pass

    def isupper(self, *args, **kwargs): # real signature unknown
        """
        Return True if the string is an uppercase string, False otherwise.
        
        A string is uppercase if all cased characters in the string are uppercase and
        there is at least one cased character in the string.
        """
        pass

    def join(self, ab=None, pq=None, rs=None): # real signature unknown; restored from __doc__
        """
        Concatenate any number of strings.
        
        The string whose method is called is inserted in between each given string.
        The result is returned as a new string.
        
        Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
        """
        pass

    def ljust(self, *args, **kwargs): # real signature unknown
        """
        Return a left-justified string of length width.
        
        Padding is done using the specified fill character (default is a space).
        """
        pass

    def lower(self, *args, **kwargs): # real signature unknown
        """ Return a copy of the string converted to lowercase. """
        pass

    def lstrip(self, *args, **kwargs): # real signature unknown
        """
        Return a copy of the string with leading whitespace removed.
        
        If chars is given and not None, remove characters in chars instead.
        """
        pass

    def maketrans(self, *args, **kwargs): # real signature unknown
        """
        Return a translation table usable for str.translate().
        
        If there is only one argument, it must be a dictionary mapping Unicode
        ordinals (integers) or characters to Unicode ordinals, strings or None.
        Character keys will be then converted to ordinals.
        If there are two arguments, they must be strings of equal length, and
        in the resulting dictionary, each character in x will be mapped to the
        character at the same position in y. If there is a third argument, it
        must be a string, whose characters will be mapped to None in the result.
        """
        pass

    def partition(self, *args, **kwargs): # real signature unknown
        """
        Partition the string into three parts using the given separator.
        
        This will search for the separator in the string.  If the separator is found,
        returns a 3-tuple containing the part before the separator, the separator
        itself, and the part after it.
        
        If the separator is not found, returns a 3-tuple containing the original string
        and two empty strings.
        """
        pass

    def replace(self, *args, **kwargs): # real signature unknown
        """
        Return a copy with all occurrences of substring old replaced by new.
        
          count
            Maximum number of occurrences to replace.
            -1 (the default value) means replace all occurrences.
        
        If the optional argument count is given, only the first count occurrences are
        replaced.
        """
        pass

    def rfind(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.rfind(sub[, start[, end]]) -> int
        
        Return the highest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    def rindex(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.rindex(sub[, start[, end]]) -> int
        
        Return the highest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Raises ValueError when the substring is not found.
        """
        return 0

    def rjust(self, *args, **kwargs): # real signature unknown
        """
        Return a right-justified string of length width.
        
        Padding is done using the specified fill character (default is a space).
        """
        pass

    def rpartition(self, *args, **kwargs): # real signature unknown
        """
        Partition the string into three parts using the given separator.
        
        This will search for the separator in the string, starting at the end. If
        the separator is found, returns a 3-tuple containing the part before the
        separator, the separator itself, and the part after it.
        
        If the separator is not found, returns a 3-tuple containing two empty strings
        and the original string.
        """
        pass

    def rsplit(self, *args, **kwargs): # real signature unknown
        """
        Return a list of the words in the string, using sep as the delimiter string.
        
          sep
            The delimiter according which to split the string.
            None (the default value) means split according to any whitespace,
            and discard empty strings from the result.
          maxsplit
            Maximum number of splits to do.
            -1 (the default value) means no limit.
        
        Splits are done starting at the end of the string and working to the front.
        """
        pass

    def rstrip(self, *args, **kwargs): # real signature unknown
        """
        Return a copy of the string with trailing whitespace removed.
        
        If chars is given and not None, remove characters in chars instead.
        """
        pass

    def split(self, *args, **kwargs): # real signature unknown
        """
        Return a list of the words in the string, using sep as the delimiter string.
        
          sep
            The delimiter according which to split the string.
            None (the default value) means split according to any whitespace,
            and discard empty strings from the result.
          maxsplit
            Maximum number of splits to do.
            -1 (the default value) means no limit.
        """
        pass

    def splitlines(self, *args, **kwargs): # real signature unknown
        """
        Return a list of the lines in the string, breaking at line boundaries.
        
        Line breaks are not included in the resulting list unless keepends is given and
        true.
        """
        pass

    def startswith(self, prefix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.startswith(prefix[, start[, end]]) -> bool
        
        Return True if S starts with the specified prefix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        prefix can also be a tuple of strings to try.
        """
        return False

    def strip(self, *args, **kwargs): # real signature unknown
        """
        Return a copy of the string with leading and trailing whitespace remove.
        
        If chars is given and not None, remove characters in chars instead.
        """
        pass

    def swapcase(self, *args, **kwargs): # real signature unknown
        """ Convert uppercase characters to lowercase and lowercase characters to uppercase. """
        pass

    def title(self, *args, **kwargs): # real signature unknown
        """
        Return a version of the string where each word is titlecased.
        
        More specifically, words start with uppercased characters and all remaining
        cased characters have lower case.
        """
        pass

    def translate(self, *args, **kwargs): # real signature unknown
        """
        Replace each character in the string using the given translation table.
        
          table
            Translation table, which must be a mapping of Unicode ordinals to
            Unicode ordinals, strings, or None.
        
        The table must implement lookup/indexing via __getitem__, for instance a
        dictionary or list.  If this operation raises LookupError, the character is
        left untouched.  Characters mapped to None are deleted.
        """
        pass

    def upper(self, *args, **kwargs): # real signature unknown
        """ Return a copy of the string converted to uppercase. """
        pass

    def zfill(self, *args, **kwargs): # real signature unknown
        """
        Pad a numeric string with zeros on the left, to fill a field of the given width.
        
        The string is never truncated.
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ Return a formatted version of the string as described by format_spec. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Return the size of the string in memory, in bytes. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass


basestring = unicode


class ElementMaker(object):
    """
    Element generator factory.
    
        Unlike the ordinary Element factory, the E factory allows you to pass in
        more than just a tag and some optional attributes; you can also pass in
        text and other elements.  The text is added as either text or tail
        attributes, and elements are inserted at the right spot.  Some small
        examples::
    
            >>> from lxml import etree as ET
            >>> from lxml.builder import E
    
            >>> ET.tostring(E("tag"))
            '<tag/>'
            >>> ET.tostring(E("tag", "text"))
            '<tag>text</tag>'
            >>> ET.tostring(E("tag", "text", key="value"))
            '<tag key="value">text</tag>'
            >>> ET.tostring(E("tag", E("subtag", "text"), "tail"))
            '<tag><subtag>text</subtag>tail</tag>'
    
        For simple tags, the factory also allows you to write ``E.tag(...)`` instead
        of ``E('tag', ...)``::
    
            >>> ET.tostring(E.tag())
            '<tag/>'
            >>> ET.tostring(E.tag("text"))
            '<tag>text</tag>'
            >>> ET.tostring(E.tag(E.subtag("text"), "tail"))
            '<tag><subtag>text</subtag>tail</tag>'
    
        Here's a somewhat larger example; this shows how to generate HTML
        documents, using a mix of prepared factory functions for inline elements,
        nested ``E.tag`` calls, and embedded XHTML fragments::
    
            # some common inline elements
            A = E.a
            I = E.i
            B = E.b
    
            def CLASS(v):
                # helper function, 'class' is a reserved word
                return {'class': v}
    
            page = (
                E.html(
                    E.head(
                        E.title("This is a sample document")
                    ),
                    E.body(
                        E.h1("Hello!", CLASS("title")),
                        E.p("This is a paragraph with ", B("bold"), " text in it!"),
                        E.p("This is another paragraph, with a ",
                            A("link", href="http://www.python.org"), "."),
                        E.p("Here are some reserved characters: <spam&egg>."),
                        ET.XML("<p>And finally, here is an embedded XHTML fragment.</p>"),
                    )
                )
            )
    
            print ET.tostring(page)
    
        Here's a prettyprinted version of the output from the above script::
    
            <html>
              <head>
                <title>This is a sample document</title>
              </head>
              <body>
                <h1 class="title">Hello!</h1>
                <p>This is a paragraph with <b>bold</b> text in it!</p>
                <p>This is another paragraph, with <a href="http://www.python.org">link</a>.</p>
                <p>Here are some reserved characters: &lt;spam&amp;egg&gt;.</p>
                <p>And finally, here is an embedded XHTML fragment.</p>
              </body>
            </html>
    
        For namespace support, you can pass a namespace map (``nsmap``)
        and/or a specific target ``namespace`` to the ElementMaker class::
    
            >>> E = ElementMaker(namespace="http://my.ns/")
            >>> print(ET.tostring( E.test ))
            <test xmlns="http://my.ns/"/>
    
            >>> E = ElementMaker(namespace="http://my.ns/", nsmap={'p':'http://my.ns/'})
            >>> print(ET.tostring( E.test ))
            <p:test xmlns:p="http://my.ns/"/>
    """
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getattr__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, namespace=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    _makeelement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _namespace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _nsmap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _typemap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000021ED2D8E400>'

__pyx_capi__ = {
    'ET': None, # (!) real value is '<capsule object "PyObject *" at 0x0000021ED2D69660>'
    'partial': None, # (!) real value is '<capsule object "PyObject *" at 0x0000021ED2D69690>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='lxml.builder', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000021ED2D8E400>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\lxml\\\\builder.cp37-win_amd64.pyd')"

__test__ = {}

