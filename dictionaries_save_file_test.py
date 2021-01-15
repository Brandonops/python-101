import pickle
with open("heroes.txt", "rb") as file_handle:
    old_message = pickle.load(file_handle)
    print(f"Old message is: {old_message}. ")
user_input = input("whaat to save?")

with open("heroes.txt", "wb") as file_handle:
    pickle.dump(user_input, file_handle)
    print("Message Saved.")