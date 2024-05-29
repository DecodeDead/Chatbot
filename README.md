# Document Q&A Chatbot

This project is a Document Q&A Chatbot built using FastAPI and Streamlit. The FastAPI backend handles document uploads and answers questions based on the uploaded document using a pre-trained language model. The Streamlit frontend provides an interface for users to upload documents and ask questions.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Backend (FastAPI)

1. Clone the repository:

    ```sh
    git clone https://github.com/DecodeDead/Chatbot.git
    cd Chatbot/fastapi-project
    ```

2. Create a virtual environment:

    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Run the FastAPI server:

    ```sh
    uvicorn app.main:app --host 0.0.0.0 --port 8000
    ```

### Frontend (Streamlit)

1. Navigate to the Streamlit app directory:

    ```sh
    cd ../UI
    ```

2. Install dependencies:

    ```sh
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:

    ```sh
    streamlit run main.py
    ```

## Usage

1. Open your web browser and navigate to `http://localhost:8501` to access the Streamlit interface.
2. Upload a text document using the upload widget.
3. Enter a question related to the document in the input field.
4. The app will display the answer based on the content of the uploaded document.

### Example

1. Upload a document containing the text: "The capital of France is Paris."
2. Ask: "What is the capital of France?"
3. The app will respond with: "Paris."

## Deployment

### FastAPI on Vercel

1. Create a `vercel.json` file in the `fastapi-app` directory with the following content:

    ```json
    {
      "version": 2,
      "builds": [
        {
          "src": "app/main.py",
          "use": "@vercel/python"
        }
      ],
      "routes": [
        {
          "src": "/(.*)",
          "dest": "app/main.py"
        }
      ]
    }
    ```

2. Deploy the FastAPI app:

    ```sh
    cd fastapi-app
    vercel --prod
    ```

### Streamlit on Streamlit Share

1. Navigate to the `UI` directory:

    ```sh
    cd ../UI
    ```

2. Deploy the Streamlit app:

    ```sh
    streamlit share
    ```

## Testing

This project includes unit tests, integration tests, and system tests to ensure the functionality and reliability of both the backend and frontend components.

### Backend Tests

#### 1. Unit Tests

Unit tests cover individual functions and modules to ensure they work as expected.

**Running Unit Tests**
   ```sh
   pytest fastapi-app/tests/test_main.py
   ```

### Frontend Tests

#### 2. System Tests

System tests validate the end-to-end functionality of the application, including interactions between the frontend and backend.

**Running System Tests**
   ```sh
   pytest UI/tests/test_system.py
   ```

### Note

- Update the FastAPI URL in the Streamlit app to the Vercel deployment URL.
- Use a static alias or custom domain for the FastAPI app to avoid changing the URL on every deployment.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

Please ensure your code follows the project's coding standards and passes all tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
