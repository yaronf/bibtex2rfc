bibtex2rfc
==========

Convert bibtex citations into bibxml references for use in Internet Drafts and RFCs

Bibtex is the most common citation format for academic publications. This tool converts bibtex into the bibxml format which is used by xml2rfc. This enables to reference such publications conveniently in Internet Drafts and RFCs.

The code has been tested with both version 1 and 2 of xml2rfc.

## Prerequisites

Install the python-bibtex package. On Ubuntu:

    apt-get install python-bibtex

**Note**: the code was tested on Ubuntu 13.10, but the python-bibtex package is also available on Fedora.

## Usage
 `bibxml file`

And try one of the *.bibtex files under the `test` directory.

## Limitations

Only the minimum number of fields are translated from bibtex to bibxml. There are two reasons for that:

 * Bibtext citations vary a lot in how they interpret the different fields, and in fact, even in their syntax.
 * Bibxml is extremely limited in what it can express.

## Futures
 * Expose this tool as a Web service (interactive or not).
 * Provide a permanent service/URL to that XML2RFC documents can reference it, instead of using manual conversion. For example, `http://bibxml.org/convert?orig=http://my-dois/11223344/ref.bibtex`
 * Integrate the tool into XML2RFC