class Invoice:
  def __init__(self, client, total):
    self.client = client
    self.total = total
    
  def __str__(self):
    return f'invoice from {self.client} for {self.total}'

  def __repr__(self):
    return f'invoice < value: client: {self.client}, total: {self.total}>'

inv = Invoice('google', 500)
print(str(inv))
print(repr(inv))
