from pyplasm import *
pts_pavimento=[[-100,-100],[200,-100],[-100,200],[200,200]]
pts_strada1=[[-100,-75],[200,-75],[-100,-55],[200,-55]]
pts_strada2=[[-100,155],[200,155],[-100,175],[200,175]]
pavimento_=AA(MK)(pts_pavimento)
pavimento__=AA(JOIN)([pavimento_[0:5]])
pavimento=STRUCT(pavimento__)


strada1_=AA(MK)(pts_strada1)
strada1__=AA(JOIN)([strada1_[0:5]])
strada1=STRUCT(strada1__)

strada2_=AA(MK)(pts_strada2)
strada2__=AA(JOIN)([strada2_[0:5]])
strada2=STRUCT(strada2__)

pts_tratteggio=[[0,0],[0,2],[4,0],[4,2]]
tratteggio_=AA(MK)(pts_tratteggio)
tratteggio__=AA(JOIN)([tratteggio_[0:5]])
tratteggio=STRUCT(tratteggio__)

linea_strada=STRUCT([tratteggio, T(1)(5)]*60)

linea1=T([1,2])([-100,-66])(linea_strada)
linea2=T([1,2])([-100,164])(linea_strada)

pts_gradone1=[[0,0],[0,58.5],[110,0],[110,58.5]]
pts_gradone2=[[2.5,2.5],[2.5,56],[107.5,2.5],[107.5,56]]
pts_gradone3=[[5,5],[5,53.5],[105,5],[105,53.5]]
pts_gradone4=[[7.5,7.5],[7.5,51],[102.5,7.5],[102.5,51]]
pts_gradone5=[[10,10],[10,48.5],[100,10],[100,48.5]]
gradone_1=AA(MK)(pts_gradone1)
gradone_2=AA(MK)(pts_gradone2)
gradone_3=AA(MK)(pts_gradone3)
gradone_4=AA(MK)(pts_gradone4)
gradone_5=AA(MK)(pts_gradone5)
gradone__1=AA(JOIN)([gradone_1[0:5]])
gradone__2=AA(JOIN)([gradone_2[0:5]])
gradone__3=AA(JOIN)([gradone_3[0:5]])
gradone__4=AA(JOIN)([gradone_4[0:5]])
gradone__5=AA(JOIN)([gradone_5[0:5]])
gradone1=STRUCT(gradone__1)
gradone2=STRUCT(gradone__2)
gradone3=STRUCT(gradone__3)
gradone4=STRUCT(gradone__4)
gradone5=STRUCT(gradone__5)
gradone2=PROD([gradone2,Q(2)])
gradone3=PROD([gradone3,Q(2)])
gradone4=PROD([gradone4,Q(2)])
gradone5=PROD([gradone5,Q(2)])
gradone2=T(3)(2)(gradone2)
gradone3=T(3)(4)(gradone3)
gradone4=T(3)(6)(gradone4)
gradone5=T(3)(8)(gradone5)
gradone1=PROD([gradone1,Q(2)])
gradoni=STRUCT([gradone1, gradone2, gradone3, gradone4, gradone5])


def disk2D(p):
	u,v = p
	return [v*COS(u), v*SIN(u)]
domain2D = PROD([INTERVALS(2*PI)(8), INTERVALS(1.05)(3)])

colonna=MAP(disk2D)(domain2D)
colonna1=T([1,2])([11.05,11.05])(colonna)
colonna2=T([1,2])([98.95,11.05])(colonna)
colonna3=T([1,2])([11.05,47.45])(colonna)
colonnatoX=STRUCT([colonna1, T(1)(7.35)]*13)
colonnatoX2=STRUCT([colonna3, T(1)(7.35)]*13)
colonnatoY=STRUCT([colonna1, T(2)(7.35)]*6)
colonnatoY2=STRUCT([colonna2, T(2)(7.35)]*6)
colonna_4=T([1,2])([23.05,25.75])(colonna)
colonna_5=T([1,2])([23.05,33.1])(colonna)
colonna_6=T([1,2])([86.95,25.75])(colonna)
colonna_7=T([1,2])([86.95,33.1])(colonna)
colonna4=STRUCT([colonna_4])
colonna5=STRUCT([colonna_5])
colonna6=STRUCT([colonna_6])
colonna7=STRUCT([colonna_7])



colonnato=STRUCT([colonnatoX, colonnatoY, colonnatoX2, colonnatoY2, colonna4, colonna5, colonna6 , 
colonna7])
colonnato=PROD([colonnato,Q(24)])
colonnato=T(3)(10)(colonnato)


pts_plinto=[[0,0],[0,2.1],[2.1,0],[2.1,2.1]]
plinto_=AA(MK)(pts_plinto)
plinto__=AA(JOIN)([plinto_[0:5]])
plinto=STRUCT(plinto__)
plinto1=T([1,2])([10,10])(plinto)
plinto2=T([1,2])([97.9,10])(plinto)
plinto3=T([1,2])([10,46.4])(plinto)
plintoX=STRUCT([plinto1, T(1)(7.35)]*13)
plintoX2=STRUCT([plinto3, T(1)(7.35)]*13)
plintoY=STRUCT([plinto1, T(2)(7.35)]*6)
plintoY2=STRUCT([plinto2, T(2)(7.35)]*6)
plinti=STRUCT([plintoX, plintoY, plintoX2, plintoY2])
plinti=PROD([plinti,Q(1)])
plinti=T(3)(34)(plinti)



pts_murointerno=[[12,9.5],[12,10.5],[78,9.5],[78,10.5]]
murointerno_=AA(MK)(pts_murointerno)
murointerno__=AA(JOIN)([murointerno_[0:5]])
murointerno=STRUCT(murointerno__)
murointerno=PROD([murointerno,Q(25)])
murointerno0=T([1,2])([10,10])(murointerno)
murointerno1=T(2)(18.5)(murointerno0)

pts_murointerno2=[[23,10.5],[24,10.5],[23,29],[24,29]]
murointerno_2=AA(MK)(pts_murointerno2)
murointerno__2=AA(JOIN)([murointerno_2[0:5]])
murointerno2=STRUCT(murointerno__2)
murointerno2=PROD([murointerno2,Q(25)])
murointerno2=T([1,2])([10,10])(murointerno2)
muri_interni=STRUCT([murointerno0, murointerno1, murointerno2])
muri_interni=T(3)(10)(muri_interni)



floor0=(STRUCT([COLOR([0.17, 0.40, 0.22])(pavimento), COLOR([0.98,0.78,0.33])(gradoni),
	COLOR([0.94,0.71,0.2])(colonnato), COLOR([0.29,0.22,0.07])(plinti), 
	COLOR([0.23,0.16,0])(muri_interni), COLOR([0.28, 0.28, 0.28])(strada1), COLOR([0.28, 0.28, 0.28])(strada2), 
	COLOR(WHITE)(linea1), COLOR(WHITE)(linea2)]))




pts_tetto1=[[0,0],[89,0],[0,37.5],[89,37.4]]
tetto1_=AA(MK)(pts_tetto1)
tetto1__=AA(JOIN)([tetto1_[0:5]])
tetto1=STRUCT(tetto1__)
tetto1=PROD([tetto1,Q(4)])
tetto1=T([1,2,3])([11,11,35])(tetto1)
tetto2=T(3)(4)(tetto1)
pts_tetto4=[[0,0],[87,0],[0,35.5],[87,35.5]]
tetto4_=AA(MK)(pts_tetto4)
tetto4__=AA(JOIN)([tetto4_[0:5]])
tetto4=STRUCT(tetto4__)
tetto4=PROD([tetto4,Q(4)])
tetto4=T([1,2,3])([12,12,35])(tetto4)
tetto5=T(3)(4)(tetto4)
tetto1=DIFFERENCE([tetto1,tetto4])
tetto2=DIFFERENCE([tetto2,tetto5])

pts_piramide=[[0,0],[2,0],[0,38.5],[2,38.5],[0,19.25,4],[2,19.25,4]]
piramide_=AA(MK)(pts_piramide)
piramide__=AA(JOIN)([piramide_[0:7]])
piramide=STRUCT(piramide__)
piramide=T([1,2,3])([11,10,43])(piramide)
piramide2=T(1)(88)(piramide)

floor1=(STRUCT([COLOR([0.84,0.56,0.12])(tetto1),COLOR([0.73,0.49,0.11])(tetto2),
	COLOR([0.92,0.8,0.61])(piramide),COLOR([0.92,0.8,0.61])(piramide2)]))

pts_building=[[0,0],[0,30],[20,0],[20,30]]
building_=AA(MK)(pts_building)
building__=AA(JOIN)([building_[0:5]])
building=STRUCT(building__)
building=PROD([building,Q(15)])
building1=T([1,2])([-80,-55])(building)
building2=T([1,2])([160,125])(building)



VIEW(STRUCT([floor0,floor1, COLOR([0.96,0.8,0.25])(building1),COLOR([0.96,0.8,0.25])(building2)]))

