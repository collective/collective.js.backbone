from setuptools import setup, find_packages
import os

version = '1.3.3'

setup(name='collective.js.underscore',
      version=version,
      description="underscore.js for plone",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",

        ],
      keywords='javascript plone underscore',
      author='Denis Krienbuehl',
      author_email='denis.krienbuehl@gmail.com',
      url='https://github.com/collective/collective.js.underscore',
      license='MIT',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.js'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
