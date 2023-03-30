# AIRTECH-OS(ORDER OF SERVICE)

<p align="center">
 <a href="#-About-the-project">About the project</a> •
 <a href="#-Functionalities">Functionalities</a> •
 <a href="#-How-to-run-the-project">How to run the project</a> •
 <a href="#-Technologies">Technologies</a> •
</p>

## 💻 About the project

This Flask CRUD API provides basic Create, Read, Update, and Delete operations for a database. The API utilizes HTTP methods (POST, GET, PUT, DELETE) to perform these operations on a specified resource. The API accepts JSON payloads and responds with JSON data. The API is designed to be flexible and easily customizable to fit various use cases. To use the API, simply specify the resource and endpoint in the URL, and the appropriate HTTP method and payload in the request.

## ⚙️ Functionalities

The project provides a generic Flask CRUD API that supports the following functionalities:

Create: Allows users to create new records in the database by sending a POST request with a JSON payload to the API endpoint.

Read: Allows users to retrieve records from the database by sending a GET request with an optional query string parameter to filter the results. If no filter is specified, all records are returned.

Update: Allows users to update existing records in the database by sending a PUT request with a JSON payload to the API endpoint, specifying the record to be updated.

Delete: Allows users to delete records from the database by sending a DELETE request to the API endpoint, specifying the record to be deleted.

The API supports JSON payloads for all requests and responds with JSON data for all requests. The API is designed to be flexible and customizable, allowing users to specify the resource and endpoint in the URL, and the appropriate HTTP method and payload in the request. The API also includes error handling and validation to ensure that data is properly formatted and the correct HTTP status codes are returned.

## 🚀 How to run the project

1. Open a command prompt or terminal window.
2. Navigate to the root directory of your project.
3. Copy and paste the following command into the terminal window:

   ```BASH SCRIPT
   echo "---> Setting up Pipenv"&& python -V && rm -fr ".venv" && python -m venv .venv && .\.venv\Scripts\activate.bat && python.exe -m pip install --upgrade pip && pip install pipenv install
   ```

   This command sets up a Python virtual environment using Pipenv, upgrades pip, and installs the required packages for the project.
4. This command activates the virtual environment and sets up the necessary environment variables.
of `.evn.exemple` for `.env`
5. Finally, run the following command to start the Flask app:

    ```BASH SCRIPT
   python -m api.app
   ```

   This command starts the Flask development server and makes the app available at the default URL `http://localhost:8080`.

That's it! Your airtech-os should now be up and running.

---

## 🛠 Technologies

- python 3.10.10
- flask
- cheroot
- mysql

- for more look at the [pipefile](airtech-os\Pipfile)

## 💪 Como contribuir para o projeto

1. **fork** the project.
2. Create a new branch with your changes: `git checkout -b my-feature`
3. Save your changes and create a commit message telling what you did: `git commit -m "feature: My new feature"`
4. Push your changes: `git push origin my-feature`

---
