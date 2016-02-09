def RobotCar(L):
    edges = {
        "50" : ["30"],
        "30" : ["50", "32"],
        "32" : ["30", "33", "12"],
        "33" : ["32", "53"],
        "53" : ["33", "51", "54"],
        "51" : ["41", "53"],
        "41" : ["42"],
        "42" : ["41"],
    }
    start = 5,0
    for destination in L:
        # find path from start to destination
        pass

print(RobotCar([[4,2]]))