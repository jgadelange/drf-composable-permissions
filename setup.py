import os
from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

try:
    from pypandoc import convert

    def read_md(f):
        return convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")

    def read_md(f):
        return open(f, 'r', encoding='utf-8').read()

setup(
    name='drf-composable-permissions',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='BSD', 
    description='',
    long_description=read_md('README.md'),
    url='https://github.com/jgadelange/drf-composable-permissions',
    author='Jeffrey de Lange',
    author_email='jeffrey@jeffreydelange.nl',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)
