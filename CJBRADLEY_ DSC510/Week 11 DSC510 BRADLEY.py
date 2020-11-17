#DSC 510                           # Change Log
#Week 11                          # No changes
#Author Carla J Bradley
#11/15/2020


#This program will allows you select and purchase one or many books and apply 15 percent discount on any book.
# CashRegister class that defines item/book and gets total and count
class CashRegister:
    def __init__(self, book_id, title, quantity, price, total_price, total_count):
        self.book_id = cart_items_id
        self.title = title
        self.quantity = quantity
        self.price = price
        self.total_price = total_price
        self.total_count = total_count

    # class method to add and item/book
    def add_item(self, price):
        global cart_items_id
        if len(cart_items) > 0:
            cart_items_id += 1
        self.quantity += 1
        cart_items.append([cart_items_id, self.title, self.quantity, self.price])
        return cart_items

    # getter method to get the total price
    def get_total(self):
        return self.total_price

    # getter method to get the total count/quantity of items/books
    def get_count(self):
        return self.total_count

    # setter method to set the total by going through the cart item prices
    def set_total(self):
        price = 3
        self.total_price = 0
        for current_price in range(len(cart_items)):
            self.total_price = self.total_price + cart_items[current_price][price]

    # setter method to set the count/quantity by going through the cart item quantities
    def set_count(self):
        quantity = 2
        self.total_count = 0
        for current_qty in range(len(cart_items)):
            self.total_count = self.total_count + cart_items[current_qty][quantity]

    # setter to set the current price to the discounted book price
    def set_disc_price(self, disc_book):
        self.price = disc_book

    # print the receipt with all the cart items in a formatted print out
    def print_receipt(self, list_type):
        self.list_type = list_type
        print(list_type)
        print('Item: {:2} {:4} {:4} {:17} {}'.format(' ', 'ID', 'Qty', 'Title', '   Price'))
        print('{:->43}'.format('-'))
        for rcpt_item in cart_items:
            print('Item: {:4} {:4}    {:17} ${:.2f}'.format(rcpt_item[0], rcpt_item[2], rcpt_item[1], rcpt_item[3]))
        print('\n')

# main program function and menu
def main():
    choice = 0
    print("    Welcome to Sashi's Bookstore")
    while choice != 4:
        # check for menu choice

        choice = input('           '
                       'Select a book\n\
            1. Python for Everybody  \n\
            2. The Grapes of Wrath  \n\
            3. The Catcher In The Rye  \n\n\
            4. Finish shopping and Check Out\n\
            5. Apply Discount\n')

        # Check for errors on input
        try:
            int(choice)
        except:
            # if choice is a string, reset the value to zero
            print('This is a string. Please type in a number.\n')
            choice = 0

        # format the valid choice value as an integer
        choice = int(choice)

        # if choice is string, reset the value to zero
        if choice is str:
            print('This is a string.  Please type in a number.\n')
            choice = 0

        # if choice is greater than the menu options, reset the value to zero
        if choice >=6:
            print('Invalid menu choice.  Please select from the menu choices.\n')
            choice = 0

        # begin processing menu choices
        # choice to add book
        if choice == 1:
            books = CashRegister(cart_items_id, "Python for Everybody", 0, 32.12, total_price, total_count)
            books.add_item(32.12)
            print('Adding:', books.title, '\n')
        # choice to add book
        elif choice == 2:
            books = CashRegister(cart_items_id, " The Grapes of Wrath ", 0, 17.76, total_price, total_count)
            books.add_item(17.76)
            print('Adding:', books.title, '\n')
        # choice to add book
        elif choice == 3:
            books = CashRegister(cart_items_id, "The Catcher In The Rye ", 0, 9.99, total_price, total_count)
            books.add_item(9.99)
            print('Adding:', books.title, '\n')
        # choice to checkout
        elif choice == 4:
            print('See you again soon!\n')

            # print(cart_items) # print a list of the items in the cart
            if len(cart_items) >= 1:

                print ("Thank you for shopping at Sashi's Bookstore")

            # if cart has 1 or more items, then get the total price and total count
            # if len(cart_items) >= 1:
                books.print_receipt("                  Receipt")
                books.set_total()
                books_total_price = books.get_total()
                books.set_count()
                books_total_count = books.get_count()
                print('Your total is: ${:.2f} for {} book(s).'.format(books_total_price, books_total_count))
            else:
                print(" No Items Were Added to The Cart")
            break
        # choice to apply discount
        elif choice == 5:
            question_disc = input('Would you like to apply your discount (y/n) ? ')
            if question_disc == 'y':
                print('Choose the book where to apply the discount?\n')
                books.print_receipt('Cart Items')

                # apply the discount to the book
                bk_id = int(input('Enter the book ID:'))
                for bookitem in cart_items:
                    if int(bookitem[0]) == bk_id:
                        disc_book = bookitem[3]
                        print('Book selected: {}, ${:.2f}'.format(bookitem[1], bookitem[3]))
                        discount = 0.15
                        book_with_disc = bookitem[3] - (bookitem[3] * discount)
                        print('Book discount: ${:.2f}'.format((bookitem[3] * discount)))
                        books.set_disc_price(book_with_disc)
                        bookitem[3] = book_with_disc
                        print('New price: ${:.2f}\n'.format(bookitem[3]))

# start the program
cart_items = []
cart_items_id = 1
counter = 0
total_price = 0
total_count = 0
bk_id = 0

main()
print('\n** Program Complete **')
