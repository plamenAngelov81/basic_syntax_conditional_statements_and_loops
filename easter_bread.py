budget = float(input())
flour_price = float(input())

egg_pack_price = flour_price * 0.75
milk_price = flour_price + (flour_price + 0.25)
milk_price_per_bread = milk_price / 4

bread_price = egg_pack_price + flour_price + milk_price_per_bread

breads_counter = 0
colored_eggs = 0
while True:
    budget -= bread_price
    if budget <= 0:
        break
    breads_counter += 1
    colored_eggs += 3
    if breads_counter % 3 == 0:
        colored_eggs -= 2

print(f"You made {breads_counter} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")