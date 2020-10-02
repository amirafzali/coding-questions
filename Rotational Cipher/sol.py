def rotationalCipher(input, rotation_factor):
  res = []
  
  for char in input:
    if char.isalpha():
      new_pos = (ord(char.lower())-ord("a")+rotation_factor)%26 +ord('a')
      new_char = chr(new_pos)
      
      if char == char.upper():
        new_char = new_char.upper()
        
      res.append(new_char)
    
    elif char.isnumeric():
      new_pos = (ord(char)-ord('0')+rotation_factor)%10 + ord('0')
      new_char = chr(new_pos)
      res.append(new_char)
      
    else:
      res.append(char)
      
  return "".join(res)