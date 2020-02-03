"""
     insertSort(data)

     Function or Procedure or Routine or method
     1. Name
     2. Inputs (May or May Not) / Parameter / Arguments
     3. return (in the end ) if you have not given it it is by default return
        act as acknowledgement
     4. Definition
        What function should do !!

        Execution happens in a sequence i.e. line by line

     loops:
        Loops will excute a sequence from 0 to n-1 or any choice or any choice of range of yours
        do the same things again and again

     function:
         Group of statements / Logic which has to be execueted
         we can give sererval different inputs to get the logic work
         and generate results accordingly

         My Prgram is MODULARIZED
"""

"""
panneer = 200
parantha = 20
bill1 = panner + parantha
print(">> bill1 is:", bill1)

dal = 100
bill2 = dal + parantha
print(">> bill2 is:", bill2)

dosa = 80
idli = 30
bill3 = dal + parantha
print(">> bill3 is:", bill3)
"""

panner = 200
paraantha = 20
dal = 100
dosa = 80
idli = 30

# def add(n1, n2):

def add(n1=0, n2=2):
# def add(n1, n2=0):
# def add(n1=0, n2):  # error
    sum = n1 + n2
    return sum

# def add(n1=0, n2, n3=0): err
# def add(n1, n2=0, n3=0): ok


print(">> bill1 is:", add(panner, paraantha))
print(">> bill2 is:", add(dal, paraantha))
print(">> bill3 is:", add(dosa, idli))
print(">> bill4 is:", add(dosa, dal))
print(">> bill6 is:", add(10))
print(">> bill7 is:", add(10))

print(">> bill8 is:", add(n1=dosa, n2=dal))
print(">> bill9 is:", add(n2=dosa, n1=dal))

print(">> bill9 is:", add(n2=10))

