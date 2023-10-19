add = lambda x, y: x+y 

result = add(3,5)

print(result)

numbers = [1,2,3,4,5]
squareNumbers=list(map(lambda x: x**2, numbers))
print(squareNumbers)

fahrenheitTemperatures = [212, 32, 100]
celsiusTemperatures = list(map(lambda f:(f-32)*5.0/9.0, fahrenheitTemperatures))
print(celsiusTemperatures)


numbers =[3,1,4,5,7,8,9]
sorttedNumbers = sorted(numbers, reverse = True)
print(sorttedNumbers)

midterm = {'Anlice': 95, 'Bob':88, 'Carol': 92, 'Dave': 30, 'Eve':100}
sortedScores = sorted(midterm.items(), key=lambda item: item[1], reverse = True)
print(sortedScores)

points = [(1,3,10),(2,1,20),(4,2,15)]
sortedPoints = sorted(points, key=lambda x :x[2])
print(sortedPoints)

