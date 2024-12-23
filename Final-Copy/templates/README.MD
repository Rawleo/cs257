### ClimateCanvas Templates Folder

Welcome to the templates directory of the ClimateCanvas project! This directory contains the HTML templates used to build our weather data website. We're excited to have you here and invite you to explore our project.

### Contents:
- homepage.html
- tables.html
- about-us.html

### Home Page (`home.html`)
- **Purpose:** Landing page for the website.
- **Functionality:**
  - Users can select an airport from a dropdown menu or an interactive map.
  - The map is embedded using the `render_template` function in the Flask app.
- **Route:** `@app.route('/', methods=("GET", "POST"))`

### Tables Page (`tables.html`)
- **Purpose:** Displays weather data tables.
- **Functionality:**
  - Users can choose an airport and specify date ranges for the data.
  - Selections are made using forms.
- **Route:** `@app.route('/tables', methods=("GET", "POST"))

### About Us Page (`about-us.html`)
- **Purpose:** Provides information about the project team.
- **Content:** Details about the team and their mission.
- **Links:** CSS, JavaScript, and image files are referenced from the static folder.
- **Route:** `@app.route('/about-us')

## Contributing

We welcome contributions from the community! If you're interested in helping us improve ClimateCanvas, here's how you can get involved:
- **Reporting Issues:** If you encounter any bugs or have suggestions for improvements, please open an issue on GitHub.
- **Submitting Pull Requests:** If you'd like to contribute code, feel free to submit a pull request with your changes. We'll review it and merge it if it aligns with our project goals.

## Getting Started

To run the ClimateCanvas project locally, follow these steps:
1. Clone this repository to your local machine.
2. Install the necessary dependencies using `pip install -r requirements.txt`.
3. Run the Flask application by executing `python app.py` in your terminal.
4. Open your web browser and navigate to `http://localhost:5000` to view the website.

For more information on how these pages function, refer to the respective HTML files in this directory. 

Happy coding! 🌦️🌍
