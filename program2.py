def decode_message( s: str, p: str) -> bool:
  
  i = 0
  j = 0

  while i < len(message) and j < len(key):
    if key[j] == '*':
      # Skip any characters in the message until the next character in the key
      while i < len(message) and j < len(key) and key[j] == '*':
        i += 1
      j += 1
    elif key[j] == '?':
      # Skip a single character in the message
      i += 1
      j += 1
    elif message[i] == key[j]:
      i += 1
      j += 1
    else:
      return False

  
  return i == len(message) and j == len(key)
  message1 = "aa"
  key1 = "a"
  print(secret_decoder_ring(message1, key1))  
  message2 = "aa"
  key2 = "*"
  print(secret_decoder_ring(message2, key2))  

  message3 = "cb"
  key3 = "?a"
  print(secret_decoder_ring(message3, key3))  
  return False
