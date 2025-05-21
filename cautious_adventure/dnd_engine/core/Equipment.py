class Equipment:
    def __init__(self, name, weight=0, properties=None):
        self.name = name
        self.weight = weight
        self.properties = properties if properties else []
        
    def __repr__(self) -> str:
        return f"<Equipment: {self.name}>"
    
    class Armor:
        pass