# END-TO-END MOVIE RECOMMENDER SYSTEM

## overview

This is an end-to-end movie recommender system built using Streamlit. The project includes a frontend for user interaction (`app.py`) and a model for recommending movies (`movie_rec.ipynb`).

## Run the Project Directly

To run this project directly, open a terminal and execute the following commands:

1. **Pull the Docker Image**:
   
   ```bash
   docker pull mitul012/movie-recommender-system
    ```

2. **Run the Docker Container**:
   
   ```bash
   docker run -p 8501:8501 mitul012/movie-recommender-system
    ```

This will start the Streamlit application, and it will be accessible at http://localhost:8501.


## Table of Contents

- [Installation](#installation)
- [Dataset](#Dataset)
- [Usage](#usage)
- [Docker](#docker)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Mitul2003/END-TO-END-MOVIE-REC-SYS.git
    cd END-TO-END-MOVIE-REC-SYS
    ```

2. **Create a virtual environment:**

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Dataset

The dataset used for this movie recommender system includes information about movies, such as titles, genres, and ratings. Here are the details:

- tmdb_5000_credits.csv
- tmdb_5000_movies.csv

## Usage

**to make similarity.pkl file run movie_rec.ipynb**

1. **Run the Streamlit app:**

    ```bash
    streamlit run app.py
    ```

2. **Open your browser and navigate to:**

    ```
    http://localhost:8501
    ```


## Docker

To run the application using Docker, follow these steps:

1. **Build the Docker image:**

    ```bash
    docker build -t movie-recommender-system .
    ```

2. **Run the Docker container:**

    ```bash
    docker run -p 8501:8501 movie-recommender-system
    ```


## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.



