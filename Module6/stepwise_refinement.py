# Todd Bartoszkiewicz
# CSC505: Principles of Software Development
# Module 6: Critical Thinking Assignment
#
# The StepwiseRefinement class will display the steps involved in the stepwise refinement process for the
# Check Writer application.
class StepwiseRefinement:
    # Dictionary holding the levels of the stepwise refinement process.
    my_dict = {
        "Level 1: High-Level Abstract of the Algorithm": ["Read user input of a decimal amount.",
                                                          "Split an amount into dollars and cents.",
                                                          "Convert the dollars to word form.",
                                                          "Format the dollar words and cents in a printed string."],
        "Level 2: Intermediate or Mid-Level Algorithm Refinement": ["Refine get_amount() to verify the amount is a valid number.",
                                                                    "Refine split_amount(amount) to split dollars and cents.",
                                                                    "Return formatted string from formatted_check_amount(dollars, cents)."],
        "Level 3: Low-Level Abstraction of our Algorithm": ["Develop convert_numbers_to_words algorithm.",
                                                            "Refine get_amount() method to verify value is valid.",
                                                            "Refactor split_amount(amount) due float math discrepancies."]
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
        # Print all of the parts of the step
        for item in items:
            print(index * "   " + "{}".format("  " if index > 0 else "") + "|" + item.center(width) + "|")
        # Only print division lines if there are more than one item
        if len(items) > 0:
            print(index * "   " + "{}".format("  " if index > 0 else "") + "+" + "-" * width + "+")

    # Loop through the stepwise process and print the level headings and steps
    def display_process(self):
        for key in self.my_dict:
            index = list(self.my_dict).index(key)
            self.print_box(key, index, self.my_dict[key])


if __name__ == "__main__":
    print("Welcome to the Stepwise Refinement process for our Check Writer application!")
    stepwise_refinement = StepwiseRefinement()
    stepwise_refinement.display_process()
