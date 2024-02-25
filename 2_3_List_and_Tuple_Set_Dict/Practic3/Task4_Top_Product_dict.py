top_products = ({'Монитор': ['HUAWEI Display 23.8', 'Xiaomi Mi Desktop Monitor 27', 'Philips 325E1C'],
           'Принтер': ['МФУ HP DeskJet 2710', 'МФУ Pantum M6507'],
         'Клавиатура': ['HIPER Rage', 'Razer Cynosa V2', 'Corsair K55 RGB Pr', 'Lenovo Legion K300', 'Razer Ornata V2']})
print(top_products)

key = input('Какой вид товара хотите добавить:').strip().capitalize()
number = int(input('Сколько товаров этого вида хотите добавить?'))
list_products = list()
for _ in range(number):
    val_products = input(f'Введите название товара {key}:')
    list_products.append(val_products)
print(list_products)
try:
    top_products[key].extend(list_products) # products[key] = products[key] + (list_products)
except (KeyError):
    top_products[key] = list_products
print(top_products)

# if products[key] == None:
#     products[key] = list_products
# else:
#     products[key].extend(list_products)

print('Какой фильтр товара хотите установить? ')
for key in top_products.keys():
    print(f"{key}")

filter_key = input('Сделайте выбор: ').strip().capitalize()
if len(filter_key) > 3:
    filter_key = filter_key[:len(filter_key)-2] # Для отбрасывания окончаний слова (учёта падежей)

for key, product_list in top_products.items():
    if filter_key in key:
        print('Советуем присмотреть топ товары из списка:')
        for el in product_list:
            print(el)
        break
# Если внешний цикл завершился (не прервался), т.е. не нашел критерий по ключу
else:
    print('Сожалею, но мы не смогли подобрать для вас товары по указанному списку')