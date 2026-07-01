import sys

import governance_check as gc


def assert_equal(name, actual, expected):
    if actual != expected:
        raise AssertionError(f"{name}: expected {expected!r}, got {actual!r}")


def main():
    assert_equal("forbidden artifacts", gc.is_forbidden_repo_path("artifacts/governance_report.txt"), True)
    assert_equal("forbidden runtime folder", gc.is_forbidden_repo_path(".agents/skills/dagger/SKILL.md"), True)
    assert_equal("allowed source file", gc.is_forbidden_repo_path("skills/arbiter/SKILL.md"), False)
    assert_equal(
        "missing changelog issue",
        gc.get_changelog_issue(["scripts/governance_check.py"], False),
        "Significant changes were detected without a matching CHANGELOG.md update.",
    )
    assert_equal("present changelog issue", gc.get_changelog_issue(["scripts/governance_check.py"], True), None)
    assert_equal("advisory exit", gc.get_exit_code(False, 3), 0)
    assert_equal("strict exit", gc.get_exit_code(True, 1), 1)
    print("Governance check helper tests passed.")
    sys.exit(0)


if __name__ == "__main__":
    main()
