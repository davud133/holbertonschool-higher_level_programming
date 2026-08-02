import logging

logging.basicConfig(level=logging.INFO)


def generate_invitations(template, attendees):
    # Validate input types
    if not isinstance(template, str):
        logging.error("Invalid input: template is not a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        logging.error("Invalid input: attendees is not a list of dictionaries.")
        return

    # Handle empty inputs
    if not template:
        logging.error("Template is empty, no output files generated.")
        return
    if not attendees:
        logging.error("No data provided, no output files generated.")
        return

    # Process each attendee
    placeholders = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        content = template
        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            content = content.replace("{" + key + "}", str(value))

        output_filename = f"output_{index}.txt"
        with open(output_filename, 'w') as f:
            f.write(content)
        logging.info(f"Generated {output_filename}")
