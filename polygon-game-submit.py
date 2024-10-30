

# Find intersection between two lines
# Function taken from https://stackoverflow.com/questions/20677795/how-do-i-compute-the-intersection-point-of-two-lines
# and from Bing chat
# Convert input string to polygon and lines
def parse_input(input_str):
    input_lines = input_str.strip().split('\n')
    N, M = map(int, input_lines[0].split())
    polygon = [tuple(map(float, line.split())) for line in input_lines[1:N+1]]
    lines = []
    for line in input_lines[N+1:]:
        line_points = tuple(map(float, line.split()))
        lines.append([(line_points[0], line_points[1]), (line_points[2], line_points[3])])
    return polygon, lines


# line intersection
# Taken from https://github.com/RussellDash332/kattis/blob/main/src/Polygon%20Game/polygongame.py
def line_intersection(s1, s2, EPS = 1e-7):
    (p1, p2), (p3, p4) = s1, s2
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = p1, p2, p3, p4
    a, b, c = y2-y1, x1-x2, (y2-y1)*x1 - (x2-x1)*y1
    d, e, f = y4-y3, x3-x4, (y4-y3)*x3 - (x4-x3)*y3
    det = b*d-a*e
    if abs(det) > EPS:
        x, y = (b*f-c*e)/det, (c*d-a*f)/det; return (x, y) if (
            min(x1, x2)-EPS <= x <= max(x1, x2)+EPS and
            min(y1, y2)-EPS <= y <= max(y1, y2)+EPS and
            min(x3, x4)-EPS <= x <= max(x3, x4)+EPS and
            min(y3, y4)-EPS <= y <= max(y3, y4)+EPS and
            abs(a*x+b*y-c) < EPS and
            abs(d*x+e*y-f) < EPS
        ) else None


def divide_polygon_by_line(polygon, line):
    
    points = set()
    modified_polygon = polygon.copy()
    
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
    
    #print("polygon:", polygon)
    #print("modified polygon: ", modified_polygon)
    
    points = list(points)
    
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
    for pol in polygons:
        areas.append(polygon_area(pol))

    print(max(areas))






M, N = tuple(map(int, input().split()))



polygon = []

for i in range(M):
    polygon.append(tuple(map(int, input().split())))

#polygon = [tuple(map(int, line.split())) for line in inpLines[1 : M + 1]]


lines = []

# Extracting the line endpoints
for i in range(N):
    values = list(map(float, input().split()))
    lines.append([(values[0], values[1]), (values[2], values[3])])



print_largest_area(polygon, lines)






