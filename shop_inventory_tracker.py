# shop inventory tracker

available_items = []
finished_items = []

def add_items(item):
  available_items.append(item)
  print(f"{item} added succssfuly")

def mark_finish(item):
  if item in available_items:
    available_items.remove(item)
    print(f"{item} sold successfuly")
    finished_items.append(item)
    print(f"finished items {item}")
  else:
    print(f"i{item} not available in the shop")

def sava_item(item):
  with open("avialable.txt","w") as f:
    for item in available_items:
      f.write(item + "\n")
  
  with open("finish.txt","w+") as f:
    for item in finished_items:
      f.write(item + "\n")

add_items("baby care")
add_items("paw paw")
add_items("vaselline cream")
add_items("caretone lotion")

add_items("visita lotion")
add_items("bio white")
mark_finish("baby care")
mark_finish("paw paw")
mark_finish("vaselline")
print(finished_items)
print(sava_item("paw paw"))

