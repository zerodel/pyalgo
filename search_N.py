# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author : zerodel
# Readme:
#

import Bio.SeqIO as bo


__doc__ = ''' detect Ns in sequence .
'''
__author__ = 'zerodel'


def find_N(fa_file, coi="N"):
    coi = coi.lower()
    up, now, down = None, None, None
    is_in_region = False
    start = None
    for seq in bo.parse(fa_file, format="fasta"):
        modified_seq = seq.seq.lower()
        for i, nt in enumerate(modified_seq):
            up, now, down = now, down, nt

            if now == coi:
                if not up == coi and not down == coi: # single N
                    yield (seq.id, i, i)

                if down == coi and not up == coi:
                    is_in_region = True
                    start = i

                elif not down == coi and up == coi and is_in_region and start:
                    is_in_region = False
                    yield (seq.id, start, i)
        if modified_seq[-1] == coi and not modified_seq[-2] == coi and len(modified_seq) > 1:
            yield (seq.id, len(modified_seq), len(modified_seq))


def main(fa, output, coi="N"):
    with open(output, "w") as out:
        out.write("chr\tstart\tend\n")
        for t in find_N(fa, coi):
            chr_id, start, end = t
            out.write("{chr}\t{start}\t{end}\n".format(chr=chr_id,
                                                       start=start,
                                                       end=end))

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print(__doc__)
    elif len(sys.argv) >= 4:
        main(sys.argv[-3], sys.argv[-2], sys.argv[-1])