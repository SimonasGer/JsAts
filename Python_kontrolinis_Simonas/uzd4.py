greitisPerValanda = float(input("Koks tarakono greitis kilometrais per valandą "))
keliasCmPerS = greitisPerValanda / 3600 * 100000

print(f"Tarakonas bėga {keliasCmPerS:.2f} centimetrų per sekundę")