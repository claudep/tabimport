==========
Tab Import
==========

Tab Import is a Python utility to ease imports of tabular data from CSV, ODF,
XLS or XLSX files.

Some formats require an external Python library:

  * ODF: ooolib
  * XLS: xlrd
  * XLSX: openpyxl

This library is meant to be used inside a Django project context.

Usage::

    #!/usr/bin/env python

    import tabimport
    
    smart_file = tabimport.FileFactory(file_path)
    for data_line in smart_file:
        do_something_with(data_line['header'])
