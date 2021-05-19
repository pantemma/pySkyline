import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.1'
PACKAGE_NAME = 'pySkyline'
AUTHOR = 'pantemma'
AUTHOR_EMAIL = 'emmanouelpans@gmail.com'
URL = 'https://github.com/pantemma/pySkyline'
LICENSE = 'MIT License'
DESCRIPTION = 'Library for computing all pareto fronts/skylines of a dataset'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'numba',
      'numpy'
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      url=URL,
      license=LICENSE,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages(),
      keywords=['python', 'pareto front', 'skyline']
      )
