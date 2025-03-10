# Todd Bartoszkiewicz
# CSC505: Principles of Software Development
# Module 4: Critical Thinking Assignment
#
# Write a Python Script that will print
# a brief description and names and number of the important steps in your program.
#
# Abstract class Trait serves as a blueprint for all traits.
class Trait:
    def __init__(self, number, name, descriptions):
        self.number = number
        self.name = name
        self.descriptions = descriptions

    # abstract method
    def display(self):
        pass


# Uses the builder to display traits
class ExcellentDeveloperTraits:
    def __init__(self, traits):
        self.traits = traits

    def display_traits(self):
        for trait in self.traits:
            print(f"Trait {trait.number}. {trait.name}")
            print("Trait Descriptions")
            print("-" * 30)
            for index, description in enumerate(trait.descriptions):
                print(f"\t{index+1}. {description}")
            print("\n")


# Concrete class
class CuriosityUnderstanding(Trait):
    def display(self):
        return f"{self.number}. {self.name}: {self.descriptions}"


# Concrete class
class AnalyticalThinking(Trait):
    def display(self):
        return f"{self.number}. {self.name}: {self.descriptions}"


# Concrete class
class Teamwork(Trait):
    def display(self):
        return f"{self.number}. {self.name}: {self.descriptions}"


# Class responsible for adding all traits
class ExcellentDeveloperTraitsBuilder:

    def __init__(self):
        self.traits = []

    def add_trait(self, trait):
        self.traits.append(trait)
        return self

    def build(self):
        return ExcellentDeveloperTraits(self.traits)


# Class constructs the complex object using the Builder interface.
class Director:
    def __init__(self, builder):
        self._builder = builder

    def construct(self):
        curiosity_understanding = CuriosityUnderstanding(1, "Curiosity & Understanding",
                                                         ["Deep understanding of the problem, the code, and underlying principles",
                                                          "Explore new technologies and concepts without prodding",
                                                          "Learn new languages, new frameworks, new tools, and libraries",
                                                          "Read documentation, dissect codebases, and experiment",
                                                          "Explore root causes and focus on first principles"])
        self._builder.add_trait(curiosity_understanding)

        analytical_thinking = AnalyticalThinking(2, "Analytical Thinking",
                                                 ["Ability to break down complex problems into smaller parts.",
                                                  "Strong problem solving skills",
                                                  "Identify patterns and anit-patterns",
                                                  "Consider maintainability, scalability, and future scenarios",
                                                  "Are methodical and thorough in development and testing strategies"])
        self._builder.add_trait(analytical_thinking)

        teamwork = Teamwork(3, "Teamwork",
                            ["Approach the team with fairness, collaboration, high standards, and openness",
                             "Communicates effectively with all team members and stakeholders",
                             "Willing to help and learn from others"])
        self._builder.add_trait(teamwork)

    def return_excellent_developer(self):
        return self._builder.build()


# Dictionary object to store steps of the builder pattern
builder_dict = {
    "1. Director": ["constructs the complex exceptional developer object using the builder interface"],
    "2. Concrete Builder (DeveloperTraitsBuilder)": [
        "constructs and puts together traits of the exceptional developer object"],
    "3. Product (excellent_developer)": ["represents complex exceptional developer object that is being built"]
}


# Method from previous assignment to print box around text
def print_box(text, index, items):
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


# Reusing implementation from previous assignment to print boxes in builder dictionary
def display_builder_steps():
    for key in builder_dict:
        index = list(builder_dict).index(key)
        print_box(key, index, builder_dict[key])


if __name__ == "__main__":
    print("Welcome to the Developer Traits Builder!")
    excellentDeveloperTraitsBuilder = ExcellentDeveloperTraitsBuilder()
    director = Director(excellentDeveloperTraitsBuilder)
    director.construct()
    display_builder_steps()
    print("\nExample Implementation of the Builder Pattern\n")
    print("Important Excellent Developer Traits\n")
    excellent_developer = director.return_excellent_developer()
    excellent_developer.display_traits()
