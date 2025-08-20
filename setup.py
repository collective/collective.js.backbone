from setuptools import setup, find_packages
import os

version = '1.6.1.dev0'

setup(name='collective.js.backbone',
      version=version,
      description="backbone.js for plone",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 6.0",
        "Framework :: Plone :: 6.1",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='javascript plone backbone',
      author='Patrick Gerken',
      author_email='gerken@patrick-gerken.de',
      url='https://github.com/collective/collective.js.backbone',
      license='MIT',
      packages=find_packages('src', exclude=['ez_setup']),
      namespace_packages=['collective'],
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.js.underscore',
      ],
      extras_require={
          "test": [
              "plone.app.testing",
          ],
      },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
