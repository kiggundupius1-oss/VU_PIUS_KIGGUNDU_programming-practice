project_name = input("Enter the project name: ")
client_name = input("Enter client name")
cement_price = float(input("Enter the price of cement: "))
cement_quantity = int(input("Enter the quantity of cement bags: "))
sand_price = float(input("Enter the price of sand per trip: "))
sand_trips = float(input("Enter the number of trips for sand: "))
aggregates_price = float(input("Enter the price of aggregates per trip: "))
aggregates_trips = float(input("Enter the number of trips for aggregates: "))
labor_cost = float(input("Enter the labor cost: "))
wastage_percentage = float(input("Enter the wastage percentage: "))
contingency_percentage = float(input("Enter the contingency percentage: "))
profit_percentage = float(input("Enter the profit percentage: "))


total_cement_cost = cement_price * cement_quantity
total_sand_cost = sand_price * sand_trips
total_aggregates_cost = aggregates_price * aggregates_trips
total_material_cost = total_cement_cost + total_sand_cost + total_aggregates_cost
wastage_amount = (wastage_percentage / 100) * total_material_cost
contingency_amount = (contingency_percentage / 100) * total_material_cost
total_project_cost = (
    total_material_cost + labor_cost + wastage_amount + contingency_amount
)
profit_amount = (profit_percentage / 100) * total_project_cost
client_payment = total_project_cost + profit_amount

print("======================================")
print(" PI CONSTRUCTION ")
print("======================================")
print("Project:", project_name)
print()
print("Cement cost:", total_cement_cost)
print("Sand cost:", total_sand_cost)
print("Aggregates cost:", total_aggregates_cost)
print("Labor cost:", labor_cost)
print("Wastage amount:", wastage_amount)
print("Contingency amount:", contingency_amount)
print("--------------------------------------")
print("Total project cost:", total_project_cost)
print("Client payment:", client_payment)
print("Profit amount:", profit_amount)
print("======================================")
