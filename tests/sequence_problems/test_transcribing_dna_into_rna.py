from rps.sequence_problems.transcribing_dna_into_rna import transcribe


def test_transcribe():
    """
    Checks if transcription properly replaces T with U
    """
    sequence = ["GATGGAACTTGACTACGTAAATT"]
    expected_rna = "GAUGGAACUUGACUACGUAAAUU"
    transcribed = transcribe(sequence)
    assert transcribed == expected_rna
