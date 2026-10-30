"""Evidence-based candidate comparison for recruiter review."""
from __future__ import annotations


def compare_candidate(role: dict, candidate: dict) -> dict:
    required = {str(x).lower() for x in role.get("required_skills", [])}
    offered = {str(x).lower() for x in candidate.get("skills", [])}
    matched, missing = sorted(required & offered), sorted(required - offered)
    required_years = max(float(role.get("minimum_years", 0)), 0)
    years = max(float(candidate.get("years_experience", 0)), 0)
    skill_score = len(matched) / len(required) if required else 1.0
    experience_score = min(1.0, years / required_years) if required_years else 1.0
    return {
        "candidate_id": candidate.get("id"),
        "match_score": round(100 * (0.75 * skill_score + 0.25 * experience_score)),
        "matched_skills": matched,
        "missing_skills": missing,
        "experience_evidence": {"candidate_years": years, "minimum_years": required_years},
        "excluded_fields": ["age", "gender", "ethnicity", "disability", "religion"],
        "uncertainty": ["Resume evidence may be incomplete or differently worded."],
        "recruiter_review_required": True,
    }
