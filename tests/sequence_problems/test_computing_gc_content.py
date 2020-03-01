from rps.sequence_problems.computing_gc_content import calculate_max_gc_content
from pytest import approx


def test_calculate_max_gc_content():
    """
    Checks if the function correctly finds sequence with largest gc_content
    :return:
    """
    sample_data = [
        ">Rosalind_6404",
        "CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC"
        "TCCCACTAATAATTCTGAGG",
        ">Rosalind_5959",
        "CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT",
        "ATATCCATTTGTCAGCAGACACGC",
        ">Rosalind_0808",
        "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC",
        "TGGGAACCTGCGGGCAGTAGGTGGAAT"
    ]
    tag: str
    content: float
    tag, content = calculate_max_gc_content(sample_data).split('\n')
    content = float(content)
    expected_tag = "Rosalind_0808"
    expected_content = 60.919540
    assert tag == expected_tag
    assert content == approx(expected_content)
