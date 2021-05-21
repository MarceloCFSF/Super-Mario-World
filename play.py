import neat
import pickle
from utils import *

# Configuração da IA
config = neat.Config(
  neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation,'config'
)

def play():
  try:
    # Carrega o agente vencedor do treinamento 
    with open('winner.pkl', 'rb') as input_file:
      genome = pickle.load(input_file)

    # Joga o jogo com o melhor agente
    fitness, time, coins, score = eval_genome(genome, config)
    
    # Imprime a pontuação alcançada
    print("Fitness:", fitness)
    print("Time:", time)
    print("Coins:", coins)
    print("Score:", score)
  except FileNotFoundError:
    # O arquivo não existe
    print("Vencedor não encontrado")

play()