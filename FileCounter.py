import os.path

class FileCounter(object):

    def __init__(self, path, start_value=0):
            self.path = path
            if os.path.isfile(path):
                self.val = self._load()
            else:
                self.val = start_value
                self._save(start_value)

    def _load(self):
        fo = open(self.path, 'r')
        v = fo.read()
        fo.close()
        return int(v)

    def _save(self, counter):
        fo = open(self.path, 'w')
        fo.write(str(counter))
        fo.close()
        return counter

    def set(self, v):
        self.val = v
        return self._save(v)

    def reset(self):
        self.val = 0
        return self._save(0)

    def up(self):
        self.val += 1
        return self._save(self.val)

    def down(self):
        self.val -= 1
        return self._save(self.val)

    def remove(self):
        if os.path.isfile(self.path):
            os.unlink(self.path)
            return True
        return False

if __name__ == '__main__':

    filename = 'test.tmp'
    fc = FileCounter('test_count.dat')

    # reset
    fc.reset()
    assert fc.val == 0
    print('Testing reset(): passed')

    # set 1
    fc.set(64)
    assert fc.val == 64
    print('Testing set() #1: passed')

    # up
    for i in range(0, 387):
        fc.up()
    assert fc.val == 451
    print('Testing up(): passed')

    # set 2
    fc.set(999)
    assert fc.val == 999
    print('Testing set() #2: passed')

    # down
    for i in range(0, 998):
        fc.down()
    assert fc.val == 1
    print('Testing down(): passed')

    # remove
    flag = fc.remove()
    assert flag and not os.path.isfile(filename)
    print('Testing remove(): passed')
