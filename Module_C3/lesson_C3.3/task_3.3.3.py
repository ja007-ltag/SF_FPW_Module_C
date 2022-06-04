# Используя модуль math, найдите значение данного выражения.

import math
res = math.trunc(math.fmod(math.fabs(-10000000), 55) + 0.3)
print(res)
