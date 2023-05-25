quantity_of_decorations = int(input())
days_left_until_christmas = int(input())

ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15
total_cost = 0
spirit_points = 0

if days_left_until_christmas % 10 == 0:
    spirit_points -= 30

for current_day in range(1, days_left_until_christmas + 1):
    if current_day % 11 == 0:
        quantity_of_decorations += 2
    if current_day % 2 == 0:
        total_cost += ornament_set_price * quantity_of_decorations
        spirit_points += 5
    if current_day % 3 == 0:
        total_cost += (tree_skirt_price + tree_garland_price) * quantity_of_decorations
        spirit_points += 13
    if current_day % 5 == 0:
        total_cost += tree_lights_price * quantity_of_decorations
        spirit_points += 17
        if current_day % 3 == 0:
            spirit_points += 30
    if current_day % 10 == 0:
        spirit_points -= 20
        total_cost += tree_skirt_price + tree_garland_price + tree_lights_price

print(f"Total cost: {total_cost}")
print(f"Total spirit: {spirit_points}")