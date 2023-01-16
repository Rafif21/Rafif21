def arithmetic_arranger(problems, results=False):
  op = {
    '+': (lambda r: r[0] + r[1]),
    '-': (lambda r: r[0] - r[1]),
  }
  top = list()
  bot = list()
  lines = list()
  res = list()
  if len(problems) > 5:
    return "Error: Too many problems."
  for problem in problems:
    part = problem.split()
    maxlength = len(max(part, key=len))
    #print(part)
    if not (part[1] in op.keys()):
      return "Error: Operator must be '+' or '-'."
    elif not all(a.isnumeric() for a in part[::2]):
      return "Error: Numbers must only contain digits."
    elif maxlength > 4:
      return "Error: Numbers cannot be more than four digits."
    top.append(part[0].rjust(maxlength + 2))
    bot.append(part[1] + (part[2].rjust(maxlength + 1)))
    line = '-' * (maxlength + 2)
    lines.append(line)
    #print(part[0])
    #print(part[2])
    if results:
      res.append(
        str(op[part[1]]([int(i) for i in part[::2]])).rjust(maxlength + 2))
      arranged_problems = '\n'.join(['    '.join(i) for i in (top, bot, lines, res)])
    else:
      arranged_problems = '\n'.join(['    '.join(i) for i in (top, bot, lines)])

  print(arranged_problems)
  return arranged_problems
print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))
