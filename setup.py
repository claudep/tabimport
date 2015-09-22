from distutils.core import setup

setup(
    name='TabImport',
    version='0.3.0',
    author='Claude Paroz',
    author_email='claude@2xlibre.net',
    packages=['tabimport'],
    url='https://github.com/claudep/tabimport/',
    license='LICENSE.txt',
    description='Utility to ease reading data from tabular data files',
    long_description=open('README.txt').read(),
    install_requires=[
        "Django >= 1.7",
        "django-formtools",
    ],
)
