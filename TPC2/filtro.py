#!/usr/bin/env python3

from jjcli import *

"""
Repetidas - Remove linhas repetidas num programa. 

Usage: 
    repetidas [options] file*

Options: 
    -s  Preserva espaços no início e fim das linhas 
    -e  Remove linhas vazias 
    -p  Adiciona # as linhas vazias, tornando as comentario 
"""

def remove_linhas_repetidas(cl): 
    linhas_vistas = set()
    
    for linha in cl.input(): 
        ln = linha if "-s" in cl.opt else linha.strip()
        
        if "-e" in cl.opt and not ln:
            continue  

        if ln not in linhas_vistas :
            print(linha, end="\n")  
            linhas_vistas.add(ln)

        elif ln in linhas_vistas and "-p" in cl.opt : 
            print("#" + ln)


def main():
    cl = clfilter(opt="s,e,p", man=__doc__)  
    remove_linhas_repetidas(cl)

if __name__ == '__main__':
    main()
