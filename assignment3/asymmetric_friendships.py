import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    sorted_record = sorted(record)
    mr.emit_intermediate(tuple(sorted(record)), record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence 
    if len(list_of_values) == 1:
        mr.emit(tuple(list_of_values[0]))
        mr.emit((list_of_values[0][1],list_of_values[0][0]))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
