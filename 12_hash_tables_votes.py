voted = {}

def check_voter(name):
  if name in voted:
    print("kick them out")
  else:
    voted[name] = True
    print("let them vote!")

check_voter("tom")
check_voter("mike")
check_voter("mike")