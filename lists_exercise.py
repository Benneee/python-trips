profit_per_day = 1.5

sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]

new_w2_value = 13
sales_w2.append(int(new_w2_value));

# Join the two list together
sales = sales_w1 + sales_w2;

best_day = max(sales);
worst_day = min(sales)

best_day_sales = best_day * profit_per_day;
worst_day_sales = worst_day * profit_per_day;
combined = best_day_sales + worst_day_sales;

print('Best day profit: ', best_day_sales)
print('Worst day profit: ', worst_day_sales)
print('Combined of the best and worst day: ', combined)
