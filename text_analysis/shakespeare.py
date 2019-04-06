import TextMapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = TextMapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # value: line of text loaded as record
    punc = ['!','?','.',',','\'',':',';','(',')','[',']','\"','&','_','*','{','}','$','%','/','@','=','\\','|','`','<','>','+']
    value = record
    for i in punc:    
        value = value.replace(i,'')
    value = value.replace('-','')
    value = value.lower()
    words = value.split()
    words = [w for w in words if not any(char.isdigit() for char in w)] 
    for w in words:
      mr.emit_intermediate(w, 1)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = 0
    for v in list_of_values:
      total += v
    mr.emit((key, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1], "r", encoding='utf-8')
  mr.execute(inputdata, mapper, reducer)
