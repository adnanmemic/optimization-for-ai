# Note: In the homework assignment the variable x, y, z and the function 'f'
# are already predefined

x_temp = 10 * (1 - y - z) / 12
y_temp = 10 * (5 - 5 * z - x) / 60
z_temp = 10 * (5 - 5 * y - x) / 60

fx_temp = f(x_temp, y, z)
fy_temp = f(x, y_temp, z)
fz_temp = f(x, y, z_temp)

if fy_temp < fx_temp and fy_temp < fz_temp:
    y = y_temp
elif fx_temp < fz_temp:
    x = x_temp
else:
    z = z_temp
