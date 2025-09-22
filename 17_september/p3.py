books = {
    "The conch Bearer" : 3,
    "The Alchemist" : 5,
    "Who I Am" : 2,
    "Elon Musk" : 1,
    "Ikigai" : 7
}

book_title = input("Enter Book Name: ")
if book_title in books:
    if books[book_title] > 0:
        books[book_title] -=1
        print(f"You have successfully borrowed '{book_title}'. ")
else :
    print("Out of stock" or "Not found")

    with open ("library.txt", 'w') as file:
        for title, quantity in books.items():
             file.write(f"{title}: {quantity}\n")
print("updated inventory saved to library.txt.")