import sys
sys.path.append(r'/1T-Start/0_REC_Module_2/2_7_Собственные модули')
print(sys.path)

try:
    import my_custom_module
except ImportError:
    print("Не удалось загрузить my_custom_module, используется альтернативный код")



from A_pack.area import area_rectangle
from A_pack.perimetr import perimetr_rectangle
from A_pack.Sub_pack.area_view import area_print
from A_pack.Sub_pack.perimetr_view import perimetr_print


s = area_rectangle(10, 20)
p = perimetr_rectangle(10, 20)
area_print(s)
perimetr_print(p)