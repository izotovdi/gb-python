# named_lambda = lambda name: f"Hello, {name}!!!"
#
# print(named_lambda("Jhon"))

print(
    (lambda name: f"Hello {name}!!!")
    ("Jhon")
)

print(
    (lambda x: x ** 2)
    (2)
)

print(
    (lambda *numbers: numbers)
    (1,2,3,)
)