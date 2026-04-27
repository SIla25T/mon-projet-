from classe_abstraite import Conte

class Characters (Conte):
    def __init__(self, text, id):
        self.text = text
        self.id = id
    def conflit(self):
        """trouve les conflits"""