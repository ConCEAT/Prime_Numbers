import math

def getNum(text):
    if type(text) != str: raise TypeError('text must be string')
    while True:
        try: num = int(input(text).strip())
        except ValueError: 
            print ("Integer needed.")
            continue
        if num > 0: break
        print ("Number must be positive.")
    return num

def checkIfPrime(number):
    if type(number) != int: raise TypeError('number must be positive intiger')
    if number <= 0: raise ValueError('number must be positive intiger') 
    if number < 4:
        return not number == 1
    if number % 6 not in [1,5]: return False
    divisor = 5
    while divisor <= math.sqrt(number):
        if number % divisor == 0: return False
        while True:
            divisor+=1
            if divisor % 6 in [1,5]: break
    return True

def checkRange(start, end):
    return filter(checkIfPrime,range(start,end+1))

def Main():
    start = getNum("Start: ")
    end = getNum("End: ")
    print (*checkRange(start,end),sep='\n')
    

if __name__ == "__main__":
	Main()