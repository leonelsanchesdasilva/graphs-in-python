import string


class Edge:
    def __init__(self, first_label: str, second_label: str, distance: int):
        self.first_label = first_label
        self.second_label = second_label
        self.distance = distance

    def __repr__(self) -> str:
        return f'<Edge first_label={self.first_label} second_label={self.second_label} distance={self.distance}>'