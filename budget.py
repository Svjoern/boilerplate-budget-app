class Category:
    #food, clothin, entertainment

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.ledger = []

    def deposit(self, amount, description=""):
        self.balance += amount
        t_obj = {"amount": amount, "description": description}
        self.ledger.append(t_obj)

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.balance -= amount
            t_obj = {"amount": -amount, "description": description}
            self.ledger.append(t_obj)
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, Category):
        if self.withdraw(amount, "Transfer to " + Category.name):
            Category.deposit(amount, "Transfer from " + self.name)
            return True
        else:
            return False

    def check_funds(self, amount):
        if (amount > self.balance):
            return False
        else:
            return True

    def __str__(self):

        header_len = 30
        name = self.name
        name_len = len(name)
        star_len = int((header_len - name_len)/2)
        spacing_len = 0
        total = "Total:"
        total_val = 0

        res = ""
        star = ""
        body = ""

        for i in range(star_len):
            star += "*"
        header = star + name + star + "\n"

        for i in self.ledger:
          description = i["description"][0:23]
          total_val += i["amount"]
          amount = "{:7.2f}".format(i["amount"])
          
          description_len = len(description)
          amount_len = len(amount)
          spacing_len = header_len - description_len - amount_len
          
          body += description

          for i in range(spacing_len):
            body += " "
          body += amount + "\n"

        res = header + body + total + "{:7.2f}".format(total_val)
        return res

def create_spend_chart(categories):
  pass

