class OrderedDict(object):
    def __init__(self):
        self._keys = []
        self._values = []
        self._length = 0

    def keys(self):
        return self._keys

    def values(self):
        return self._values

    def items(self):
        return [(k,v) for k,v in zip(self._keys, self._values)]
        
    def __setitem__(self, key, value):
        for i in range(len(self)):
            if self._keys[i] == key:
                self._values[i] = value
                return None
        self._keys.append(key)
        self._values.append(value)
        self._length += 1
        
    def __getitem__(self, a_key):
        for key, value in zip(self._keys, self._values):
            if a_key == key:
                return value
        raise KeyError("No value for key {}".format(repr(a_key)))
        
    def __contains__(self, item):
        for key in self._keys:
            if key == item:
                return True
        return False
        
    def __len__(self):
        return self._length
        
    
    def __eq__(self, other):
        if len(self) != len(other):
            return False
            
        # if self.keys() != list(other.keys()):
        #     return False
        for key, value in zip(self._keys, self._values):
            if key not in other or other[key] != value:
                return False
            if self.keys().index(key) != list(other.keys()).index(key):
                return False
            return True
        
    def __ne__(self, other):
        return not self == other
        
    def __str__(self):
        result = '{'
        for key, value in zip(self._keys, self._values):
            result += '{}: {}, '.format(repr(key), repr(value))
        result = result.rstrip(', ')
        result += '}'
        return result
        
    __repr__ = __str__
    
    
    def __add__(self, other):
        new = OrderedDict()
        for key, value in zip(self._keys, self._values):
            new[key] = value
            
        for key, value in zip(other._keys, other._values):
            new[key] = value
            
        return new
    
    @classmethod
    def from_keys(cls, sequence):
        new = OrderedDict()
        for item in sequence:
            new[item] = None
        return new