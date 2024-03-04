# Julia Chen 349860031

def cipher(word, num):
    # variables
    p = list(inList[0].lower())
    n = int(inList[1])
    alpha = "abcdefghijklmnopqrstuvwxyz"

    # processing
    for i in range(0, len(p)):
        a = True
        temp = alpha.find(p[i])
        tempIn = temp + n
        while a: 
            if tempIn > 25: # checking if the index is out of bounds
                tempIn -= 26
            else: # index is in bounds
                a = False
                p[i] = alpha[tempIn]

    result = ''.join(p)
    return result

# input
input = input()
inList = input.split(", ")
print(cipher(inList[0], inList[1]))