#! /usr/bin/env python
# encoding: utf-8

from pdfrw import PdfReader, IndirectPdfDict, BookmarkedPdfWriter
from datetime import datetime


output = BookmarkedPdfWriter()

for i in xrange(3):
    totalPages = len(output.pagearray)
    output.addpages(PdfReader(
        'static_pdfs/global/0ae80b493bc21e6de99f2ff6bbb8bc2c.pdf').pages)

    bmname = 'Bm (%s) - %s' % (i+1, 'Root')

    t1 = output.addBookmark(bmname, totalPages)
    t2 = output.addBookmark("Child 1", totalPages+1, t1)
    output.addBookmark("Child 1.1", totalPages+2, t2)


now = datetime.utcnow()
date = 'D:%04d%02d%02d%02d%02d%02d' % (
    now.year, now.month, now.day, now.hour, now.minute, now.second)

info = output.trailer.Info = IndirectPdfDict()
info.Title = 'Test PDF with Bookmarks'
info.Author = 'asdasd'
info.Creator = 'random dude'
info.Producer = 'another random dude'
info.CreationDate = date

output.write('result.pdf')
