def lgbt(s: int) -> None:
  print("\033[41m"+"\xA0"*s);
  print("\033[48;2;255;165;0m"+"\xA0"*s);
  print("\033[43m"+"\xA0"*s);
  print("\033[42m"+"\xA0"*s);
  print("\033[44m"+"\xA0"*s);
  print("\033[45m"+"\xA0"*s);
  print(end="\033[0m");

