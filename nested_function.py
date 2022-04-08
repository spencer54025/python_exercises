def greeting(first, last):
  def full_name():
    return f'{first} {last}'

  print(f'hi {full_name()}!')

greeting('spencer', 'van')