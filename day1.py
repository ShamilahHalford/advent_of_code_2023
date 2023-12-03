with open("puzzle_input.txt") as file:
  numbers = []
  for each_line in file:
    word_digit_pairs = [
      ('zero', 'zzeroo'),
      ('one', 'oonee'),
      ('two', 'ttwoo'),
      ('three', 'tthreee'),
      ("four", 'ffourr'),
      ('five', 'ffivee'),
      ('six', 'ssixx'),
      ('seven', 'ssevenn'),
      ('eight', 'eeightt'),
      ('nine', 'nninee')
    ]
    for word, digit in word_digit_pairs:
      each_line=each_line.replace(word, digit)
      print(each_line)

    
    
    word_digit_pairs = [
      ('zero', '0'),
      ('one', '1'),
      ('two', '2'),
      ('three', '3'),
      ("four", '4'),
      ('five', '5'),
      ('six', '6'),
      ('seven', '7'),
      ('eight', '8'),
      ('nine', '9')
    ]
      
    for word, digit in word_digit_pairs:
        each_line=each_line.replace(word, digit)
      
    numbers_eachline=''.join(filter(str.isdigit, each_line))
    lastDigit = numbers_eachline[-1]
    firstDigit = numbers_eachline[0]
    combine=str(firstDigit)+str(lastDigit)
    numbers.append(int(combine))
  print(sum(numbers))
