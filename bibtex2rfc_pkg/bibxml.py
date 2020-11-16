#!/usr/bin/env python3

# bibxml: minimal conversion of bibtex citations into bibxml references
# (c) Yaron Sheffer, 2013, 2020

import bibtexparser as btp
import sys, re
import xml.etree.ElementTree as ET

def _clean_anchor(a):
    if a[0].isdigit():
        a = 'ref' + a
    return a.replace('/', ':')

def record_to_bibxml(rec):
    rec = btp.customization.doi(rec) # clean up doi/link
    rec = btp.customization.author(rec) # clean up author field
    rec = btp.customization.keyword(rec) # split keywords into list

    # Work around a crash in this customization
    try:
        rec = btp.customization.add_plaintext_fields(rec) # Add fields cleaned of braces
    except:
        rec['plain_title'] = rec['title']

    anchor = _clean_anchor(rec['ID'])
    root_attrib = {'anchor': anchor}
    if 'url' in rec:
        root_attrib['target'] = rec['url']
    elif 'link' in rec:
        root_attrib['target'] = rec['link'][0]['url'] # strange DOI customization
    root = ET.Element('reference', attrib = root_attrib)
    front = ET.SubElement(root, 'front')
    title = ET.SubElement(front, 'title')
    title.text = rec['plain_title']
    if not 'author' in rec:
        print("Error: the 'author' field is mandatory", file=sys.stderr)
        return b''
    authors = rec['author']
    for a in authors:
        # print("a: "+repr(a))
        names = a.split(', ')
        surname = names[0]
        author_attribs = {}
        author_attribs['surname'] = surname
        fullname = names[1] + ' ' + surname if len(names) > 0 else surname
        author_attribs['fullname'] = fullname
        a = ET.SubElement(front, 'author', attrib = author_attribs)
    if not 'year' in rec:
        print("Error: the 'year' field is mandatory", file=sys.stderr)
        return b''
    year = rec['year']
    date_attrib = {'year': year}
    if 'month' in rec:
        if isinstance(rec['month'], str):
            date_attrib['month'] = rec['month']
        else:
            date_attrib['month'] = rec['month'].get_value() # because these are often unquoted strings
    date = ET.SubElement(front, 'date', attrib = date_attrib)
    if 'keyword' in rec:
        for k in rec['keyword']:
            kw = ET.SubElement(front, 'keyword')
            kw.text = k

    return ET.tostring(root)

def main():
    if len(sys.argv) == 2 and sys.argv[1] == '--help':
        print('Usage: ' + sys.argv[0] + ' [infile]', file=sys.stderr)
        sys.exit(1)

    if len(sys.argv) == 1:
        fname = '/dev/stdin'
    else:
        fname = sys.argv[1]

    # Configure parser, need "common_strings" for unquoted month names
    # Do not interpolate strings, to avoid choking on undefined strings, but then need to hack
    # around month names
    parser = btp.bparser.BibTexParser(common_strings = True, homogenize_fields = True, interpolate_strings = False)

    with open(fname) as bibtex_file:
        bibs = btp.load(bibtex_file, parser)
    if len(bibs.entries) == 0:
        print("Warning: no entries found", file=sys.stderr)

    for bib in bibs.entries:
        # print("bib: " + repr(bib))
        print(record_to_bibxml(bib).decode("utf-8"))

if __name__ == "__main__":
    main()

