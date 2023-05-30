import sys

def global_alignment(seq1, seq2, match_score, mismatch, gap):
    m = len(seq1)
    n = len(seq2)
    F = [[0] * (n+1) for _ in range(m+1)]
    matrix = [[0] * (n+1) for _ in range(m+1)]
    for i in range(m+1):
        F[i][0] = i * gap
        matrix[i][0] = i * gap
    
    for j in range(n+1):
        F[0][j] = j * gap
        matrix[0][j] = j * gap
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if seq1[i-1] == seq2[j-1]:
                match = F[i-1][j-1] + match_score
            else:
                match = F[i-1][j-1] + mismatch
            u = F[i-1][j] + gap
            l = F[i][j-1] + gap
            
            F[i][j] = max(match, u, l)

            if F[i][j] == u:
                matrix[i][j] = 'U'
            elif F[i][j] == l:
                matrix[i][j] = 'L'
            else:
                matrix[i][j] = 'C'
                
    
    aligned_seq1 = ""
    aligned_seq2 = ""
    i = len(seq1)
    j = len(seq2)

    while i > 0 and j > 0:
        current = F[i][j]
        up = F[i][j-1]
        left = F[i-1][j]

        if current == up + gap:
            aligned_seq1 = "-" + aligned_seq1
            aligned_seq2 = seq2[j-1] + aligned_seq2
            j -= 1
        elif current == left + gap:
            aligned_seq1 = seq1[i-1] + aligned_seq1
            aligned_seq2 = "-" + aligned_seq2
            i -= 1
        else:
            aligned_seq1 = seq1[i-1] + aligned_seq1
            aligned_seq2 = seq2[j-1] + aligned_seq2
            i -= 1
            j -= 1

    while i > 0:
        aligned_seq1 = seq1[i-1] + aligned_seq1
        aligned_seq2 = "-" + aligned_seq2
        i -= 1

    while j > 0:
        aligned_seq1 = "-" + aligned_seq1
        aligned_seq2 = seq2[j-1] + aligned_seq2
        j -= 1

    return aligned_seq1, aligned_seq2, matrix, F

seq1 = sys.argv[1]
seq2 = sys.argv[2]
match_score = 1
mismatch = -1
gap = -1

result = global_alignment(seq1, seq2, match_score, mismatch, gap)
print(result[0])
print(result[1])
for i in result[2]:
    print(i)
print()
for i in result[3]:
    print(i)

