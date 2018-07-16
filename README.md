# Dismantler
[![PyPI version](https://img.shields.io/pypi/v/dismantler-python.svg)](https://badge.fury.io/py/dismantler-python)
[![Apache 2.0 License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)]()
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dismantler-python.svg)
[![Say Thanks](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/harrydrippin)

```
██████╗ ██╗███████╗███╗   ███╗ █████╗ ███╗   ██╗████████╗██╗     ███████╗██████╗ 
██╔══██╗██║██╔════╝████╗ ████║██╔══██╗████╗  ██║╚══██╔══╝██║     ██╔════╝██╔══██╗
██║  ██║██║███████╗██╔████╔██║███████║██╔██╗ ██║   ██║   ██║     █████╗  ██████╔╝
██║  ██║██║╚════██║██║╚██╔╝██║██╔══██║██║╚██╗██║   ██║   ██║     ██╔══╝  ██╔══██╗
██████╔╝██║███████║██║ ╚═╝ ██║██║  ██║██║ ╚████║   ██║   ███████╗███████╗██║  ██║
╚═════╝ ╚═╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚══════╝╚═╝  ╚═╝
```
This module dismantles python code to parse tree, token, symbols and reproduces it to dictionary and string.

## What is this?

Dismantler takes a Python code as input and creates a parse tree in a short time. It also export the parse tree to a dictionary or json. You can get list of tokens or symbols separately if you want. This project can be used for research purpose, such as teaching the source code to deep learning model as tokenized sequential data or interpreting the Python code on token level and using it for educational programs (like tutoring).

## Basic Usage

```python
>>> import dismantler

>>> d = dismantler.run_from_string('a + 5').dictionary()
>>> print(d)
{
    "type": "symbol",
    "name": "stmt",
    "value": [
        // Nodes...
    ]
}

>>> d = dismantler.run_from_file('file.py').json(indent=4)
>>> print(d)
"{
    "type": "symbol",
    "name": "stmt",
    "value": [
        // Nodes...
    ]
}"
```

## Installation

### Via pip
```bash
pip3 install dismantler-python
```

### Via source
```bash
git clone http://github.com/harrydrippin/dismantler-python
cd dismantler-python
python3 setup.py install
```

## Contribution

This project is very small now, so contribution to this project is very welcome. Feel free to submit some issues or PRs to this project.