__author__ = 'skebix'

'''Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs
$3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for
60 copies?'''

cover_price = 24.95

discount = 0.4

book_with_discount = cover_price * (1 - discount) #Same as cover_price - cover_price * discount

books_total = book_with_discount * 60

shipping_costs = 3 + 0.75 * 59

wholesale_cost = books_total + shipping_costs

print wholesale_cost