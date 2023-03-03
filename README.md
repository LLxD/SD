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
