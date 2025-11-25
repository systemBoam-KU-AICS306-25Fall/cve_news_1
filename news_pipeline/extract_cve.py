import re

def extract_cves(text):

    pattern = r"CVE-\d{4}-\d+"
    matches = re.findall(pattern, text)
    return list(set(matches))  # 중복 제거
