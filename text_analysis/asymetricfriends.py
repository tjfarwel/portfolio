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
    person = record[0]
    friend = record[1]
    mr.emit_intermediate(person, [friend,1])
    mr.emit_intermediate(friend, [person,0])

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    friends = []
    for v in list_of_values:
        if v[1]:
            friends.append([v[0],key])
    for v in list_of_values:
        if v[1] == 0:
            if [v[0],key] in friends:
                friends.remove([v[0],key])
    if friends:
        for friend in friends:
            mr.emit((friend))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)