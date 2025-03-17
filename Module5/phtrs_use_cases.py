# Todd Bartoszkiewicz
# CSC505: Principles of Software Development
# Module 5: Critical Thinking Assignment
#
# Use Python to write a script that will print out the different actors
# and use cases and a brief description of your diagram.
#
# Abstract class Actor serves as a blueprint for all actors.
class Actor:
    def __init__(self, name, description, use_cases):
        self.name = name
        self.description = description
        self.use_cases = use_cases


# Builder class
class PotholeTrackingAndRepairSystemBuilder:
    def __init__(self):
        self.actors = []

    def add_actor(self, name, description, use_cases):
        self.actors.append(Actor(name, description, use_cases))

    def build(self):
        return PotholeTrackingAndRepairSystemDirector(self.actors)


# Director class
class PotholeTrackingAndRepairSystemDirector:
    def __init__(self, actors):
        self.actors = actors

    def print_use_cases(self):
        print("Actors:")
        for actor in self.actors:
            print(f"- {actor.name}: {actor.description}")

        for actor in self.actors:
            print(f"\nUse Cases for {actor.name}: {actor.description}")
            for use_case in actor.use_cases:
                print(f"- {use_case}:")
                # Reusing implementation from previous assignment to print boxes in builder dictionary
                for item in actor.use_cases[use_case]:
                    index = list(actor.use_cases[use_case]).index(item)
                    self.print_headings(item, index)

    # Print only the Phase headings in a pretty box
    def print_headings(self, text, index):
        width = len(text)
        print(index * "   " + "{}".format("| " if index > 0 else "") + "+" + "-" * width + "+")
        print(index * "   " + "{}".format("->" if index > 0 else "") + "|" + text.center(width) + "|")
        print(index * "   " + "{}".format("  " if index > 0 else "") + "+" + "-" * width + "+")


if __name__ == "__main__":
    print("Welcome to the Pothole Tracking and Repair System (PHTRS) Use Cases!")
    # Create a builder
    potholeTrackingAndRepairSystemBuilder = PotholeTrackingAndRepairSystemBuilder()

    # Dictionary object to store use cases
    citizen_use_cases = {
        "1. Create Citizen Account": ["A citizen navigates to the PHTRS homepage.",
                                      "The citizen clicks on the “Create Account” button.",
                                      "PHTRS displays the “Create New Account” page.",
                                      "The citizen enters their name, address, phone number, a user id, a password, and confirms their password.",
                                      "PHTRS creates their account and displays a dashboard where the logged in citizen can see the status of their submissions, report a new pothole, and report pothole damage.",
                                      "The logged in citizen logs out of the PHTRS system."],
        "2. Report Pothole": ["A citizen logs into PHTRS by entering user id and password.",
                              "PHTRS displays a dashboard where the logged in citizen can see the status of their submissions, report a new pothole, and report pothole damage.",
                              "The logged in citizen clicks on the button to report a new pothole.",
                              "The logged in citizen enters the pothole information including the address, size, and location of the pothole on the street.",
                              "The logged in citizen submits the pothole information to the PHTRS system to be stored in the system database.",
                              "The PHTRS system returns the dashboard displaying the status of the submission along with previously submitted reports and the options to submit a new pothole or report pothole damage.",
                              "The logged in citizen logs out of the PHTRS system."],
        "3. View Pothole Report Status": ["A citizen logs into PHTRS by entering their user id and password.",
                                          "PHTRS displays a dashboard where the logged in citizen can see the status of their submissions, report a new pothole, and report pothole damage.",
                                          "The logged in citizen clicks on the pothole report that they are interested in seeing the details on.",
                                          "The PHTRS system returns the pothole report details including the current status of the pothole repair.",
                                          "The logged in citizen logs out of the PHTRS system."],
        "4. Report Damage": ["A citizen logs into PHTRS by entering user id and password.",
                             "PHTRS displays a dashboard where the logged in citizen can see the status of their submissions, report a new pothole, and report pothole damage.",
                             "The logged in citizen clicks on the button to report pothole damage.",
                             "The logged in citizen enters the damage information including type of damage and damage amount.",
                             "The logged in citizen submits the damage information to the PHTRS system to be stored in the system database.",
                             "The PHTRS system returns the dashboard displaying the status of the submission along with previously submitted reports and the options to submit a new pothole or report pothole damage.",
                             "The logged in citizen logs out of the PHTRS system."]
    }

    # Add actors
    potholeTrackingAndRepairSystemBuilder.add_actor("Citizen", "Reports potholes and damages due to potholes.", citizen_use_cases)

    # Dictionary object to store use cases
    employee_use_cases = {
        "1. Create new Repair Crew": ["A public works department employee logs into PHTRS by entering their user id and password.",
                                      "PHTRS displays the employee dashboard where the logged in employee can see the new potholes submitted, potholes in progress, potholes with a temporary repair, potholes that have been repaired, and damage reports that have been submitted.",
                                      "The logged in employee clicks on the 'Create New Repair Crew' button.",
                                      "PHTRS displays the 'Create New Repair Crew' page.",
                                      "The employee enters the new repair crew’s information, user id, and a temporary password.",
                                      "The employee clicks the 'Submit' button.",
                                      "PHTRS creates the new repair crew account, mails their user id and temporary password to them, and displays the employee dashboard.",
                                      "The logged in employee logs out of the PHTRS system"],
        "2. Assign Work Order": ["A public works department employee logs into PHTRS by entering their user id and password.",
                                 "PHTRS displays the employee dashboard where the logged in employee can see the new potholes submitted, potholes in progress, potholes with a temporary repair, potholes that have been repaired, and damage reports that have been submitted.",
                                 "The logged in employee clicks on a pothole report that was recently submitted and hasn’t been assigned a work crew yet.",
                                 "The PHTRS system returns the details of the pothole report.",
                                 "The logged in employee clicks on the button to assign a work order.",
                                 "The PHTRS system displays a list of available crews that have the number of crew available that can handle the work order.",
                                 "The logged in employee selects a crew for the work order.",
                                 "The PHTRS system assigns the work crew to the work order and returns the display of the pothole details showing the work order and assigned crew.",
                                 "The logged in employee logs out of the PHTRS system."],
        "3. View Damage Report": ["A public works department employee logs into PHTRS by entering their user id and password.",
                                  "PHTRS displays the employee dashboard where the logged in employee can see the new potholes submitted, potholes in progress, potholes with a temporary repair, potholes that have been repaired, and damage reports that have been submitted.",
                                  "The logged in employee clicks on a damage report that was recently submitted.",
                                  "The PHTRS system returns the details of the damage report.",
                                  "The logged in employee views the damage report details including the citizen’s details, type of damage, and dollar amount of the damage.",
                                  "The logged in employee logs out of the PHTRS system."]
    }

    potholeTrackingAndRepairSystemBuilder.add_actor("Public Works Department Employee", "Manages pothole repairs and assigns work orders.", employee_use_cases)

    # Dictionary object to store use cases
    repair_crew_use_cases = {
        "1. Execute Work Order": ["A repair crew logs into PHTRS by entering their user id and password.",
                                  "PHTRS displays the repair crew dashboard where the logged in member of the repair crew can see the new work orders assigned to their crew.",
                                  "The logged in repair crew member clicks on a work order recently assigned to the repair crew.",
                                  "The PHTRS system returns the details of the work order including the size of the pothole, address, and location of the pothole.",
                                  "The logged in repair crew member logs out of the PHTRS system.",
                                  "The repair crew performs the pothole repair from the work order."],
        "2. Update Work Order Status": ["A repair crew member logs into PHTRS by entering their user id and password.",
                                        "PHTRS displays the repair crew dashboard where the logged in member of the repair crew can see the new work orders assigned to their crew.",
                                        "The logged in repair crew member clicks on the work order that work was recently performed for.",
                                        "The PHTRS system returns the details of the work order including the status of the pothole.",
                                        "The logged in repair crew member clicks on the edit button to edit the work order.",
                                        "The logged in repair crew member updates the status of the work order and updates the amount of filler material used.",
                                        "The logged in repair crew member clicks update to update the work order.",
                                        "The PHTRS system returns the details of the work order including the updated status of the pothole and amount of filler material used.",
                                        "The logged in repair crew member logs out of the PHTRS system."]
    }

    potholeTrackingAndRepairSystemBuilder.add_actor("Repair Crew", "Performs pothole repairs.", repair_crew_use_cases)

    # Dictionary object to store use cases
    administrator_use_cases = {
        "1. Create Employee Account": ["An administrator navigates to the PHTRS administration page.",
                                       "The administrator logs in.",
                                       "The administrator clicks on the “Create Employee Account” button.",
                                       "PHTRS displays the “Create New Employee” page.",
                                       "The administrator enters the new employee’s name, user id, and a temporary password.",
                                       "The administrator clicks the “Submit” button.",
                                       "PHTRS creates the new employee account, mails their user id and temporary password to them, and displays the administration dashboard.",
                                       "The logged in administrator logs out of the PHTRS system."]
    }

    potholeTrackingAndRepairSystemBuilder.add_actor("Administrator", "Creates Public Works Department Employee accounts.", administrator_use_cases)

    # Build
    director = potholeTrackingAndRepairSystemBuilder.build()
    # Display actors and use cases for each actor
    director.print_use_cases()
