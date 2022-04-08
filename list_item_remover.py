list_one = 1, 2, 3, 4, 5
list_two = 10, 20, 50, 20
list_three = ['apple', 'banana', 'pear', 'apricot']


def remove_items(list):
  list = list[1 : -1]
  print(list)

remove_items(list_one)
###
def remove_first_and_last(list_to_clean):
  _, *content, _ = list_to_clean
  return content


html = ['<h1>', 'My content', '</h1>']

print(remove_first_and_last(html))

other_content_to_clean = ['', 'My content', 'Something else', '/']

print(remove_first_and_last(other_content_to_clean))
###