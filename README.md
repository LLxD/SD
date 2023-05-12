Documentação para a disciplina de Sistemas Distribuídos da Universidade Federal de Uberlândia (UFU).

- [Tipos de sistemas distribuídos](#tipos-de-sistemas-distribuídos)
- [Características de sistemas distribuídos](#características-de-sistemas-distribuídos)
- [Clusters](#clusters)
  - [Componentes de um cluster](#componentes-de-um-cluster)
  - [Grid Computing](#grid-computing)
- [Comunicação](#comunicação)
  - [Redes](#redes)
    - [Topologias](#topologias)
  - [OSI (Open System Interconnection)](#osi-open-system-interconnection)
    - [Camada 7 - Aplicação](#camada-7---aplicação)
    - [Camada 6 - Apresentação](#camada-6---apresentação)
    - [Camada 5 - Sessão](#camada-5---sessão)
    - [Camada 4 - Transporte](#camada-4---transporte)
    - [Camada 3 - Rede](#camada-3---rede)
    - [Camada 2 - Enlace](#camada-2---enlace)
    - [Camada 1 - Física](#camada-1---física)
- [Websockets](#websockets)
  - [Comparação entre HTTP e WebSocket](#comparação-entre-http-e-websocket)
  - [Co-rotinas](#co-rotinas)
  - [Exemplo em Python](#exemplo-em-python)
  - [RPC](#rpc)
    - [Proto](#proto)
- [Modelos computacionais](#modelos-computacionais)
  - [Comunicação](#comunicação-1)
  - [Processos - Definição](#processos---definição)
  - [Recursos computacionais](#recursos-computacionais)
  - [Threads](#threads)
  - [Multithreading](#multithreading)
  - [Multiprocessing](#multiprocessing)
- [Mensageria com Kafka](#mensageria-com-kafka)
  - [Quando usar e não usar](#quando-usar-e-não-usar)
  - [Arquitetura](#arquitetura)
  - [Exemplo em Python](#exemplo-em-python-1)

## Tipos de sistemas distribuídos

- Sistemas de Computação Distribuída de Alto Desempenho (HPC)
  Sistemas utilizados para computação científica e engenharia, tarefas de alto desempenho, como simulações de física, processamento de imagens, etc.

- Sistemas de Informação Distribuída
  Sistemas utilizados para armazenamento e processamento de dados, como bancos de dados, sistemas de arquivos, etc. Se faz necessário a interoperabilidade entre redes.

- Sistemas Embarcados Distribuídos
  Sistemas utilizados para controle de dispositivos, como robôs, automóveis, etc. Normalmente de pequeno porte e baixo consumo de energia.

## Características de sistemas distribuídos

- Possibilidade de agregar poder de processamento de vários computadores para resolver um problema. Normalmente, via rede de computadores com alta largura de banda.
- São usados para programação paralela, onde o processamento é dividido em tarefas que são executadas simultaneamente.

## Clusters

- Um cluster é um conjunto de computadores interligados por uma rede de alta velocidade, que trabalham em conjunto para resolver um problema.
- Dedicados a tarefas específicas, como computação científica, processamento de imagens, etc.

![Cluster](https://bugbusters.com.br/wp-content/uploads/2018/05/cluster_.jpg)

- Conjunto de nós controlados por um sistema operacional distribuído, que permite a comunicação entre os nós. São acessados por um nó mestre, que é responsável por gerenciar os demais nós. O mestre é responsável por executar um middleware, que é um software que permite a comunicação entre os nós, execução de tarefas, gerenciamento de recursos, etc.

### Componentes de um cluster

- Administração
  Responsável por gerenciar os nós do cluster, como adicionar, remover, etc. Também é responsável por gerenciar os recursos do cluster, como memória, disco, etc.

- Computação
  Responsável por executar as tarefas do cluster, como processamento de dados, etc.

- Armazenamento
    Responsável por armazenar os dados do cluster, como arquivos, etc.

### Grid Computing

- É um tipo de computação distribuída, onde os recursos computacionais são compartilhados entre usuários, que podem acessar os recursos de forma remota. Os recursos são distribuídos em vários computadores, que podem estar em diferentes locais geográficos. São fracamente acoplados, ou seja, não há dependência entre os recursos.

## Comunicação

- É a troca de informações entre dois ou mais processos, que podem estar em diferentes computadores. A comunicação pode ser síncrona ou assíncrona.

### Redes

#### Topologias
 - Ponto a ponto
 - Barramento Compartilhado
 - Token Ring

### OSI (Open System Interconnection)

- Modelo de referência para comunicação entre sistemas de computadores. Foi desenvolvido pela ISO (International Organization for Standardization) e é composto por 7 camadas.

#### Camada 7 - Aplicação

- É a camada mais alta do modelo OSI. É responsável por fornecer serviços para as aplicações, como acesso a arquivos, acesso a banco de dados, etc.

#### Camada 6 - Apresentação

- É responsável por converter os dados de uma aplicação para um formato que possa ser entendido por outra aplicação. Por exemplo, converter um arquivo de texto para um arquivo binário.

#### Camada 5 - Sessão

- É responsável por estabelecer, gerenciar e terminar uma sessão entre duas aplicações. Também é responsável por sincronizar as mensagens entre as aplicações.

#### Camada 4 - Transporte

- É responsável por estabelecer, gerenciar e terminar uma conexão entre duas aplicações. Também é responsável por sincronizar as mensagens entre as aplicações.

#### Camada 3 - Rede

- É responsável por estabelecer, gerenciar e terminar uma conexão entre dois hosts. Também é responsável por rotear os pacotes entre os hosts.

#### Camada 2 - Enlace

- É responsável por estabelecer, gerenciar e terminar uma conexão entre dois dispositivos de rede. Também é responsável por sincronizar os bits entre os dispositivos.

#### Camada 1 - Física

- É responsável por transmitir os bits entre os dispositivos de rede.

## Websockets

- É um protocolo de comunicação que permite a comunicação bidirecional entre um cliente e um servidor. É baseado em TCP, que é um protocolo de comunicação orientado a conexão. O protocolo WebSocket foi desenvolvido para substituir o protocolo HTTP, que é um protocolo de comunicação não orientado a conexão.

### Comparação entre HTTP e WebSocket

| HTTP | WebSocket |
| --- | --- |
| Comunicação unidirecional | Comunicação bidirecional |
| Comunicação síncrona | Comunicação assíncrona |
| Comunicação baseada em requisição e resposta | Comunicação baseada em eventos |

### Co-rotinas

- São funções que podem ser pausadas e retomadas a qualquer momento. São utilizadas para programação assíncrona.

### Exemplo em Python

Servidor:

  ```python
  import asyncio
  import websockets

  async def hello(websocket, path):
      name = await websocket.recv()
      print(f"< {name}")

      greeting = f"Hello {name}!"

      await websocket.send(greeting)
      print(f"> {greeting}")

  start_server = websockets.serve(hello, "localhost", 8765)

  asyncio.get_event_loop().run_until_complete(start_server)

  asyncio.get_event_loop().run_forever()
  ```

Cliente:

  ```python
  import asyncio
  import websockets

  async def hello():
      uri = "ws://localhost:8765"
      async with websockets.connect(uri) as websocket:
          name = input("What's your name? ")

          await websocket.send(name)
          print(f"> {name}")

          greeting = await websocket.recv()
          print(f"< {greeting}")

  asyncio.get_event_loop().run_until_complete(hello())
  ```

### RPC

- É um protocolo de comunicação que permite a comunicação entre processos em diferentes máquinas. É baseado em requisições e respostas. O cliente envia uma requisição para o servidor, que executa a tarefa e retorna uma resposta para o cliente.

- Abre a possibilidade de executar tarefas em diferentes máquinas, de forma transparente para o cliente.

#### Proto

- É um framework RPC para Python. É baseado em protocol buffers, que é um formato de serialização de dados. O Proto é baseado em co-rotinas, que permite a comunicação assíncrona.


## Modelos computacionais

### Comunicação

- É a troca de informações entre dois ou mais processos, que podem estar em diferentes computadores. A comunicação pode ser síncrona ou assíncrona.
- Os SDs têm a disposição processadores que permitem o desenvolvimento de aplicações paralelas
- Multiprocessamento é importante para o desenvolvimento de aplicações paralelas
- A Memória Compartilhada Distribuída (MCD) é um recurso importante para o desenvolvimento de aplicações paralelas
![MCD](https://media.geeksforgeeks.org/wp-content/uploads/20210903190914/Screenshot767-660x394.png)

### Processos - Definição

- O conceito de processo é definido como um programa de execução
- Concorrência x Paralelismo
  - Concorrência: vários processos são executados simultaneamente, mas não necessariamente em paralelo
    - Mais de um processo pode ser executado no mesmo núcleo de processamento.
  - Paralelismo: vários processos são executados simultaneamente e em paralelo
    - É necessário que os processos sejam executados em diferentes núcleos de processamento
![Concorrência x Paralelismo](https://jrblog.com.br/wp-content/uploads/2022/06/Concorrencia_Paralalismo.jpg)

- Classificação dos processos
  - CPU Bound x I/O Bound
    - CPU Bound: processos que utilizam mais a CPU para executar suas tarefas
    - I/O Bound: processos que utilizam mais a entrada e saída para executar suas tarefas


### Recursos computacionais

- Threads
- Multithreading
- Multiprocessing


### Threads

- Threads são processos leves, que são executados dentro de um processo

### Multithreading

- É a execução de múltiplas threads em um mesmo processo
  - Vantagens
    - Melhor utilização da CPU
    - Melhor utilização da memória
    - Melhor utilização dos recursos computacionais

### Multiprocessing

- É a execução de múltiplos processos em um mesmo computador
  - Vantagens
    - Realizar tarefas em um período de tempo menor
    - Velocidade alta de processamento
    - Se um processo falhar, os outros processos continuam funcionando

## Mensageria com Kafka

- Kafka é uma plataforma de streaming de dados distribuída, que permite a publicação e assinatura de mensagens. É baseado em tópicos, que são fluxos de dados. Os tópicos são divididos em partições, que são os fluxos de dados. As partições são divididas em segmentos, que são os dados. Os segmentos são divididos em mensagens, que são os dados. As mensagens são divididas em registros, que são os dados.

### Quando usar e não usar

- Usar
  - Quando a aplicação precisa de um sistema de mensageria
  - Quando a aplicação precisa de um sistema de streaming de dados
  - Quando a aplicação precisa de um sistema de processamento de dados em tempo real
  - Quando a aplicação precisa de um sistema de processamento de dados em lote
  - Quando a aplicação precisa de um sistema de processamento de dados em tempo real e em lote

- Não usar
  - Quando a aplicação não precisa de um sistema de mensageria
  - Quando a aplicação não precisa de um sistema de streaming de dados
  - Quando a aplicação não precisa de um sistema de processamento de dados em tempo real
  - Quando a aplicação não precisa de um sistema de processamento de dados em lote
  - Quando a aplicação não precisa de um sistema de processamento de dados em tempo real e em lote

### Arquitetura

- Kafka é baseado em tópicos, que são fluxos de dados. Os tópicos são divididos em partições, que são os fluxos de dados. As partições são divididas em segmentos, que são os dados. Os segmentos são divididos em mensagens, que são os dados. As mensagens são divididas em registros, que são os dados.

![Arquitetura](https://i0.wp.com/www.cienciaedados.com/wp-content/uploads/2016/04/Apache-Kafka.jpg?resize=638%2C479&ssl=1)

### Exemplo em Python

```python
from kafka import KafkaProducer
from kafka import KafkaConsumer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('meu-topico', b'Hello, World!')

consumer = KafkaConsumer('meu-topico', bootstrap_servers='localhost:9092')
for msg in consumer:
    print (msg)
```

