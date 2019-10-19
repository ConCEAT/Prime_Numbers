import math
def getNum(text):
    while True:
        try: num = int(input(text).strip())
        except ValueError: 
            print ("Integer needed.")
            continue
        if num > 0: break
        print ("Number must be positive.")
    return num

def checkIfPrime(num):
    if num < 4:
        return not num == 1
    if num % 6 not in [1,5]: return False
    divisor = 5
    while divisor <= math.sqrt(num):
        if num % divisor == 0: return False
        while True:
            divisor+=1
            if divisor % 6 in [1,5]: break
    return True

def checkRange(start, end):
    for num in range(start,end+1):
        if checkIfPrime(num):
            yield num

def Main():
    #start = getNum("Start: ")
    #end = getNum("End: ")
    #print(list(checkRange(start,end))[-1])
    pass

if __name__ == "__main__":
	Main()
