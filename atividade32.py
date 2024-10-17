# Crie duas funções:
# - calcular_area_base, que recebe o raio de um círculo e retorna sua área.
# - calcular_volume_cilindro, que utiliza a função calcular_area_base para calcular o volume de um cilindro dado o raio e a altura.
def raio_circulo(nm1):
    raio = (raio1**2)*3.14
    return f"{raio}"
     
def volume_cilindro(nm2,nm3):
    volume = raio2**2*h*3.14
    return f"{volume}"

operaçao = int(input("digite o numero corespondente da operaçao "))
if operaçao == 1:
    raio1 = int(input("digite o raio1 "))
    resultado_raio = raio_circulo(raio1)
    print(f"a area do circulo e {resultado_raio} ")
elif operaçao == 2:
    raio2 = int(input("digite o raio2 "))
    h = int(input("digite a altura "))
    resultado_volumer = volume_cilindro(raio2, h)
    print(f"o volume do cilindro e {resultado_volumer} ")
    

