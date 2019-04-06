import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    #print(key)
    value = record[1]
    words = value.split()
    #print words
    for w in words:
      mr.emit_intermediate(w, key)

def reducer(word, list_of_values):
    # word: a different word from text
    # list_of_values: 
    index = []
    for v in list_of_values:
        index.append(v)
    mr.emit((word, index))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
