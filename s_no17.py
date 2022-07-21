def longest_line(filename) :
    lo_line = ""
    f=open(filename,'r')
    
    for line in f.readlines():
        if len(line) > len(lo_line):
            lo_line = line
    return(lo_line)
  
print(longest_line("abc_file.txt"))
