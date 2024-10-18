import asyncio
import inspect

import aiofiles

from TheApi import api


async def test_method(method, *args):
    try:
        if inspect.iscoroutinefunction(method):
            result = await method(*args)
        else:
            result = method(*args)
        status = "✅"
        return status, result
    except Exception as e:
        status = "❌"
        return status, str(e)


async def generate_api_status(methods):
    function_statuses = []
    readme_content = []
    preface_content = []
    function_count = 1

    for name, method in methods:
        print(f"Processing {name}")
        if name.startswith("_"):
            continue

        signature = inspect.signature(method)
        preface_content.append(f"{function_count}. [{name}](#{name.lower()})")

        if name == "upload_image":
            status = "✅"
            result = "You will get the URL for the image."
            readme_content.append(
                f"### {name}\n\n"
                f"```python\nfrom TheApi import api\n\n"
                f"result = await api.upload_image(file_path='file/to/image')\n"
                f"print(result)\n```\n\n"
                f"```text\n{result}\n```\n"
            )
        elif len(signature.parameters) == 0:
            status, result = await test_method(method)
            readme_content.append(
                f"### {name}\n\n"
                f"```python\nfrom TheApi import api\n\n"
                f"result = await api.{name}()\n"
                f"print(result)\n```\n\n"
                f"```text\n{result}\n```\n"
            )
        else:
            params = []
            for param in signature.parameters.values():
                if param.default is not param.empty:
                    param_value = repr(param.default)
                    params.append(f"{param.name}={param_value}")
                elif param.annotation is int:
                    params.append(f"{param.name}=5")
                else:
                    params.append(f"{param.name}='pokemon'")

            status, result = await test_method(
                method, *[eval(param.split("=")[1]) for param in params]
            )

            params_str = ", ".join(params)

            if status == "✅":
                readme_content.append(
                    f"### {name}\n\n"
                    f"```python\nfrom TheApi import api\n\n"
                    f"result = await api.{name}({params_str})\n"
                    f"print(result)\n```\n\n"
                    f"```text\n{result}\n```\n"
                )
            else:
                readme_content.append(
                    f"### {name}\n\n"
                    f"```python\nfrom TheApi import api\n\n"
                    f"result = await api.{name}({params_str})\n"
                    f"print(result)\n```\n\n"
                    f"```text\n# Error:\n{result}\n```\n"
                )

        function_statuses.append((name, status))
        function_count += 1

    return preface_content, function_statuses, readme_content


async def write_api_status_to_file(
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

    preface_str = "\n".join(preface_content)
    new_content = "\n".join(readme_content)

    preface = "# API Documentation\n\n"
    preface += (
        "This API provides both synchronous and asynchronous usage:\n\n"
        "- **Sync**: `from TheApi.sync import api`\n"
        "- **Async**: `from TheApi import api`\n\n"
        "The following examples use the **async** version.\n\n"
        "## Function List\n\n"
        f"{preface_str}\n\n"
    )

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

    async with aiofiles.open(readme_file, "w") as f:
        await f.write(updated_content)


async def main():
    methods = inspect.getmembers(
        api, predicate=lambda m: inspect.ismethod(m) or inspect.isfunction(m)
    )
    preface_content, function_statuses, readme_content = await generate_api_status(
        methods
    )
    await write_api_status_to_file(preface_content, function_statuses, readme_content)


if __name__ == "__main__":
    asyncio.run(main())
