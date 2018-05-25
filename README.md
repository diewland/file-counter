# file-counter
File based Python Counter Utility

```python
# initial
filename = 'test.tmp'
fc = FileCounter('test_count.dat')

# examples
fc.val       # return counter value
fc.reset()   # reset to zero
fc.set(64)   # set value to 64
fc.up()      # counter +1
fc.down()    # counter -1
fc.remove()  # remove file
