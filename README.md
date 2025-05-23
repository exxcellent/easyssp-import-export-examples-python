![easyssp-logo-light](https://raw.githubusercontent.com/exxcellent/easyssp-auth-client-python/refs/heads/master/images/logo-light.png#gh-light-mode-only)
![easyssp-logo-dark](https://raw.githubusercontent.com/exxcellent/easyssp-auth-client-python/refs/heads/master/images/logo-dark.png#gh-dark-mode-only)

# 📘 easySSP – Import/Export Client Examples

This repository provides real-world examples for using the
official [easySSP Import/Export Client](https://github.com/exxcellent/easyssp-import-export-client-python). Whether
you're testing the API or building production workflows, these scripts will help you get started quickly.

---

## 🎯 What’s Inside

- 🔐 Authentication via the authentication module
- 🧪 Import and export .ssp/.ssd files
- 📘 **Includes documentation for all Import/Export API endpoints and models**

---

## 📁 Repository Structure

```bash
easyssp-import-export-examples-python/
├── demo_config.py             # User agent and easySSP username and password config.
├── ssd_import_demo.py         # Run a .ssd file import demo.
├── ssp_export_demo.py         # Run a .ssp file export demo.
├── ssp_import_demo.py         # Run a .ssp file import demo.
├── input/
│   └── ssd_example.ssd        # SSD file for importing
│   └── ssp_example.ssp        # SSP file for importing
└── output                     # Directory for storing the exported SSP models.
```

# 🚀 Getting Started with easySSP Import/Export Examples

This guide walks you through setting up and running the example scripts provided in the easySSP Import/Export Examples
repository.

---

## 1. Clone the Repository

To begin, clone the repository and navigate into the project directory:

- Clone the repo:  
  `git clone https://github.com/exxcellent/easyssp-import-export-examples-python.git`
- Change into the directory:  
  `cd easyssp-import-export-examples-python`

---

## 2. Install Dependencies

Ensure you have Python 3.11 or higher installed and a Pro Edition easySSP Account.
Create the virtual environment by running

```bash
python -m venv .venv
.\.venv\Scripts\activate   # or source .venv/bin/activate on macOS
```

Then, install all required dependencies using uv:

```bash
pip install uv
uv sync
```

---

## 3. Provide your login credentials

In the `demo_config.py` file, provide your easySSP credentials to start the demo.

---

## 4. Run an Example Script

### 📂 Input & Output Directories

This repository uses structured folders to organize data and results:

#### 📥 `input/`

The `input/` directory contains .ssd and .ssp files used for **import**.
Each script pulls its input data from this folder when submitting a request to the Import/Export API.

---

#### 📤 `output/`

The `output/` directory is where **exported SSP models** are stored.
This separation of input and output ensures clarity, reproducibility, and easy cleanup.

---

#### 🧪 Demo

The `ssd_import_demo.py`, `ssp_export_demo.py`, and `ssp_import_demo.py` scripts in the `demo` directory act as **central demo runners** and contain example requests that show
how to use the client.
They're a great starting point if you're exploring the API for the first time or want to see full workflows in action.
To start a demo, run

```bash
cd demo
python -m demo_file
```

Replace `demo_file` with one of the following: `ssd_import_demo`, `ssp_export_demo` or `ssp_import_demo`.

## 📚 Related Projects

### 🧠 [**Import/Export Client**](https://github.com/exxcellent/easyssp-import-export-client-python)

The official Python client for interacting with the easySSP Import/Export API.

### 🔐 [**Auth Client**](https://github.com/exxcellent/easyssp-auth-client-python)

Handles authentication by retrieving and storing JWT tokens.

### 🧰 [**Utils**](https://github.com/exxcellent/easyssp-python-clients-util)

A shared utility module used by all Python clients. Includes request handling, exceptions, and other reusable helpers.

---

## 🤝 Contributing

Spotted a bug or want to add your own scenario?  
Pull requests and issues are welcome!

## 📄 License

This project is licensed under the MIT License.
