def calculate_ats_score(skills, experience, education):

    score = 0

    if len(skills) >= 5:
        score += 40

    if len(experience) > 50:
        score += 30

    if len(education) > 5:
        score += 20

    score += 10

    return min(score, 100)