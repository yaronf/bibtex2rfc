bibtex2rfc
==========

Convert bibtex citations into bibxml references for use in Internet Drafts and RFCs

Bibtex is the most common citation format for academic publications. This tool converts bibtex into the
bibxml format which is used by [xml2rfc](http://xml.resource.org/).
This enables to reference such publications conveniently in Internet Drafts and RFCs.

The code has been tested with both version 1 and 2 of xml2rfc.

> :warning: **Obsolete**: the `python-bibtex` dependency is no longer available on Ubuntu 20.10 and is itself stuck on Python 2.7.
The code needs to be rewritten, possibly with [BibTexParser](https://github.com/sciunto-org/python-bibtexparser).

## Prerequisites

Install the python-bibtex package. On Ubuntu:

    apt-get install python-bibtex

**Note**: the code was tested on Ubuntu 13.10, but the python-bibtex package is also available on Fedora.

## Usage
 `bibxml file`

And try one of the *.bibtex files under the `test` directory.

## Limitations

Only the minimum number of fields are translated from bibtex to bibxml. There are two reasons for that:

 * Bibtex citations vary a lot in how they interpret the different fields, and in fact, even in their syntax.
 * Bibxml is extremely limited in what it can express.

## Futures
 * Expose this tool as a Web service (interactive or not).
 * Provide a permanent service/URL so that xml2rfc documents can reference it, instead of using manual conversion. For example, `http://bibxml.org/convert?orig=http%3A%2F%2Fmy-dois%2F11223344%2Fref.bibtex`
 * Integrate the tool into xml2rfc
