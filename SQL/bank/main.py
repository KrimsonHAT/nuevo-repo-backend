'''
Se busca definir la representación de una cuenta de banco en una Clase... es decir, usando herramientas de Programación orientada a objetos.
La cuenta de banco solo llevará el tracking del balance del usuario: depósitos y retiros (como si se tratara de un cajero )
No nos preocuparemos por mas de un usuario ni mas de una cuenta. ( por el momento )
Entonces el reto en si es:
Definir un menú que simbolice la cuenta de banco con opciones:
[d] Depositar
[r] Retirar
[m] Mostrar Balance
[s] Salir
Y obviamente hacer que funcione :)
ahora creara mas cuentas y se podra transferir de una cuenta a otra
'''
from Db.py import
from sqlite3 import connect
connection = connect("accounts.db")
cursor = connection.cursor()
accounts_list = []

sql_command = """
                CREATE TABLE IF NOT EXISTS accounts(
                  id INTEGER PRIMARY KEY,
                  balance FLOAT,
                  account_number VARCHAR(20)
                );
                """

cursor.execute(sql_command)

def parse_to_float(str_number):
    try:
      return float(str_number)
    except ValueError:
      return print('ups! only numbers are alowed!')

def menu():
  return input(' [d] Deposit \n [r] withdraw \n [s] Show Balance \n [t] Transfer \n [delete] delete_account \n [e] Exit \n')
def get_account_option():
  return input(' [a] Add account \n [v] View or select account \n [e] Exit \n')
def show_accounts():
  print("========Account List======")
  for position, account in enumerate(accounts_list):
    print(f"[{position}]", account)
  print("==========================")

class Account():
  def __init__(self, balance = 0.0, account_number = 'XXX'):
    self.balance = float(balance)
    self.account_number = account_number
    self.id = len(accounts_list)
  def __str__(self):
    return f"{self.account_number} -> ${self.balance}"
  def deposit(self, quantity):
    value = parse_to_float(quantity)
    if value:
      self.balance += value
    return True
  def withdraw(self, quantity):
    value = parse_to_float(quantity)
    if value:
      if value > self.balance:
        return print('Uff there\'s not enough balance! :( get a job!')
      self.balance -= value
      return True
  def show_balance(self):
    print("========================")
    print(f"You have ${self.balance} available in your account")
    print("========================")
  def transfer(self, quantity, receiver_id):
    try:
      receiver_card = accounts_list[receiver_id]
      if(self.withdraw(quantity)):
        receiver_card.deposit(quantity)
    except Exception as error:
      print('ups!, something went wrong maybe the id is incorrect!')
  def remove_this_account(self):
    accounts_list.remove(self)

def get_accounts_from_disk():
  sql_command = 'SELECT * FROM accounts;'
  cursor.execute(sql_command)
  result = cursor.fetchall()

  for register in result:
      (id, balance, account_number) = register
      new_account = Account(balance, account_number)
      accounts_list.append(new_account) 

def save_accounts():
  sql_command = 'DELETE FROM accounts;'
  cursor.execute(sql_command)

  for account in accounts_list:
    sql_command = f'INSERT INTO accounts(id, balance, account_number) VALUES (NULL, "{account.balance}", "{account.account_number}");'
    cursor.execute(sql_command)
    connection.commit()

get_accounts_from_disk()
while True:
  account_option = get_account_option()
  selected_card = None
  if account_option == 'e':
    print('Bye!')
    save_accounts()
    connection.close()
    break
  elif account_option == 'a':
    try:
      account_number = input('account number? ')
      balance = float(input('How much balance ? ') or "0.0")
      new_account = Account(balance, account_number)
      accounts_list.append(new_account)   
      show_accounts()
    except Exception as error:
      print('Eeehm something wrong!', error)
    continue 
  elif account_option == 'v':
    show_accounts()
    try:
      card_id = input("Select id? ")
      if card_id == '':
        continue
      selected_card = accounts_list[int(card_id)]
    except Exception:
      print('ups, this Id is not valid...')
      continue
  else:
    print('Hey that option is not valid :(')
    continue
  while True:
    option = menu()
    if option == 'e':
      print('Bye!')
      break
    elif option == 'delete':
      selected_card.remove_this_account()
    elif option == 'd':
      selected_card.deposit(input('How much? '))
    elif option == 'r':
      selected_card.withdraw(input('How much? '))
    elif option == 's':
      selected_card.show_balance()
    elif option == 't':
      show_accounts()
      receiver_card_id = int(input("what's the id of the receiver? "))
      amount = input('How much? ')
      selected_card.transfer(amount, receiver_card_id)