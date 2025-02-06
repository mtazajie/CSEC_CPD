def minimum_road_width(n, h, height):
    width = 0
    for i in height:
        if i > h:
            width += 2
        else:
            width += 1
    return width
n, h = map(int, input().split())
height = list(map(int, input().split()))
result = minimum_road_width(n, h, height)
print(result)

