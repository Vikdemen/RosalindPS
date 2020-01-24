import VDBioinfo

file = open("input.txt")
text_lines = file.readlines()
file.close()

# sequence may span several lines
#unfininshed
dna_strings = []
sequence = ''
tag = ''
for i in range[0: len(text_lines)]:
    if text_lines[i].startswith('>'):
        dna_strings.append(VDBioinfo.DNA(sequence, line))
        sequence = ''
    else:
        sequence += line

greatest = None
greatest_gc = 0
for dna in dna_strings:
    gc = dna.gc_content()
    if gc > greatest_gc:
        greatest = dna
        greatest_gc = gc
print(greatest.tag)
print(greatest_gc)