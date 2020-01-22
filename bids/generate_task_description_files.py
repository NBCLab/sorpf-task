import json

events_description = {
    'prompt': {
        'LongName': 'Trial prompt',
        'Description': ('Trial prompt. Spaces are replaced with underscores. '
                        'The first word is the target (presented as an image '
                        'in the task).'),
    },
    'response': {
        'LongName': 'Participant response',
        'Description': ('The button pressed by the participant.'),
        'Levels': {
            '1': 'Image is calm',
            '2': 'Image is somewhat calm',
            '3': 'Image is somewhat intense',
            '4': 'Image is intense'
        }
    }
}

bold_description = {
    'CogAtlasID': '',
    'TaskName': 'Dual Self and Other Referential Processing and Flanker Task'
}

with open('task-SORPF_events.json', 'w') as fo:
    json.dump(events_description, fo, sort_keys=True, indent=4)

with open('task-SORPF_bold.json', 'w') as fo:
    json.dump(bold_description, fo, sort_keys=True, indent=4)
