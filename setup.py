# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


dependencies = [dependency.strip()
                for dependency in open("requirements.txt").readlines()]

setup(
    name='gerencianet',

    version='0.0.1',

    description='Module for integration with Gerencianet API',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/gerencianet/gn-api-sdk-python',

    # Author details
    author='Cecília Deveza, Danniel Hugo, Francisco Thiene, Talita Campos, Thomaz Feitoza',
    author_email='suportetecnico@gerencianet.com.br',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development',

        # Pick your license as you wish (should match "license" above)
        'License :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],

    # What does your project relate to?
    keywords='payment Gerencianet',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'test': ['pytest-cov', 'pytest', 'responses'],
    },

    include_package_data=True,

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'config' package, too:
        'config': ['*.json'],
    },

    install_requires=dependencies,


)
