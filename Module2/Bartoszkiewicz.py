# Todd Bartoszkiewicz
# CSC505: Principles of Software Development
# Module 2: Critical Thinking Assignment
#
# Implement the YourLastName class using Python,
# which will prompt the user to input the key
# elements of the diagram and return these objects
# in a well-formatted output.
class Bartoszkiewicz:
    # Default model stored in the dictionary data type
    my_dict = {
        "Communication": ["project initiation", " initial high-level requirements gathering",
                          "document initial requirements", "identify key stakeholders"],
        "Planning & Risk Analysis": ["estimating", "scheduling", "tracking", "initial risk assessment"],
        "Modeling": ["analysis", "high-level design", "identify critical features"],
        "Prototyping": ["prototype development"],
        "Prototype Review": ["requirements refinement"],
        "Construction": ["code increment", "unit test"],
        "Integration & Review": ["peer validation", "integration & system testing", "stakeholder review"],
        "Deployment": ["delivery","maintenance & support", "feedback", "TAM"]
    }

    # Print the phase with the steps in a nice box
    def print_box(self, text, index, items):
        # Find the max width between the phase and all the steps
        width = len(text)
        for item in items:
            if len(item) > width:
                width = len(item)
        # Print the Phase in a pretty box
        print(index * "   " + "{}".format("| " if index > 0 else "") + "+" + "-" * width + "+")
        print(index * "   " + "{}".format("->" if index > 0 else "") + "|" + text.center(width) + "|")
        print(index * "   " + "{}".format("  " if index > 0 else "") + "+" + "-" * width + "+")
        # Print all of the steps in the Phase
        for item in items:
            print(index * "   " + "{}".format("  " if index > 0 else "") + "|" + item.center(width) + "|")
        # Only print division lines if there are steps
        if len(items) > 0:
            print(index * "   " + "{}".format("  " if index > 0 else "") + "+" + "-" * width + "+")

    # Print only the Phase headings in a pretty box
    def print_headings(self, text, index):
        width = len(text)
        print(index * "   " + "{}".format("| " if index > 0 else "") + "+" + "-" * width + "+")
        print(index * "   " + "{}".format("->" if index > 0 else "") + "|" + text.center(width) + "|")
        print(index * "   " + "{}".format("  " if index > 0 else "") + "+" + "-" * width + "+")

    # Loop through the default model and only print the phase headings
    def display_model_headings(self):
        for key in self.my_dict:
            index = list(self.my_dict).index(key)
            self.print_headings(key, index)

    # Loop through the default model and print the phase headings and the steps
    def display_model(self):
        for key in self.my_dict:
            index = list(self.my_dict).index(key)
            self.print_box(key, index, self.my_dict[key])

    # Create a custom user model
    def get_user_model(self):
        user_dict = dict()
        phase_choice = input("Do you want to enter a Phase for your Model? (yes/no): ").lower()
        while phase_choice == "yes":
            phase_name = input("Phase Name: ")
            user_dict[phase_name] = []
            step_choice = input("Do you want to enter a step for your Phase? (yes/no): ").lower()
            while step_choice == "yes":
                user_dict[phase_name].append(input("Step Name: "))
                step_choice = input("Do you want to enter a step for your Phase? (yes/no): ").lower()
            phase_choice = input("Do you want to enter a Phase for your Model? (yes/no): ").lower()

        for key in user_dict:
            index = list(user_dict).index(key)
            self.print_box(key, index, user_dict[key])

if __name__ == "__main__":
    print("Welcome to the Bartoszkiewicz Model Creator!")
    model = Bartoszkiewicz()
    default_model_choice = input("Do you want to print the default Bartoszkiewicz Model? (yes/no): ").lower()
    if default_model_choice == "yes":
        phase_headings_choice = input("Do you want to only print the Phase headings? (yes/no): ").lower()
        print("")
        if phase_headings_choice == "yes":
            model.display_model_headings()
        elif phase_headings_choice == "no":
            model.display_model()
        else:
            print("This was an invalid choice: ", phase_headings_choice)
    elif default_model_choice == "no":
        print("")
        model.get_user_model()
    else:
        print("This was an invalid choice: ", default_model_choice)
