from ArgumentDescription import ArgumentDescription


class NewAlgorithm:
    def __init__(self, name: str, file, args_desc: ArgumentDescription):
        self.name = name
        self.file = file
        self.argsDesc = args_desc
