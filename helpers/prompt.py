from helpers import string


def build(db_driver, schema_info, user_prompt, chart_prompt):
    system_prompt = f"""
    Given the following {db_driver} database schema:

    {schema_info}

    ### Query Rules:
    - Use **only** tables and columns that exist in the schema.
    - **Do not invent** table names, column names, or values.
    - If the user refers to a table or column that **does not exist**, find the most relevant column based on its **meaning**.
    - If no relevant column exists, respond with: "Error: The requested table or column does not exist."
    - The output must contain **only** the SQL query, with no explanations, formatting, or additional text.
    - The query **must** start directly with 'SELECT'.
    - Dates should be formatted as 'YYYY-MM-DD'.
    - **Absolutely do not use markdown (` ```sql `) or any code blocks.**
    - **Do not wrap the query with triple backticks (` ``` `) or any other formatting characters.**
    - The output must be **plain text** containing only the SQL query.

    ### Optimization Rules:
    - Ensure queries are optimized for performance, using indexes where applicable.
    - Use `JOIN` only if necessary, avoiding unnecessary joins.
    - If filtering by date, ensure an indexed column is used whenever possible.
    """

    # Add chart-specific rules if provided
    if chart_prompt:
        system_prompt += f"""
        ### Chart-Specific Instructions:
        {chart_prompt}
        """

    system_prompt += """
    Generate the SQL query for the following request **without any extra formatting**:
    """

    # Clean formatting
    clean_prompt = string.clean_multiline(system_prompt)

    # Final prompt structure
    prompt = [
        {
            "role": "system",
            "content": f"You are an advanced SQL assistant specialized in {db_driver} databases.",
        },
        {
            "role": "user",
            "content": f"{clean_prompt}\n\n'{user_prompt}'",
        },
    ]

    return prompt
