import sys
def calculate_wer(reference, hypothesis):
    """
        Calculation of WER with Levenshtein distance.
        Works only for iterables up to 254 elements (uint8).
        O(nm) time and space complexity.

        >>> calculate_wer("who is there".split(), "is there".split())
        1
        >>> calculate_wer("who is there".split(), "".split())
        3
        >>> calculate_wer("".split(), "who is there".split())
        3
    """
    # initialisation
    import numpy
    d = numpy.zeros((len(reference) + 1) * (len(hypothesis) + 1),
                    dtype=numpy.uint8)
    d = d.reshape((len(reference) + 1, len(hypothesis) + 1))
    for i in range(len(reference) + 1):
        for j in range(len(hypothesis) + 1):
            if i == 0:
                d[0][j] = j
            elif j == 0:
                d[i][0] = i

    # computation
    for i in range(1, len(reference) + 1):
        for j in range(1, len(hypothesis) + 1):
            if reference[i - 1] == hypothesis[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                substitution = d[i - 1][j - 1] + 1
                insertion = d[i][j - 1] + 1
                deletion = d[i - 1][j] + 1
                d[i][j] = min(substitution, insertion, deletion)

    return d[len(reference)][len(hypothesis)] / float(len(reference))
 
if __name__ == "__main__":
    with open(sys.argv[1], 'r') as file:
        o = " ".join(file.readlines())

    with open(sys.argv[2], 'r') as file:
        t = " ".join(file.readlines())
  
    print(calculate_wer(o.split(), t.split()))
    print(o.split(), t.split())
print("hello")
