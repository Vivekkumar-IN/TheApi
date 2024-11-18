"""
I'm not deeply skilled in Python, so this script was created with AI's help.

The script analyzes `TheApi` methods and auto-generates documentation for them in the README, providing examples, outputs, and functionality statuses.

Here's a breakdown of each part:

1. **test_method**: Runs each function and returns a status (success/failure) and output or error details.

2. **format_docstring**: Formats the function's docstring into a cleaner markdown style for the README.

3. **generate_api_status**: Loops through the methods in `TheApi`, tests them, and organizes usage examples and status marks for each.

4. **format_result**: This function formats the result returned by an API method for easier readability in the README.

   - If the result is a dictionary, it will be formatted as a JSON code block.
   - If the result is a list of dictionaries, it will also be formatted as a JSON code block.
   - If the result is a list of non-dictionary items, it will be formatted as plain text.
   - For all other types of results, it will be formatted as plain text.

5. **write_api_status_to_file**: Compiles the generated statuses and documentation, saving them into the README file.

6. **main**: Collects methods, generates documentation and statuses, and triggers the README update.

When you run this, the README will get an API reference with examples and statuses for easy access.
"""

import json
import asyncio
import inspect

import aiofiles

from TheApi import api


# Helper function to test each API method
async def test_method(method, *args):
    try:
        if inspect.iscoroutinefunction(method):
            result = await method(*args)  # If async, await the result
        else:
            result = method(*args)  # If sync, call directly
        status = "✅"  # Mark as successful
        return status, result
    except Exception as e:
        status = "❌"  # Mark as failed
        return status, str(e)


# Formats docstring into a readable markdown format for README
def format_docstring(docstring):
    lines = docstring.splitlines()
    formatted_lines = []
    in_section = False
    nested_item = False

    for line in lines:
        stripped_line = line.strip()

        # Check if it's a section header like "Args:", "Returns:", "Raises:"
        if stripped_line in ["Args:", "Returns:", "Raises:"]:
            formatted_lines.append(f"**{stripped_line}**")
            in_section = True
            nested_item = False
        elif in_section and line.startswith("    "):  # Handle indented lines
            # Detect nested items in sections
            if stripped_line.startswith("- "):
                formatted_lines.append(f"    - {stripped_line[2:]}")
                nested_item = True
            else:
                parts = stripped_line.split(": ", 1)
                if len(parts) == 2 and not nested_item:
                    formatted_lines.append(f"  - **{parts[0]}**: {parts[1]}")
                else:
                    formatted_lines.append(f"    {stripped_line}")
        elif stripped_line == "":
            formatted_lines.append("")  # Keep blank lines
            in_section = False
            nested_item = False
        else:
            # General description lines outside sections
            if formatted_lines and formatted_lines[-1].startswith("**Description**"):
                formatted_lines[-1] += f" {stripped_line}"
            else:
                formatted_lines.append(f"**Description**:\n{stripped_line}")
            in_section = False
            nested_item = False

    return "\n".join(formatted_lines)


def format_result(result):
    if isinstance(result, dict):
        json_content = json.dumps(result, indent=4)
        return f"```json\n{json_content}\n```"
    elif isinstance(result, list):
        if len(result) > 0 and isinstance(result[0], dict):
            json_content = json.dumps(result, indent=4)
            return f"```json\n{json_content}\n```"
        else:
            return "```text\n" + "\n".join(map(str, result)) + "\n```"
    else:
        return f"```text\n{str(result)}\n```"


# Main function to generate API status table and function documentation


async def generate_api_status(methods):
    function_statuses = []
    readme_content = []
    status_content = []
    function_count = 1

    for name, method in methods:
        # Skip private methods
        if name.startswith("_"):
            continue

        # Get the source code of the method
        source = inspect.getsource(method)

        # Create a status table entry with a link
        status_content.append(
            f"| [{function_count}. {name.replace('_', ' ').title()}](#{function_count}-{name.replace('_', '-').lower()}) | "
        )

        # Format the docstring for better readability
        formatted_docstring = format_docstring(
            inspect.getdoc(method) or "No description available."
        )

        # Check if the method contains the comment "# gh-actions Don't check
        # it"
        if "# gh-actions it's Example ignore it" in source:
            # Add method to README but without Example section
            readme_content.append(
                f"### {function_count}. {name.replace('_', ' ').title()}\n\n"
                f"{formatted_docstring}\n\n"
            )
        else:
            # Handle functions based on parameters
            signature = inspect.signature(method)
            if len(signature.parameters) == 0:
                status, result = await test_method(method)  # No params
                readme_content.append(
                    f"### {function_count}. {name.replace('_', ' ').title()}\n\n"
                    f"{formatted_docstring}\n\n"
                    f"```python\nfrom Pokemon import api\n\n"
                    f"result = await api.{name}()\n"
                    f"print(result)\n```\n\n"
                    f"#### Expected Output\n\n"
                    f"{format_result(result)}\n"
                )
            else:
                # Handle functions with parameters
                params = []
                for param in signature.parameters.values():
                    if param.default is not param.empty:
                        param_value = repr(param.default)
                        params.append(f"{param.name}={param_value}")
                    elif param.annotation is int:
                        params.append(f"{param.name}=2")
                    else:
                        params.append(f"{param.name}='Pokemon'")

                # Test the function with sample parameters
                status, result = await test_method(
                    method, *[eval(param.split("=")[1]) for param in params]
                )

                params_str = ", ".join(params)
                readme_content.append(
                    f"### {function_count}. {name.replace('_', ' ').title()}\n\n"
                    f"{formatted_docstring}\n\n"
                    f"```python\nfrom TheApi import api\n\n"
                    f"result = await api.{name}({params_str})\n"
                    f"print(result)\n```\n\n"
                    f"#### Expected Output\n\n"
                    f"{format_result(result)}\n"
                )

        status_content[-1] += status
        function_statuses.append((name, status))
        function_count += 1

    return status_content, readme_content


# Writes the API status and documentation to README.md
async def write_api_status_to_file(
    status_content,
    readme_content,
    readme_file="README.md",
    separator="---",
    license_text="\nThis Project is Licensed under [MIT License](https://github.com/Vivekkumar-IN/TheApi/blob/main/LICENSE)",
):
    try:
        with open(readme_file, "r") as f:
            existing_content = f.read()
    except FileNotFoundError:
        existing_content = ""

    # If separator exists, keep only the part before it
    if separator in existing_content:
        pre_separator_content, _ = existing_content.split(separator, 1)
    else:
        pre_separator_content = existing_content

    # Build the new README content
    status_str = "\n".join(status_content)
    new_content = "\n".join(readme_content)

    preface = "# 📘 API Documentation\n\n"
    preface += (
        "## Status\n\n"
        "| Function           | Status |\n"
        "|--------------------|--------|\n"
        f"{status_str}\n\n"
    )

    updated_content = (
        pre_separator_content.strip() + "\n\n" + separator + "\n\n" + preface
    )
    updated_content += "\n## 🎓 How to Use Each Function\n\n" + new_content
    updated_content += "\n" + license_text

    async with aiofiles.open(readme_file, "w") as f:
        await f.write(updated_content)


# Main function to run the script
async def main():
    methods = inspect.getmembers(
        api, predicate=lambda m: inspect.ismethod(m) or inspect.isfunction(m)
    )
    status_content, readme_content = await generate_api_status(methods)
    await write_api_status_to_file(status_content, readme_content)


if __name__ == "__main__":
    asyncio.run(main())
