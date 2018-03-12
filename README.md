# Class 11: Advanced OOP

Your job is to implement the current `OrderedDict`. The recommended way to create it is to keep two synched lists. One containing the keys and the other the values. Example:

```python
d = {
  'a': 1,
  'b': 2,
  'c': 3
}

keys = ['a', 'b', 'c']
values = [1, 2, 3]
```

The best way to iterate over these two collections is with the `[zip](https://docs.python.org/3/library/functions.html#zip)` function:


```python
keys = ['a', 'b', 'c']
values = [1, 2, 3]

for k, v in zip(keys, values):
  print('{} => {}'.format(k, v))
```

Output:

```
a => 1
b => 2
c => 3
```

### Install

```bash
$ pip install -r requirements.txt
```

### Usage

There's a script `main.py` created for debugging. Feel free to change it and experiment with it.

### Tests

Tests in `tests.py` are written in order. You can use the `-k` flag to select them:

```bash
$ py.test tests.py -k test_set_new_items
```

### Homework

Look for those tests marked with `pytest.mark.skip`.
