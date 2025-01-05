import subprocess


def execute_code_block(code: str):
    """Executes a given code block and returns its output."""
    try:
        result = subprocess.check_output(
            ["python", "-c", code], stderr=subprocess.STDOUT
        )
        return result.decode("utf-8")
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output.decode('utf-8')}"


def process_docstring(app, what, name, obj, options, lines):
    """Custom handler to execute `.. exec-code::` blocks in docstrings."""
    new_lines = []
    in_exec_block = False
    code_block = []

    for line in lines:
        if line.strip() == ".. exec-code::":
            in_exec_block = True
            code_block = []
        elif in_exec_block and line.strip() == "":
            in_exec_block = False
            # Execute the code block and append output
            code_str = "\n".join(code_block)
            output = execute_code_block(code_str)
            new_lines.append("::")
            new_lines.extend(["    " + l for l in output.splitlines()])
        elif in_exec_block:
            code_block.append(line)
        else:
            new_lines.append(line)

    lines[:] = new_lines


def setup(app):
    app.connect("autodoc-process-docstring", process_docstring)
