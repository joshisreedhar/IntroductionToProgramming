canBewith={"fox":"corn",
    "corn":"fox",
    "goose":None}


shoreA=["corn","fox","goose",]
shoreB=[]

def pickFirst():
    for k,v in canBewith.items():
        if(v==None):
            return k
    return None

def pickNext():
    if(len(shoreA) > 0):
        return shoreA[0]
    else:
        return None

def isLastCharacterToPick():
    return len(shoreA) == 1

def whoToPickBackToShareA(character):
    canbe = canBewith[character]
    if(isLastCharacterToPick()):
        return None
    for existingCharacter in shoreB:
        if(existingCharacter != canbe):
            return existingCharacter
    return None

def transferToOtherShore(character):
    global shoreB
    global shoreA
    whoToPickUpBack=whoToPickBackToShareA(character)
    if( whoToPickUpBack== None):
        shoreA.remove(character)
        shoreB.append(character)
    else:
        shoreA.remove(character)
        shoreB.append(character)
        shoreA.append(whoToPickUpBack)
        shoreB.remove(whoToPickUpBack)
    
    
trip=1
characterToPickup = pickFirst()
while(characterToPickup != None):
    transferToOtherShore(characterToPickup)
    characterToPickup = pickNext()
    print("========After trip " + str(trip))
    print(shoreA)
    print(shoreB)
    print("==========================")
    trip = trip+1


