class Category:
    #food, clothin, entertainment

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.ledger = []
        self.total_val = 0
        self.spend_val = 0

    def deposit(self, amount, description=""):
        self.balance += amount
        t_obj = {"amount": amount, "description": description}
        self.ledger.append(t_obj)

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.balance -= amount
            t_obj = {"amount": -amount, "description": description}
            self.ledger.append(t_obj)
            self.spend_val += amount
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
        total = "Total: "
        # total_val = 0

        res = ""
        star = ""
        body = ""

        for i in range(star_len):
            star += "*"
        header = star + name + star + "\n"

        for elem in self.ledger:
            description = elem["description"][0:23]
            self.total_val += elem["amount"]
            amount = "{:7.2f}".format(elem["amount"])

            description_len = len(description)
            amount_len = len(amount)
            spacing_len = header_len - description_len - amount_len

            body += description

            for i in range(spacing_len):
                body += " "
            body += amount + "\n"

        res = header + body + total + "{:5.2f}".format(self.total_val)
        return res

def create_spend_chart(categories):
  percentages = []
  header_elem = []
  header_all = []
  elem_header = ""
  bottom = "     "
  body = ""
  body_bot = ""
  header = "Percentage spent by category\n"
  header_100= "100|          "
  header_00 = "  0| o  o  o  \n"
  bar_line  = "    ----------"
  header_nn = ""
  total = 0
  longest = 0

  for elem in categories:
    percentages.append(elem.spend_val)
    total += elem.spend_val
    longest = len(elem.name) if len(elem.name)>longest else longest

  percentages = [float("{:5.2f}".format(p*100/total)) for p in percentages]

  for i in range(100,0,-10):  # 100 to 0 in steps of 10
    header_nn = header_100 if (i==100) else (" "+str(i)+"| ")

    for elem_percentage in percentages:
      header_nn += "o  " if elem_percentage >= i else "   "
      # header_nn += " o" if (elem_percentage >= i-5 and elem_percentage <= i+5) else "  "
    
    body += header_nn + "\n"
  body += header_00
  body += bar_line

  # print("longest", longest)
  for i in range(longest):  # 13 entertainment
    body_bot += "\n"+bottom
    for j in range(len(percentages)):
      if len(categories[j].name) > i:
        # print("j=", j, "i=", i, categories[j].name)
        body_bot += categories[j].name[i] + "  "
      else:
        body_bot += "   "
    # body_bot += "\n"
    # print(body_bot)

  return header + body + body_bot
