# -*- coding: utf-8 -*-
"""
This module contains the osha.whoswho package
"""
import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '1.2.3dev'

long_description = (
    read('README.txt')
    + '\n' +
    'Change history\n'
    '**************\n'
    + '\n' +
    read('CHANGES.txt')
    + '\n' +
    'Detailed Documentation\n'
    '**********************\n'
    + '\n' +
    read('src', 'osha', 'whoswho', 'README.txt')
    + '\n' +
    'Contributors\n'
    '************\n'
    + '\n' +
    read('CONTRIBUTORS.txt')
    + '\n' 
    )
    
tests_require=[
    'Products.PloneTestCase',
    'zope.testing',
    'PIL',
    ]

setup(name='osha.whoswho',
      version=version,
      description="",
      long_description=long_description,
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "License :: OSI Approved :: European Union Public Licence 1.1 (EUPL 1.1)",
        ],
      keywords='osha contenttype whoswho belgium',
      author='Syslab.com GmbH',
      author_email='info@syslab.com',
      url='https://svn.syslab.com/svn/OSHA/osha.whoswho/',
      license='GPL + EUPL',
      packages=['osha', 'osha.whoswho'], 
      package_dir={'':'src'},
      namespace_packages=['osha'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
        'kss.core',
        'plone.app.layout',
        'plone.memoize',
        'Products.Archetypes',
        'Products.ATContentTypes',
        'Products.CMFCore',
        'zope.app.container',
        'zope.component',
        'zope.i18nmessageid',
        'zope.schema',
        'zope.interface',
        'Acquisition',  
        'Products.ATVocabularyManager',
        'Products.VocabularyPickerWidget',
        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite = 'osha.whoswho.tests.test_docs.test_suite',
      entry_points="""
      # -*- entry_points -*- 
      """,
      )      
      
