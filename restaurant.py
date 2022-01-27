class Table:
    def __init__(self, diners):
        self.diners = int(diners)
        self.bill = []

    def order(self, foodstuff, price, quantity=1):
        for dictionaries in self.bill:
            if dictionaries.get('item') == foodstuff and dictionaries.get('price') == price:
                dictionaries['quantity'] += quantity
                break
        self.bill.append({'item': foodstuff, 'price': round(float(price), 2), 'quantity': quantity})

    def remove(self, foodstuff, price, quantity=1):
        for dictionaries in self.bill:
            if dictionaries.get('item') == foodstuff and dictionaries.get('price') == price and dictionaries.get('quantity') >= quantity:
                dictionaries['quantity'] -= quantity
                return True
        return False

    def get_subtotal(self):
        subtotal = 0
        for dictionaries in self.bill:
            subtotal += dictionaries.get('price') * dictionaries.get('quantity')
        return float(round(subtotal, 2))

    def get_total(self, service_charge_percent):
        return {'Sub Total': f"£{self.get_subtotal():.2f}", 'Service Charge': f"£{self.get_subtotal() * service_charge_percent:.2f}", 'Total': f"£{self.get_subtotal() * (1+service_charge_percent):.2f}"}

    def split_bill(self):
        return self.get_subtotal()/6
