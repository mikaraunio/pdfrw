class PdfBool(object):
    ''' A PdfBool is either 'true' or 'false'.
    '''

    def __init__(self, value):
        self._value = bool(value)

    def __str__(self):
        return str(self._value).lower()
