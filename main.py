from margin import Margin
from search import Search
import sys

def main():
    if(len(sys.argv) > 2):
        n_ind = int(sys.argv[1])      #Pega o numero de individuos do terminal
        capacity = int(sys.argv[2])   #Pega a capacidade do barco do terminal
    else:
        n_ind = 3
        capacity = 2

    l_margin = Margin(0, 0, n_ind, n_ind, "MargemEsquerda")
    r_margin = Margin(n_ind, n_ind, n_ind, n_ind, "MargemDireita")
    search = Search(l_margin, r_margin, capacity)
    search.search()

if __name__ == "__main__":
    main()