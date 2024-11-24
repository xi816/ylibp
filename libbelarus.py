def belarus(s: int) -> None:
  print("\033[41m{ "+"\xA0"*(s-2));
  print("\033[41m }"+"\xA0"*(s-2));
  print("\033[41m{ "+"\xA0"*(s-2));
  print("\033[41m }"+"\xA0"*(s-2));
  print("\033[42m{ "+"\xA0"*(s-2));
  print("\033[42m }"+"\xA0"*(s-2));
  print(end="\033[0m");

