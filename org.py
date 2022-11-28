
def isorg(p1values: list, p2values: list, p1get: list, p2get: list = None):
    """
    gets two vectors of values
    gets two vectors that describes how to give the items between two playes (1 vectors is the compliemnt of the other)

    returns true or fixes the vectors
    """
    if p2get == None:
        for i in p1get:
            p2get.append(1-i)
    else:
        for i in range(len(p1get)):
            if p1get[i]+p2get[i] != 1:
                raise Exception("every item should be given fully")
    if len(p1values) != len(p2values) != len(p1get) != len(p2get):
        raise Exception("bad input")
        
    for i in range(len(p1get)):
        a = p1values[i]*p2get[i]
        b = p1values[i]*p1get[i]
        if a != 0 and b != 0 and b < a:
            jump = 0.0000001
            while b < a:
                p1get[i] += jump
                p2get[i] -= jump
                a = p1values[i]*p2get[i]
                b = p1values[i]*p1get[i]
            return p1get, p2get

    return True


if __name__ == "__main__":
    print(isorg(p1values=[10,20,30,40], p2values=[40,30,20,10], p1get=[0.7, 0.4, 0, 1], p2get=[0.3, 0.6, 1, 0]))
    print(isorg(p1values=[10,20,30,40], p2values=[40,30,20,10], p1get=[0.6, 0.5, 0, 1], p2get=[0.4, 0.5, 1, 0]))

    print(isorg(p1values=[15,15,40,30], p2values=[40,25,30,5], p1get=[0.6, 0.5, 0, 1], p2get=[0.4, 0.5, 1, 0]))