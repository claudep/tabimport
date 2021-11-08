==========
Tab Import
==========

Tab Import is a Python utility to ease imports of tabular data from CSV, ODF,
XLS or XLSX files.

Some formats require an external Python library:

  * ODF: ooolib
  * XLS/XLSX: xlrd

This library is meant to be used inside a Django project context.

Usage::

    #!/usr/bin/env python

    import tabimport
    
    smart_file = tabimport.FileFactory(file_path)
    for data_line in smart_file:
        do_something_with(data_line['header'])

Import helper
=============

To use the Django import helper in your Django project, follow the steps below.

  1. Add 'tabimport' into your INSTALLED_APPS setting.

  2. Include the urls of tabimport into your urls::

        url(r'^data-import/', include('tabimport.urls')),

  3. In any of your models for which you'd like to enable data import, set a
     class variable like this: ``support_tabimport = True``.

  4. You can then link to the tabimport utility from one of your templates by
     reversing a url with ``tabimport``::

        <a href="{% url 'tabimport' %}">Import utility</a>

Alternatively, your models can include a class method which will receive the
imported data as a dictionary just before they are used to create a new
instance. This allows you to handle special cases in imported data::

    @classmethod
    def prepare_import(cls, values):
        return values
