# Įvedamas dydis bitais. Parašykite programą, kuri tą dydį paverstu kilobaitais, baitais ir bitais.

bit = int(input('Įveskite dydį bitais '))

kByte = bit // 1024 # Bitai paverčiami kilobaitais
bit = bit % 1024 # Iš bitų atimami kilobaitai
byte = bit // 8 # Bitai paverčiami baitais
bit = bit % 8 # Iš bitų atimami baitai


print(f"{kByte} kilobaitai, {byte} baitai ir {bit} bitai") # Atsakymas atspaudinamas