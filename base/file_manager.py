import json


class FileManager:

    def __init__(self) -> None:
        pass

    def read_file(self, location):

        return json.load(open(location))

    def write_file(self, location, data):

        with open(location, "w") as outfile:
            json.dump(data, outfile, indent=2)


f = FileManager()

print(f.read_file("sample.json"))
