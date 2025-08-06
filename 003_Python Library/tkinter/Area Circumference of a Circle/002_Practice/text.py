import math

def calculate_circle_area_and_circumference(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

# 输入半径
radius = float(input("请输入圆的半径: "))

# 计算并输出结果
area, circumference = calculate_circle_area_and_circumference(radius)
print(f"圆的面积: {area:.2f}")
print(f"圆的周长: {circumference:.2f}")
