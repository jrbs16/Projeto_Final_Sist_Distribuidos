import Pyro4

def main():
    ns = Pyro4.locateNS()
    uri = ns.lookup("servidor.worker")
    servidor = Pyro4.Proxy(uri)

    numeros = [5, 8, 10, 12]

    print("\n Enviando para o servidor")
    for n in numeros:
        resultado = servidor.fatorial(n)
        print(f"fatorial({n}) = {resultado}")

if __name__ == "__main__":
    main()
