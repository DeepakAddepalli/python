#pickling
import pickle,pprint
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': (r'str\n\n\t\b\v\cing', u'Unicode string'),
         'c': None}
selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)
output = open('data.pkl', 'wb')

pickle.dump(data1, output)			# Pickle dictionary

pickle.dump(selfref_list, output)	# Pickle the list
output.close()


pkl_file = open('data.pkl', 'rb')
data1 = pickle.load(pkl_file)
pprint.pprint(data1)
data2 = pickle.load(pkl_file)
pprint.pprint(data2)
pkl_file.close()
