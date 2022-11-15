import random

def genetic_algorithm(gene_pool, fitness_fn, state_length, pop_number=10, f_thres=None, maxGen=1000, pmut=0.1, tsize=5, pcross=0.6):
  manting_pool = init_population(pop_number, gene_pool, state_length)
  for i in range(maxGen):
    manting_pool = [mutate(crossover(*selection(2, manting_pool, fitness_fn, tsize), pcross), gene_pool, pmut) for i in range(len(manting_pool))]

    fittest_individual = fitness_threshold(fitness_fn, f_thres, manting_pool) 
    if fittest_individual:
      return fittest_individual, i

  return max(manting_pool, key=fitness_fn), maxGen


def selection(runs, population, fitness_fn, tsize):
  """Do truns (tournament runs) and return new population"""
  return [tournament_selection(population, fitness_fn, tsize) for i in range(runs)]

def tournament_selection(population, fitness_fn, k):
  """Selects k individuals from population and returns the fittest"""
  best = None
  for _ in range(k):
      candidate = random.choice(population)
      if not best or fitness_fn(candidate) > fitness_fn(best):
          best = candidate
  return best

def crossover(x, y, pcross):
  n = len(x)
  #c = random.randrange(0, n)
  c = int(n * pcross)
  return x[:c] + y[c:]

def mutate(x, gene_pool, pmut):
  if random.uniform(0, 1) >= pmut:
      return x
  g = len(gene_pool)
  c = random.randrange(0, len(x))
  m = gene_pool[random.randrange(0, g)]
  return x[:c] + [m] + x[c + 1:]

def init_population(pop_number, gene_pool, state_length):
  """Initializes population for genetic algorithm
  pop_number  :  Number of individuals in population
  gene_pool   :  List of possible values for individuals
  state_length:  The length of each individual"""
  g = len(gene_pool)
  population = []
  for _ in range(pop_number):
      new_individual = [gene_pool[random.randrange(0, g)] for j in range(state_length)]
      population.append(new_individual)

  return population


def fitness_threshold(fitness_fn, f_thres, population):
  if not f_thres:
      return None

  fittest_individual = max(population, key=fitness_fn)
  if fitness_fn(fittest_individual) >= f_thres:
      return fittest_individual

  return None

def fitness_fn(individual):
  fitness_v = 0

  counter = 0
  # fittness_v max=240
  for h in range(len(individual)):
    for i in range(len(individual)):
      if individual[h] != individual[i]:
        if h == i: continue
        fitness_v += 1

  # 1 semester fintess_v max=10
  if individual[0][:4] != individual[1][:4]:
      fitness_v += 1
  if individual[0][:4] != individual[2][:4]:
      fitness_v += 1
  if individual[0][:4] != individual[3][:4]:
      fitness_v += 1
  if individual[0][:4] != individual[4][:4]:
      fitness_v += 1
  if individual[1][:4] != individual[2][:4]:
      fitness_v += 1
  if individual[1][:4] != individual[3][:4]:
      fitness_v += 1
  if individual[1][:4] != individual[4][:4]:
      fitness_v += 1
  if individual[2][:4] != individual[3][:4]:
      fitness_v += 1
  if individual[2][:4] != individual[4][:4]:
      fitness_v += 1
  if individual[3][:4] != individual[4][:4]:
      fitness_v += 1
  
  # 3 semeseter fitness_v max=10
  if individual[5][:4] != individual[6][:4]:
      fitness_v += 1
  if individual[5][:4] != individual[7][:4]:
      fitness_v += 1
  if individual[5][:4] != individual[8][:4]:
      fitness_v += 1
  if individual[5][:4] != individual[9][:4]:
      fitness_v += 1
  if individual[6][:4] != individual[7][:4]:
      fitness_v += 1
  if individual[6][:4] != individual[8][:4]:
      fitness_v += 1
  if individual[6][:4] != individual[9][:4]:
      fitness_v += 1
  if individual[7][:4] != individual[8][:4]:
      fitness_v += 1
  if individual[7][:4] != individual[9][:4]:
      fitness_v += 1
  if individual[8][:4] != individual[9][:4]:
      fitness_v += 1

  # 5 semester fitness_v max=15
  if individual[10][:4] != individual[11][:4]:
      fitness_v += 1
  if individual[10][:4] != individual[12][:4]:
      fitness_v += 1
  if individual[10][:4] != individual[13][:4]:
      fitness_v += 1
  if individual[10][:4] != individual[14][:4]:
      fitness_v += 1
  if individual[10][:4] != individual[15][:4]:
      fitness_v += 1
  if individual[11][:4] != individual[12][:4]:
      fitness_v += 1
  if individual[11][:4] != individual[13][:4]:
      fitness_v += 1
  if individual[11][:4] != individual[14][:4]:
      fitness_v += 1
  if individual[11][:4] != individual[15][:4]:
      fitness_v += 1
  if individual[12][:4] != individual[13][:4]:
      fitness_v += 1
  if individual[12][:4] != individual[14][:4]:
      fitness_v += 1
  if individual[12][:4] != individual[15][:4]:
      fitness_v += 1
  if individual[13][:4] != individual[14][:4]:
      fitness_v += 1
  if individual[13][:4] != individual[15][:4]:
      fitness_v += 1
  if individual[14][:4] != individual[15][:4]:
      fitness_v += 1

  # lectures with same prof, not in same semester
  # fitness_v max=5
  # behrens
  if individual[1][:4] != individual[12][:4]:
    fitness_v += 1
  # rexilius
  if individual[2][:4] != individual[14][:4]:
    fitness_v += 1
  # gips
  if individual[9][:4] != individual[11][:4]:
    fitness_v += 1
  if individual[9][:4] != individual[13][:4]:
    fitness_v += 1
  if individual[11][:4] != individual[13][:4]:
    fitness_v += 1
  
  return fitness_v

  



gene_pool = ["Di10R1", "Di10R2", "Di12R1", "Di12R2", "Di14R1", "Di14R2", "Mi10R1", "Mi10R2", "Mi12R1", "Mi12R2", "Mi14R1", "Mi14R2",
             "Do10R1", "Do10R2", "Do12R1", "Do12R2", "Do14R1", "Do14R2"]
state_length = 16 

runs = 100
successful_solutions = 0
sum_generations_to_solution = 0
f_threshold = 280

for i in range(runs):
  solution, generations_to_solution = genetic_algorithm(gene_pool, fitness_fn, state_length, f_thres=f_threshold)
  fittness = fitness_fn(solution)
  if fittness == f_threshold:
    successful_solutions += 1
    sum_generations_to_solution += generations_to_solution
  print("Solution: {0} Fitness: {1}, GOS: {2}".format(solution, fittness, generations_to_solution))
  
sr = successful_solutions / runs

if sum_generations_to_solution == 0:
  aes = 0
else:
  aes = sum_generations_to_solution / successful_solutions
print("Success rate: {0} Average Evalutaions to Solution: {1}".format(sr, aes))
