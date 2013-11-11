#!/bin/bash

BIBXML=../bibxml.py

draft=$(mktemp --suffix .xml)
text=$(mktemp --suffix .txt)

cp preamble.xml $draft
for b in *.bibtex; do
	$BIBXML $b >> $draft
done
cat postamble.xml >> $draft

xml2rfc $draft $text

# rm -f $draft $text
echo $draft
