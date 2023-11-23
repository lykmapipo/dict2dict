# dict2dict

Opinionated dictionary utilities for Python.

## Requirements

- [Python 3.8+](https://www.python.org/)
- [pip 23.3+](https://github.com/pypa/pip)

## Installation

```sh
pip install -U dict2dict
```

## Usage

- Merge multiple dictionaries into one dictionary
```python
from dict2dict import dicts_to_dict

a = {"a": 1, "b": None, "c": None, }
b = {"b": 2, "c": None, }
c = dicts_to_dict(a, b)

c == {"a": 1, "b": 2, "c": None, }
# True
```

- Normalize and remove ``Falsey`` items from a dictionary
```python
from dict2dict import dict_to_dict
a = { "a": 1, "b": None, "c": [], }
b = dict_to_dict(a)

b == { "a": 1, }
#True
```

- Normalize ``Falsey`` items from a dictionary to ``None``
```python
from dict2dict import falsey_to_none

a = { "a": 1, "b": [], }
b = falsey_to_none(a)

b == { "a": 1, "b": None, }
# True
```

- Remove ``Falsey`` items from a dictionary
```python
from dict2dict import omit_falsey

a = { "a": 1, "b": None, }
b = omit_falsey(a)

b == { "a": 1, }
# True
```

## Test

- Clone this repository

- Install all dependencies

```sh
pip install -e .[dev]
```

- Then run test

```sh
pytest
```

## Contribute

It will be nice, if you open an issue first so that we can know what is going on, then, fork this repo and push in your ideas. Do not forget to add a bit of test(s) of what value you adding.

## Licence

The MIT License (MIT)

Copyright (c) lykmapipo & Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
