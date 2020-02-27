from rps.io_manager import parse_fasta


def test_parse_fasta():
    """
    Checks proper parsing of fasta files
    :return:
    """
    data = [">Tag1", "ATGC", "CGTA", "GGCC", ">Tag2", "ATGC", "AATT"]
    output = parse_fasta(data)
    output = [(line.sequence, line.tag) for line in output]
    expected = [("ATGCCGTAGGCC", "Tag1"), ("ATGCAATT", "Tag2")]
    assert output == expected
