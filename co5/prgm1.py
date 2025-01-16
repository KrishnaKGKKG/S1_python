source="prgm1.txt"
destination="prgm2.txt"

with open(source,'r') as src,open(destination,'w') as dest:
    for line_number ,line in enumerate(src,start=1):
         if line_number%2 !=0:
             dest.write(line)
             
