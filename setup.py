from setuptools import setup, find_packages
import os

version = '0.9.2'

setup(name='collective.js.backbone',
      version=version,
      description="backbone.js for plone",
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
      keywords='javascript plone backbone',
      author='Patrick Gerken',
      author_email='do3ccqrv@googlemail.com',
      url='https://github.com/collective/collective.js.backbone',
      license='MIT',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.js'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.js.underscore',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
