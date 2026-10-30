# Candidate Matching Advisor Explainability

## Decision and Reasoning Process

The agent's decision support maps candidate evidence to essential and preferred role criteria. Its reasoning shows the basis for each match, partial match, gap, or unresolved item.

## Inputs and Data Sources Used

Input data consists of the approved role profile, recruiter criteria, and candidate-submitted information. The agent does not use inferred demographic data, social profiles, or undisclosed data sources.

## Outputs and Supporting Evidence

The output is a match matrix with evidence, gaps, questions, and a non-binding summary. Supporting evidence is traceable to the role profile and candidate materials.

## Limits, Constraints, and Known Issues

One limitation is that matching cannot establish future performance or cultural contribution. The agent is constrained from automatically ranking, rejecting, or selecting candidates.

## Uncertainty and Human Review

Uncertainty is shown for missing, inconsistent, or unverifiable claims. Human review is required before shortlisting or any other hiring action.

## Implementation in This Repository

`agent.py` implements `compare_candidate(role, candidate)`. It normalizes declared role and resume skills, reports matched and missing skills, compares supplied experience years, combines those two transparent components into a score, lists excluded protected fields, reports uncertainty, and requires recruiter review. `test_agent.py` verifies that missing required skills are preserved in the output.

There is no applicant-tracking integration or trained ranking model. The caller supplies the role and candidate evidence, and the code cannot select or reject anyone.
