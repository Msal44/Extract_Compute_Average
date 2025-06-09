# Use the file name mbox-short.txt as the file name

total = 0
count = 0
fname = input("Enter file name: ")
fh = open(fname)

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        atpos = line.find(":")
        val = line[atpos+2:]
        val = float(val)
        total += val
        #x = len(line)
    #print(val)
#print("The total is ", total)
#print("Line length is ", x)
#print("Colon position is ", atpos)    
#print("Count of lines is ", count)
print("Average spam confidence:", total / count)
