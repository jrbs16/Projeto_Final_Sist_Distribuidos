import Pyro4
import math

@Pyro4.expose
class Worker:
    def fatorial(self,n):
        print(f"[Servidor] Recebido fatorial({n})")
        return math.factorial(n)
    
def main():
    daemon=Pyro4.Daemon()
    ns=Pyro4.locateNS()
    uri=daemon.register(Worker())
    ns.register("servidor.worker",uri)
    print("Servidor disponível...")
    daemon.requestLoop()

if __name__=="__main__":
    main()