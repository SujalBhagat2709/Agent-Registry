from agent_registry import AgentRegistry


class RegistryStudio:

    def __init__(self):

        self.registry = AgentRegistry()

    def display_menu(self):

        while True:

            print("\n")

            print("=" * 65)

            print("                 AGENT REGISTRY")

            print("=" * 65)

            print("1. Register Agent")

            print("2. View All Agents")

            print("3. Search Agent")

            print("4. Update Agent Status")

            print("5. Remove Agent")

            print("6. Registry Statistics")

            print("7. Exit")

            choice = input("\nEnter Choice: ").strip()

            if choice == "1":

                try:

                    self.registry.register_agent()

                except ValueError:

                    print("\nInvalid Input.")

            elif choice == "2":

                self.registry.list_agents()

            elif choice == "3":

                self.registry.search_agent()

            elif choice == "4":

                self.registry.update_status()

            elif choice == "5":

                self.registry.remove_agent()

            elif choice == "6":

                self.registry.statistics()

            elif choice == "7":

                print("\nThank You For Using Agent Registry!")

                break

            else:

                print("\nInvalid Choice. Please Try Again.")


if __name__ == "__main__":

    studio = RegistryStudio()

    studio.display_menu()