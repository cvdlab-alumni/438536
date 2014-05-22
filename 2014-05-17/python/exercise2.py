
from larcc import *
DRAW = COMP([VIEW,STRUCT,MKPOLS])

master = assemblyDiagramInit([13,12,2])([[2,13,2,20,1,4,1,10,1,8,2,12,2],[2,10,2,29,1,1,8,1,21,2,8,2],[2,27]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,6)
#VIEW(hpc)

toRemove = [27,29,31,37,39,41,45,75,77,79,83,85,87,89,93,123,125,127,131,133,137,141,143,171,173,175,179,181,185,189,191,
219,221,223,227,229,231,233,237,239,267,271,270,284,295,272,273,274,275,296,297,298,299,276,277,300,301,281,284,285,286,287,
308,309,310,311,140,141,142,143,164,165,166,167,188,189,190,191,212,213,214,215,236,237,238,239,260,261,262,263,61,63,65,69,
99,101,103,107,109,147,149,151,161,195,197,199,243,257,294]
master = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
#DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,6)
#VIEW(hpc)



toRemove = [201]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)


hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,6)
#VIEW(hpc)



toMerge = 48
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([1,5,3])([[2],[3,3.5,1,3.5,3],[1.5,24,1.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,7)
#VIEW(hpc)


toRemove = [212,218]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)


hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,6)
#VIEW(hpc)




toMerge = 25
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([1,1,2])([[13],[2],[13.5,13.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,7)
#VIEW(hpc)

toRemove = [221]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,8)
#VIEW(hpc)

toMerge = 1
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([1,1,2])([[2],[2],[13.5,13.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,7)
#VIEW(hpc)

toRemove = [221]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)


hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,8)
#VIEW(hpc)




toMerge = 2
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([1,1,2])([[2],[10],[13.5,13.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,7)
#VIEW(hpc)

toRemove = [221]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)


hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,8)
#VIEW(hpc)

toMerge = 3
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([1,1,2])([[2],[2],[13.5,13.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,7)
#VIEW(hpc)


toRemove = [221]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)


hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,8)
#VIEW(hpc)

toMerge = 4
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([1,1,2])([[2],[29],[13.5,13.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,7)
#VIEW(hpc)

toRemove = [221]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,8)
#VIEW(hpc)

toRemove = [126,144,142,130,112,114]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,8)
#VIEW(hpc)

toMerge = 17
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([1,1,2])([[2],[8],[13.5,13.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,7)
#VIEW(hpc)

toRemove = [215]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,8)
#VIEW(hpc)



toMerge = 18
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([1,1,2])([[2],[2],[13.5,13.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,7)
#VIEW(hpc)

toRemove = [215]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,8)
#VIEW(hpc)

toMerge = 33
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([1,1,2])([[13],[2],[13.5,13.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,7)
#VIEW(hpc)


toRemove = [215]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,8)
#VIEW(hpc)

toMerge = 51
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([1,1,2])([[2],[2],[13.5,13.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,7)
#VIEW(hpc)


toRemove = [215]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,8)
#VIEW(hpc)



toMerge = 66
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([1,1,2])([[20],[2],[13.5,13.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,7)
#VIEW(hpc)

toRemove = [215]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,8)
#VIEW(hpc)


toMerge = 84
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([1,1,2])([[1],[2],[13.5,13.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,7)
#VIEW(hpc)


toRemove = [215]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,8)
#VIEW(hpc)

toMerge = 82
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([1,1,2])([[1],[8],[13.5,13.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,7)
#VIEW(hpc)

toRemove = [215]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,8)
#VIEW(hpc)

toMerge = 63
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([5,1,3])([[1,3.5,1,3.5,1],[2],[1.5,24,1.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,7)
#VIEW(hpc)

toRemove = [218,224]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,8)
#VIEW(hpc)

toMerge = 121
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([3,1,3])([[.5,3.5,1],[2],[13.5,12,1.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,7)
#VIEW(hpc)

toRemove = [230]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,8)
#VIEW(hpc)


toMerge = 176
cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([hpc,cell]))

diagram = assemblyDiagramInit([3,1,3])([[.5,3.5,2],[2],[13.5,12,1.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,7)
#VIEW(hpc)

toRemove = [237]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,8)
#VIEW(hpc)



###############################################
###################ES2#########################
###############################################


casa= COLOR(WHITE)(STRUCT(MKPOLS(master)))
casa2 = T(1)(170)(S(1)(-1)(casa))  #specchiare casa

giardino = COLOR(GREEN)(CUBOID([220,100,3 ]))
giardino = T([1,2,3])([-25,-8,-3])(giardino)
struttura = ( STRUCT([casa, casa2]) )

VIEW(struttura)

duepiano = T(3)(29)(struttura)
struttura =STRUCT([struttura,duepiano])
VIEW(struttura)



muro_dietro = CUBOID([16,2,58 ])
muro_dietro = COLOR(WHITE)(T([1])([78])(muro_dietro))
struttura = STRUCT([struttura,muro_dietro])

glass = [0.1,0.2,0.47,1,  0,0,0,0.48,  2,2,2,1, 0,0,0,1, 50]

muro_avanti = CUBOID([14,2,29 ])
muro_avanti = MATERIAL(glass)(T([1,2,3])([78,75,29])(muro_avanti)) #VETROOOOOOO
struttura = STRUCT([struttura,muro_avanti])


base = CUBOID([42,77,2])
base = COLOR(WHITE)(T([1])([64])(base))

pianerottolo = CUBOID([14,75,2])
pianerottolo = COLOR(WHITE)(T([1,3])([78,29])(pianerottolo))
struttura= STRUCT ([struttura,pianerottolo,base])
pianerottolo_dx = CUBOID([14,75,2])
pianerottolo_dx = COLOR(WHITE)(T([1,3])([92,29])(pianerottolo_dx))
struttura= STRUCT ([struttura,pianerottolo_dx])
pianerottolo_sx= CUBOID([14,6,2])
pianerottolo_sx = COLOR(WHITE)(T([1,2,3])([64,14,29])(pianerottolo_sx))

ghiera= CUBOID([1,33,10])
ghiera = COLOR(RED)(T([1,2,3])([77,20,28])(ghiera))




scalino= CUBOID([14,1,1])
scalino = COLOR(RED)(T([1,2,3])([64,20,28])(scalino))
scalinata=STRUCT([scalino, T([2,3])([1,-1])]*27)
struttura= STRUCT ([struttura,pianerottolo_dx, scalinata,pianerottolo_sx,ghiera])


VIEW(struttura)


soffitto = CUBOID([180,95,3 ])


soffitto = COLOR(RED)(T([1,2,3])([-4,-6,58])(soffitto))
struttura = STRUCT([struttura,soffitto, giardino])

scala =T([1,2])([88,-1])(STRUCT(MKPOLS(spiralStair(2, 8, 5, 1, 25, 2.5, 35))))
#struttura = STRUCT([struttura,scala])


VIEW(struttura)

