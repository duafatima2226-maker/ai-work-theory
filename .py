from ai_helper import calculate_priority, sort_subjects

def format_time(t):
    h = int(t)
    m = int((t - h) * 60)
    return f"{h}:{m:02d}"

def allocate_time(subjects, total_hours):
    subjects = sort_subjects(subjects)
    total_priority = sum(calculate_priority(s) for s in subjects)

    for s in subjects:
        weight = calculate_priority(s) / total_priority
        s["time"] = round(total_hours * weight, 2)

    return subjects

def create_schedule(subjects):
    current = 9
    schedule = []

    for s in subjects:
        start = format_time(current)
        end_time = current + s["time"]
        end = format_time(end_time)

        schedule.append((s["name"], start, end))

        if s["difficulty"] == "hard":
            current = end_time + 0.5
        else:
            current = end_time + 0.25

    return schedule