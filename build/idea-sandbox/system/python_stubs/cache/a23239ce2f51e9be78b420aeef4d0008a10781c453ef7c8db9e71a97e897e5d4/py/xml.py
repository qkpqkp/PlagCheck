# encoding: utf-8
# module py.xml
# from C:\Users\Doly\Anaconda3\lib\site-packages\sklearn\neighbors\quad_tree.cp37-win_amd64.pyd
# by generator 1.147
"""
module for generating and serializing xml and html structures
by using simple python objects.

(c) holger krekel, holger at merlinux eu. 2009
"""

# imports
import py._xmlgen as __py__xmlgen


# Variables with simple values

_ApiModule__doc = '\nmodule for generating and serializing xml and html structures\nby using simple python objects.\n\n(c) holger krekel, holger at merlinux eu. 2009\n'

__implprefix__ = 'py'

# functions

def escape(*args, **kwargs): # real signature unknown
    pass

# classes

class Namespace(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__tagspec__': None, '__tagclass__': <class 'py._xmlgen.Tag'>, '__stickyname__': False, '__module__': 'py._xmlgen', '__dict__': <attribute '__dict__' of 'Namespace' objects>, '__weakref__': <attribute '__weakref__' of 'Namespace' objects>, '__doc__': None})"
    __stickyname__ = False
    __tagclass__ = None # (!) forward: Tag, real value is "<class 'py._xmlgen.Tag'>"
    __tagspec__ = None


class html(__py__xmlgen.Namespace):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    Style = None # (!) real value is "<class 'py._xmlgen.html.Style'>"
    __stickyname__ = True
    __tagclass__ = None # (!) real value is "<class 'py._xmlgen.HtmlTag'>"
    __tagspec__ = {
        'a': 1,
        'abbr': 1,
        'acronym': 1,
        'address': 1,
        'applet': 1,
        'area': 1,
        'article': 1,
        'aside': 1,
        'audio': 1,
        'b': 1,
        'base': 1,
        'basefont': 1,
        'bdi': 1,
        'bdo': 1,
        'big': 1,
        'blink': 1,
        'blockquote': 1,
        'body': 1,
        'br': 1,
        'button': 1,
        'canvas': 1,
        'caption': 1,
        'center': 1,
        'cite': 1,
        'code': 1,
        'col': 1,
        'colgroup': 1,
        'command': 1,
        'comment': 1,
        'datalist': 1,
        'dd': 1,
        'del': 1,
        'details': 1,
        'dfn': 1,
        'dir': 1,
        'div': 1,
        'dl': 1,
        'dt': 1,
        'em': 1,
        'embed': 1,
        'fieldset': 1,
        'figcaption': 1,
        'figure': 1,
        'font': 1,
        'footer': 1,
        'form': 1,
        'frame': 1,
        'frameset': 1,
        'h1': 1,
        'h2': 1,
        'h3': 1,
        'h4': 1,
        'h5': 1,
        'h6': 1,
        'head': 1,
        'header': 1,
        'hgroup': 1,
        'hr': 1,
        'html': 1,
        'i': 1,
        'iframe': 1,
        'img': 1,
        'input': 1,
        'ins': 1,
        'isindex': 1,
        'kbd': 1,
        'keygen': 1,
        'label': 1,
        'legend': 1,
        'li': 1,
        'link': 1,
        'listing': 1,
        'map': 1,
        'mark': 1,
        'marquee': 1,
        'menu': 1,
        'meta': 1,
        'meter': 1,
        'multicol': 1,
        'nav': 1,
        'nobr': 1,
        'noembed': 1,
        'noframes': 1,
        'noscript': 1,
        'object': 1,
        'ol': 1,
        'optgroup': 1,
        'option': 1,
        'output': 1,
        'p': 1,
        'param': 1,
        'pre': 1,
        'progress': 1,
        'q': 1,
        'rp': 1,
        'rt': 1,
        'ruby': 1,
        's': 1,
        'samp': 1,
        'script': 1,
        'section': 1,
        'select': 1,
        'small': 1,
        'source': 1,
        'span': 1,
        'strike': 1,
        'strong': 1,
        'style': 1,
        'sub': 1,
        'summary': 1,
        'sup': 1,
        'table': 1,
        'tbody': 1,
        'td': 1,
        'textarea': 1,
        'tfoot': 1,
        'th': 1,
        'thead': 1,
        'time': 1,
        'title': 1,
        'tr': 1,
        'track': 1,
        'tt': 1,
        'u': 1,
        'ul': 1,
        'var': 1,
        'video': 1,
        'wbr': 1,
        'xmp': 1,
    }


class raw(object):
    """
    just a box that can contain a unicode string that will be
        included directly in the output
    """
    def __init__(self, uniobj): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'py._xmlgen', '__doc__': 'just a box that can contain a unicode string that will be\\n    included directly in the output', '__init__': <function raw.__init__ at 0x00000146BE2D4F28>, '__dict__': <attribute '__dict__' of 'raw' objects>, '__weakref__': <attribute '__weakref__' of 'raw' objects>})"


class Tag(list):
    # no doc
    def unicode(self, indent=2): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, *args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    def __str__(self): # reliably restored by inspect
        # no doc
        pass

    def __unicode__(self): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Attr = None # (!) real value is "<class 'py._xmlgen.Tag.Attr'>"
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'py._xmlgen', 'Attr': <class 'py._xmlgen.Tag.Attr'>, '__init__': <function Tag.__init__ at 0x00000146BE2D4AE8>, '__unicode__': <function Tag.__unicode__ at 0x00000146BE2D4D08>, '__str__': <function Tag.__unicode__ at 0x00000146BE2D4D08>, 'unicode': <function Tag.unicode at 0x00000146BE2D4D90>, '__repr__': <function Tag.__repr__ at 0x00000146BE2D4E18>, '__dict__': <attribute '__dict__' of 'Tag' objects>, '__weakref__': <attribute '__weakref__' of 'Tag' objects>, '__doc__': None})"


# variables with complex values

__all__ = [
    '__doc__',
    'html',
    'Tag',
    'raw',
    'Namespace',
    'escape',
]

__map__ = {}

