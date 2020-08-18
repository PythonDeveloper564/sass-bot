

import time
print("TYPE $HALP FOR HELP")
def testloop():
  x = input(">>> ")
  if x == "foo":
    print("bar")
  elif x == "chkchk":
    print("boom")
  elif x == "hi":
    print("yea what u want")
  elif x == "i want food":
    print("no")
  elif x == "i want you":
    print("ew")
  elif x == "i want goods":
    print("come around back")
    time.sleep(2)
    print("What do you want")
  elif x == "you know goods":
    print("911 Whats your emergency, um yes there is someone high over here ")
  elif x == "$HALP":
    print("WHAT YOU WANT:")
    print("i want you")
    print("i want food")
    print("i want goods")
    print("GREETINGS:")
    print("hi")

while True:
  testloop()

    



