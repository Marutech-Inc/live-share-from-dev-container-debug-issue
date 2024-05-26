# Trigger an error to bring up the debugger

def raise_exception():
  raise Exception("Intentional bug")

def intentional_bug():
  raise_exception()

if __name__ == "__main__":
  intentional_bug()
