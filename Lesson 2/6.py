products = []
list_keys = ("название", "цена", "количество", "ед")
x_elem = 0

while True:
    x_elem += 1
    product_dict = dict()

    for key_name in list_keys:
        tmp_dict = {key_name: input(f"{key_name} >>> ")}
        product_dict.update(tmp_dict)

    tmp_tuple = (
        x_elem,
        product_dict
    )

    products.append(tmp_tuple)

    if int(input("добавить еще товар? 1-да / 0-нет >>>")) == 0:
        break

analytic_dict = dict()

for key_name in list_keys:
    my_list = []

    for item in products:
        my_list.append(item[1].get(key_name))

    tmp_dict = {key_name: my_list}
    analytic_dict.update(tmp_dict)

# Из текста задания по аналитике не понятно выводить элементы через множества
# или через список, поэтому вариант с множествами оставляю закомментированным
# for key_name in list_keys:
#     my_set = set()
#
#     for item in products:
#         my_set.add(item[1].get(key_name))
#
#     tmp_dict = {key_name : my_set}
#     analytic_dict.update(tmp_dict)

print(products)
print(analytic_dict)
