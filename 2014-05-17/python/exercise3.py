from larcc import *

def rinumeraCelle(master,hpc):
    hpc = cellNumbering(master,hpc)(range(len(master[1])),CYAN,8)
    VIEW(hpc)
    return hpc

def eliminaCella(master,celleDaEliminare):
    master = master[0],[cell for k,cell in enumerate(CV) if not (k in celleDaEliminare)]
    hpc = SKEL_1(STRUCT(MKPOLS(master)))
    hpc = rinumeraCelle(master, hpc)
    return hpc

def merge(toMerge, diagram, master):
    cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
    master = diagram2cell(diagram,master,toMerge)
    hpc = SKEL_1(STRUCT(MKPOLS(master)))
    hpc = rinumeraCelle(master, hpc)
    return hpc
  