#!/usr/bin/env python


def to_rna(dna):
    rna = ''
    for i in dna:
        rna += {
            'G': 'C',
            'C': 'G',
            'T': 'A',
            'A': 'U',
        }[i]
    return rna
