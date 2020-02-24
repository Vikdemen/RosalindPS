import rps.io_manager as io


def test_parse_fasta():
    """
    Checks proper parsing of fasta files
    :return:
    """
    data = [">Tag1", "ATGC", "CGTA", "GGCC", ">Tag2", "ATGC", "AATT"]
    output = io.parse_fasta(data)
    expected = [["ATGCCGTAGGCC", "Tag1"], ["ATGCAATT", "Tag2"]]
    assert output == expected
