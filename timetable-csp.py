# TimeTable Problem
import time
from collections import defaultdict

def BT_Search(assignment, domains, constraint_fn, select_unassigned_var):
  """Backtracking search."""
  if constraint_fn(assignment) and None not in assignment.values():
    return assignment
  print(assignment)
  var = select_unassigned_var(assignment)

  for value in domains[var]:
    assignment[var] = value;
    if constraint_fn(assignment):
      result = BT_Search(assignment, domains, constraint_fn, select_unassigned_var)
      if result != -1: return result
      
    assignment[var] = None;
  return -1

def get_unassigned_var(assignment):
  for var, val in assignment.items():
    if val != None: continue
    return var

def timetable_constraints(a):
  #unqiue
  if a['M1'] != None:
    if a['M1'] == a['EidI']: return False
    if a['M1'] == a['OOP']: return False
    if a['M1'] == a['TI']: return False
    if a['M1'] == a['EidPmS']: return False
    if a['M1'] == a['DB']: return False
    if a['M1'] == a['ES']: return False
    if a['M1'] == a['SE']: return False
    if a['M1'] == a['SProj']: return False
    if a['M1'] == a['SP']: return False
    if a['M1'] == a['SuZ']: return False
    if a['M1'] == a['CB']: return False
    if a['M1'] == a['WE']: return False
    if a['M1'] == a['KI']: return False
    if a['M1'] == a['CV']: return False
    if a['M1'] == a['TE']: return False
  if a['EidI'] != None:
    if a['EidI'] == a['OOP']: return False
    if a['EidI'] == a['TI']: return False
    if a['EidI'] == a['EidPmS']: return False
    if a['EidI'] == a['DB']: return False
    if a['EidI'] == a['ES']: return False
    if a['EidI'] == a['SE']: return False
    if a['EidI'] == a['SProj']: return False
    if a['EidI'] == a['SP']: return False
    if a['EidI'] == a['SuZ']: return False
    if a['EidI'] == a['CB']: return False
    if a['EidI'] == a['WE']: return False
    if a['EidI'] == a['KI']: return False
    if a['EidI'] == a['CV']: return False
    if a['EidI'] == a['TE']: return False
  if a['OOP'] != None:
    if a['OOP'] == a['TI']: return False
    if a['OOP'] == a['EidPmS']: return False
    if a['OOP'] == a['DB']: return False
    if a['OOP'] == a['ES']: return False
    if a['OOP'] == a['SE']: return False
    if a['OOP'] == a['SProj']: return False
    if a['OOP'] == a['SP']: return False
    if a['OOP'] == a['SuZ']: return False
    if a['OOP'] == a['CB']: return False
    if a['OOP'] == a['WE']: return False
    if a['OOP'] == a['KI']: return False
    if a['OOP'] == a['CV']: return False
    if a['OOP'] == a['TE']: return False
  if a['TI'] != None:
    if a['TI'] == a['EidPmS']: return False
    if a['TI'] == a['DB']: return False
    if a['TI'] == a['ES']: return False
    if a['TI'] == a['SE']: return False
    if a['TI'] == a['SProj']: return False
    if a['TI'] == a['SP']: return False
    if a['TI'] == a['SuZ']: return False
    if a['TI'] == a['CB']: return False
    if a['TI'] == a['WE']: return False
    if a['TI'] == a['KI']: return False
    if a['TI'] == a['CV']: return False
    if a['TI'] == a['TE']: return False
  if a['EidPmS'] != None:
    if a['EidPmS'] == a['DB']: return False
    if a['EidPmS'] == a['ES']: return False
    if a['EidPmS'] == a['SE']: return False
    if a['EidPmS'] == a['SProj']: return False
    if a['EidPmS'] == a['SP']: return False
    if a['EidPmS'] == a['SuZ']: return False
    if a['EidPmS'] == a['CB']: return False
    if a['EidPmS'] == a['WE']: return False
    if a['EidPmS'] == a['KI']: return False
    if a['EidPmS'] == a['CV']: return False
    if a['EidPmS'] == a['TE']: return False
  if a['DB'] != None:
    if a['DB'] == a['ES']: return False
    if a['DB'] == a['SE']: return False
    if a['DB'] == a['SProj']: return False
    if a['DB'] == a['SP']: return False
    if a['DB'] == a['SuZ']: return False
    if a['DB'] == a['CB']: return False
    if a['DB'] == a['WE']: return False
    if a['DB'] == a['KI']: return False
    if a['DB'] == a['CV']: return False
    if a['DB'] == a['TE']: return False
  if a['ES'] != None:
    if a['ES'] == a['SE']: return False
    if a['ES'] == a['SProj']: return False
    if a['ES'] == a['SP']: return False
    if a['ES'] == a['SuZ']: return False
    if a['ES'] == a['CB']: return False
    if a['ES'] == a['WE']: return False
    if a['ES'] == a['KI']: return False
    if a['ES'] == a['CV']: return False
    if a['ES'] == a['TE']: return False
  if a['SE'] != None:
    if a['SE'] == a['SProj']: return False
    if a['SE'] == a['SP']: return False
    if a['SE'] == a['SuZ']: return False
    if a['SE'] == a['CB']: return False
    if a['SE'] == a['WE']: return False
    if a['SE'] == a['KI']: return False
    if a['SE'] == a['CV']: return False
    if a['SE'] == a['TE']: return False
  if a['SProj'] != None:
    if a['SProj'] == a['SP']: return False
    if a['SProj'] == a['SuZ']: return False
    if a['SProj'] == a['CB']: return False
    if a['SProj'] == a['WE']: return False
    if a['SProj'] == a['KI']: return False
    if a['SProj'] == a['CV']: return False
    if a['SProj'] == a['TE']: return False
  if a['SP'] != None:
    if a['SP'] == a['SuZ']: return False
    if a['SP'] == a['CB']: return False
    if a['SP'] == a['WE']: return False
    if a['SP'] == a['KI']: return False
    if a['SP'] == a['CV']: return False
    if a['SP'] == a['TE']: return False
  if a['SuZ'] != None:
    if a['SuZ'] == a['CB']: return False
    if a['SuZ'] == a['WE']: return False
    if a['SuZ'] == a['KI']: return False
    if a['SuZ'] == a['CV']: return False
    if a['SuZ'] == a['TE']: return False
  if a['CB'] != None:
    if a['CB'] == a['WE']: return False
    if a['CB'] == a['KI']: return False
    if a['CB'] == a['CV']: return False
    if a['CB'] == a['TE']: return False
  if a['WE'] != None:
    if a['WE'] == a['KI']: return False
    if a['WE'] == a['CV']: return False
    if a['WE'] == a['TE']: return False
  if a['KI'] != None:
    if a['KI'] == a['CV']: return False
    if a['KI'] == a['TE']: return False
  if a['CV'] != None:
    if a['CV'] == a['TE']: return False
  
  # not same semester 1
  if a['M1'] != None and a['EidI'] !=None:
    if a['M1'][:2] == a['EidI'][:2]: return False
  if a['M1'] != None and a['TI'] !=None:
    if a['M1'][:2] == a['TI'][:2]: return False
  if a['M1'] != None and a['EidPmS'] !=None:
    if a['M1'][:2] == a['EidPmS'][:2]: return False
  if a['M1'] != None and a['OOP'] !=None:
    if a['M1'][:2] == a['OOP'][:2]: return False
  if a['EidI'] != None and a['TI'] !=None:
    if a['EidI'][:2] == a['TI'][:2]: return False
  if a['EidI'] != None and a['EidPmS'] !=None:
    if a['EidI'][:2] == a['EidPmS'][:2]: return False
  if a['EidI'] != None and a['OOP'] !=None:
    if a['EidI'][:2] == a['OOP'][:2]: return False
  if a['TI'] != None and a['EidPmS'] !=None:
    if a['TI'][:2] == a['EidPmS'][:2]: return False
  if a['TI'] != None and a['OOP'] !=None:
    if a['TI'][:2] == a['OOP'][:2]: return False
  if a['EidPmS'] != None and a['OOP'] !=None:
    if a['EidPmS'][:2] == a['OOP'][:2]: return False

  
  # not same semester 3
  if a['DB'] != None and a['ES'] !=None:
    if a['DB'][:2] == a['ES'][:2]: return False
  if a['DB'] != None and a['SE'] !=None:
    if a['DB'][:2] == a['SE'][:2]: return False
  if a['DB'] != None and a['SProj'] !=None:
    if a['DB'][:2] == a['SProj'][:2]: return False
  if a['DB'] != None and a['SP'] !=None:
    if a['DB'][:2] == a['SP'][:2]: return False
  if a['ES'] != None and a['SE'] !=None:
    if a['ES'][:2] == a['SE'][:2]: return False
  if a['ES'] != None and a['SProj'] !=None:
    if a['ES'][:2] == a['SProj'][:2]: return False
  if a['ES'] != None and a['SP'] !=None:
    if a['ES'][:2] == a['SP'][:2]: return False
  if a['SE'] != None and a['SProj'] !=None:
    if a['SE'][:2] == a['SProj'][:2]: return False
  if a['SE'] != None and a['SP'] !=None:
    if a['SE'][:2] == a['SP'][:2]: return False
  if a['SProj'] != None and a['SP'] !=None:
    if a['SProj'][:2] == a['SP'][:2]: return False
  
  # not same semester 6
  if a['SuZ'] != None and a['CB'] !=None:
    if a['SuZ'][:2] == a['CB'][:2]: return False
  if a['SuZ'] != None and a['WE'] !=None:
    if a['SuZ'][:2] == a['WE'][:2]: return False
  if a['SuZ'] != None and a['KI'] !=None:
    if a['SuZ'][:2] == a['KI'][:2]: return False
  if a['SuZ'] != None and a['CV'] !=None:
    if a['SuZ'][:2] == a['CV'][:2]: return False
  if a['SuZ'] != None and a['TE'] !=None:
    if a['SuZ'][:2] == a['TE'][:2]: return False
  if a['CB'] != None and a['WE'] !=None:
    if a['CB'][:2] == a['WE'][:2]: return False
  if a['CB'] != None and a['KI'] !=None:
    if a['CB'][:2] == a['KI'][:2]: return False
  if a['CB'] != None and a['CV'] !=None:
    if a['CB'][:2] == a['CV'][:2]: return False
  if a['CB'] != None and a['TE'] !=None:
    if a['CB'][:2] == a['TE'][:2]: return False
  if a['WE'] != None and a['KI'] !=None:
    if a['WE'][:2] == a['KI'][:2]: return False
  if a['WE'] != None and a['CV'] !=None:
    if a['WE'][:2] == a['CV'][:2]: return False
  if a['WE'] != None and a['TE'] !=None:
    if a['WE'][:2] == a['TE'][:2]: return False
  if a['KI'] != None and a['CV'] !=None:
    if a['KI'][:2] == a['CV'][:2]: return False
  if a['KI'] != None and a['TE'] !=None:
    if a['KI'][:2] == a['TE'][:2]: return False
  if a['CV'] != None and a['TE'] !=None:
    if a['CV'][:2] == a['TE'][:2]: return False

  # not same professor
  # george
  if a['M1'] != None and a['EidI'] !=None:
    if a['M1'][:2] == a['EidI'][:2]: return False
  # behrens
  if a['EidI'] != None and a['WE'] !=None:
    if a['EidI'][:2] == a['WE'][:2]: return False
  # rexilius
  if a['OOP'] != None and a['CV'] != None:
    if a['OOP'][:2] == a['CV'][:2]: return False
  # gips
  if a['SP'] != None and a['KI'] != None:
    if a['SP'][:2] == a['KI'][:2]: return False
  if a['SP'] != None and a['CB'] != None:
    if a['SP'][:2] == a['CB'][:2]: return False
  if a['KI'] != None and a['CB'] != None:
    if a['KI'][:2] == a['CB'][:2]: return False

  return True

def ARC_Reduce(A, B, domains):
  change = False 
  for i in domains[A]:
    if not (any(i != j for j in domains[B])):
      domains[A].remove(i)
      change = True
  return change

def AC3(variables, neighbors, domains):
  queue = {(A, B) for A in variables for B in neighbors[A]} 
  while queue:
    (A, B) = queue.pop()
    if ARC_Reduce(A, B, domains):
      if domains[A] == []:
        return domains, False
      for Z in neighbors[A]:
        if Z != A:
          queue.add((Z, A))
  return domains, True 

lecture = 'M1 EidI OOP TI EidPmS DB ES SE SProj SP SuZ CB WE KI CV TE'.split()
variables = lecture

domain = []
# 3 number
for i in range(2):
  # 3 days
  for j in range(2):
    # 3 times
    for k in range(2):
      # 3 rooms
      for l in range(2):
        domain.append((j,k,l))

domains = {} 
assignment = {}
for var in variables:
  assignment[var] = None
  domains[var] = domain
neighbors = {'M1': ['DB', 'ES', 'SE', 'SProj', 'SP', 'SuZ', 'CB', 'WE', 'KI', 'CV', 'TE'], 'EidI': ['DB', 'ES', 'SE', 'SProj', 'SP', 'SuZ', 'CB', 'WE', 'KI', 'CV', 'TE'], 'OOP': ['DB', 'ES', 'SE', 'SProj', 'SP', 'SuZ', 'CB', 'WE', 'KI', 'CV', 'TE'], 'TI': ['DB', 'ES', 'SE', 'SProj', 'SP', 'SuZ', 'CB', 'WE', 'KI', 'CV', 'TE'], 'EidPmS': ['DB', 'ES', 'SE', 'SProj', 'SP', 'SuZ', 'CB', 'WE', 'KI', 'CV', 'TE'], 'DB': ['M1', 'EidI', 'OOP', 'TI', 'EidPmS', 'SuZ', 'CB', 'WE', 'KI', 'CV', 'TE'], 'ES': ['M1', 'EidI', 'OOP', 'TI', 'EidPmS', 'SuZ', 'CB', 'WE', 'KI', 'CV', 'TE'], 'SE': ['M1', 'EidI', 'OOP', 'TI', 'EidPmS', 'SuZ', 'CB', 'WE', 'KI', 'CV', 'TE'], 'SProj': ['M1', 'EidI', 'OOP', 'TI', 'EidPmS', 'SuZ', 'CB', 'WE', 'KI', 'CV', 'TE'], 'SP': ['M1', 'EidI', 'OOP', 'TI', 'EidPmS', 'SuZ', 'CB', 'WE', 'KI', 'CV', 'TE'], 'SuZ': ['M1', 'EidI', 'OOP', 'TI', 'EidPmS', 'DB', 'ES', 'SE', 'SProj', 'SP'], 'CB': ['M1', 'EidI', 'OOP', 'TI', 'EidPmS', 'DB', 'ES', 'SE', 'SProj'], 'WE': ['M1', 'EidI', 'OOP', 'TI', 'EidPmS', 'DB', 'ES', 'SE', 'SProj', 'SP'], 'KI': ['M1', 'EidI', 'OOP', 'TI', 'EidPmS', 'DB', 'ES', 'SE', 'SProj'], 'CV': ['M1', 'EidI', 'OOP', 'TI', 'EidPmS', 'DB', 'ES', 'SE', 'SProj', 'SP'], 'TE': ['M1', 'EidI', 'OOP', 'TI', 'EidPmS', 'DB', 'ES', 'SE', 'SProj', 'SP']} 
new_domains, satisfiable = AC3(variables, neighbors, domains)

print("start")
starttime = time.time()
sol = BT_Search(assignment, domains, timetable_constraints, get_unassigned_var)
endtime = (time.time() - starttime) * 1000
print("BT_Search + Random Var")
print("Solution: \nTime: {0} ms\nDict:\n{1}\n".format(endtime, sol))
print("end\n\n")

# if satisfiable:
#   print("start with AC3")
#   starttime = time.time()
#   sol = BT_Search(assignment, new_domains, timetable_constraints, get_unassigned_var, 8, 17)
#   endtime = (time.time() - starttime) * 1000
#   print("AC3 + BT_Search + Random Var")
#   print("Solution: \nTime: {0} ms\nDict:\n{1}\n".format(endtime, sol))
#   print("end\n\n")

# starttime = time.time()
# sol = BT_Search(assignment, domains, timetable_constraints, mrv)
# endtime = (time.time() - starttime) * 1000
# print("BT_Search + MRV")
# print("Solution: {0}\nZebra: {1}\nWater: {2}\nTime: {3} ms\n\n".format(sol, sol['Zebra'], sol['Water'], endtime))

# starttime = time.time()
# sol = BT_Search(assignment, domains, timetable_constraints, degree_heuristic)
# endtime = (time.time() - starttime) * 1000
# print("BT_Search + Degree Heuristic")
# print("Solution: {0}\nZebra: {1}\nWater: {2}\nTime: {3} ms\n\n".format(sol, sol['Zebra'], sol['Water'], endtime))

# if satisfiable:
#   starttime = time.time()
#   sol = BT_Search(assignment, new_domains, timetable_constraints, get_unassigned_var)
#   endtime = (time.time() - starttime) * 1000
#   print("AC3 + BT Search Random Var")
#   print("Solution: {0}\nZebra: {1}\nWater: {2}\nTime: {3} ms\n\n".format(sol, sol['Zebra'], sol['Water'], endtime))

#   starttime = time.time()
#   sol = BT_Search(assignment, new_domains, timetable_constraints, mrv)
#   endtime = (time.time() - starttime) * 1000
#   print("AC3 + BT Search MRV")
#   print("Solution: {0}\nZebra: {1}\nWater: {2}\nTime: {3} ms\n\n".format(sol, sol['Zebra'], sol['Water'], endtime))

#   starttime = time.time()
#   sol = BT_Search(assignment, new_domains, timetable_constraints, degree_heuristic)
#   endtime = (time.time() - starttime) * 1000
#   print("AC3 + BT Search Degree Heuristic")
#   print("Solution: {0}\nZebra: {1}\nWater: {2}\nTime: {3} ms\n\n".format(sol, sol['Zebra'], sol['Water'], endtime))
