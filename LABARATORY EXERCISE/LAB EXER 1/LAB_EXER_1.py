
incident_tickets = []


# Function: Add a new incident ticket
# This function collects the incident ID, bot name, and description,
# checks for duplicates, and saves the new ticket.
def add_ticket():
    """Add a new incident ticket to the list."""
    print("\n--- Add New Incident Ticket ---")
    incident_id = input("Enter Incident ID (e.g., INC1392950): ").strip()
    bot = input("Enter Bot name (e.g., BOT-Inventory): ").strip()
    description = input("Enter Short Description (e.g., Failed to generate the daily report): ").strip()

    # Prevent duplicate Incident IDs
    for ticket in incident_tickets:
        if ticket["Incident ID"].lower() == incident_id.lower():
            print(f"Ticket with Incident ID '{incident_id}' already exists.")
            return

    new_ticket = {
        "Incident ID": incident_id,
        "Bot": bot,
        "Short Description": description
    }
    incident_tickets.append(new_ticket)
    print(f"Ticket '{incident_id}' added successfully.")


# Function: Display all active tickets
# This function prints every saved ticket currently in the list.
def display_tickets():
    """Display all active incident tickets."""
    print("\n--- Active Incident Tickets ---")
    if not incident_tickets:
        print("No active incident tickets.")
        return

    print(f"{'Incident ID':<15}{'Bot':<20}{'Short Description'}")
    print("-" * 70)
    for ticket in incident_tickets:
        print(f"{ticket['Incident ID']:<15}{ticket['Bot']:<20}{ticket['Short Description']}")


# Function: Search for a ticket by incident ID
# This function asks the user for an ID and shows the matching ticket details.
def search_ticket():
    """Search for a specific ticket using its Incident ID."""
    print("\n--- Search Incident Ticket ---")
    incident_id = input("Enter Incident ID to search (e.g., INC1392939): ").strip()

    for ticket in incident_tickets:
        if ticket["Incident ID"].lower() == incident_id.lower():
            print("Ticket found:")
            print(f"  Incident ID       : {ticket['Incident ID']}")
            print(f"  Bot               : {ticket['Bot']}")
            print(f"  Short Description : {ticket['Short Description']}")
            return

    print(f"No ticket found with Incident ID '{incident_id}'.")


# Function: Remove a resolved ticket
# This function deletes a ticket when the user enters its incident ID.
def remove_ticket():
    """Remove a resolved incident ticket using its Incident ID."""
    print("\n--- Remove Resolved Ticket ---")
    incident_id = input("Enter Incident ID to remove (e.g., INC1392939): ").strip()

    for ticket in incident_tickets:
        if ticket["Incident ID"].lower() == incident_id.lower():
            incident_tickets.remove(ticket)
            print(f"Ticket '{incident_id}' has been removed (resolved).")
            return

    print(f"No ticket found with Incident ID '{incident_id}'.")


# Function: Count total active tickets
# This function prints how many tickets are currently in the list.
def count_tickets():
    """Display the total number of active incident tickets."""
    print("\n--- Total Active Incident Tickets ---")
    print(f"Total active tickets: {len(incident_tickets)}")


def load_sample_data():
    """Pre-load the list with the 10 sample incident tickets for testing."""
    sample_data = [
        ("INC1392939", "BOT-Inventory", "Failed to generate the daily report"),
        ("INC1392940", "BOT-Email", "Failed to send the scheduled notification"),
        ("INC1392941", "BOT-DataSync", "Encountered an error during data transfer"),
        ("INC1392942", "BOT-Invoice", "Failed to process an invoice"),
        ("INC1392943", "BOT-Report", "Failed to generate the weekly report"),
        ("INC1392944", "BOT-FileTransfer", "Failed to upload the required file"),
        ("INC1392945", "BOT-DataEntry", "Encountered an error while entering records"),
        ("INC1392946", "BOT-Backup", "Failed to complete the scheduled backup"),
        ("INC1392947", "BOT-Validation", "Failed to validate the submitted records"),
        ("INC1392948", "BOT-Notification", "Failed to send the system alert"),
    ]
    for incident_id, bot, description in sample_data:
        incident_tickets.append({
            "Incident ID": incident_id,
            "Bot": bot,
            "Short Description": description
        })
    print(f"{len(sample_data)} sample incident tickets loaded.")


def display_menu():
    """Display the main menu."""
    print("\n===== IT AUTOMATION INCIDENT TICKET MANAGER =====")
    print("1. Add a new incident ticket")
    print("2. Display all active incident tickets")
    print("3. Search for an incident ticket")
    print("4. Remove a resolved incident ticket")
    print("5. Display total number of active tickets")
    print("6. Exit")
    print("==================================================")


def main():
    """Main program loop."""
    load_sample_data()

    while True:
        display_menu()
        choice = input(
            "Enter your choice "
            "[1=Add, 2=Display, 3=Search, 4=Remove, 5=Count, 6=Exit]: "
        ).strip()

        if choice == "1":
            add_ticket()
        elif choice == "2":
            display_tickets()
        elif choice == "3":
            search_ticket()
        elif choice == "4":
            remove_ticket()
        elif choice == "5":
            count_tickets()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:SSS
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()