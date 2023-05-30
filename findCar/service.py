import networkx as nx
import matplotlib.pyplot as plt
from geopy.distance import geodesic



class Graf:
    G = nx.DiGraph()

    def __init__(self):
        from findCar.models import Cargo, Car
        for i in Car.objects.all():
            self.G.add_node(i.id, pos=(i.current_location.lat, i.current_location.lng), type="car",
                            max_weight=i.carrying_capacity)
        for g in Cargo.objects.all():
            self.createCargo(g)

    def updateGrafCars(self, listCars):
        for i in listCars:
            self.G.add_node(i.id, pos=(i.current_location.lat, i.current_location.lng), type="car",
                            max_weight=i.carrying_capacity)

    def deleteGrafCars(self, listCars):
        for i in listCars:
            self.G.remove_node(i.id)

    def deleteGrafCar(self, car):
        self.G.remove_node(car.id)

    def createCargo(self, cargo):
        self.G.add_node(f"{cargo.id}_start", pos=(cargo.pickup_lat, cargo.pickup_lng),
                        type="cargoStart", weight=cargo.weight)
        self.G.add_node(f"{cargo.id}_finish", pos=(cargo.zipCode.lat, cargo.zipCode.lng),
                        type="cargoFinish", weight=cargo.weight)
        self.G.add_edge(f"{cargo.id}_start", f"{cargo.id}_finish")

    def deleteCargo(self, cargo):
        self.G.remove_edge(f"{cargo.id}_start", f"{cargo.id}_finish")
        self.G.remove_node(f"{cargo.id}_start")
        self.G.remove_node(f"{cargo.id}_finish")

    def getCarsByCargo(self, cargo, radius):
        source_node = f"{cargo.id}_start"
        nearest_nodes = []
        source_position = (cargo.pickup_lat, cargo.pickup_lng)
        for node in self.G.nodes:
            if node == source_node:
                continue
            node_position = self.G.nodes[node]['pos']
            distance_ = geodesic(source_position, node_position).miles
            if distance_ <= radius:
                if self.G.nodes[node].get("max_weight"):
                    if self.G.nodes[node]["max_weight"] >= cargo.weight:
                        nearest_nodes.append((node, distance_))
        return nearest_nodes

    def __call__(self):
        pos = nx.get_node_attributes(self.G, 'pos')
        nx.draw(self.G, pos)
        nx.draw_networkx(self.G, pos, with_labels=True, arrows=True, node_color='lightblue', font_color='black',
                         edge_color='gray')
        plt.show()


graf = Graf()
