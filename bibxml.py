#!/usr/bin/env python

# bibxml: minimal conversion of bibtex citations into bibxml references
# (c) Yaron Sheffer, 2013

from __future__ import print_function
import bibtex
import sys, re
import xml.etree.ElementTree as ET

    
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December']

def _month_name(num):
    return MONTHS[num - 1]


def _clean_anchor(a):
    if a[0].isdigit():
        a = 'ref' + a
    return a.replace('/', ':')

 
def _make_initials(names):
    return " ".join([(n[0] + '.') for n in names])


def record_to_bibxml(rec):
    anchor = _clean_anchor(rec.handle)
    root_attrib = {'anchor': anchor}
    if 'url' in rec.data:
        root_attrib['target'] = rec.data['url']
    root = ET.Element('reference', attrib = root_attrib)
    front = ET.SubElement(root, 'front')
    title = ET.SubElement(front, 'title')
    title.text = rec.data['title']
    if not 'author' in rec.data:
        print("Error: the 'author' field is mandatory", file=sys.stderr)
        return ''
    authors = rec.data['author']
    for a in authors:
        surname = a[1]
        author_attribs = {}
        author_attribs['surname'] = surname
        fullname = ' '.join(a[0]) + ' ' + surname if len(a[0]) > 0 else surname
        author_attribs['fullname'] = fullname
        initials = _make_initials(a[0])
        author_attribs['initials'] = initials
        a = ET.SubElement(front, 'author', attrib = author_attribs)
    month = _month_name(rec.data['month']) if 'month' in rec.data else None
    year = str(rec.data['year'])
    date_attrib = {'year': year}
    if month:
        date_attrib['month'] = month
    date = ET.SubElement(front, 'date', attrib = date_attrib)
    if 'keywords' in rec.data:
        keywords = re.split(',|;', rec.data['keywords'])
        for k in keywords:
            kw = ET.SubElement(front, 'keyword')
            kw.text = k

    return ET.tostring(root)

    
if __name__ == '__main__':
    bibs = bibtex.read_file(sys.argv[1])
    # bibs = bibtex.read_string(bibtex.EXAMPLE_STRING)
    # print(bibs[0].handle + ": " + repr(bibs[0].data))
    for bib in bibs:
        print(record_to_bibxml(bib))
