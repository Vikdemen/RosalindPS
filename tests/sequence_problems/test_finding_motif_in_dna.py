from rps.sequence_problems.finding_a_motif_in_dna import get_motif_positions


def test_finding_motif_in_dna():
    sequence = 'GATATATGCATATACTT'
    motif = 'ATAT'
    positions = get_motif_positions([sequence, motif])
    assert positions == [2, 4, 10]
