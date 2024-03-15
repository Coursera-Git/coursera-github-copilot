# Todo App

This Todo App is a simple web application built with Flask, allowing users to manage their todo list. Users can add new todos, mark them as complete or not complete, and delete them.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.6 or higher
- pip (Python package installer)

### Installation

1. Activate the virtual environment:

```bash
source venv/bin/activate
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```


### Configuration

The application uses SQLite as its database. The configuration is set in `config.py`. No additional configuration should be needed to run the application locally.

### Running the Application

To run the application, execute the following command in the root directory of the project:

```bash
python3 -m run
```

This will start a local server. Access the web application by navigating to `http://127.0.0.1:5000/` in your web browser.

## Usage

- **Add a Todo**: Enter a title for your todo in the input field and click the "Add Todo" button.
- **Toggle Completion**: Click on "Mark Complete" or "Mark Not Complete" next to a todo to toggle its completion status.
- **Delete a Todo**: Click on "Delete" next to a todo to remove it from the list.

## Running Tests

To run tests, execute the following command:

```bash
pytest
```


## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the LICENSE file for details.