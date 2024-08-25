# Yurl - URL Shortener

Yurl is a simple URL shortener built with Flask. It allows users to shorten long URLs and redirect them to the original URL. The application includes a basic web interface and an API endpoint for URL shortening.

## Features

- **Shorten URLs**: Convert long URLs into short, easy-to-share links.
- **Redirect**: Automatically redirect users from short URLs to the original URLs.
- **Simple Web Interface**: Input and view shortened URLs through a web interface.
- **API Endpoint**: Shorten URLs via a POST request to the `/shorten` endpoint.

## Installation

### Prerequisites

- Python 3.6+
- Flask

### Website 
[https://yurl.vercel.app/]


### Web Interface

1. Navigate to `http://127.0.0.1:5000/`.
2. Enter the URL you want to shorten and submit the form.
3. The shortened URL will be displayed on the page.

### API Endpoint

- **POST /shorten**

    Request Body:
    ```json
    {
        "url": "http://example.com"
    }
    ```

    Response:
    ```json
    {
        "short_url": "https://yurl.vercel.app/abc123"
    }
    ```

## File Structure

- `app.py`: The main Flask application file.
- `static/`: Directory for static files (e.g., favicon.ico).
- `templates/`: Directory for HTML templates (e.g., index.html).
- `requirements.txt`: File listing the dependencies for the project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to open issues or submit pull requests. Contributions are welcome!



