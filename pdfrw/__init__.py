# A part of pdfrw (https://github.com/pmaupin/pdfrw)
# Copyright (C) 2006-2015 Patrick Maupin, Austin, Texas
# MIT license -- See LICENSE.txt for details

from .pdfwriter import PdfWriter
from .pdfreader import PdfReader
from .bookmarkedpdfwriter import BookmarkedPdfWriter
from .objects import (PdfObject, PdfName, PdfArray,
                      PdfDict, IndirectPdfDict, PdfString, PdfBool)
from .tokens import PdfTokens
from .errors import PdfParseError
from .pagemerge import PageMerge

__version__ = '0.4'

# Add a tiny bit of compatibility to pyPdf

PdfFileReader = PdfReader
PdfFileWriter = PdfWriter

__all__ = """PdfWriter PdfReader PdfObject PdfName PdfArray
             PdfTokens PdfParseError PdfDict IndirectPdfDict
             PdfString PdfBool PageMerge BookmarkedPdfWriter""".split()

