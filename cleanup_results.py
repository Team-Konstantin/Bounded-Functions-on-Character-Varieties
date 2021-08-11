# removes all the timings from the output
# and only leaves the diagonal entries that are outputted for each M

filename = "Q3 adjoin x^2+3x+1.txt"
out = ""
with open(filename,'r') as f:
    for line in f:
        if line[0] == "[":
            out = out + line

with open(filename,'w') as f:
    f.write(out)
