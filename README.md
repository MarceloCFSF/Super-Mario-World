# Super Mario World - Inteligência Artificial

## Enunciado

Este diretório é o resultado de um projeto feito para a matéria de inteligência artificial da UFABC. O objetivo era criar um agente capaz de passar pela fase `Yoshi Island 2` do jogo `Super Mario World`.

## Bibliotecas

Biblioteca| Uso
---|---
[Gym reto](https://openai.com/blog/gym-retro/)| Rodar jogo
[Neat](https://neat-python.readthedocs.io/en/latest/)| Criação e treinamento do agente
[Pickle](https://docs.python.org/3/library/pickle.html)| Salvar e carregar o melhor agente

## Instruções de instalação:

Copie a ROM do jogo para o diretório *site-packages/retro/data/stable/SuperMarioWorldSnes/* com o nome *rom.sfc* (se estiver utilizando o Anaconda, ele deve
estar em *~/anaconda3/lib/python3.6/*)

# Execução

Para treinar a IA execute o arquivo train.py (`python train.py`).

Para usar o melhor agente para jogar o jogo execute o arquivo play.py (`python play.py`)