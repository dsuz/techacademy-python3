shipping_cost = 350
price_tax_excluded = int(input('税抜価格を入力してください：'))
price_tax_included = int(price_tax_excluded * 1.08)

if price_tax_included >= 2000:
    print('送料は無料です')
    shipping_cost = 0
else:
    print('送料として', shipping_cost, '円かかります')

total_price = price_tax_included + shipping_cost
print('送料込みの価格は', total_price, '円です。')
