# translate.py

# 打包密码子字典
table = {'TTT': 'F', 'CTT': 'L', 'ATT': 'I', 'GTT': 'V', 'TTC': 'F', 'CTC': 'L',
         'ATC': 'I', 'GTC': 'V', 'TTA': 'L', 'CTA': 'L', 'ATA': 'I', 'GTA': 'V',
         'TTG': 'L', 'CTG': 'L', 'ATG': 'M', 'GTG': 'V', 'TCT': 'S', 'CCT': 'P',
         'ACT': 'T', 'GCT': 'A', 'TCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
         'TCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A', 'TCG': 'S', 'CCG': 'P',
         'ACG': 'T', 'GCG': 'A', 'TAT': 'Y', 'CAT': 'H', 'AAT': 'N', 'GAT': 'D',
         'TAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D', 'TAA': 'Stop', 'CAA': 'Q',
         'AAA': 'K', 'GAA': 'E', 'TAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
         'TGT': 'C', 'CGT': 'R', 'AGT': 'S', 'GGT': 'G', 'TGC': 'C', 'CGC': 'R',
         'AGC': 'S', 'GGC': 'G', 'TGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
         'TGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'}

# 找到序列的编码区段
def find_coding_part(dna):
    seq = []
    start = 0
    dna_len = int(len(dna) / 3) * 3
    end = len(dna)-1
    for i in range(0,dna_len-3):
        temp_codon = dna[i:i+3]
        if temp_codon =='ATG':
            start = i
            temp_seq = ''
            for j in range(i,dna_len-3,3):
                temp_codon = dna[j:j+3]
                temp_seq += temp_codon
                if table[temp_codon] == 'Stop':
                    seq.append(temp_seq)
                    break
                if (j == dna_len-6):
                    temp_seq +="---(didn't match a stop codon)"
                    seq.append(temp_seq)
        continue
    return seq

# 互补序列
def reverse_complement(dna):
    revc = ""
    basepair = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    for c in dna:
        revc = basepair[c] + revc
    return revc

# 翻译序列
def translate(dna):
    aa = ''
    for i in range(0, len(dna), 3):
        temp_codon = dna[i:i + 3]
        if  temp_codon == '---':
            break
        if table[temp_codon] == 'Stop':
            break
        aa += table[dna[i:i + 3]]
    return aa


# 程序接口函数
def translate_raw(dna):
    dna = dna.upper()
    aa = []
    seq = find_coding_part(dna)
    for dna_seq in seq:
        aa.append(translate(dna_seq))
    return aa,seq
# 下为测试代码
if __name__ == '__main__':
    dna = input("please code your dna:")
    aa,seq = translate_raw(dna)
    print(aa)
    print(seq)
    for item,result in zip(seq,aa):
        print("index:{}\n\tDNA coding sequence:{}\n\taa:{}\n".format(seq.index(item)+1,item,result))









