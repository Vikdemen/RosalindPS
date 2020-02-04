from typing import List, Tuple
import rps.io_manager as io
import rps.sequences as seq


def main():
    fasta_sequences = io.read_file("input.txt")
    max_tag, max_gc_content = calculate_max_gc_content(fasta_sequences)
    print(max_tag)
    print(max_gc_content)


def calculate_max_gc_content(unparsed: List[str]) -> Tuple[str, float]:
    """
    :param unparsed: - sequence_problems in FASTA format
    :return: the tag and gc content of DNA strand with highest GC content
    """
    parsed = io.parse_fasta(unparsed)
    strands = [seq.DNA(sequence, tag) for sequence, tag in parsed]
    gc_content_values = [(strand.tag, strand.gc_content()) for strand in strands]
    max_tag, max_gc_content = max(gc_content_values, key=lambda dna: dna.gc_content())
    return max_tag, max_gc_content


if __name__ == '__main__':
    main()
