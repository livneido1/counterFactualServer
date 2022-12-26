from BussinessLayer.Engine import Engine


class AlgorithmsController:
    def __init__(self):
        self.algorithms_lst: list = list()
        self.running_engines: list[tuple[str, Engine]] = list()

        raise Exception("Not implemented.")

    def get_algorithm(self, name):
        raise Exception("Not implemented.")

    def get_all_algorithms(self):
        raise Exception("Not implemented.")

    def add_new_algorithm(self):
        raise Exception("Not implemented.")

    def remove_algorithm(self, algorithm):
        raise Exception("Not implemented.")

    def run_all_algorithms(self):
        raise Exception("Not implemented.")

    def load_algorithms(self):
        raise Exception("Not implemented.")

    def edit_algorithm(self, algorithm):
        raise Exception("Not implemented.")
