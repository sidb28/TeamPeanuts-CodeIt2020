def getBestDRI(geneSequence):
    numberOfGenomes = {
        "A":0, "C":0, "G":0, "T":0
    }
    for genome in geneSequence:
        numberOfGenomes[genome]+=1
    
    finalGenome = ""
    numberOfAPairs = numberOfGenomes["A"]//2
    numberOfGenomes["A"]-=numberOfAPairs*2
    remainingNonA = numberOfGenomes["G"] + numberOfGenomes["T"] + numberOfGenomes["C"]

    for i in range(numberOfAPairs):
        numberOfPairsLeft = numberOfAPairs-i
        if(numberOfGenomes["C"]>=2):
            finalGenome+="AACC"
            numberOfGenomes["C"]-=2
        elif(numberOfGenomes["G"]>1 and numberOfGenomes["C"]==1) or numberOfGenomes["G"]>0:
            finalGenome+="AAG"
            numberOfGenomes["G"]-=1
        elif(numberOfGenomes["T"]>1 and numberOfGenomes["C"]==1) or numberOfGenomes["T"]>0:
            finalGenome+="AAT"
            numberOfGenomes["T"]-=1
        elif(numberOfGenomes["A"]==1 and numberOfGenomes["C"]==1):
            # 1 G, 1 T, 1 C
            if numberOfPairsLeft<=2: # 3-5A
                finalGenome+="ACGTAA"
                for genome in numberOfGenomes:
                    numberOfGenomes[genome]-=1
            else: # >5A
                finalGenome+="AAC"
                numberOfGenomes["C"]-=1
        elif(numberOfGenomes["A"]==0 and numberOfGenomes["C"]==1):
            # 1 G, 1 T, 1 C, >2 A
            if(numberOfAPairs<=2): #<4
                finalGenome+="ACGTA"
                for genome in numberOfGenomes:
                    if(genome!="A"):
                        numberOfGenomes[genome]-=1
            else:
                finalGenome+="AAC"
                numberOfGenomes["C"]-=1
        else:
            finalGenome += "AA"
    
    for genome in numberOfGenomes:
        finalGenome+=genome*numberOfGenomes[genome]

    return finalGenome

print(getBestDRI("AAACCCAAAGGTTACTGAAAAG"))