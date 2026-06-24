"""Send review prompt to Qwen CLI via stdin pipe and capture output."""
import subprocess, sys, os

base = os.path.dirname(os.path.abspath(__file__))
prompt_file = os.path.join(base, 'audience_stability_review_qwen_20260621.txt')

with open(prompt_file, 'r', encoding='utf-8') as f:
    prompt = f.read()

# Try piping via stdin instead of --prompt flag
result = subprocess.run(
    'qwen',
    input=prompt,
    capture_output=True,
    text=True,
    timeout=300,
    shell=True,
    encoding='utf-8'
)

output_file = os.path.join(base, '..', 'qwen_review_audience_stability_20260621.txt')
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(result.stdout)
    if result.stderr:
        f.write('\n\n=== STDERR ===\n')
        f.write(result.stderr)

print(f"Output written to {output_file}")
print(f"Return code: {result.returncode}")
