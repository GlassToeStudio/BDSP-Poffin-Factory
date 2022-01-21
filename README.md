
# How to make a python package/library

https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f

##### *more comprehensive with docs, uplaod, etc.*
https://towardsdatascience.com/deep-dive-create-and-publish-your-first-python-library-f7f618719e14

## Folder structure
```
library_name/
        /setup.py
        /.gitignore
        /readme.md
        /requirements.txt
        /library_name/
                /__init__.py
                /module.py
        /tests/
                /__init__.py
                test_module.py
```


## For virtual environment:

> python3 -m venv venv

> source venv/bin/activate

## Required packages

> pip install wheel

> pip install setuptools

> pip install twine

> pip install pytest

> pip install pytest-runner

#### or requirements.txt
```text
wheel
setuptools
twine
pytest
pytest-runner
```

```powershell
pip install -r requirements.txt
```


## setup.py

```python
from setuptools import find_packages, setup
setup(
    name='mypythonlib',
    packages=find_packages(include=['mypythonlib']),
    version='0.1.0',
    description='My first Python library',
    author='Me',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)
```

## Run

#### Test

> python setup.py pytest

#### Build

> python setup.py bdist_wheel

#### Install
> pip install /path/to/wheelfile.whl

 ######  *wheel file is stored in the “dist” folder that is now created*

### Usage

```python
import mypythonlib
from mypythonlib import myfunctions
```
