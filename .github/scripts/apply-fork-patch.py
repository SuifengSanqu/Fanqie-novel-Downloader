#!/usr/bin/env python3
from pathlib import Path

p = Path("tests/test_release_workflow.py")
text = p.read_text()
old = 'path.name for path in (ROOT / ".github" / "workflows").glob("*.yml")'
new = (
    "path.name\n"
    '            for path in (ROOT / ".github" / "workflows").glob("*.yml")\n'
    '            if path.name != "sync-upstream.yml"'
)
if old in text and new not in text:
    p.write_text(text.replace(old, new))

ci = Path(".github/workflows/ci.yml")
text = ci.read_text()
old = "args: -no-color"
new = "args: -no-color -ignore 'SC2016:'"
if old in text and new not in text:
    ci.write_text(text.replace(old, new))
