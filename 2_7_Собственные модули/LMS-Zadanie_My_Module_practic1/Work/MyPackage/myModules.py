def area_trapezoid(a, b, h):
   s =  (a + b) / 2 * h
   print(f'Площадь трапеции со сторонами {a},{b} и высотой {h} будет = {s}')
   return s

if __name__ == 'main':
   area_trapezoid(10, 16, 12)
