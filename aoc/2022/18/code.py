import os
path_to_day = os.path.dirname(__file__)
with open(f'{path_to_day}/input.txt') as f: input = f.read()

sample_input = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
"""

sample_answer1 = 64
sample_answer2 = 58

def process(input):
    return [i.strip() for i in input.splitlines()]

# print(process(sample_input))
# adjacent cubes from cube 0,0,0
ADJ = [(0,0,1), (0,0,-1), (0,1,0), (0,-1,0), (1,0,0), (-1,0,0)]

def p1(input):
    data = process(input)
    space = set()
    for i in data:
        x,y,z = [int(j) for j in i.split(",")]
        space.add((x,y,z))
    surf = 0
    for x,y,z in space:
        adj = 0
        for dx,dy,dz in ADJ:
            if (x+dx,y+dy,z+dz) in space:
                adj += 1
        surf += 6-adj
    # cube is touching if it has any side touching another side
    # cube at 2,2,2 is touching cube at 2,3,2 on one side
    return surf

# def p2(input):
#     data = process(input)
#     space = set()
#     highz,lowz,highy,lowy,highx,lowx = 0,0,0,0,0,0
#     for i in data:
#         x,y,z = [int(j) for j in i.split(",")]
#         highz = max(highz,z)
#         lowz = min(lowz,z)
#         highy = max(highy,y)
#         lowy = min(lowy,y)
#         highx = max(highx,x)
#         lowx = min(lowx,x)
#         space.add((x,y,z))
#     surf = 0
#     for x,y,z in space:
#         adj = 0
#         for x in range(lowx-1,x):
#             if (x,y,z) in space:
#                 adj += 1
#                 break
#         for x in range(x,highx+1):
#             if (x,y,z) in space:
#                 adj += 1
#                 break
#         for y in range(lowy-1,y):
#             if (x,y,z) in space:
#                 adj += 1
#                 break
#         for y in range(y,highy+1):
#             if (x,y,z) in space:
#                 adj += 1
#                 break
#         for z in range(lowz-1,z):
#             if (x,y,z) in space:
#                 adj += 1
#                 break
#         for z in range(z,highz+1):
#             if (x,y,z) in space:
#                 adj += 1
#                 break
#         surf += 6-adj
#     return surf

STORE = set()

def reachable(x,y,z,space):
    if (x,y,z) in STORE:
        return STORE[(x,y,z)]
    c = 0
    for dx,dy,dz in ADJ:
        if (x+dx,y+dy,z+dz) in space: #immidiate neighbor is blocking
            c += 1
        else:
            if reachable(x+dx,y+dy,z+dz,space):
                return True

def countreachablesides(space, bounds):
    c = 0
    for x,y,z in space:
        c += reachable(x,y,z,space,bounds)


def p2(input):
    data = process(input)
    space = set()
    highz,lowz,highy,lowy,highx,lowx = 0,0,0,0,0,0
    for i in data:
        x,y,z = [int(j) for j in i.split(",")]
        highz = max(highz,z)
        lowz = min(lowz,z)
        highy = max(highy,y)
        lowy = min(lowy,y)
        highx = max(highx,x)
        lowx = min(lowx,x)
        space.add((x,y,z))
    bounds = (highx,lowx,highy,lowy,highz,lowz)
    surf = countreachablesides(space, bounds)
    return surf


if sample_answer1:
    sample_result = p1(sample_input)
    print("sample1", sample_result)
    if sample_result == sample_answer1:
        print("sample1 test pass")
        print("\nproblem1", p1(input), "\n\n")

if sample_answer2:
    sample_result = p2(sample_input)
    print("sample2", sample_result)
    if sample_result == sample_answer2:
        print("sample2 test pass")
        print("\nproblem2", p2(input), "\n\n")


print("\ndone")
