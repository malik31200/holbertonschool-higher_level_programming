#!/usr/bin/python3
import os


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template must be a string")
        return
    if (not isinstance(attendees, list)
            or not all(isinstance(a, dict) for a in attendees)):
        print("Error: Attendees must be a list of dictionaries")
        return

    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated")
        return

    for i, person in enumerate(attendees, start=1):
        content = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = person.get(key) if person.get(key) else "N/A"
            content = content.replace(f"{{{key}}}", value)

        filename = f"output_{i}.txt"

        if os.path.exists(filename):
            print(f"Warning: {filename} already exists, skipping.")
            continue
        try:
            with open(filename, "w") as file:
                file.write(content)
        except Exception as e:
            print(f"Error: writing {filename}: {e}")

    print(f"{len(attendees)} invitations generated successful!")
