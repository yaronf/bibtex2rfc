bibtex2rfc
==========

Convert BibTeX citations into bibxml references for use in Internet Drafts and RFCs

BibTeX is the most common citation format for academic publications. This tool converts BibTeX into the
bibxml format which is used by [xml2rfc](http://xml.resource.org/).
This enables to reference such publications conveniently in Internet Drafts and RFCs.

Version 2 of this tool has been modernized to Python3 and xml2rfc v3.

## Installation

    pip3 install bibtex2rfc

## Usage

    bibtex2rfc file

Where `file` contains one or more BibTeX entries. If `file` is omitted, reads from standard input. You can try one of the `*.bibtex` files under the `tests` directory on GitHub.

**Note**: the code was tested on MacOS.

## Limitations

Only the minimum number of fields are translated from BibTeX to bibxml. There are two reasons for that:

 * BibTeX citations vary a lot in how they interpret the different fields, and in fact, even in their syntax.
 * Bibxml is extremely limited in what it can express.
