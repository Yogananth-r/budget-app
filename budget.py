class Category:
  def __init__(self,cat_name):
    self.cat_name=cat_name
    self.ledger=[]

  def __str__(self):
    title=f"{self.cat_name:*^30}\n"
    items=""
    tot=0
    for it in self.ledger:
      items+=f"{it['description'][0:23]:23}" + f"{it['amount']:>7.2f}"+'\n'

      tot+=it['amount']
    output=title+items+"Total: "+str(tot)
    return output
  
  def deposit(self,amount,description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self,amount,description=""): 
    if(self.check_funds(amount)):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    return False

  def get_balance(self):
    cash_available=0
    for each_cat in self.ledger:
      cash_available+=each_cat["amount"]
    return cash_available

  def transfer(self,amount,dest_category):
    if(self.check_funds(amount)):
      self.withdraw(amount,"Transfer to "+dest_category.cat_name)
      dest_category.deposit(amount,"Transfer from "+self.cat_name)
      return True
    return False

  def check_funds(self,amount):
    if(self.get_balance()>=amount):
      return True
    return False

  
  def cat_withdrawals(self):
    total=0
    for each_item in self.ledger:
      if each_item["amount"]<0:
        total+=each_item["amount"]
    return total

        
def truncate(n):
  mult=10
  return int(n*mult)/mult

def getoverral(categories):
  total=0
  splitup=[]
  for cat in categories:
    total+=cat.cat_withdrawals()
    splitup.append(cat.cat_withdrawals())
  roundoff=list(map(lambda x: truncate(x/total),splitup))
  return roundoff

  
def create_spend_chart(categories):
  title="Percentage spent by category\n"
  i=100
  overrall=getoverral(categories)
  while i>=0:
    cat_space=" "
    for total in overrall:
      if total*100>=i:
        cat_space+="o  "
      else:
        cat_space+="   "
    title+=str(i).rjust(3)+"|"+cat_space+"\n"
    i-=10

  dash="-"+"---"* len(categories)
  names=[]
  x=""
  for category in categories:
    names.append(category.cat_name)
  maxm=max(names,key = len)
  for y in range(len(maxm)):
    namestr="     "
    for name in names:
      if y>=len(name):
        namestr+="   "
      else:
        namestr+=name[y]+"  "
    if(y!=len(maxm)-1):
      namestr+="\n"

    x+=namestr
  
  title+=dash.rjust(len(dash)+4)+"\n"+x
  return title
        
  