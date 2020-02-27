from typing import List
from rps.io_manager import as_fasta
from rps.sequence_problems.sequences import DNA


@as_fasta
def get_possible_proteins(strands: List[DNA]) -> str:
    # there should be only one sequence
    strand, = strands
    orfs = strand.search_for_orf()
    proteins = {orf.transcribe().translate_to_protein().sequence for orf in orfs}
    return '\n'.join(proteins)
