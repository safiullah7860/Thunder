import re
import math
rows = []
NonCornerThrees = {'Team A': {'Attempts':0, 'Makes':0} , 'Team B': {'Attempts':0, 'Makes':0}}
CornerThrees = {'Team A': {'Attempts':0, 'Makes':0} , 'Team B': {'Attempts':0, 'Makes':0}}
TwoPoints = {'Team A': {'Attempts':0, 'Makes':0} , 'Team B': {'Attempts':0, 'Makes':0}}
with open('shots_data.csv') as f:
    totalAttempts = 0
    next(f)  #skip headers
    for line in f:
        totalAttempts+=1
        line = line.strip()
        line = line.split(',')
        rows.append(line)
        def calculateDistance(x1,y1):
            dist = math.sqrt((x1 - 0)**2 + (y1 - 0)**2)
            return dist
        def zone(team,x,y,bool):
            if (x>22 or x<-22) and y<=7.8: #if it's a corner three
                if bool== 1:
                    CornerThrees[team]['Makes']+=1
                CornerThrees[team]['Attempts']+=1
            elif (calculateDistance(x, y)>23.75 and y>7.8):  #if it's a noncorner three
                if bool== 1:
                    NonCornerThrees[team]['Makes']+=1
                NonCornerThrees[team]['Attempts']+=1
            else:  #if it's a two pointer
                if bool== 1:
                    TwoPoints[team]['Makes']+=1
                TwoPoints[team]['Attempts']+=1
        one = float(line[1])
        two = float(line[2])
        zone(line[0], float(line[1]), float(line[2]), float(line[3]))
teamATA=CornerThrees['Team A']['Attempts'] + NonCornerThrees['Team A']['Attempts'] + TwoPoints['Team A']['Attempts']
teamBTA=CornerThrees['Team B']['Attempts'] + NonCornerThrees['Team B']['Attempts'] + TwoPoints['Team B']['Attempts']
print('Corner 3(C3):')
print('    Shot Distribution:')
teamA = "{:.2%}".format(CornerThrees['Team A']['Attempts']/teamATA)
teamB = "{:.2%}".format(CornerThrees['Team B']['Attempts']/teamBTA)
print(f'        The shot distribution of Team A is {teamA}')
print(f'        The shot distribution of Team B is {teamB}')
print('    eFG%:')
teamA = "{:.2%}".format((1.5*(CornerThrees['Team A']['Makes'] ) )/ CornerThrees['Team A']['Attempts'])
teamB = "{:.2%}".format((1.5*(CornerThrees['Team B']['Makes'] ))/ CornerThrees['Team B']['Attempts'])
print(f'        The eFG% of Team A is {teamA}')
print(f'        The eFG% of Team B is {teamB}')

print('Non Corner 3(NC3):')
print('    Shot Distribution:')
teamA = "{:.2%}".format(NonCornerThrees['Team A']['Attempts']/teamATA)
teamB = "{:.2%}".format(NonCornerThrees['Team B']['Attempts']/teamBTA)
print(f'        The shot distribution of Team A is {teamA}')
print(f'        The shot distribution of Team B is {teamB}')
print('    eFG%:')
teamA = "{:.2%}".format((1.5*(NonCornerThrees['Team A']['Makes'] ) )/ NonCornerThrees['Team A']['Attempts'])
teamB = "{:.2%}".format((1.5*(NonCornerThrees['Team B']['Makes'] ))/ NonCornerThrees['Team B']['Attempts'])
print(f'        The eFG% of Team A is {teamA}')
print(f'        The eFG% of Team B is {teamB}')

print('Two Point(2PT):')
print('    Shot Distribution:')
teamA = "{:.2%}".format(TwoPoints['Team A']['Attempts']/teamATA)
teamB = "{:.2%}".format(TwoPoints['Team B']['Attempts']/teamBTA)
print(f'        The shot distribution of Team A is {teamA}')
print(f'        The shot distribution of Team B is {teamB}')
print('    eFG%:')
teamA = "{:.2%}".format((TwoPoints['Team A']['Makes']  )/ TwoPoints['Team A']['Attempts'])
teamB = "{:.2%}".format((TwoPoints['Team B']['Makes'] )/ TwoPoints['Team B']['Attempts'])
print(f'        The eFG% of Team A is {teamA}')
print(f'        The eFG% of Team B is {teamB}') #should be the same, since two pointers neq three pointers