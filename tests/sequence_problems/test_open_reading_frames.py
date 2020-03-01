from rps.sequence_problems.open_reading_frames import get_possible_proteins


def test_get_possible_proteins():
    fasta_sequences = [
        ">Rosalind_99",
        "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
    ]
    expected_proteins = {"MLLGSFRLIPKETLIQVAGSSPCNLS", "M", "MGMTPRLGLESLLE", "MTPRLGLESLLE"}
    translated_proteins = get_possible_proteins(fasta_sequences)
    translated_proteins = set(translated_proteins.split('\n'))
    assert translated_proteins == expected_proteins
