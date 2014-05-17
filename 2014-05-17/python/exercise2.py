
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
giardino = COLOR(GREEN)(CUBOID([140,100,3 ]))
giardino = T([1,2])([-25,-8])(giardino)
struttura = ( STRUCT([giardino, casa]) )

VIEW(struttura)

duepiano = T(3)(29)(casa)
struttura =STRUCT([struttura,duepiano])
VIEW(struttura)

soffitto = CUBOID([90,95,3 ])

soffitto = COLOR(RED)(T([1,2,3])([-4,-6,58])(soffitto))
struttura = STRUCT([struttura,soffitto])


VIEW(struttura)

pianerottolo = CUBOID([10,10,2])
pianerottolo = COLOR(WHITE)(T([1,2,3])([78,2,29])(pianerottolo))
struttura= STRUCT ([struttura,pianerottolo])


scala =T([1,2])([88,-1])(STRUCT(MKPOLS(spiralStair(2, 8, 5, 1, 25, 2.5, 35))))
struttura = STRUCT([struttura,scala])


VIEW(struttura)
