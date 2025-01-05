import os
import inspect
import docstring_parser


def generate_method_docs(cls, method_name, file_path):
    method = getattr(cls, method_name, None)
    if method is None:
        raise ValueError(
            f"The method '{method_name}' does not exist in class '{cls.__name__}'."
        )

    is_async = inspect.iscoroutinefunction(method)
    func_type = "async" if is_async else "sync"
    func_signature = inspect.signature(method)
    func_return_type = method.__annotations__.get("return", None)
    docstring = inspect.getdoc(method) or ""
    parsed_docstring = docstring_parser.parse(docstring)

    # Generate method documentation
    doc_string = f"""
{method_name}
{'=' * len(method_name)}

``{func_type} {cls.__name__}.{method_name}{func_signature}``::
   {parsed_docstring.short_description or "".strip()}

**Parameters:**
"""
    for param in parsed_docstring.params:
        param_name = param.arg_name
        param_type = param.type_name or "Unknown"
        doc_string += f"    - **{param_name}** (``{param_type}``): {param.description or 'No description'}.\n"

    if func_return_type and func_return_type != "None":
        doc_string += f"""

**Returns:**

    **{func_return_type}**: {parsed_docstring.returns.description if parsed_docstring.returns else 'No return description.'}
"""

    if parsed_docstring.raises:
        doc_string += "\n**Raises:**\n\n"
        for exc in parsed_docstring.raises:
            doc_string += f"    - {exc.type_name}: {exc.description}\n"

    if parsed_docstring.examples:
        doc_string += "\n**Examples:**\n\n"
        for example in parsed_docstring.examples:
            doc_string += f"    - {example.description}\n"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w") as file:
        file.write(doc_string.strip())
    print(f"Documentation written to {file_path}")


from TheApi import SaavnAPI

file_path = "source/test.rst"
generate_method_docs(SaavnAPI, "search", file_path)
