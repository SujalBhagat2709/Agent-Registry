import json
import os
from datetime import datetime


class AgentRegistry:

    def __init__(self):

        self.file_name = "agents.json"

        self.agents = []

        self.load_agents()

    def load_agents(self):

        if os.path.exists(self.file_name):

            try:

                with open(

                    self.file_name,

                    "r",

                    encoding="utf-8"

                ) as file:

                    self.agents = json.load(file)

            except:

                self.agents = []

    def save_agents(self):

        with open(

            self.file_name,

            "w",

            encoding="utf-8"

        ) as file:

            json.dump(

                self.agents,

                file,

                indent=4

            )

    def generate_agent_id(self):

        return f"AGENT-{len(self.agents)+1:03d}"

    def register_agent(self):

        print("\n========== REGISTER AGENT ==========\n")

        name = input(

            "Agent Name: "

        ).strip()

        if name == "":

            print("\nInvalid Name.")

            return

        role = input(

            "Primary Role: "

        ).strip()

        print("\nSupported Tools")

        print("Example : Calculator, Search, Retriever")

        tools = [

            tool.strip()

            for tool in input(

                "Tools: "

            ).split(",")

            if tool.strip()

        ]

        print("\nCapabilities")

        print("Example : Coding, Planning, Reasoning")

        capabilities = [

            capability.strip()

            for capability in input(

                "Capabilities: "

            ).split(",")

            if capability.strip()

        ]

        max_context = int(

            input(

                "\nMaximum Context Tokens: "

            )

        )

        status = input(

            "Status (Active/Inactive): "

        ).strip()

        if status == "":

            status = "Active"

        agent = {

            "agent_id":

                self.generate_agent_id(),

            "name":

                name,

            "role":

                role,

            "tools":

                tools,

            "capabilities":

                capabilities,

            "context_limit":

                max_context,

            "status":

                status,

            "created":

                datetime.now().strftime(

                    "%d-%m-%Y %H:%M:%S"

                )

        }

        self.agents.append(

            agent

        )

        self.save_agents()

        print("\nAgent Registered Successfully.")

    def list_agents(self):

        if not self.agents:

            print("\nNo Agents Registered.")

            return

        print("\n========== AGENT REGISTRY ==========\n")

        for agent in self.agents:

            print(

                "ID :", agent["agent_id"]

            )

            print(

                "Name :", agent["name"]

            )

            print(

                "Role :", agent["role"]

            )

            print(

                "Status :", agent["status"]

            )

            print(

                "Context Limit :",

                agent["context_limit"]

            )

            print(

                "Tools :",

                ", ".join(

                    agent["tools"]

                )

            )

            print(

                "Capabilities :",

                ", ".join(

                    agent["capabilities"]

                )

            )

            print(

                "Created :",

                agent["created"]

            )

            print("-" * 60)

    def search_agent(self):

        if not self.agents:

            print("\nNo Agents Registered.")

            return

        keyword = input(

            "\nSearch Name or Role: "

        ).lower()

        found = False

        print()

        for agent in self.agents:

            if (

                keyword in

                agent["name"].lower()

                or

                keyword in

                agent["role"].lower()

            ):

                print(

                    "ID :",

                    agent["agent_id"]

                )

                print(

                    "Name :",

                    agent["name"]

                )

                print(

                    "Role :",

                    agent["role"]

                )

                print(

                    "Status :",

                    agent["status"]

                )

                print("-" * 60)

                found = True

        if not found:

            print("No Matching Agent Found.")

    def update_status(self):

        if not self.agents:

            print("\nNo Agents Registered.")

            return

        agent_id = input(

            "\nAgent ID: "

        ).upper()

        for agent in self.agents:

            if agent["agent_id"] == agent_id:

                status = input(

                    "New Status: "

                )

                agent["status"] = status

                self.save_agents()

                print("\nStatus Updated.")

                return

        print("\nAgent Not Found.")

    def remove_agent(self):

        if not self.agents:

            print("\nNo Agents Registered.")

            return

        agent_id = input(

            "\nAgent ID: "

        ).upper()

        for agent in self.agents:

            if agent["agent_id"] == agent_id:

                self.agents.remove(

                    agent

                )

                self.save_agents()

                print("\nAgent Removed.")

                return

        print("\nAgent Not Found.")

    def statistics(self):

        if not self.agents:

            print("\nNo Statistics Available.")

            return

        active = 0

        inactive = 0

        tools = set()

        capabilities = set()

        for agent in self.agents:

            if agent["status"].lower() == "active":

                active += 1

            else:

                inactive += 1

            for tool in agent["tools"]:

                tools.add(tool)

            for capability in agent["capabilities"]:

                capabilities.add(capability)

        print("\n========== REGISTRY STATISTICS ==========\n")

        print(

            "Total Agents :",

            len(self.agents)

        )

        print(

            "Active Agents :",

            active

        )

        print(

            "Inactive Agents :",

            inactive

        )

        print(

            "Registered Tools :",

            len(tools)

        )

        print(

            "Capabilities :",

            len(capabilities)

        )