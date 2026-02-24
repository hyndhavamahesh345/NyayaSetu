import re
punishments = {
    "302": "Murder — life imprisonment or death penalty.",
    "420": "Cheating — imprisonment up to 7 years and fine.",
    "41A": "Notice of appearance before police officer."
}

def extract_sections(text: str):
    """
    Detect IPC/BNS sections from text.
    """
    pattern = r"(IPC|BNS)?\s*(Section)?\s*(\d{1,3})"
    matches = re.findall(pattern, text, re.IGNORECASE)

    sections = []
    for match in matches:
        sec = match[2]
        if sec:
            sections.append(sec)

    return list(set(sections))


def calculate_severity(sections):
    """
    Rule-based severity scoring.
    """
    score = 0

    for sec in sections:
        try:
            num = int(sec)

            if num >= 300:
                score += 3
            elif num >= 150:
                score += 2
            else:
                score += 1

        except:
            continue

    if score >= 6:
        return "High"
    elif score >= 3:
        return "Medium"
    else:
        return "Low"


def generate_guidance(level):
    """
    Provide legal guidance text.
    """
    if level == "High":
        return "Serious offense detected. Immediate legal consultation is strongly recommended."
    elif level == "Medium":
        return "Moderate legal risk identified. Consider consulting a legal professional."
    else:
        return "Low severity indicators detected. Monitor the situation carefully."


def analyze_risk(text: str):
    """
    Main pipeline function.
    """
    sections = extract_sections(text)
    severity = calculate_severity(sections)
    guidance = generate_guidance(severity)

    return {
        "sections": sections,
        "severity": severity,
        "guidance": guidance
    }