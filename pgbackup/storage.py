# Implement Local Storage

def local(infile, outfile):
    outfile.write(infile.read())
    outfile.close()
    infile.close()

def s_3(client, infile, bucket, name):
    client.upload_fileobj(infile, bucket, name)
