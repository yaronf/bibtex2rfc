import _bibtex

# The purpose of this library is to wrap the very mysterious python-bibtex Debian package. I have no API documentation for this package, but I am going to use it anyway. Hiding it inside here.

# Same numerical codes used by _bibtex
_BIBTEX_OTHER = 0
_BIBTEX_AUTHOR = 1
_BIBTEX_TITLE = 2
_BIBTEX_DATE = 3
_BIBTEX_VERBATIM = 4

BIBTEX_MONTHS = {
    "jan": 1,
    "feb": 2,
    "mar": 3,
    "apr": 4,
    "may": 5,
    "jun": 6,
    "jul": 7,
    "aug": 8,
    "sep": 9,
    "oct": 10,
    "nov": 11,
    "dec": 12,
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}

# For testing convenience
EXAMPLE_STRING = """@ARTICLE{2012PhRvD..85d4027A,
   author = {{Anderson}, C. and {Carlip}, S.~J. and {Cooperman}, J.~H. and 
	{Ho{\v r}ava}, P. and {Kommu}, R.~K. and {Zulkowski}, P.~R.},
    title = "{Quantizing Ho{\v r}ava-Lifshitz gravity via causal dynamical triangulations}",
  journal = {\prd},
archivePrefix = "arXiv",
   eprint = {1111.6634},
 primaryClass = "hep-th",
 keywords = {Quantum gravity, Covariant and sum-over-histories quantization, Lattice and discrete methods, Modified theories of gravity},
     year = 2012,
    month = feb,
   volume = 85,
   number = 4,
      eid = {044027},
    pages = {044027},
      doi = {10.1103/PhysRevD.85.044027},
   adsurl = {http://adsabs.harvard.edu/abs/2012PhRvD..85d4027A},
  adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}"""

class BibtexRecord():
    def __init__(self, context, t):
        """Constructs a BibtexRecord using the _bibtex mystery tuple."""
        ## A hack to deal with _bibtex' incomplete handling of the "month" field
        self.date = [0,0] # Month, Year
        ##
        self.handle = t[0]
        self.entry_type = t[1]
        t[2] #Mystery!
        t[3] #Mystery!
        self.typemap = {} #If we know that some fields should be a particular type.
        self.data = {}
        items = t[4]
        for k in items.keys():
            ty = self.typemap.get(k, -1)
            x = _bibtex.expand(context, items[k], ty)
            if k == "month":
                month = BIBTEX_MONTHS[self._strip_braces(_bibtex.get_native(items[k]))]
                self.date[0] = month
                self.data["month"] = month
                continue
            if ty == -1: ty = x[0]
            self.data[k] = self.build(ty, x)
        self.date[1] = self.data["year"]

    def _strip_braces(self, s):
        if s[0] == '{' and s[-1:] == '}':
            return s[1:-1]
        else:
            return s


    def _build_author(self, t):
        names, honorifics, lineage, last = [], [], [], ''
        if t[0]: honorifics = [t[0]] # Prof, doctor, etc.
        if t[3]: lineage = t[3]
        if t[2]: last = t[2]
        if t[1]: names = t[1].split(' ') #XXX
        return [names, last, lineage, honorifics]

    def build(self, ty, x):
        if ty in (_BIBTEX_OTHER, _BIBTEX_VERBATIM):
            return x[2]
        elif ty == _BIBTEX_AUTHOR:
            return map(self._build_author, x[3])
        elif ty == _BIBTEX_TITLE:
            return x[2]
        elif ty == _BIBTEX_DATE:
            return x[3]
        return None

    def get(self, name):
        return self.data.get(name,None)

def _iterate_bibtexsource(bs):
    """Takes one of _bibtex' BibtexSouce objects and returns a list of BibtexRecord objects"""
    out = []
    while True:
        e = _bibtex.next(bs)
        if not e: break
        out.append(e)
    return map(lambda x: BibtexRecord(bs, x), out)

def read_string(string):
    """Takes a string and returns a list containing objects of type BibtexRecord"""
    # Mystery arguments:
    strictness = False
    name = "Name"
    # Read the string:
    return _iterate_bibtexsource(_bibtex.open_string(name, string, strictness))

def read_file(path):
    """Takes a file path and returns a list containing objects of type BibtexRecord"""
    # Mystery arguments:
    strictness = False
    # Read the string:
    return _iterate_bibtexsource(_bibtex.open_file(path, strictness))
