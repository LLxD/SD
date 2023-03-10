Documentação para a disciplina de Sistemas Distribuídos da Universidade Federal de Uberlândia (UFU).

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