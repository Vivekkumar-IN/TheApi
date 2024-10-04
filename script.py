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
    preface_content = []
    function_count = 1  # Add a count prefix for each function

    for name, method in methods:
        if name.startswith("_") or name == "help":
            continue

        signature = inspect.signature(method)

        # Add the function name with a hyperlink to the usage section
        preface_content.append(f"{function_count}. [{name}](#{name.lower()})")

        # Special case for 'upload_image' function
        if name == "upload_image":
            status = "✅"
            result = "You will get the URL for the image."

            # Hardcode the usage for upload_image
            readme_content.append(
                f"### {name}\n\n```python\nfrom TheApi import api\n\nresult = api.upload_image(file_path='file/to/image')\nprint(result)\n```\n\n```text\n{result}\n```\n"
            )
        elif len(signature.parameters) == 0:
            status, result = test_method(method)
            readme_content.append(
                f"### {name}\n\n```python\nfrom TheApi import api\n\nresult = api.{name}()\nprint(result)\n```\n\n```text\n{result}\n```\n"
            )
        else:
            params = []
            for param in signature.parameters.values():
                if param.default is not param.empty:
                    param_value = repr(param.default)
                    params.append(f"{param.name}={param_value}")
                elif param.annotation is int:
                    params.append(f"{param.name}=5")  # Example integer
                else:
                    params.append(f"{param.name}='pokemon'")  # Example string

            status, result = test_method(
                method, *[eval(param.split("=")[1]) for param in params]
            )

            params_str = ", ".join(params)

            if status == "✅":
                readme_content.append(
                    f"### {name}\n\n```python\nfrom TheApi import api\n\nresult = api.{name}({params_str})\nprint(result)\n```\n\n```text\n{result}\n```\n"
                )
            else:
                readme_content.append(
                    f"### {name}\n\n```python\nfrom TheApi import api\n\nresult = api.{name}({params_str})\nprint(result)\n```\n\n```text\n# Error:\n{result}\n```\n"
                )

        function_statuses.append((name, status))
        function_count += 1  # Increment the count for each function

    return preface_content, function_statuses, readme_content


def write_api_status_to_file(
    preface_content,
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

    # Convert the preface content to a string with numbered functions
    preface_str = "\n".join(preface_content)

    new_content = "\n".join(readme_content)

    # Preface including the count of each function with hyperlinks
    preface = "# API Documentation\n\n"
    preface += "This document provides a list of all functions in `TheApi`, along with their status and usage examples.\n\n"
    preface += "## Function List\n\n"
    preface += f"{preface_str}\n\n"

    # API Status Table
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
    methods = inspect.getmembers(api, predicate=lambda m: inspect.ismethod(m) or inspect.isfunction(m))
    preface_content, function_statuses, readme_content = generate_api_status(methods)
    write_api_status_to_file(preface_content, function_statuses, readme_content)



if __name__ == "__main__":
    main()
