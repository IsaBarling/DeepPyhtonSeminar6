import random

def getMap(x, y):
    mapping = []
    #движения ферзя можно описать формулами:
    #y=c - вертикальная линия передвижения
    #x=c - горизонтальная линия передвижения
    #y=x+b диагональ    
    #b= y - x
    for x1 in range(y):
        mapping.append([x1, y])
        
    for y1 in range(x):
        mapping.append([x, y1])
    
    b = y - x
    
    for x2 in range(0,8):
        for y2 in range(0,8):
            if y2 - x2 == b:
                mapping.append([x2, y2])
                
    return mapping

def Check(maps, pos):
    for i in range(len(maps)):
        for j in range(len(pos)):
            if i==j:#игнорируем карту для данной фигуры
                continue
            if pos[j] in maps[i]:
                print(pos[j], pos[i], maps[i])
                return True
    return False
    
   


pos = []
#генерация рандомных позиций
while len(pos) < 8:
    point = [random.randint(0,7), random.randint(0,7)]
    if point not in pos:
        pos.append(point)
        
#заранее подготовленный вариант расположения 8 ферзей, который вернет False
#pos = [[1, 0], [6, 1], [4,2], [7, 3], [0, 4], [3, 5], [5,6], [2,7]  ]

#maps это массив карт для каждой из фигур, описывающий возможные ходы
maps = []
for p in pos:
    #print(p)
    maps.append(getMap(p[0], p[1]))

print(Check(maps, pos))



                
