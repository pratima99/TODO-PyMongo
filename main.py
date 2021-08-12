from pymongo import MongoClient

client = MongoClient()

allDb = client.list_database_names()
myDb = client['tasks']
collection = myDb['todos']


def create_single_document():
    single_data = {
        "title": "Task from python",
        "time": "Till friday"
    }
    collection.insert_one(single_data)


def create_multiple_document():
    multiple_data = [
        {"title": "Multiple task 1", "time": "you decide"},
        {"title": "Testing task"}
    ]
    collection.insert_many(multiple_data)


def find_document():
    found_data = collection.find_one({"title": "Multiple task 1"})
    print(found_data)


def update_document():
    previous_data = {"title": "Task from python"}
    update_data = {"$set": {"title": "Task from python update"}}
    collection.update_one(previous_data, update_data)


def delete_document():
    delete_data = {"title": "Testing task"}
    collection.delete_one(delete_data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    find_document()
