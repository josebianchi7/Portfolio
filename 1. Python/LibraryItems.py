# Author: Jose Bianchi
# GitHub username: josebianchi7
# Description: Library simulator with multiple classes to create system for storing, checking out, holding, and
# returning library items including books, albums, and movies. Code will store Patron information and count days checked
# out to ensure items are not late. If items are held late, fines will accrue.

class LibraryItem:
    """Represents an Item from the Library"""

    def __init__(self, library_item_id, title):
        """Creates private data members for Library Item Class"""
        self._library_item_id = library_item_id
        self._title = title

        self._location = "ON_SHELF"  # Initial location of all items can be assumed to be on the shelves of library

        # Initial statuses below of library items default to None as all items begin in library
        self._checked_out_by = None
        self._requested_by = None
        self._date_checked_out = 0

    def get_library_item_id(self):
        """Enforces the get method will be used to retrieve a library item's ID"""
        return self._library_item_id

    def get_title(self):
        """Enforces the get method will be used to retrieve a library item's title"""
        return self._title

    def get_location(self):
        """Enforces get method on location and returns one of three possible results"""
        return self._location

    def set_location(self, new_location):
        """Location can be changed based on actions by patron or library staff"""
        self._location = new_location

    def get_checked_out_by(self):
        """Enforces get method and returns Patron information if a Patron has checked it out"""
        return self._checked_out_by

    def set_checked_out_by(self, checked_out_by_patron):
        """Checked out by can change to new Patron or be held by library"""
        self._checked_out_by = checked_out_by_patron

    def get_requested_by(self):
        """Enforces get method and refers to a Patron if one has requested the library item. One request at a time"""
        return self._requested_by

    def set_requested_by(self, new_requesting_patron):
        """Requesting individual can change to none or be set to new requestor if no one has requested item"""
        self._requested_by = new_requesting_patron

    def get_date_checked_out(self):
        """Enforces get method and upon checkout, will be set to current date of Library"""
        return self._date_checked_out

    def set_date_checked_out(self, new_checkout_date):
        """Set new checkout date based on actions taken"""
        self._date_checked_out = new_checkout_date


class Book(LibraryItem):
    """Represents a Book and inherits from Library Item"""

    def __init__(self, library_item_id, title, author):
        """Initializes additional data member onto Library Item for author"""
        super().__init__(library_item_id, title)
        self._author = author

    def get_author(self):
        """Enforces get method and returns author of library Book item"""
        return self._author

    def get_check_out_length(self):
        """Returns maximum number of days a library Book item may be checked out for, which is 21 days"""
        return 21


class Album(LibraryItem):
    """Represents a Book and inherits from Library Item"""

    def __init__(self, library_item_id, title, artist):
        """Initializes additional data member onto Library Item for artist"""
        super().__init__(library_item_id, title)
        self._artist = artist

    def get_artist(self):
        """Enforces get method and returns artist of library Album item"""
        return self._artist

    def get_check_out_length(self):
        """Returns maximum number of days a library Album item may be checked out for, which is 14 days"""
        return 14


class Movie(LibraryItem):
    """Represents a Book and inherits from Library Item"""

    def __init__(self, library_item_id, title, director):
        """Initializes additional data member onto Library Item for director"""
        super().__init__(library_item_id, title)
        self._director = director

    def get_director(self):
        """Enforces get method and returns director of library Movie item"""
        return self._director

    def get_check_out_length(self):
        """Returns maximum number of days a library Movie item may be checked out for, which is 7 days"""
        return 7


class Patron:
    """Represents a patron at the library"""

    def __init__(self, patron_id, name):
        """Initializes private data members for Patron class"""
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0

    def get_patron_id(self):
        """Enforces get method and returns ID of Patron"""
        return self._patron_id

    def get_name(self):
        """Enforces get method and returns name of Patron"""
        return self._name

    def get_checked_out_items(self):
        """Enforces get method and returns checked out items for Patron"""
        return self._checked_out_items

    def get_fine_amount(self):
        """Enforces get method and returns fine amount for possible late fees"""
        return self._fine_amount

    def set_fine_amount(self, new_fine_amount):
        """Allows fine amount to be set to new value"""
        self._fine_amount = new_fine_amount

    def add_library_item(self, library_obj):
        """Adds specified Library Item to checked out items"""
        self._checked_out_items.append(library_obj)

    def remove_library_item(self, library_obj):
        """Removes Library Item from checked out items"""
        self._checked_out_items.remove(library_obj)

    def amend_fine(self, change_in_fine):
        """Action to change fine amount"""
        self._fine_amount += float(change_in_fine)


class Library:
    """Represent the library"""

    def __init__(self):
        """Private data members for Library class"""
        self._holdings = []
        self._members = []
        self._current_date = 0  # Number of days since Library was created

    def get_members(self):
        """Returns members of the Library"""
        return self._members

    def add_library_item(self, library_obj):
        """Adds Library Item object to holdings collection"""
        self._holdings.append(library_obj)

    def add_patron(self, patron_obj):
        """Adds a Patron object to members collection"""
        self._members.append(patron_obj)

    def lookup_libray_item_from_id(self, library_item_id):
        """Returns Library Item object corresponding to ID parameter or None if not found"""
        for library_obj in self._holdings:
            if library_obj.get_library_item_id() == library_item_id:
                return library_obj
        else:
            return None

    def lookup_patron_from_id(self, patron_id):
        """Returns the Patron object corresponding to ID parameter or None if not found"""
        for patron_obj in self._members:
            if patron_obj.get_patron_id() == patron_id:
                return patron_obj
        else:
            return None

    def check_out_library_item(self, patron_id, library_item_id):
        """Returns status of both patron and library item for check out purposes"""

        patron_obj = self.lookup_patron_from_id(patron_id)
        if patron_obj is None:
            return "patron not found"

        library_item_obj = self.lookup_libray_item_from_id(library_item_id)
        if library_item_obj is None:
            return "item not found"

        library_obj_checked_status = library_item_obj.get_checked_out_by()
        if library_obj_checked_status is not None:
            return "item already checked out"

        library_obj_request_status = library_item_obj.get_requested_by()
        if library_obj_request_status is None and patron_obj.get_patron_id() != patron_id:
            return "item is on hold by other patron"

        patron_obj.add_library_item(library_item_obj)
        library_item_obj.set_checked_out_by(patron_obj)
        library_item_obj.set_date_checked_out(self._current_date)
        library_item_obj.set_location("CHECKED_OUT")
        library_item_obj.set_requested_by(None)

        return "check out successful"

    def return_library_item(self, library_item_id):
        """Updates status of both patron and library item for return scenarios"""
        library_item_obj = self.lookup_libray_item_from_id(library_item_id)
        if library_item_obj is None:
            return "item not found"

        library_obj_location = library_item_obj.get_location()
        if library_obj_location == "ON_SHELF":
            return "item already in library"

        patron_obj = library_item_obj.get_checked_out_by()
        patron_obj.remove_library_item(library_item_obj)

        library_obj_request_status = library_item_obj.get_requested_by()
        if library_obj_request_status is None:
            library_item_obj.set_location("ON_SHELF")
        else:
            library_item_obj.set_location("ON_HOLD_SHELF")

        library_item_obj.set_checked_out_by(None)

        return print("return successful")

    def request_library_item(self, patron_id, library_item_id):
        """Searches library holdings and members for checking status of library item request ability"""

        patron_obj = self.lookup_patron_from_id(patron_id)
        if patron_obj is None:
            return "patron not found"

        library_item_obj = self.lookup_libray_item_from_id(library_item_id)
        if library_item_obj is None:
            return "item not found"
        library_obj_request_status = library_item_obj.get_requested_by()
        if library_obj_request_status is not None:
            return "item already on hold"

        if library_obj_request_status is None:
            library_item_obj.set_requested_by(patron_obj)
            library_item_obj.set_location("ON_HOLD_SHELF")
            return "request successful"
        # else:
        #     return "item already on hold"

    def pay_fine(self, patron_id, paid_amount):
        """Updates fine amount if Patron is a member of library"""
        patron_obj = self.lookup_patron_from_id(patron_id)
        # if patron_obj is None:
        #     return "patron not found"

        patron_obj.amend_fine(-paid_amount)
        return "payment successful"

    def increment_current_date(self):
        """Increments current date"""

        self._current_date += 1

        for patron_obj in self._members:
            for library_item in patron_obj.get_checked_out_items():
                if self._current_date > (library_item.get_date_checked_out() + library_item.get_check_out_length()):
                    patron_obj.amend_fine(0.1)


if __name__ == "__main__":
    b1 = Book("345", "Phantom Tollbooth", "Juster")
    a1 = Album("456", "...And His Orchestra", "The Fastbacks")
    m1 = Movie("567", "Laputa", "Miyazaki")
    print(b1.get_author())
    print(a1.get_artist())
    print(m1.get_director())

    p1 = Patron("abc", "Felicity")
    p2 = Patron("bcd", "Waldo")

    lib = Library()
    lib.add_library_item(b1)
    lib.add_library_item(a1)
    lib.add_library_item(m1)
    lib.add_patron(p1)
    lib.add_patron(p2)

    print(lib.get_members())

    lib.check_out_library_item("bcd", "456")
    print(p2.get_checked_out_items())
    for _ in range(15):
        lib.increment_current_date()  # 7 days pass
    lib.check_out_library_item("abc", "567")
    loc = a1.get_location()
    print(loc)
    lib.request_library_item("abc", "456")
    for _ in range(8):
        lib.increment_current_date()  # 57 days pass
    p2_fine = p2.get_fine_amount()
    p1_fine = p1.get_fine_amount()
    lib.pay_fine("bcd", p2_fine)
    lib.pay_fine("abc", p1_fine)
    lib.return_library_item("456")
    print(p1.get_checked_out_items())
    print(p2.get_checked_out_items())
    print(p2.get_fine_amount())
    print(p1.get_fine_amount())
