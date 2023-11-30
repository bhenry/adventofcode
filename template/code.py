import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: puzzleinput = f.read()

samples = {

}
sample2s = {

}

def process(input):
    return [i.strip() for i in input.splitlines()]

def p1(pz):

    return None

def p2(pz):

    return None

pzz = process(puzzleinput)

if answer2 := p2(pzz):
    print("\nproblem2", answer2, "\n\n")

    # debug
    if sample2s:
        for sample in sample2s:
            sample_result = p2(sample)
            print("sample2", sample_result)
            if sample_result == sample2s[sample]:
                print("sample2 test pass")

if answer1 := p1(pzz):
    print("\nproblem1", answer1, "\n\n")

    # debug
    if samples:
        for sample in samples:
            sample_result = p1(sample)
            print("sample1", sample_result)
            if sample_result == samples[sample]:
                print("sample1 test pass")



print("\ndone")
