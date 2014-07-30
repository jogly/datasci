import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    mr.emit_intermediate(record[1][:-10], None)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence 
    mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
