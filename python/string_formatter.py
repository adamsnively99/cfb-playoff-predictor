# TODO: Optimize string formatting
def format_team_name(name, removal_chars):
    for c in removal_chars:
        name = name.replace(c, '')
    return name.strip()
