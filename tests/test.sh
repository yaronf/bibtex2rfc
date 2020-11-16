#!/bin/bash

BIBXML=../bibtex2rfc_pkg/bibxml.py

# mktemp on the Mac is bad
draft=/tmp/$(uuidgen).xml
text=/tmp/$(uuidgen).txt

cp preamble.xml $draft
for b in *.bibtex; do
	echo $BIBXML $b ">>" $draft
	$BIBXML $b >> $draft
done
cat postamble.xml >> $draft

# echo xml2rfc $draft $text
xml2rfc --v3 --no-pagination $draft -o $text

cat $text

rm -f $draft $text
