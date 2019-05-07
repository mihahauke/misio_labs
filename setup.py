# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='misio',
    version='0.1.0',
    description="Package for MISiO course at PUT",
    long_description="Package for MISiO course at PUT",
    author='Michał Kempka',
    author_email='mkempka@cs.put.poznan.pl',
    packages=find_packages(),
    install_requires=['numpy', 'aima3','scikit-learn','scipy'],
    # package_data={'misio': []},
    classifiers=[
        # Development Status :: 1 - Planning
        'Development Status :: 2 - Pre-Alpha',
        # Development Status :: 3 - Alpha
        # Development Status :: 4 - Beta
        # Development Status :: 5 - Production/Stable
        # Development Status :: 6 - Mature
        # Development Status :: 7 - Inactive
        # 'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords=['AI', 'Teaching']

)
