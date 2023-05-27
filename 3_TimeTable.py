tt = {'mon':[],'tue':[],'wed':[],'thurs':[],'fri':[],'sat':[]}

def init():
    for i in range(len([9,10,11,12])):
        for j in tt.keys():
            tt[j].append(None)
            
def insert(day,slot,course):
    if tt[day][slot-9]== None:
        tt[day][slot-9] = course
        return course
    else:
        return None
    
init()
insert('mon',10,'DSA')
insert('wed',9,'LD')
insert('sat',12,'DM')

print(tt)
