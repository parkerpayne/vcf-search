# vcf-search

`vcf-search` is a graphical tool designed to simplify the process of searching and exploring VCF (Variant Call Format) files. It provides a user-friendly interface, allowing users to configure search parameters and preview results without the need for command-line interactions.

## Features

- **Graphical User Interface (GUI):** No command-line required. Simply run the tool and interact with it through an intuitive graphical interface.

- **File Selection:** Upon launching, the tool prompts users to select a VCF file using a file browser.

- **Parameter Configuration:** Configure search parameters using a block-based interface. Specify columns, operators, values, and whether null values are permitted. Add as many or few parameters as needed (minimum of one).

- **Search:** Initiate the search with the configured parameters. The tool performs the search and provides a preview of the first 100 rows matching the criteria.

- **Results Preview:** View a window displaying the first 100 rows of the search results.

- **File Browsing:** After completion, users can choose to start a new search by browsing for another file.

- **Save Output:** Option to save the search results.

## Usage

1. **Run the Tool:**
   - Execute the tool, and a file browser will appear.

2. **File Selection:**
   - Choose a VCF file through the file browser.

3. **Parameter Configuration:**
   - Configure search parameters, specifying columns, operators, values, and null value permissions.

4. **Search:**
   - Initiate the search to retrieve matching rows.

5. **Results Preview:**
   - View a preview window showing the first 100 rows of the search results.

6. **Options:**
   - Choose to browse for another file or save the output.

## Compilation and Execution

`vcf-search` is a 100% Python tool. It can be compiled into an executable for easy distribution. Ensure all necessary packages are installed, then follow the steps below:

```bash
# Install dependencies
pip install pyinstaller

# Compile into an executable
pyinstaller -F app.py

# Run the executable
./dist/app
```

## License

`vcf-search` is open-source software licensed under the [MIT License](LICENSE). See the [LICENSE](LICENSE) file for details.

**MIT License**
