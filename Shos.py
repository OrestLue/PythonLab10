class Shos:
    shos_amount = 0

    def init(self, name="Vans", size=39, type="Skaters", price=150,
                    color="Black"):
        self.name = name
        self.size = size
        self.type = type
        self.price = price
        self.color = color
        Shos.shos_amount += 1

    @staticmethod
    def get_static_field():
        return Shos.shos_amount

    def del(self):
        print(self.name + " deleted")

    def str(self):
        return str(self.dict)

def main():
    vans = Shos()
    nike = Shos("Nike", 40, "Skarers", 100)
    new_balance = Shos("New Balance", 41, "normal", 80)

    print(vans)
    print(nike)
    print(new_balance)
    print(Shos.shos_amount)

if name == 'main':
    main()