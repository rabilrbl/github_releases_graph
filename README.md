# GitHub Release Downloads Visualizer

This Python project utilizes Flask and Matplotlib to generate a bar graph plot for file downloads from GitHub releases.

> The app is available at https://ghrs.rabil.me/

## Introduction

This project provides a simple web application that visualizes download statistics of files from GitHub repositories. It fetches data from the GitHub API and generates a bar graph illustrating the download counts for each release file.

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/your_username/your_repository.git
    cd your_repository
    ```

2. **Install Dependencies**

    Make sure you have Python installed. Then, install the required Python libraries:

    ```bash
    pip install Flask matplotlib requests
    ```

3. **Run the Application**

    ```bash
    python3 main.py
    ```

4. **Access the Web Interface**

    Open your web browser and go to `http://127.0.0.1:5000/` to interact with the application.

## Usage

- **Home Page**

  - Navigate to the root URL (`/`) to access the main page of the application.

- **GitHub Stats**

  - Access statistics for a specific GitHub repository using the URL pattern: `/owner/repository_name`.
  - Add a query parameter `tag` to specify a release tag, e.g., `/owner/repository_name?tag=v1.0`.

## Functionality

- **`/`**

  - Renders a form for entering a GitHub repository details.

- **`/<owner>/<repo_name>`**
  
  - Retrieves GitHub release data for a specified repository and generates a bar graph visualizing download counts of release files.
  - Missing or unspecified `tag` defaults to the latest release.

- **`/page/<owner>/<repo_name>`**

  - Renders a page displaying the image of the GitHub statistics graph.

## Contributions

Feel free to contribute by submitting issues or pull requests to enhance the functionality or fix any bugs.