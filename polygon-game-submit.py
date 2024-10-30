# Solution to "Polygon game" from Kattis: https://open.kattis.com/submissions/14775606

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
def line_intersection(line1, line2, epsilon=1e-7):
    x1, y1 = line1[0]
    x2, y2 = line1[1]
    x3, y3 = line2[0]
    x4, y4 = line2[1]

    # Calculate the directional vectors for the lines and the determinant (denom)
    dx1, dy1 = x1 - x2, y1 - y2
    dx2, dy2 = x3 - x4, y3 - y4
    denom = dx1 * dy2 - dy1 * dx2

    if abs(denom) < epsilon:
        return None  # Lines are parallel or coincident

    # Calculate determinants to find intersection point
    det1 = x1 * y2 - y1 * x2
    det2 = x3 * y4 - y3 * x4
    Px = (det1 * dx2 - dx1 * det2) / denom
    Py = (det1 * dy2 - dy1 * det2) / denom
    intersection_point = (Px, Py)

    # Helper function to check if a point is on a segment
    def is_point_on_segment(P, A, B, epsilon=1e-7):
        x, y = P
        x1, y1 = A
        x2, y2 = B
        # Collinearity check
        cross_product = (x2 - x1) * (y - y1) - (y2 - y1) * (x - x1)
        if abs(cross_product) > epsilon:
            return False
        # Bound check for being within segment endpoints
        if min(x1, x2) - epsilon <= x <= max(x1, x2) + epsilon and \
           min(y1, y2) - epsilon <= y <= max(y1, y2) + epsilon:
            return True
        return False

    # Verify if the intersection point lies on both segments
    if is_point_on_segment(intersection_point, line1[0], line1[1]) and is_point_on_segment(intersection_point, line2[0], line2[1]):
        return intersection_point
    else:
        return None  # Intersection point is outside the segments


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






