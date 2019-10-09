def query(dataBase, group, id):
    try: 
        key = (group, id)
        return dataBase[key]
    except KeyError: 
        return None 

def listGrades(dataBase, group):
    scoreList = []
    keys = [x for x in dataBase.keys if x[0] == group]
    
def maxGrade(dataBase, group):
    scores = listGrades(dataBase, group)
    return max(scores)
    
def showInterface():
    print("1:....")