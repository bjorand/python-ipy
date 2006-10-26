# $Id: setup.py 671 2004-08-22 21:02:29Z md $
try:
    from setuptools.core import setup
except ImportError:
    from distutils.core import setup

import IPy

LONG_DESCRIPTION=open('README').read()
CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Environment :: Plugins',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Communications',
    'Topic :: Internet',
    'Topic :: System :: Networking',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Natural Language :: English',
    'Programming Language :: Python']
URL = "https://software.inl.fr/trac/trac.cgi/wiki/IPy"

setup(name="IPy",
      version=IPy.__version__,
      description="IPv4 and IPv6 parsing and handling class",
      long_description=LONG_DESCRIPTION,
      author="drt",
      maintainer="Victor Stinner",
      maintainer_email="victor.stinner AT inl.fr",
      license="BSD License",
      keywords="ipv4 ipv6 netmask",
      url=URL,
      download_url=URL,
      classifiers= CLASSIFIERS,
      py_modules=["IPy"])

