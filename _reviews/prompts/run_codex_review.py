"""Send review prompt to Codex CLI and capture output."""
import subprocess, sys, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
prompt_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'audience_stability_review_codex_20260621.txt')

with open(prompt_file, 'r', encoding='utf-8') as f:
    prompt = f.read()

result = subprocess.run(
    ['codex', 'exec', '--skip-git-repo-check'],
    input=prompt,
    capture_output=True,
    text=True,
    timeout=300,
    encoding='utf-8'
)

output_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'codex_review_audience_stability_20260621.txt')
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(result.stdout)
    if result.stderr:
        f.write('\n\n=== STDERR ===\n')
        f.write(result.stderr)

print(f"Output written to {output_file}")
print(f"Return code: {result.returncode}")
