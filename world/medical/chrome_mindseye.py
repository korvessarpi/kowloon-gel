from typeclasses.items import Item

class ChromeMindseye(Item):
    """
    Mind's Eye Chrome Implant
    Lets the user hear thoughts of those in the same room (not the thoughts channel).
    Empathy cost: -0.25
    """
    def at_object_creation(self):
        self.db.chrome_name = "Mind's Eye"
        self.db.chrome_shortname = "mindseye"
        self.db.chrome_buff = "None"
        self.db.chrome_ability = "Hear thoughts."
        self.db.empathy_cost = -0.25
        self.db.is_chrome = True
        self.db.is_medical_item = True
        self.db.is_physical = True
        self.db.desc = "A small neural implant behind the ear, rumored to let you hear the thoughts of those nearby."
        super().at_object_creation()
