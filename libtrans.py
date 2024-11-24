def trans(s: int) -> None:
  print("\033[46m"+"\xA0"*s);
  print("\033[45m"+"\xA0"*s);
  print("\033[47m"+"\xA0"*s);
  print("\033[45m"+"\xA0"*s);
  print("\033[46m"+"\xA0"*s);
  print(end="\033[0m");

