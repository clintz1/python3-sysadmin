# Implement Local Storage
def local(infile, outfile):
    outfile.write(infile.read())
    outfile.close()
    infile.close()
