import rps_io_manager
import rps_sequences as bio
import rps_io_manager as file


def main():
    data = file.read_file("../input.txt")
    sequences = rps_io_manager.parse_fasta(data)
    greatest = max(sequences, key=lambda seq: seq.gc_content())
    print(greatest.tag)
    print(greatest.gc_content())

if __name__ == '__main__':
    main()
