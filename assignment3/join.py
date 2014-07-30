import MapReduce
import sys

mr = MapReduce.MapReduce()

def mapper(record):
    rowid = record[1]
    mr.emit_intermediate(rowid, record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence 
    order = []
    for record in list_of_values:
      if record[0] == 'order':
        order = record
        break
    
    for record in list_of_values:
      if record[0] != 'order':
        mr.emit(order + record)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
