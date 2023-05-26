# Trabalho Final

## Objetivo

# Você foi selecionado para desenvolver um sistema para emissão de avisos para o preparo de alimentos em um restaurante. O restaurante está dividido em 4 departamentos:
# - Sanduiches
# - Bebidas
# - Pratos Prontos
# - Sobremesas

# O garçom irá atender os clientes e de acordo com o pedido dos clientes, o sistema irá enviar para os departamentos os alimentos que devem ser preparados. Dessa forma, os pedidos enviados pelos garçons serão enviados para um servidor, que por sua vez, irá distribuir para os serviços que estão em cada departamento.

# Para a realização desse sistema, é necessário utilizar o padrão RPC para comunicação do sistema distribuído. Para o processamento, é necessário usar threads ou multiprocessing

from kafka import KafkaProducer
from kafka import KafkaConsumer
import threading
import time
from food import Sandwich, Drink, ReadyMeal, Dessert


class RestaurantServer:
    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers="localhost:9092")

    def send_order(self, topic, food):
        self.producer.send(topic, str(food).encode("utf-8"))
        self.producer.flush()


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.consumer = KafkaConsumer(
            department_name, bootstrap_servers="localhost:9092"
        )
        self.running = False

    def process_orders(self):
        self.running = True
        while self.running:
            for message in self.consumer:
                food_order = message.value.decode("utf-8")
                print(f"\nPreparing {food_order} in {self.department_name}\n")
                get_ready_time = int(food_order.split(" - ")[1].split(" ")[0])
                time.sleep(get_ready_time)
                print(f"\n{food_order} is ready!\n")

    def start_processing_orders(self):
        thread = threading.Thread(target=self.process_orders)
        thread.start()

    def stop_processing_orders(self):
        self.running = False


def main():
    server = RestaurantServer()
    departments = [
        Department("Sanduiches"),
        Department("Bebidas"),
        Department("Pratos_Prontos"),
        Department("Sobremesas"),
    ]

    for department in departments:
        department.start_processing_orders()

    while True:
        print("\n\n")
        print("------------------------------------")
        print("Selecione um departamento:")
        print("1. Sanduiches")
        print("2. Bebidas")
        print("3. Pratos Prontos")
        print("4. Sobremesas")
        print("------------------------------------")
        choice = int(input("Digite a opção desejada: "))

        if choice < 1 or choice > 4:
            print("Opção inválida. Tente novamente.")
            continue

        department_index = choice - 1
        department = departments[department_index]
        client_name = input("Digite o nome do cliente: ")
        quantity = int(input("Digite a quantidade desejada: "))

        if department_index == 0:
            food = Sandwich(client_name, quantity)
        elif department_index == 1:
            food = Drink(client_name, quantity)
        elif department_index == 2:
            food = ReadyMeal(client_name, quantity)
        else:
            food = Dessert(client_name, quantity)

        server.send_order(department.department_name, food)
        print("Pedido enviado com sucesso!")


if __name__ == "__main__":
    main()
