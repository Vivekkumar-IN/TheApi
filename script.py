import inspect
from TheApi import api


def test_method(method, *args):
    try:
        result = method(*args)
        status = "✅"
        return status, result
    except Exception as e:
        status = "❌"
        return status, str(e)


def generate_api_status(methods):
    function_statuses = []
    readme_content = []

    for name, method in methods:
        if name.startswith("_") or name == "help":
            continue

        signature = inspect.signature(method)

        if len(signature.parameters) == 0:
            status, result = test_method(method)
            readme_content.append(
                f"### {name}\n\n```python\n# Usage:\nfrom TheApi import api\n\nresult = api.{name}()\nprint(result)\n```\n\n```text\n# Result:\n{result}\n```\n"
            )
        else:
            params = []
            for param in signature.parameters.values():
                if param.default is not param.empty:
                    # Get the default value as a string
                    param_value = repr(param.default)
                    params.append(f"{param.name}={param_value}")
                elif param.annotation is int:
                    params.append(f"{param.name}=5")  # Example integer
                else:
                    params.append(f"{param.name}='pokemon'")  # Example string

            status, result = test_method(
                method, *[eval(param.split("=")[1]) for param in params]
            )

            # Create a string for the parameters
            params_str = ", ".join(params)

            if status == "✅":
                readme_content.append(
                    f"### {name}\n\n```python\n# Usage:\nfrom TheApi import api\n\nresult = api.{name}({params_str})\nprint(result)\n```\n\n```text\n# Result:\n{result}\n```\n"
                )
            else:
                readme_content.append(
                    f"### {name}\n\n```python\n# Usage:\nfrom TheApi import api\n\nresult = api.{name}({params_str})\nprint(result)\n```\n\n```text\n# Error:\n{result}\n```\n"
                )

        function_statuses.append((name, status))

    return function_statuses, readme_content


def write_api_status_to_file(
    function_statuses,
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

    if separator in existing_content:
        pre_separator_content, _ = existing_content.split(separator, 1)
    else:
        pre_separator_content = existing_content

    new_content = "\n".join(readme_content)

    preface = "# API Documentation\n\n"
    preface += "This document provides the results of calling each function in `TheApi` class.\n\n"
    preface += "## API Status\n\n"
    preface += "| Function Name | Status |\n"
    preface += "|---------------|--------|\n"

    for function, status in function_statuses:
        preface += f"| [{function}](#{function.lower()}) | {status} |\n"

    updated_content = (
        pre_separator_content.strip() + "\n\n" + separator + "\n\n" + preface
    )
    updated_content += "\n## Code Usage and Results:\n\n" + new_content

    updated_content += "\n" + license_text

    with open(readme_file, "w") as f:
        f.write(updated_content)


def main():
    methods = inspect.getmembers(api, predicate=inspect.ismethod)
    function_statuses, readme_content = generate_api_status(methods)
    write_api_status_to_file(function_statuses, readme_content)


if __name__ == "__main__":
    main()
