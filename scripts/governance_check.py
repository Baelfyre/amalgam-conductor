import os
import json
import sys

def main():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    
    print("========================================")
    print(" Orchestra CI/CD Governance Check (Phase 1) ")
    print(" Advisory Mode: ON (Non-blocking)")
    print("========================================\n")

    warnings = 0
    errors = 0

    # 1. Required Files Check
    print("[1] Checking required files...")
    required_files = [
        "plugin.json",
        "README.md",
        "CHANGELOG.md",
        "SECURITY.md",
        "LICENSE"
    ]
    for rf in required_files:
        path = os.path.join(repo_root, rf)
        if os.path.exists(path):
            print(f"  [PASS] {rf} exists.")
        else:
            print(f"  [WARN] Missing required file: {rf}")
            warnings += 1

    # 2. Plugin.json Validation
    print("\n[2] Validating plugin.json...")
    plugin_path = os.path.join(repo_root, "plugin.json")
    plugin_data = None
    if os.path.exists(plugin_path):
        try:
            with open(plugin_path, "r", encoding="utf-8") as f:
                plugin_data = json.load(f)
            print("  [PASS] plugin.json is valid JSON.")
        except json.JSONDecodeError as e:
            print(f"  [FAIL] plugin.json is invalid JSON: {e}")
            errors += 1
    else:
        print("  [FAIL] plugin.json not found.")
        errors += 1

    # 3. Skills Validation
    if plugin_data and "skills" in plugin_data:
        print("\n[3] Validating registered skills...")
        for skill in plugin_data.get("skills", []):
            skill_name = skill.get("name")
            if not skill_name:
                continue
            skill_file_path = os.path.join(repo_root, "skills", skill_name, "SKILL.md")
            if os.path.exists(skill_file_path):
                print(f"  [PASS] Skill validated: {skill_name}")
            else:
                print(f"  [FAIL] Missing SKILL.md for registered skill: {skill_name}")
                errors += 1

    # 4. Commands Validation
    if plugin_data and "commands" in plugin_data:
        print("\n[4] Validating registered commands...")
        for cmd in plugin_data.get("commands", []):
            cmd_path = os.path.join(repo_root, "commands", f"{cmd}.md")
            if os.path.exists(cmd_path):
                print(f"  [PASS] Command file validated: {cmd}")
            else:
                print(f"  [FAIL] Missing command file for: {cmd}")
                errors += 1

    # 5. Output Templates Check
    print("\n[5] Checking output templates...")
    templates_dir = os.path.join(repo_root, "templates")
    if os.path.exists(templates_dir) and os.listdir(templates_dir):
        print("  [PASS] Output templates directory is populated.")
    else:
        print("  [WARN] Output templates directory is missing or empty.")
        warnings += 1

    # 6. Secrets / Forbidden Files Check
    print("\n[6] Checking for forbidden files (secrets)...")
    forbidden_extensions = [".env", ".pem", ".key"]
    found_forbidden = []
    for root, dirs, files in os.walk(repo_root):
        if ".git" in root or ".agents" in root:
            continue
        for file in files:
            if any(file.endswith(ext) for ext in forbidden_extensions):
                found_forbidden.append(os.path.relpath(os.path.join(root, file), repo_root))
    
    if not found_forbidden:
        print("  [PASS] No forbidden files detected.")
    else:
        for f in found_forbidden:
            print(f"  [FAIL] Forbidden file detected: {f}")
            errors += 1

    print("\n========================================")
    print(f" Summary: {errors} Errors, {warnings} Warnings")
    print(" Status: ADVISORY MODE (Returning Exit Code 0)")
    print("========================================")
    
    # Phase 1: Always return 0 unless instructed otherwise
    sys.exit(0)

if __name__ == "__main__":
    main()
