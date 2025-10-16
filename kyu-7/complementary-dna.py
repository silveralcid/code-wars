# defined once to avoid repeating for every call
dna_dict = {
    "A": "T",
    "C": "G",
    "T": "A",
    "G": "C"
}


def DNA_strand(dna):
    dna = dna.upper()
    return "".join(dna_dict[ch] for ch in dna)
