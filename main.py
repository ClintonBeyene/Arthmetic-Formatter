def arithmetic_arranger(problems,answer = False):
  arranged_problems = []
  # Too many problems.
  if len(problems) > 5 :
    return("Error: Too many problems.")

  for problem in problems :    
    number1,operator,number2 = problem.split()

    # Operator must be "+" or "-".
    if operator != "+" and operator != "-":
      return("Error: Operator must be '+' or '-'.")

    # Number must only be digits.  
    if not number1.isdigit() or not number2.isdigit():
      return("Error: Numbers must only contain digits.")

    # Too many digits.    
    if len(number1) > 4 or len(number2) > 4:
      return("Error: Numbers cannot be more than four digits.")

    width = max(len(number1),len(number2)) + 2

    # Formating each line.
    line1 = f"{number1.rjust(width)}"
    line2 = f"{operator}{number2.rjust(width-1)}"
    line3 = "-" * width

    # Arranging the problems.
    if answer is False :
      try:
        arranged_problems[0] += (" " * 4)+ line1
      except IndexError:
        arranged_problems.append(line1)
      try:
        arranged_problems[1] += (" " * 4)+ line2
      except IndexError :
        arranged_problems.append(line2)
      try:
        arranged_problems[2] += (" " * 4)+ line3
      except IndexError :
        arranged_problems.append(line3)
    elif answer is True :
      if operator == "+" :
        solution = int(number1) + int(number2)
        solution = str(solution)
      else :
        solution = int(number1) - int(number2)
        solution = str(solution)
      line4 = f"{solution.rjust(width)}"
      try:
        arranged_problems[0] += (" " * 4)+ line1
      except IndexError:
        arranged_problems.append(line1)
      try:
        arranged_problems[1] += (" " * 4)+ line2
      except IndexError :
        arranged_problems.append(line2)
      try:
        arranged_problems[2] += (" " * 4)+ line3
      except IndexError :
        arranged_problems.append(line3)
      try:
        arranged_problems[3] += " " * 4 + line4
      except IndexError :
          arranged_problems.append(line4)
  if answer is False :
    return(f"{arranged_problems[0]}\n{arranged_problems[1]}\n{arranged_problems[2]}")
  else :
    return(f"{arranged_problems[0]}\n{arranged_problems[1]}\n{arranged_problems[2]}\n{arranged_problems[3]}")
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')