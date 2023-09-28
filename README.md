# eCertificate Generator - Python Project

The **eCertificate Generator** is a Python project designed to simplify the process of generating digital certificates for multiple recipients listed in a text file. This tool is useful for creating certificates for events, workshops, courses, or any occasion where you need to distribute certificates to a large number of individuals.

![certificate](https://github.com/mohit-thakur09/eCertificateGenerator/assets/82665617/a2f2f1e4-b271-4a7e-aded-5faa71245d48)


## Features

- **Batch Certificate Generation**: Generate certificates for multiple recipients in one go by providing a list of names in a text file.

- **Customizable Templates**: Easily customize certificate templates with the recipient's name and any other relevant information.

- **Efficient and Time-Saving**: Automate the certificate generation process, saving time and effort, especially for large events.

## Getting Started

To use the eCertificate Generator, follow these steps:

1. Clone or download this repository to your local machine.

2. Ensure you have Python installed on your system.

3. Place your certificate template (in txt format) inside the `current` directory.

4. Prepare a text file with the names of the recipients, with each name separated with ` , `.

5. Run the `ecertificateGenerator.py` script:

   ```bash
   python ecertificate_generator.py
   ```

6. The generated certificates will be saved in the `assets` directory.

## Usage

1. **Prepare Certificate Template**:
   - Create a certificate template in PDF format with placeholders for recipient names or any other relevant information. Place this template in the `templates` directory.

2. **Prepare Names File**:
   - Create a text file (`names.txt`) with the names of the recipients, with each name on a separate line.

3. **Generate Certificates**:
   - Run the `ecertificate_generator.py` script, specifying the template and names file as arguments.
   - Customize the script to adjust the position and style of the recipient's name on the certificate template.

4. **Output**:
   - The generated certificates will be saved in the `assets` directory with unique filenames.

## Customization

You can customize the certificate template and the script to match your requirements. Open the `ecertificate_generator.py` script and modify the following:

- **Template Path**: Update the `template_path` variable to point to your certificate template.

- **Text Positioning**: Adjust the X and Y coordinates to position the recipient's name correctly on the template.

- **Text Style**: Customize the font size, font type, and text color as desired.

## Contributing

Contributions to this project are welcome. You can contribute by opening issues, providing feedback, or submitting pull requests to enhance the eCertificate Generator.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Enjoy using the eCertificate Generator for hassle-free certificate generation! 📜🎓
