
# Example 1
input_str1 = '''4 2
0 0
1 0
1 1
0 1
0 0 1 1
0.5 0 0.5 1
'''

input_str2 = '''5 4
0 0
1 0
2 1
1 2
0 2
0 0 2 0
2 0 2 2
2 2 0 2
0 2 0 0
'''

input_str3 = '''6 3
0 0
1 0
2 1
2 2
1 3
0 2
0 0 2 2
1 0 1 3
0 2 2 0
'''

input_str4 = '''4 4
0 0
2 0
2 2
0 2
0 0 2 0
2 0 2 2
2 2 0 2
0 2 0 0
'''

input_str5 = '''5 5
0 0
2 0
2 2
1 3
0 2
0 0 2 1
2 1 0 2
0 2 1 0
1 0 2 1
2 1 1 2
'''

input_str6 = '''6 4
0 0
2 0
3 1
2 2
1 2
0 1
0 0 3 1
3 1 2 2
2 2 0 1
0 1 1 2
'''

input_str7 = '''5 6
0 0
2 0
2 2
1 3
0 2
0 0 2 1
2 1 0 2
0 2 1 0
1 0 2 1
2 1 1 2
1 2 0 0
'''

input_str8 = '''7 5
0 0
1 0
2 1
3 0
4 2
3 3
0 2
0 0 2 1
2 1 0 2
0 2 1 0
1 0 3 3
2 1 4 2
'''

input_str9 = '''5 5
0 0
1 0
2 1
1 2
0 2
0.2344324234 0.43324324234 2.1223123 0.32124124324
2.122231247 0.5434352343 2.433457877225 2.23467893423
2.432423543546 2.00005422003 0.0009900122123 2.4667888212
0.99999999001 2.00989002323123 0 0
1 0 1.088008399300002 2.0000099000991111009
'''

input_str10 = '''8 7
0 0
2 0
3 1
4 2
4 4
3 5
1 5
0 4
0 0 2 1
2 1 0 2
0 2 2 4
2 4 0 4
0 4 1 5
1 5 3 5
3 5 4 4
'''

input_str11 = '''6 6
0 1
1 0
3 0
4 1
4 3
0 3
0.5 0.5 3.5 0.5
0.0 1.0 4.0 1.0
0.0 2.0 4.0 2.0
0.0 2.5 4.0 2.5
1.0 0.0 1.0 3.0
3.0 0.0 3.0 3.0
'''


input_str12 = '''7 6
0 0
2 0
3 1
4 2
4 3
2 4
0 3
0 0 4 2
4 1 2 4
4 3 0 3
0 3 2 0
2 0 4 3
4 3 2 4
'''

input_strings = [input_str1, input_str2, input_str3, input_str4, input_str5, input_str6, 
                 input_str7, input_str8, input_str9, input_str10, input_str11, input_str12]


def parse_input(input_str):
    input_lines = input_str.strip().split('\n')
    N, M = map(int, input_lines[0].split())
    polygon = [tuple(map(float, line.split())) for line in input_lines[1:N+1]]
    lines = []
    for line in input_lines[N+1:]:
        line_points = tuple(map(float, line.split()))
        lines.append([(line_points[0], line_points[1]), (line_points[2], line_points[3])])
    return polygon, lines


# Function taken from https://stackoverflow.com/questions/20677795/how-do-i-compute-the-intersection-point-of-two-lines
# and from Bing chat
def line_intersection(line1, line2):
    x1, y1 = line1[0]
    x2, y2 = line1[1]
    x3, y3 = line2[0]
    x4, y4 = line2[1]

    d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if d == 0:
        return None

    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / d
    u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / d

    if not(0 <= t <= 1 and 0 <= u <= 1):
        return None

    x = x1 + t * (x2 - x1)
    y = y1 + t * (y2 - y1)

    return x, y


A = (0,0)
B = (1,1)
C = (0.5,0)
D = (0.5,1)

E = (-3,-3)
F = (3,3)






def divide_polygon_by_line(polygon, line):
    
    points = set()
    modified_polygon = polygon.copy()
    #print("Original polygon:", polygon)
    plen = len(polygon)
    for i in range(plen-1):
        side = polygon[i:i+2]
        #print("Side: " ,side)
        intersect = line_intersection(side, line)
        # TODO: check if line is dividing or not
        if intersect:
            #print("Side: ",side, " and line " ,line)
            if intersect not in modified_polygon:
                index = modified_polygon.index(polygon[i]) + 1
                modified_polygon.insert(index, intersect)
            points.add(intersect)
        
    intersect = line_intersection((polygon[0], polygon[-1]), line)
    if intersect:
       # print("Side: ",side, " and line " ,line)
        if intersect not in modified_polygon:
            modified_polygon.insert(0, intersect)
        points.add(intersect)
    
   # print("polygon:", polygon)
    #print("modified polygon: ", modified_polygon)
    
    points = list(points)
    #print("Points: ", points)
    
    if len(points) > 1:    
        #Construct first polygon
        index1 = modified_polygon.index(points[0])
        index2 = modified_polygon.index(points[1])
        
        if index1 < index2:
            polygon1 = modified_polygon[index1:index2+1]
            polygon2 = modified_polygon[index2:] + modified_polygon[:index1+1]
        else:
            polygon1 = modified_polygon[index1:] + modified_polygon[:index2+1]
            polygon2 = modified_polygon[index2:index1+1]
        
        #print("Polygon1: ", polygon1)
        #print("Polygon2: ", polygon2)
        return polygon1, polygon2
    else:
        return None, None



def divide_polygon_by_lines(polygon, lines):
    
    polsToReturn = [polygon]
    #print(polygon)
    for line in lines:
        polsToDivide = polsToReturn.copy()
        polsToReturn.clear()
        for pol in polsToDivide:
            pol1, pol2 = divide_polygon_by_line(pol, line)
            if pol1 and pol2:
                polsToReturn.append(pol1)
                polsToReturn.append(pol2)
            else:
                polsToReturn.append(pol)
            #print("Nr of pols to return", len(polsToReturn))
            #print("Pol ", pol)
            #print("Line ", line)
            #print("Pol1 ", pol1)
            #print("Pol2 ", pol2)
    return polsToReturn


def polygon_area(vertices):
    n = len(vertices)
    area = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += (x1 * y2 - x2 * y1)
    return abs(area) / 2.0
    




# Find all vertices

def print_largest_area(polygon, lines):
    polygons = divide_polygon_by_lines(polygon, lines)
    areas = []
    #print("polygons: ", polygons)
    for pol in polygons:
        areas.append(polygon_area(pol))
    #print("Areas: ", areas)
    print(max(areas))
 
ex = 0

for input_str in input_strings:
    ex += 1
    #print("Example: ", ex)
    polygon, lines = parse_input(input_str)
    print_largest_area(polygon, lines)







