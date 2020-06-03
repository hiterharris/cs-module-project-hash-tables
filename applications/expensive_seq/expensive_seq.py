computed_results = dict()

def expensive_seq(x, y, z):
    
    if x <= 0:
        return y + z

    else:

        if (x-1,y+1,z) in computed_results:
            addend1 = computed_results[(x-1,y+1,z)]
        else:
            addend1 = expensive_seq(x-1,y+1,z)
            computed_results[(x-1,y+1,z)] = addend1

        if (x-2,y+2,z*2) in computed_results:
            addend2 = computed_results[(x-2,y+2,z*2)]
        else:
            addend2 = expensive_seq(x-2,y+2,z*2)
            computed_results[(x-2,y+2,z*2)] = addend2

        if (x-3,y+3,z*3) in computed_results:
            addend3 = computed_results[(x-3,y+3,z*3)]
        else:
            addend3 = expensive_seq(x-3,y+3,z*3)
            computed_results[(x-3,y+3,z*3)] = addend3

    result = addend1 + addend2 + addend3
    computed_results[(x, y, z)] = result

    return result

if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))