# Trabalho Final

## Objetivo

Você foi selecionado para desenvolver um sistema para emissão de avisos para o preparo de alimentos em um restaurante. O restaurante está dividido em 4 departamentos:
- Sanduíches
- Bebidas
- Pratos Prontos
- Sobremesas

O garçom irá atender os clientes e de acordo com o pedido dos clientes, o sistema irá enviar para os departamentos os alimentos que devem ser preparados. Dessa forma, os pedidos enviados pelos garçons serão enviados para um servidor, que por sua vez, irá distribuir para os serviços que estão em cada departamento.

Para a realização desse sistema, é necessário utilizar o padrão RPC para comunicação do sistema distribuído. Para o processamento, é necessário usar threads ou multiprocessing

## Classes
Food:
- name: Nome do alimento
- client_name: Nome do cliente
- time_to_be_prepared_in_minutes: Tempo de preparo do alimento em minutos
- quantity: Quantidade de alimentos (utilizada numa multiplicação linear do tempo de preparo)

Sandwich, Beverage, ReadyDish, Dessert:
- herdam de Food
- possuem os tempos de preparo definidos

RestaurantServer:
- Producer
- Recebe os pedidos dos garçons e envia para os departamentos

Department:
- Consumer
- Recebe os pedidos do servidor e prepara os alimentos (dorme por um tempo = tempo de preparo * quantidade)