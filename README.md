
# PDF_duplex_scan_reorderer

[![Build Status](https://travis-ci.org/Tomok/PDF_duplex_scan_reorderer.svg?branch=master)](https://travis-ci.org/Tomok/PDF_duplex_scan_reorderer)

A simple python script to reorder pages in a scanned PDF to help with scanners
that do not natively support duplex scanning


It assumes you scanned front pages first and than the back pages in inverse order 
(as you would if you just flipped the stack of paper).
In case of an odd page number, it assumes, the last page does not have a (scanned) back side.

So for example a PDF with 5 pages would be saved in this order: 
Page 1, Page 5, Page 2, Page 4, Page 3.

Based on pyPDF2 - see requirements.txt.
Can be installed via pip, e.g. pip install -r /path/to/requirements.txt
