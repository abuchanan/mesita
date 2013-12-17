from distutils.core import setup
import os

_this_dir = os.path.dirname(__file__)
readme_path = os.path.join(_this_dir, 'README.md')
readme = open(readme_path).read()

setup(
    name='mesita',
    description='Simple, stupid utilitiy for working with tabular data',
    long_description=readme,
    version='1.0.1',
    author='Alex Buchanan',
    author_email='buchanae@gmail.com',
    license='MIT',
    py_modules=['mesita'],
)
