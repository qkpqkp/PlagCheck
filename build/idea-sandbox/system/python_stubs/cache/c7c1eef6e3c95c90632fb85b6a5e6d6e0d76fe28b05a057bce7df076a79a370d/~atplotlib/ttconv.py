# encoding: utf-8
# module ~atplotlib.ttconv
# from C:\Users\Doly\Anaconda3\lib\site-packages\~atplotlib\ttconv.cp37-win_amd64.pyd
# by generator 1.147
""" Module to handle converting and subsetting TrueType fonts to Postscript Type 3, Postscript Type 42 and Pdf Type 3 fonts. """
# no imports

# functions

def convert_ttf_to_ps(filename, output, fonttype, glyph_ids): # real signature unknown; restored from __doc__
    """
    convert_ttf_to_ps(filename, output, fonttype, glyph_ids)
    
    Converts the Truetype font into a Type 3 or Type 42 Postscript font, optionally subsetting the font to only the desired set of characters.
    
    filename is the path to a TTF font file.
    output is a Python file-like object with a write method that the Postscript font data will be written to.
    fonttype may be either 3 or 42.  Type 3 is a "raw Postscript" font. Type 42 is an embedded Truetype font.  Glyph subsetting is not supported for Type 42 fonts.
    glyph_ids (optional) is a list of glyph ids (integers) to keep when subsetting to a Type 3 font.  If glyph_ids is not provided or is None, then all glyphs will be included.  If any of the glyphs specified are composite glyphs, then the component glyphs will also be included.
    """
    pass

def get_pdf_charprocs(filename, glyph_ids): # real signature unknown; restored from __doc__
    """
    get_pdf_charprocs(filename, glyph_ids)
    
    Given a Truetype font file, returns a dictionary containing the PDF Type 3
    representation of its paths.  Useful for subsetting a Truetype font inside
    of a PDF file.
    
    filename is the path to a TTF font file.
    glyph_ids is a list of the numeric glyph ids to include.
    The return value is a dictionary where the keys are glyph names and
    the values are the stream content needed to render that glyph.  This
    is useful to generate the CharProcs dictionary in a PDF Type 3 font.
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001E498FBF400>'

__spec__ = None # (!) real value is "ModuleSpec(name='~atplotlib.ttconv', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001E498FBF400>, origin='C:\\\\Users\\\\Doly\\\\Anaconda3\\\\lib\\\\site-packages\\\\~atplotlib\\\\ttconv.cp37-win_amd64.pyd')"

