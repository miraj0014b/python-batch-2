def area_volume(length, width, height):
    area = length * width
    volume = length * width * height
    return area, volume

test = area_volume(2,3,4)
print(test)