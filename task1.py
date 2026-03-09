import pickle


class Record:
    def __init__(self, name):
        self.name = name
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        if old_phone in self.phones:
            index = self.phones.index(old_phone)
            self.phones[index] = new_phone

    def __str__(self):
        phones = ", ".join(self.phones)
        return f"{self.name}: {phones}"


class AddressBook:
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())


def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()


def main():
    book = load_data()

    while True:
        command = input("Enter command: ").strip().lower()

        if command == "add":
            name = input("Name: ")
            phone = input("Phone: ")

            record = book.find(name)
            if record is None:
                record = Record(name)
                book.add_record(record)

            record.add_phone(phone)
            print("Contact added.")

        elif command == "change":
            name = input("Name: ")
            old_phone = input("Old phone: ")
            new_phone = input("New phone: ")

            record = book.find(name)
            if record:
                record.edit_phone(old_phone, new_phone)
                print("Phone updated.")
            else:
                print("Contact not found.")

        elif command == "phone":
            name = input("Name: ")
            record = book.find(name)
            if record:
                print(record)
            else:
                print("Contact not found.")

        elif command == "all":
            print(book)

        elif command in ["exit", "close"]:
            save_data(book)
            print("Good bye!")
            break

        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()