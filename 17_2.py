from sys import argv

script,from_file,to_file = argv

in_file = open(from_file)
indata = in_file.read()
#print(indata)
to_file=open(to_file,'w')
to_file.write(indata)
to_file.close()
in_file.close()