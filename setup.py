from codecs import open
from os import path

from setuptools import find_packages, setup

import make_poffins

HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='make_poffins',
    version='0.1.2',
    description='Making Poffins',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GlassToeStudio/MakePoffins/",
    author='Glass Toe Studio',
    author_email="GlassToeStudio@gmail.com",
    license='MIT',
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    packages=find_packages(include=['make_poffins', 'make_poffins.*'], exclude=['tests']),
    include_package_data=True,
    package_data={
        "": ["./results/*"]
    },
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)
