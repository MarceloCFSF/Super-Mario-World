import neat
import pickle
from utils import *

# Carrega o melhor genoma até agora e coloca o valor de seu fitness em BestFitness
try:
  with open('winner.pkl', 'rb') as input_file:
    bestGenome = pickle.load(input_file)
    bestFitness = bestGenome.fitness - 100000
except:
  bestFitness = 0

# Função para evoluir os genomas
def eval_genomes(genomes, config):
  
  # Joga o jogo com vários agentes até um deles terminar 
  # a fase e ser melhor que o agente vencedor anterior
  for genome_id, genome in genomes:
    eval_genome(genome, config, bestFitness)

def train():
  print("Atual Vencedor: ", bestFitness)

  try:
    # Configuração da IA
    config = neat.Config(
      neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, 'config'
    )

    # Configuração da População    
    p = neat.Population(config)  
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(5))

    # Inicia a IA
    winner = p.run(eval_genomes)

    # Salva o agente vencedor do treinamento
    with open("winner.pkl", "wb") as f:
      pickle.dump(winner, f)
      f.close()

    print("Novo Vencedor: ", winner.fitness)

  except KeyboardInterrupt:
    # Caso o usuário pare a execução, por exemplo
    # apertando Ctrl + C
    print("User break")

train()
