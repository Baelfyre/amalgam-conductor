# Output Formats

## Compact Format (Default)
*Use this format to save tokens. Exception-only reporting. Omit the scoring matrix and empty sections.*

```markdown
# Cloak Meister Review

## Critical & Major Issues
- **[Location/Element]**: [Problem] -> [Fix] (Principle: [Principle])

## AI Anti-Patterns Detected
- [List any sterile UX, overdecoration, or inconsistent tokens]

## Quick Wins
- [List 1-2 fast, high-impact UI tweaks]

## Missing Evidence
- [List unverified assumptions]
```

## Full Format (Only when requested)

```markdown
# Cloak Meister Review

## Scope Reviewed
- Artifact Type:
- Primary User Goal:
- Target User:
- Review Mode:
- Evidence Reviewed:

## Review Confidence
Confidence Level: High / Medium / Low
Reason:

## Scoring Matrix
- Task Completion & Usability: __/100
- Accessibility & Screen Reader: __/100
- Cognitive Load & Navigation: __/100
- Discoverability & States: __/100
- Visual Hierarchy & Typography: __/100
- Layout Rhythm (Spacing, Alignment): __/100
- Color & Contrast: __/100
- Consistency & Design System: __/100
- Responsiveness: __/100
- Maintainability: __/100
- Overall Score: __/100

## Executive Summary

## Confirmed Findings

## Assumptions

## Critical Issues
### [Issue title]
- Severity:
- Principle Applied:
- Finding:
- Impact:
- Recommendation:
- Implementation Notes:

## Major Issues

## Minor Issues

## Strengths

## Quick Wins

## Long-Term Improvements

## Accessibility Notes

## Information Architecture Notes

## Visual Design & Typography Notes

## AI-Generated Anti-Patterns
*(e.g., sterile/utilitarian UX, inconsistent design systems, overdecoration)*

## Design Debt

## Frontend Implementation Notes

## Performance Notes

## Missing Evidence

## Final Recommendation
```

Write `None confirmed` for empty issue sections. State whether the interface is ready, needs revision, or needs major restructuring.
