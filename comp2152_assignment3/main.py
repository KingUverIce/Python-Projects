# LIBRARY

# Jerome Delos Reyes - 101324620
# Mustafizur Rahman - 101383735
# Haider Farooqui - 1012

# IMPORT STATEMENTS
import sqlite3
import datetime
import os


# CLASSES
# PRIVATE
class User:
    def __init__(self):
        self.__name = ""

        return

    # getters
    @property
    def name(self):
        return self.__name

    # setters
    @name.setter
    def name(self, name: str):
        self.__name = name


class Book:
    def __init__(self, title: str, author: str,
                 description: str, category: str, quantity: int = 5, book_id: int = -1):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__description = description
        self.__category = category
        self.__quantity = quantity

        return

    # getters
    @property
    def book_id(self):
        return self.__book_id

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def description(self):
        return self.__description

    @property
    def category(self):
        return self.__category

    @property
    def quantity(self):
        return self.__quantity

    # setters
    @book_id.setter
    def book_id(self, book_id: int):
        self.__book_id = book_id

    @title.setter
    def title(self, title: str):
        self.__title = title

    @author.setter
    def author(self, author: str):
        self.__author = author

    @description.setter
    def description(self, description: str):
        self.__description = description

    @category.setter
    def category(self, category: str):
        self.__category = category

    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    def __repr__(self):
        return \
                "Book ID: " + str(self.__book_id) + "\n" + \
                "Title: " + self.__title + "\n" + \
                "Author: " + self.__author + "\n" + \
                "Description: " + self.__description + "\n" + \
                "Category: " + self.__category + "\n" + \
                "Quantity: " + str(self.__quantity) + "\n"


class Database:
    def db_connect(self):
        try:
            conn = sqlite3.connect("data/library.db")
            c = conn.cursor()
            c.execute(''' CREATE TABLE IF NOT EXISTS books (
                                    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    title TEXT NOT NULL,
                                    author TEXT NOT NULL,
                                    description TEXT NOT NULL,
                                    category TEXT NOT NULL,
                                    quantity INTEGER NOT NULL ); 
                                ''')

            # populates initial values
            c.execute(str('''INSERT INTO books (title, author, description, category, quantity) 
            VALUES ("The last doctor: Lessons in Living from the Front Lines of Medical Assistance in Dying", 
            "Marmoreo, Jean", "Dr. Jean Marmoreo spent her career keeping people alive. But when the Supreme Court of 
            Canada gave the green light to Medical Assistance in Dying (MAiD) in 2016, she became one of a small group 
            of doctors who chose to immediately train themselves in this new field. Over the course of a single year,
            Marmoreo learns about end-of-life practices in bustling Toronto hospitals, in hospices, and in the
            facilities of smaller communities. She found that the needed services were often minimal--or
            non-existent. The Last Doctor recounts Marmoreo's crash course in MAiD and introduces a range of very 
            different and memorable patients, some aged, some suffering from degenerative conditions or with a
            terminal disease, some surrounded by supportive love, some quite alone, who ask her help to end their 
            suffering with dignity and on their own terms. Dr. Marmoreo also shares her own emotional transformation 
            as she climbs a steep learning curve and learns the intimate truths of the vast range of end-of-life
            situations. What she experiences with MAiD shakes her to her core, makes her think deeply about pain, 
            loneliness, and joy, and brings her closer to life's most profound questions. At a time when end-of-life 
            care and its quality are more in the public eye than ever before, The Last Doctor provides an accessibly
            personal, deeply humane, and authoritative guide through this difficult subject.", "Motivational", 5),
            ("Motherthing", "Hogarth, Ainslie", "A darkly funny domestic horror novel about a woman who must take
            drastic measures to save her husband and herself from the vengeful ghost of her mother-in-law. Abby Lamb 
            has done it. She's found the Great Good in her husband, Ralph, and together they will start a family and
            put all the darkness in her childhood to rest. But then the Lambs move in with Ralph's mother, Laura,
            whose depression has made it impossible for her to live on her own. She's venomous and cruel, especially 
            to Abby, who has a complicated understanding of motherhood given the way her own, now-estranged,
            mother raised her. When Laura takes her own life, her ghost starts to haunt Abby and Ralph in very 
            different ways. Ralph is plunged into depression, and Abby is being terrorized by a force intent on 
            taking everything she loves away from her. With everything on the line, Abby must make the ultimate
            sacrifice in order to prove her adoration to Ralph and break Laura's hold on the family for good",
            "Horror", 4), ("Stay true : a memoir", "Hsu, Hua", "From the New Yorker staff writer Hua Hsu, a gripping 
            memoir on friendship, grief, the search for self, and the solace that can be found through art. In the
            eyes of 18-year-old Hua Hsu, the problem with Ken-with his passion for Dave Matthews, Abercrombie &
            Fitch, and his fraternity-is that he is exactly like everyone else. Ken, whose Japanese American family 
            has been in the United States for generations, is mainstream; for Hua, a first-generation Taiwanese
            American who has a 'zine and haunts Bay Area record shops, Ken represents all that he defines himself in 
            opposition to. The only thing Hua and Ken have in common is that, however they engage with it,
            American culture doesn't seem to have a place for either of them. But despite his first impressions, 
            Hua and Ken become best friends, a friendship built of late-night conversations over cigarettes,
            long drives along the California coast, and the textbook successes and humiliations of everyday college 
            life. And then violently, senselessly, Ken is gone, killed in a carjacking, not even three years after
            the day they first meet. Determined to hold on to all that was left of his best friend-his memories-Hua 
            turned to writing. Stay True is the book he's been working on ever since. A coming-of-age story that
            details both the ordinary and extraordinary, Stay True is a bracing memoir about growing up,
            and about moving through the world in search of meaning and belonging", "True Story", 3); ''')
                      .replace('           ', ''))

            return c

        except Exception as e:
            print("Error: " + str(e))
            return None


# PUBLIC
class Library(Database):
    def __init__(self):
        self.__books = list()
        self.__lib_db_conn = Database().db_connect()
        self.__user = User()

        self.update_library()

        return

    # getters
    @property
    def books(self):
        return self.__books

    @property
    def lib_db_conn(self):
        return self.__lib_db_conn

    @property
    def user(self):
        return self.__user

    # setters
    @books.setter
    def books(self, books: list):
        self.__books = books

    @lib_db_conn.setter
    def lib_db_conn(self, lib_db_conn: Database.db_connect):
        self.__lib_db_conn = lib_db_conn

    @user.setter
    def user(self, user: User):
        self.__user = user

    def add_book(self,
                 book: Book):
        self.lib_db_conn.execute(f''' 
            INSERT INTO books (title, author, description, category, quantity)
            VALUES ("{book.title}", "{book.author}",
            "{book.description}", "{book.category}", {book.quantity});
        ''')

        self.update_library()

        return True

    def search_book_by_author(self,
                              author: str):
        book_str = "\n"

        books = self.lib_db_conn.execute(f''' 
                SELECT *
                FROM books
                WHERE title 
                LIKE "%{author}%";
        ''').fetchall()

        for book in books:
            book_str += f"Book ID: {book[0]}\n" \
                        f"Title: {book[1]}\n" \
                        f"Author: {book[2]}\n" \
                        f"Description: {book[3]}\n" \
                        f"Category: {book[4]}\n" \
                        f"Quantity: {book[5]}\n\n"

        return book_str

    def search_book_by_title(self,
                             title: str):
        book_str = "\n"

        books = self.lib_db_conn.execute(f''' 
                SELECT *
                FROM books
                WHERE title 
                LIKE "%{title}%";
        ''').fetchall()

        for book in books:
            book_str += f"Book ID: {book[0]}\n" \
                        f"Title: {book[1]}\n" \
                        f"Author: {book[2]}\n" \
                        f"Description: {book[3]}\n" \
                        f"Category: {book[4]}\n" \
                        f"Quantity: {book[5]}\n\n"

        return book_str

    def search_book_by_category(self,
                                category: str):
        book_str = "\n"

        books = self.lib_db_conn.execute(f''' 
                SELECT *
                FROM books
                WHERE title 
                LIKE "%{category}%";
        ''').fetchall()

        for book in books:
            book_str += f"Book ID: {book[0]}\n" \
                        f"Title: {book[1]}\n" \
                        f"Author: {book[2]}\n" \
                        f"Description: {book[3]}\n" \
                        f"Category: {book[4]}\n" \
                        f"Quantity: {book[5]}\n\n"

        return book_str

    def search_book_by_id(self,
                          book_id: int):
        low = 0
        high = len(self.__books) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.__books[mid].book_id == book_id:
                return f"Book ID: {self.__books[mid].book_id}\n" \
                       f"Title: {self.__books[mid].title}\n" \
                       f"Author: {self.__books[mid].author}\n" \
                       f"Description: {self.__books[mid].description}\n" \
                       f"Category: {self.__books[mid].category}\n" \
                       f"Quantity: {self.__books[mid].quantity}\n"
            if self.__books[mid].book_id < book_id:
                low = mid + 1
            if self.__books[mid].book_id > book_id:
                high = mid - 1
        return None

    def rent_books(self,
                   book_id_list: list):

        # validations
        for book_id in book_id_list:
            if self.book_exists(book_id) is False:
                return False
            if self.book_available(book_id) is False:
                return False

        # variables
        keys = ["Book ID", "Title", "Author", "Description", "Category"]
        book_list = []
        file_str = ""

        file_str += "\t\t\t\tLIBRARY RECEIPT\n"
        file_str += " ------------------------------------------------ \n\n"

        file_str += f"\t\tNAME OF RENTER: {self.__user.name}\n"
        file_str += f"\t\tTOTAL RENTED BOOK(S): {str(len(book_id_list))}\n"
        file_str += f"\t\tDATE AND TIME OF RENT: {str(datetime.datetime.now().strftime('%Y-%m-%d'))}\n"
        file_str += f"\t\tDATE AND TIME OF RETURN: " \
                    f"{str((datetime.datetime.now() + datetime.timedelta(30)).strftime('%Y-%m-%d'))}\n\n"

        for book_id in book_id_list:
            book = self.__lib_db_conn.execute(f'''
                            UPDATE books
                            SET quantity = quantity - 1
                            WHERE book_id = {book_id}
                            RETURNING book_id, title, author, description, category;
            ''').fetchone()

            self.update_library()

            for book_details in book:
                book_list.append(str(book_details))

            book_dictionary = {key: value
                               for (key, value) in zip(keys, book_list)}

            file_str += " -----------------BOOK DETAILS------------------- \n"
            for key, value in zip(book_dictionary.keys(), book_dictionary.values()):
                file_str += f"  {key}:\n\t {value}\n"
            file_str += "\n"

            book_dictionary.clear()
            book_list.clear()

        with open("receipt/" + str(self.__user.name) + "_receipt_" + str(datetime.datetime.now()) + ".txt",
                  "w+") as file:
            file.write(file_str)

        return True

    def update_library(self):
        books = self.__lib_db_conn.execute(''' 
                                            SELECT *
                                            FROM books;
                                        ''')

        for book in books:
            self.__books.append(Book(book[1], book[2],
                                     book[3], book[4], book[5], book[0]))

        return

    def book_available(self, book_id: int):
        book = self.__lib_db_conn.execute(f'''
            SELECT quantity
            FROM books
            WHERE book_id = {book_id};
        ''').fetchone()

        if book[0] == 0:
            return False
        return True

    def book_exists(self, book_id: int):
        if self.search_book_by_id(book_id) is None:
            return False
        return True

    def __repr__(self):  # todo
        string_output = ""

        for book in self.books:
            string_output += "\n" + repr(book)

        return string_output


class Validation:
    def __init__(self):
        self.__valid_numbers = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
        self.__valid_option_numbers = ("1", "2", "3", "4", "5")
        self.__valid_book_search_numbers = ("1", "2", "3", "4")

    # getters
    @property
    def valid_number(self):
        return self.__valid_numbers

    @property
    def valid_option_numbers(self):
        return self.__valid_option_numbers

    @property
    def valid_book_search_numbers(self):
        return self.__valid_book_search_numbers

    # setters
    @valid_number.setter
    def valid_number(self, valid_number: list):
        self.__valid_numbers = valid_number

    @valid_option_numbers.setter
    def valid_option_numbers(self, valid_option_numbers: list):
        self.__valid_option_numbers = valid_option_numbers

    @valid_book_search_numbers.setter
    def valid_book_search_numbers(self, valid_book_search_numbers: list):
        self.__valid_book_search_numbers = valid_book_search_numbers

    def validate_int(self, number: str):
        for n in number:
            if n not in self.__valid_numbers:
                return False

        return True

    def validate_option_numbers(self, number: str):
        for n in number:
            if n not in self.__valid_option_numbers:
                return False

        return True

    def validate_book_search_numbers(self, number: str):
        for n in number:
            if n not in self.__valid_book_search_numbers:
                return False

        return True


# MENU/ MAIN PROGRAM
print(" -------------------- ")
print("Welcome to the library!")

# CREATING NECESSARY DIRECTORIES
if not os.path.exists("./data"):
    os.mkdir("./data")
if not os.path.exists("./receipt"):
    os.mkdir("./receipt")

# INSTANTIATING OBJECT
library = Library()
validation = Validation()

while True:
    print(" -------------------- ")
    user_name = input("Please enter your name: ")
    if user_name != "":
        library.user.name = user_name
        break

while True:
    try:
        print(" --------------------- ")
        print("|    LIBRARY MENU     |")
        print("|   1. Add Book       |")
        print("|   2. Rent Book      |")
        print("|   3. Search Book By |")
        print("|   4. Print Books    |")
        print("|   5. Exit           |")
        print(" --------------------- ")

        user_option = input("Please choose an option: ")

        if validation.validate_int(user_option) is False:
            raise Exception("Failed: Option should be a positive integer")
        if validation.validate_option_numbers(user_option) is False:
            raise Exception("Failed: Option should be less than 1 or greater than 5")

        if user_option == "1":
            while True:
                print("----------------------------------- ")
                print("\t\t| Enter book details below")
                user_title = input("\t\t| Title: ")
                user_author = input("\t\t| Author: ")
                user_description = input("\t\t| Description: ")
                user_category = input("\t\t| Category: ")
                user_quantity = input("\t\t| Quantity: ")

                if validation.validate_int(user_quantity) is False:
                    raise Exception("Failed: Quantity should be an integer")

                library.add_book(Book(user_title, user_author, user_description, user_category, int(user_quantity)))

                print("\t\t| Success: Book has been added")

                print("\t\t----------------------------- ")
                print("\t\t| Would you like to add more books?")
                user_choice = input("\t\t| Enter ANYTHING if yes, enter (n) if no: ")

                if user_choice == "n":
                    break
        if user_option == "2":  # todo: make option 2 crash-proof
            book_id_list = []

            print("----------------------------- ")
            print(repr(library))

            while True:
                user_book_id = input("Please enter book id that is to be rented: ")

                book_id_list.append(int(user_book_id))

                print("Would you like to add more books?")
                user_choice = input("Enter ANYTHING if yes, enter (n) if no: ")

                if user_choice == "n":
                    break

            if library.rent_books(book_id_list):
                print("success")
            else:
                print("failed")

        if user_option == "3":  # todo: make option 3 crash-proof
            print("----------------------------- ")
            print("\t\t|    1. ID           |")
            print("\t\t|    2. Category     |")
            print("\t\t|    3. Title        |")
            print("\t\t|    4. Author       |")
            print("\t\t -------------------- ")

            user_choice = input("\t\tPlease choose an option: ")

            if user_option == "1":
                print(library.search_book_by_id(2))
            # NON-FUNCTIONAL code below
            if user_option == "2":
                print(library.search_book_by_category(""))
            if user_option == "3":
                print(library.search_book_by_title(""))
            if user_option == "4":
                print(library.search_book_by_author(""))
        if user_option == "4":
            print("----------------------------- ")
            print(repr(library))
        if user_option == "5":
            break
    except Exception as e:
        print(" -------------------- ")
        print(str(e))
