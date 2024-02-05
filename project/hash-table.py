class HashTable:
    DEFAULT_CAPACITY = 4

    def __init__(self):
        self.capacity = HashTable.DEFAULT_CAPACITY
        self.__keys = [None] * self.capacity
        self.__values = [None] * self.capacity

    def __setitem__(self, key, value):

        # same key -> should not be duplicated
        if key in self.__values:
            idx = self.__keys.index(value)
            self.__values[idx] = value
            return

        # overflow
        if self.capacity == self.__size():
            self.__resize()

        # collision
        idx = self.__calc_idx(key)
        idx = self.__get_idx(idx)
        self.__keys[idx] = key
        self.__values[idx] = value

    def __calc_idx(self, key):
        idx = sum([ord(ch) for ch in key]) % self.capacity
        return idx

    def __get_idx(self, idx):
        if idx == self.capacity:
            idx = 0
        if self.__keys[idx] is None:
            return idx
        return self.__get_idx(idx + 1)

    def __size(self):
        return len([el for el in self.__keys if el is not None])

    def __resize(self):
        self.__keys = self.__keys + [None] * self.capacity
        self.__values = self.__values + [None] * self.capacity
        self.capacity *= 2

    def __str__(self):
        result = []
        for i in range(len(self.__keys)):
            if self.__keys[i] is not None:
                result.append(f'"{self.__keys[i]}": {self.__values[i]}')
        return '{' + ', '.join(result) + '}'

    def get(self, key, default=None):
        if key in self.__keys:
            return self.__values[self.__keys.index(key)]
        return default

    def __getitem__(self, key):
        if key in self.__keys:
            return self.__values[self.__keys.index(key)]
        raise KeyError('Key not found')

    def __len__(self):
        return len([el for el in self.__keys if el is not None])

    def add(self, key: str, value: any):
        self[key] = value
