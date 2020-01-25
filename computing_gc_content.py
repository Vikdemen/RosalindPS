import vd_bio_info as bio

data = bio.read_files("input.txt")
sequences = bio.parse_fasta(data)
greatest = max(sequences, key=lambda seq: seq.gc_content())
print(greatest.tag)
print(greatest.gc_content())
