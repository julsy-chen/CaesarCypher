# Julia Chen 349860031

def cipher(word, num):
    '''
    this encrypts the target string using the caesar encryption

    arguments
        target : string
        value : integer

    return
        string : the encrypted version of target
    '''
    # variables
    p = list(inList[0].lower())
    n = int(inList[1])
    alpha = "abcdefghijklmnopqrstuvwxyz"

    # processing
    for i in range(0, len(p)):
        a = True
        temp = alpha.find(p[i]) # index of the letter in alpha
        tempIn = temp + n # index of the shifted letter
        while a: 
            if tempIn > 25: # checking if the index is out of bounds
                tempIn = tempIn % 26
            elif tempIn < 0:
                tempIn = 26 + tempIn
            else: # index is in bounds
                a = False
                p[i] = alpha[tempIn]

    result = ''.join(p)
    return result

# input
input = input()
inList = input.split(", ")
print(cipher(inList[0], inList[1]))
# this is a comment yippee