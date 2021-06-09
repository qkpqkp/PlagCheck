# encoding: utf-8
# module lxml.html.clean
# from C:\Users\Doly\Anaconda3\lib\site-packages\lxml\html\clean.cp37-win_amd64.pyd
# by generator 1.147
"""
A cleanup tool for HTML.

Removes unwanted tags and content.  See the `Cleaner` class for
details.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import re as re # C:\Users\Doly\Anaconda3\lib\re.py
import copy as copy # C:\Users\Doly\Anaconda3\lib\copy.py
import lxml.etree as etree # C:\Users\Doly\Anaconda3\lib\site-packages\lxml\etree.cp37-win_amd64.pyd
import lxml.html.defs as defs # C:\Users\Doly\Anaconda3\lib\site-packages\lxml\html\defs.py

# Variables with simple values

XHTML_NAMESPACE = 'http://www.w3.org/1999/xhtml'

# functions

def autolink(*args, **kwargs): # real signature unknown
    """
    Turn any URLs into links.
    
        It will search for links identified by the given regular
        expressions (by default mailto and http(s) links).
    
        It won't link text in an element in avoid_elements, or an element
        with a class in avoid_classes.  It won't link to anything with a
        host that matches one of the regular expressions in avoid_hosts
        (default localhost and 127.0.0.1).
    
        If you pass in an element, the element's tail will not be
        substituted, only the contents of the element.
    """
    pass

def autolink_html(*args, **kwargs): # real signature unknown
    """
    Turn any URLs into links.
    
        It will search for links identified by the given regular
        expressions (by default mailto and http(s) links).
    
        It won't link text in an element in avoid_elements, or an element
        with a class in avoid_classes.  It won't link to anything with a
        host that matches one of the regular expressions in avoid_hosts
        (default localhost and 127.0.0.1).
    
        If you pass in an element, the element's tail will not be
        substituted, only the contents of the element.
    """
    pass

def clean(*args, **kwargs): # real signature unknown
    """
    Instances cleans the document of each of the possible offending
        elements.  The cleaning is controlled by attributes; you can
        override attributes in a subclass, or set them in the constructor.
    
        ``scripts``:
            Removes any ``<script>`` tags.
    
        ``javascript``:
            Removes any Javascript, like an ``onclick`` attribute. Also removes stylesheets
            as they could contain Javascript.
    
        ``comments``:
            Removes any comments.
    
        ``style``:
            Removes any style tags.
    
        ``inline_style``
            Removes any style attributes.  Defaults to the value of the ``style`` option.
    
        ``links``:
            Removes any ``<link>`` tags
    
        ``meta``:
            Removes any ``<meta>`` tags
    
        ``page_structure``:
            Structural parts of a page: ``<head>``, ``<html>``, ``<title>``.
    
        ``processing_instructions``:
            Removes any processing instructions.
    
        ``embedded``:
            Removes any embedded objects (flash, iframes)
    
        ``frames``:
            Removes any frame-related tags
    
        ``forms``:
            Removes any form tags
    
        ``annoying_tags``:
            Tags that aren't *wrong*, but are annoying.  ``<blink>`` and ``<marquee>``
    
        ``remove_tags``:
            A list of tags to remove.  Only the tags will be removed,
            their content will get pulled up into the parent tag.
    
        ``kill_tags``:
            A list of tags to kill.  Killing also removes the tag's content,
            i.e. the whole subtree, not just the tag itself.
    
        ``allow_tags``:
            A list of tags to include (default include all).
    
        ``remove_unknown_tags``:
            Remove any tags that aren't standard parts of HTML.
    
        ``safe_attrs_only``:
            If true, only include 'safe' attributes (specifically the list
            from the feedparser HTML sanitisation web site).
    
        ``safe_attrs``:
            A set of attribute names to override the default list of attributes
            considered 'safe' (when safe_attrs_only=True).
    
        ``add_nofollow``:
            If true, then any <a> tags will have ``rel="nofollow"`` added to them.
    
        ``host_whitelist``:
            A list or set of hosts that you can use for embedded content
            (for content like ``<object>``, ``<link rel="stylesheet">``, etc).
            You can also implement/override the method
            ``allow_embedded_url(el, url)`` or ``allow_element(el)`` to
            implement more complex rules for what can be embedded.
            Anything that passes this test will be shown, regardless of
            the value of (for instance) ``embedded``.
    
            Note that this parameter might not work as intended if you do not
            make the links absolute before doing the cleaning.
    
            Note that you may also need to set ``whitelist_tags``.
    
        ``whitelist_tags``:
            A set of tags that can be included with ``host_whitelist``.
            The default is ``iframe`` and ``embed``; you may wish to
            include other tags like ``script``, or you may want to
            implement ``allow_embedded_url`` for more control.  Set to None to
            include all tags.
    
        This modifies the document *in place*.
    """
    pass

def clean_html(*args, **kwargs): # real signature unknown
    pass

def fromstring(html, base_url=None, parser=None, **kw): # reliably restored by inspect
    """
    Parse the html, returning a single element/document.
    
        This tries to minimally parse the chunk of text, without knowing if it
        is a fragment or a document.
    
        base_url will set the document's base_url attribute (and the tree's docinfo.URL)
    """
    pass

def unichr(*args, **kwargs): # real signature unknown
    """ Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff. """
    pass

def unquote_plus(string, encoding=None, errors=None): # reliably restored by inspect
    """
    Like unquote(), but also replace plus signs by spaces, as required for
        unquoting HTML form values.
    
        unquote_plus('%7e/abc+def') -> '~/abc def'
    """
    pass

def urlsplit(url, scheme=None, allow_fragments=True): # reliably restored by inspect
    """
    Parse a URL into 5 components:
        <scheme>://<netloc>/<path>?<query>#<fragment>
        Return a 5-tuple: (scheme, netloc, path, query, fragment).
        Note that we don't break the components up in smaller bits
        (e.g. netloc is a single string) and we don't expand % escapes.
    """
    pass

def word_break(*args, **kwargs): # real signature unknown
    """
    Breaks any long words found in the body of the text (not attributes).
    
        Doesn't effect any of the tags in avoid_elements, by default
        ``<textarea>`` and ``<pre>``
    
        Breaks words by inserting &#8203;, which is a unicode character
        for Zero Width Space character.  This generally takes up no space
        in rendering, but does copy as a space, and in monospace contexts
        usually takes up space.
    
        See http://www.cs.tut.fi/~jkorpela/html/nobr.html for a discussion
    """
    pass

def word_break_html(*args, **kwargs): # real signature unknown
    pass

def xhtml_to_html(xhtml): # reliably restored by inspect
    """
    Convert all tags in an XHTML tree to HTML by removing their
        XHTML namespace.
    """
    pass

def _break_text(*args, **kwargs): # real signature unknown
    pass

def _find_external_links(*args, **kwargs): # real signature unknown
    """
    XPath(self, path, namespaces=None, extensions=None, regexp=True, smart_strings=True)
        A compiled XPath expression that can be called on Elements and ElementTrees.
    
        Besides the XPath expression, you can pass prefix-namespace
        mappings and extension functions to the constructor through the
        keyword arguments ``namespaces`` and ``extensions``.  EXSLT
        regular expression support can be disabled with the 'regexp'
        boolean keyword (defaults to True).  Smart strings will be
        returned for string results unless you pass
        ``smart_strings=False``.
    """
    pass

def _find_styled_elements(*args, **kwargs): # real signature unknown
    """
    XPath(self, path, namespaces=None, extensions=None, regexp=True, smart_strings=True)
        A compiled XPath expression that can be called on Elements and ElementTrees.
    
        Besides the XPath expression, you can pass prefix-namespace
        mappings and extension functions to the constructor through the
        keyword arguments ``namespaces`` and ``extensions``.  EXSLT
        regular expression support can be disabled with the 'regexp'
        boolean keyword (defaults to True).  Smart strings will be
        returned for string results unless you pass
        ``smart_strings=False``.
    """
    pass

def _insert_break(*args, **kwargs): # real signature unknown
    pass

def _is_image_dataurl(*args, **kwargs): # real signature unknown
    """
    Scan through string looking for a match, and return a corresponding match object instance.
    
    Return None if no position in the string matches.
    """
    pass

def _is_javascript_scheme(*args, **kwargs): # real signature unknown
    pass

def _is_possibly_malicious_scheme(*args, **kwargs): # real signature unknown
    """
    Scan through string looking for a match, and return a corresponding match object instance.
    
    Return None if no position in the string matches.
    """
    pass

def _link_text(*args, **kwargs): # real signature unknown
    pass

def _substitute_whitespace(*args, **kwargs): # real signature unknown
    """ Return the string obtained by replacing the leftmost non-overlapping occurrences of pattern in string by the replacement repl. """
    pass

def _transform_result(typ, result): # reliably restored by inspect
    """ Convert the result back into the input type. """
    pass

# classes

class Cleaner(object):
    """
    Instances cleans the document of each of the possible offending
        elements.  The cleaning is controlled by attributes; you can
        override attributes in a subclass, or set them in the constructor.
    
        ``scripts``:
            Removes any ``<script>`` tags.
    
        ``javascript``:
            Removes any Javascript, like an ``onclick`` attribute. Also removes stylesheets
            as they could contain Javascript.
    
        ``comments``:
            Removes any comments.
    
        ``style``:
            Removes any style tags.
    
        ``inline_style``
            Removes any style attributes.  Defaults to the value of the ``style`` option.
    
        ``links``:
            Removes any ``<link>`` tags
    
        ``meta``:
            Removes any ``<meta>`` tags
    
        ``page_structure``:
            Structural parts of a page: ``<head>``, ``<html>``, ``<title>``.
    
        ``processing_instructions``:
            Removes any processing instructions.
    
        ``embedded``:
            Removes any embedded objects (flash, iframes)
    
        ``frames``:
            Removes any frame-related tags
    
        ``forms``:
            Removes any form tags
    
        ``annoying_tags``:
            Tags that aren't *wrong*, but are annoying.  ``<blink>`` and ``<marquee>``
    
        ``remove_tags``:
            A list of tags to remove.  Only the tags will be removed,
            their content will get pulled up into the parent tag.
    
        ``kill_tags``:
            A list of tags to kill.  Killing also removes the tag's content,
            i.e. the whole subtree, not just the tag itself.
    
        ``allow_tags``:
            A list of tags to include (default include all).
    
        ``remove_unknown_tags``:
            Remove any tags that aren't standard parts of HTML.
    
        ``safe_attrs_only``:
            If true, only include 'safe' attributes (specifically the list
            from the feedparser HTML sanitisation web site).
    
        ``safe_attrs``:
            A set of attribute names to override the default list of attributes
            considered 'safe' (when safe_attrs_only=True).
    
        ``add_nofollow``:
            If true, then any <a> tags will have ``rel="nofollow"`` added to them.
    
        ``host_whitelist``:
            A list or set of hosts that you can use for embedded content
            (for content like ``<object>``, ``<link rel="stylesheet">``, etc).
            You can also implement/override the method
            ``allow_embedded_url(el, url)`` or ``allow_element(el)`` to
            implement more complex rules for what can be embedded.
            Anything that passes this test will be shown, regardless of
            the value of (for instance) ``embedded``.
    
            Note that this parameter might not work as intended if you do not
            make the links absolute before doing the cleaning.
    
            Note that you may also need to set ``whitelist_tags``.
    
        ``whitelist_tags``:
            A set of tags that can be included with ``host_whitelist``.
            The default is ``iframe`` and ``embed``; you may wish to
            include other tags like ``script``, or you may want to
            implement ``allow_embedded_url`` for more control.  Set to None to
            include all tags.
    
        This modifies the document *in place*.
    """
    def allow_element(self, *args, **kwargs): # real signature unknown
        pass

    def allow_embedded_url(self, *args, **kwargs): # real signature unknown
        pass

    def allow_follow(self, *args, **kwargs): # real signature unknown
        """ Override to suppress rel="nofollow" on some anchors. """
        pass

    def clean_html(self, *args, **kwargs): # real signature unknown
        pass

    def kill_conditional_comments(self, *args, **kwargs): # real signature unknown
        """
        IE conditional comments basically embed HTML that the parser
                doesn't normally see.  We can't allow anything like that, so
                we'll kill any comments that could be conditional.
        """
        pass

    def _has_sneaky_javascript(self, *args, **kwargs): # real signature unknown
        """
        Depending on the browser, stuff like ``e x p r e s s i o n(...)``
                can get interpreted, or ``expre/* stuff */ssion(...)``.  This
                checks for attempt to do stuff like this.
        
                Typically the response will be to kill the entire style; if you
                have just a bit of Javascript in the style another rule will catch
                that and remove only the Javascript from the style; this catches
                more sneaky attempts.
        """
        pass

    def _kill_elements(self, *args, **kwargs): # real signature unknown
        pass

    def _remove_javascript_link(self, *args, **kwargs): # real signature unknown
        pass

    def _substitute_comments(self, *args, **kwargs): # real signature unknown
        """ Return the string obtained by replacing the leftmost non-overlapping occurrences of pattern in string by the replacement repl. """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Cleans the document. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    add_nofollow = False
    allow_tags = None
    annoying_tags = True
    comments = True
    embedded = True
    forms = True
    frames = True
    host_whitelist = ()
    inline_style = None
    javascript = True
    kill_tags = None
    links = True
    meta = True
    page_structure = True
    processing_instructions = True
    remove_tags = None
    remove_unknown_tags = True
    safe_attrs = defs.safe_attrs
    safe_attrs_only = True
    scripts = True
    style = False
    whitelist_tags = None # (!) real value is "{'iframe', 'embed'}"
    _tag_link_attrs = {
        'a': 'href',
        'applet': [
            'code',
            'object',
        ],
        'embed': 'src',
        'iframe': 'src',
        'layer': 'src',
        'link': 'href',
        'script': 'src',
    }
    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'lxml.html.clean\', \'__doc__\': \'\\n    Instances cleans the document of each of the possible offending\\n    elements.  The cleaning is controlled by attributes; you can\\n    override attributes in a subclass, or set them in the constructor.\\n\\n    ``scripts``:\\n        Removes any ``<script>`` tags.\\n\\n    ``javascript``:\\n        Removes any Javascript, like an ``onclick`` attribute. Also removes stylesheets\\n        as they could contain Javascript.\\n\\n    ``comments``:\\n        Removes any comments.\\n\\n    ``style``:\\n        Removes any style tags.\\n\\n    ``inline_style``\\n        Removes any style attributes.  Defaults to the value of the ``style`` option.\\n\\n    ``links``:\\n        Removes any ``<link>`` tags\\n\\n    ``meta``:\\n        Removes any ``<meta>`` tags\\n\\n    ``page_structure``:\\n        Structural parts of a page: ``<head>``, ``<html>``, ``<title>``.\\n\\n    ``processing_instructions``:\\n        Removes any processing instructions.\\n\\n    ``embedded``:\\n        Removes any embedded objects (flash, iframes)\\n\\n    ``frames``:\\n        Removes any frame-related tags\\n\\n    ``forms``:\\n        Removes any form tags\\n\\n    ``annoying_tags``:\\n        Tags that aren\\\'t *wrong*, but are annoying.  ``<blink>`` and ``<marquee>``\\n\\n    ``remove_tags``:\\n        A list of tags to remove.  Only the tags will be removed,\\n        their content will get pulled up into the parent tag.\\n\\n    ``kill_tags``:\\n        A list of tags to kill.  Killing also removes the tag\\\'s content,\\n        i.e. the whole subtree, not just the tag itself.\\n\\n    ``allow_tags``:\\n        A list of tags to include (default include all).\\n\\n    ``remove_unknown_tags``:\\n        Remove any tags that aren\\\'t standard parts of HTML.\\n\\n    ``safe_attrs_only``:\\n        If true, only include \\\'safe\\\' attributes (specifically the list\\n        from the feedparser HTML sanitisation web site).\\n\\n    ``safe_attrs``:\\n        A set of attribute names to override the default list of attributes\\n        considered \\\'safe\\\' (when safe_attrs_only=True).\\n\\n    ``add_nofollow``:\\n        If true, then any <a> tags will have ``rel="nofollow"`` added to them.\\n\\n    ``host_whitelist``:\\n        A list or set of hosts that you can use for embedded content\\n        (for content like ``<object>``, ``<link rel="stylesheet">``, etc).\\n        You can also implement/override the method\\n        ``allow_embedded_url(el, url)`` or ``allow_element(el)`` to\\n        implement more complex rules for what can be embedded.\\n        Anything that passes this test will be shown, regardless of\\n        the value of (for instance) ``embedded``.\\n\\n        Note that this parameter might not work as intended if you do not\\n        make the links absolute before doing the cleaning.\\n\\n        Note that you may also need to set ``whitelist_tags``.\\n\\n    ``whitelist_tags``:\\n        A set of tags that can be included with ``host_whitelist``.\\n        The default is ``iframe`` and ``embed``; you may wish to\\n        include other tags like ``script``, or you may want to\\n        implement ``allow_embedded_url`` for more control.  Set to None to\\n        include all tags.\\n\\n    This modifies the document *in place*.\\n    \', \'scripts\': True, \'javascript\': True, \'comments\': True, \'style\': False, \'inline_style\': None, \'links\': True, \'meta\': True, \'page_structure\': True, \'processing_instructions\': True, \'embedded\': True, \'frames\': True, \'forms\': True, \'annoying_tags\': True, \'remove_tags\': None, \'allow_tags\': None, \'kill_tags\': None, \'remove_unknown_tags\': True, \'safe_attrs_only\': True, \'safe_attrs\': frozenset({\'rowspan\', \'class\', \'usemap\', \'charset\', \'label\', \'src\', \'align\', \'char\', \'colspan\', \'rules\', \'scope\', \'clear\', \'size\', \'ismap\', \'name\', \'action\', \'dir\', \'abbr\', \'border\', \'coords\', \'nowrap\', \'hreflang\', \'longdesc\', \'rows\', \'valign\', \'accesskey\', \'datetime\', \'maxlength\', \'prompt\', \'checked\', \'cite\', \'cellspacing\', \'id\', \'rev\', \'for\', \'vspace\', \'target\', \'type\', \'span\', \'charoff\', \'href\', \'cellpadding\', \'summary\', \'selected\', \'enctype\', \'headers\', \'noshade\', \'disabled\', \'readonly\', \'accept\', \'cols\', \'compact\', \'method\', \'lang\', \'multiple\', \'start\', \'value\', \'nohref\', \'tabindex\', \'hspace\', \'alt\', \'width\', \'accept-charset\', \'title\', \'frame\', \'media\', \'rel\', \'axis\', \'height\', \'color\', \'shape\'}), \'add_nofollow\': False, \'host_whitelist\': (), \'whitelist_tags\': {\'iframe\', \'embed\'}, \'__init__\': <cyfunction Cleaner.__init__ at 0x00000223981C9D38>, \'_tag_link_attrs\': {\'script\': \'src\', \'link\': \'href\', \'applet\': [\'code\', \'object\'], \'iframe\': \'src\', \'embed\': \'src\', \'layer\': \'src\', \'a\': \'href\'}, \'__call__\': <cyfunction Cleaner.__call__ at 0x00000223981C9DF0>, \'allow_follow\': <cyfunction Cleaner.allow_follow at 0x00000223981C9EA8>, \'allow_element\': <cyfunction Cleaner.allow_element at 0x00000223981C9F60>, \'allow_embedded_url\': <cyfunction Cleaner.allow_embedded_url at 0x0000022398285048>, \'kill_conditional_comments\': <cyfunction Cleaner.kill_conditional_comments at 0x0000022398285100>, \'_kill_elements\': <cyfunction Cleaner._kill_elements at 0x00000223982851B8>, \'_remove_javascript_link\': <cyfunction Cleaner._remove_javascript_link at 0x0000022398285270>, \'_substitute_comments\': <built-in method sub of re.Pattern object at 0x00000223968DABE8>, \'_has_sneaky_javascript\': <cyfunction Cleaner._has_sneaky_javascript at 0x0000022398285328>, \'clean_html\': <cyfunction Cleaner.clean_html at 0x00000223982853E0>, \'__dict__\': <attribute \'__dict__\' of \'Cleaner\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'Cleaner\' objects>})'


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


# variables with complex values

basestring = (
    str,
    bytes,
)

_avoid_classes = [
    'nolink',
]

_avoid_elements = [
    'textarea',
    'pre',
    'code',
    'head',
    'select',
    'a',
]

_avoid_hosts = [
    re.compile('^localhost', re.IGNORECASE),
    re.compile('\\bexample\\.(?:com|org|net)$', re.IGNORECASE),
    re.compile('^127\\.0\\.0\\.1$'),
]

_avoid_word_break_classes = [
    'nobreak',
]

_avoid_word_break_elements = [
    'pre',
    'textarea',
    'code',
]

_break_prefer_re = None # (!) real value is "re.compile('[^a-z]', re.IGNORECASE)"

_conditional_comment_re = None # (!) real value is "re.compile('\\\\[if[\\\\s\\\\n\\\\r]+.*?][\\\\s\\\\n\\\\r]*>', re.IGNORECASE|re.DOTALL)"

_css_import_re = None # (!) real value is "re.compile('@\\\\s*import', re.IGNORECASE)"

_css_javascript_re = None # (!) real value is "re.compile('expression\\\\s*\\\\(.*?\\\\)', re.IGNORECASE|re.DOTALL)"

_link_regexes = [
    re.compile('(?P<body>https?://(?P<host>[a-z0-9._-]+)(?:/[/\\-_.,a-z0-9%&?;=~]*)?(?:\\([/\\-_.,a-z0-9%&?;=~]*\\))?)', re.IGNORECASE),
    re.compile('mailto:(?P<body>[a-z0-9._-]+@(?P<host>[a-z0-9_.-]+[a-z]))', re.IGNORECASE),
]

__all__ = [
    'clean_html',
    'clean',
    'Cleaner',
    'autolink',
    'autolink_html',
    'word_break',
    'word_break_html',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000022398240EB8>'

__spec__ = None # (!) real value is "ModuleSpec(name='lxml.html.clean', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000022398240EB8>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\lxml\\\\html\\\\clean.cp37-win_amd64.pyd')"

__test__ = {}

