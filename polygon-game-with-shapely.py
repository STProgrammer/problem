from shapely.geometry import LineString, Polygon, MultiPolygon
from shapely.ops import split

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


# Convert input string to polygon and lines
def parse_input(input_str):
    input_lines = input_str.strip().split('\n')
    N, M = map(int, input_lines[0].split())
    polygon_points = [tuple(map(float, line.split())) for line in input_lines[1:N+1]]
    polygon = Polygon(polygon_points)
    lines = []
    for line in input_lines[N+1:]:
        line_points = tuple(map(float, line.split()))
        lines.append(LineString([(line_points[0], line_points[1]), (line_points[2], line_points[3])]))
    return polygon, lines



def divide_polygon_by_lines(polygon, lines):
    #print("Original polygon:", polygon)
    polsToReturn = [polygon]
    for line in lines:
        polsToDivide = polsToReturn.copy()
        polsToReturn.clear()
        for pol in polsToDivide:
            intersection = split(pol, line)
            #print("Pol ", pol)
            #print("Line ", line)
            if not intersection.is_empty:
                for geom in intersection.geoms:
                    polsToReturn.append(geom)
            else:
                polsToReturn.append(pol)
            #print("Nr of pols to return", len(polsToReturn))
            #print("Pols to return", polsToReturn)
    
    return polsToReturn



def print_largest_area(polygon, lines):
    polygons = divide_polygon_by_lines(polygon, lines)
    areas = []
    #print("polygons: ", polygons)
    for pol in polygons:
        areas.append(pol.area)
    #print("Areas: ", areas)
    print(max(areas))


# Example 1
polygon1, lines1 = parse_input(input_str1)




ex = 0


for input_str in input_strings:  
    ex += 1
    polygon, lines = parse_input(input_str)
    print_largest_area(polygon, lines)



