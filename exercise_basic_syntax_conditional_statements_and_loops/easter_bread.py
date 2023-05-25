budget = float(input())
price_for_1_kg_flour = float(input())

price_for_a_pack_of_eggs = price_for_1_kg_flour * 0.75
price_for_1_liter_milk = price_for_1_kg_flour + (price_for_1_kg_flour * 0.25)
milk_cost_per_bread = price_for_1_liter_milk / 4
recipe_cost = price_for_a_pack_of_eggs + price_for_1_kg_flour + milk_cost_per_bread

total_sum = 0
current_bread_count = 0
colored_eggs = 0

while True:
    total_sum += recipe_cost
    if budget < total_sum:
        total_sum -= recipe_cost
        break
    current_bread_count += 1
    colored_eggs += 3
    if current_bread_count % 3 == 0:
        colored_eggs -= current_bread_count - 2
    if budget < total_sum:
        total_sum -= recipe_cost
        break

money_left = abs(total_sum - budget)
print(f"You made {current_bread_count} loaves of Easter bread! \
Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")
