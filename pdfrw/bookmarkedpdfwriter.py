from pdfrw.pdfwriter import PdfWriter, IndirectPdfDict, PdfName, \
    PdfOutputError, PdfDict, user_fmt


class BookmarkedPdfWriter(PdfWriter):

    _outline = None

    def addBookmark(self, title, pageNum, parent=None):
        '''
        Adds a new bookmark entry.
        pageNum must be a valid page number in the writer
        and parent can be a bookmark object returned by
        a previous addBookmark call
        '''

        try:
            page = self.pagearray[pageNum]
        except IndexError:
            raise PdfOutputError("Invalid page number: %i" % (pageNum, ))

        parent = parent or self._outline
        if parent is None:
            parent = self._outline = IndirectPdfDict()

        bookmark = IndirectPdfDict(
            Parent=parent,
            Title=title,
            A=PdfDict(
                D=[page, PdfName.Fit],
                S=PdfName.GoTo
            )
        )

        if parent.Count:
            parent.Count += 1
            prev = parent.Last
            bookmark.Prev = prev
            prev.Next = bookmark
            parent.Last = bookmark
        else:
            parent.Count = 1
            parent.First = bookmark
            parent.Last = bookmark

        while True:
            parent = parent.Parent
            if parent is None:
                break
            parent.Count += 1

        return bookmark

    def write(self, fname, trailer=None, user_fmt=user_fmt,
              disable_gc=True):
        trailer = trailer or self.trailer
        trailer.Root.Outlines = self._outline
        super(BookmarkedPdfWriter, self).write(
            fname, trailer, user_fmt, disable_gc)
