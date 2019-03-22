#A “shelf” is a persistent, dictionary-like object.
import shelve

d = shelve.open("boashelf") # open -- file may get suffix added by low-level
                          # library
data="test data"

d["key1"] = data   # store data at key (overwrites old data if
                # using an existing key)
data = d["key1"]   # retrieve a COPY of data at key (raise KeyError if no
                # such key)
print(data)
#del d["key1"]      # delete data stored at key (raises KeyError
                # if no such key)

flag = "key1" in d   # true if the key exists
print(flag)
klist = d.keys() # a list of all existing keys (slow!)

d["xx"]=[]

# having opened d without writeback=True, you need to code carefully:
temp = d['xx']      # extracts the copy
temp.append(5)      # mutates the copy
d['xx'] = temp      # stores the copy right back, to persist it

d.close()       # close it

