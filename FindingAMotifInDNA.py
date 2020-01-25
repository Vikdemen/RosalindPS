import vd_bio_info

strand = input("Input the sequence")
motif = input("Input the motif")
results = []
start = 0
while True:
    result = strand.find(motif, start)
    if result == -1:
        break
    else:
        start = result + 1
        results.append(result)
results = [str(x + 1) for x in results]
formatted = ' '.join(results)
print(formatted)

# We need to find motifs in a strand of DNA
# Answer needs to use 1-based numbering
