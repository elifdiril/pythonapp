#!/bin/python3

alphabet='abcdefghijklmnoprstuwxyz'
key=3
newMessage=''

message=input('Please enter a message: ')

for character in message:
  if character in alphabet:
    position=alphabet.find(character)
    newPosition=(position+key) % 26
    newCharacter=alphabet[newPosition]
    #print(newCharacter)
    newMessage+=newCharacter
  else:
    newMessage+=character
  
print(newMessage)
