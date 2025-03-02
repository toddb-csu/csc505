# Todd Bartoszkiewicz
# CSC505: Principles of Software Development
# Module 3: Critical Thinking Assignment
#
# You have been contacted and are thinking about developing a "first" prototype
# for a mobile app that let users save a shopping list on their devices.
#
# Use Python to write a script that will print out the names and number
# of pages in your prototype and the sequence or flow of the pages.
prototype_pages = [
    "1. Landing Page",
    "2. Login Page",
    "3. Create Account",
    "4. Create Shopping List",
    "5. Add/Remove Items",
    "6. Edit/Remove Items"
]

create_account_page_flow = [
    "1. Landing Page -> Click 'Create Account' Button -> 3. Create Account",
    "3. Create Account -> Click 'Submit' Button -> 4. Create Shopping List",
    "4. Create Shopping List -> Click 'Create Shopping List' Button -> 5. Add/Remove Items"
]

login_page_flow = [
    "1. Landing Page -> Click 'Login' Button -> 2. Login Page",
    "2. Login Page -> Enter username and password and click 'Login' Button -> 5. Add/Remove Items"
]

common_page_flow = [
    """5. Add/Remove Items -> Click 'Add Item' (visualized by new row added to the list) -> 
    Enter Item and Quantity -> Click Green Checkmark""",
    "5. Add/Remove Items -> Click Red 'X' (visualized by row being removed from the list)",
    "5. Add/Remove Items -> Click Black Pencil (visualized by row being changing to editable) -> 6. Edit/Remove Items",
    "6. Edit/Remove Items -> Update Item and Quantity -> Click Green Checkmark -> 5. Add/Remove Items",
    "5. Add/Remove Items -> Click 'Exit' Button -> Application Closes"
]

if __name__ == "__main__":
    print("Welcome to the Shopping List Application!\n")

    print("Shopping List Prototype Details:")
    print(f"Number of pages: {len(prototype_pages)}")
    print("Page Names:")
    for page in prototype_pages:
        print(f"- {page}")

    print("\nNew User Page Flow:")
    for flow in create_account_page_flow:
        print(f"- {flow}")
    for flow in common_page_flow:
        print(f"- {flow}")

    print("\nReturning User Page Flow:")
    for flow in login_page_flow:
        print(f"- {flow}")
    for flow in common_page_flow:
        print(f"- {flow}")
