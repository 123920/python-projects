# PEAR TO DO LIST PROGRAM
to_do_list = []
print("welcome to pear to do")
choice = "add"

while choice != "stop":

  if choice == "add":
    add_task = input("what task do you want to add? ")
    if add_task in to_do_list:
      print("this task is already in the list")
    else:
      to_do_list.append(add_task)

  elif choice == "remove":
    user_remove = input("ok what task should I remove? ")
    if user_remove in to_do_list:
      to_do_list.remove(user_remove)
      print("task removed!")
    else:
      print("that task is not in the list")

  else:
    print("that is not an action")

  for ind in range(len(to_do_list) ):
    print(str(ind) + ": " + to_do_list[ind])
  choice = input("would you like to add remove or stop? ")
