import heapq

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target:
            return 0

        max_dist = startFuel
        refuel_stops = 0
        station_index = 0
        num_stations = len(stations)
        fuel_heap = []

        while max_dist < target:
            # Adicione todas as estações que são alcançáveis com o alcance de combustível atual ao heap máximo
            while station_index < num_stations and stations[station_index][0] <= max_dist:
                heapq.heappush(fuel_heap, -stations[station_index][1])
                station_index += 1

            # Se não houver estações que possam ser alcançadas, retorne -1 (impossível alcançar o destino)
            if not fuel_heap:
                return -1

            # Abasteça na estação com o máximo de combustível disponível (o heap máximo armazena valores negativos)
            max_dist -= heapq.heappop(fuel_heap)
            refuel_stops += 1

        return refuel_stops
