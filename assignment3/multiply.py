import MapReduce
import sys
import operator

mr = MapReduce.MapReduce()

def mapper(record):
    if record[0] == 'a':
        for k in range(5):
            # emit key = (a_i, a_k), value = (a_j, a[i,j])
            mr.emit_intermediate((record[1], k), (record[2], record[3]))
    else:
        for i in range(5):
            # emit key = (b_i, b_k), value = (b_j, b[j,k])
            mr.emit_intermediate((i, record[2]), (record[1], record[3]))

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence 
    dik = {0: [], 1:[], 2:[], 3:[], 4:[]}
    map (lambda tupl: dik[tupl[0]].append(tupl[1]), list_of_values)
    
    mr.emit((key[0], key[1], \
        reduce(lambda x,y: x + y, \
            map(lambda lis: lis[0] * lis[1], \
                filter(lambda lis: len(lis) == 2, dik.itervalues())))))
    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
