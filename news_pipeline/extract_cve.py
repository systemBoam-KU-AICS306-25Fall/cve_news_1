import re

def extract_cves(text):
    """
    텍스트에서 CVE 목록(CVE-xxxx-xxxxx 형태)을 추출하여 리스트로 반환
    """
    pattern = r"CVE-\d{4}-\d+"
    matches = re.findall(pattern, text)
    return list(set(matches))  # 중복 제거
