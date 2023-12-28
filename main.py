from flask import Flask, request, Response, render_template, send_from_directory
import requests
import matplotlib.pyplot as plt
from matplotlib import colormaps
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Define a route to serve the static file
@app.route('/loading.gif')
def serve_loading_gif():
    # Specify the directory path where your static files are located
    static_directory = 'static'  # Replace with your actual path

    # Use send_from_directory to send the file
    return send_from_directory(static_directory, 'loading.gif')

@app.route('/<owner>/<repo_name>')
def github_stats(owner, repo_name):
    # Get the GitHub release ID from the query parameter (default to "latest" if not specified)
    release_id = request.args.get('tag')
    
    if release_id is None or release_id == "":
        release_id = "latest"
    else:
        release_id = f"tags/{release_id}"
    # GitHub API URL for the specified repository and release ID
    api_url = f"https://api.github.com/repos/{owner}/{repo_name}/releases/{release_id}"

    # Send a GET request to the GitHub Releases API
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract information about release files and download counts
        files = [file["name"] for file in data["assets"]]
        download_counts = [file["download_count"] for file in data["assets"]]

        # Generate distinct colors for each file using a numpy colormap
        colors = colormaps['viridis'].resampled(len(files))
        
        # Plot the bar graph with distinct colors
        bars = plt.bar(range(1, len(files)+1), download_counts, color=[color for color in colors(range(len(files)))])
        plt.xlabel("File Index")  # Index used instead of file names
        plt.ylabel("Download Count")
        plt.title("Download Counts for Release Files")

        # Create a legend for the color-coded file names
        legend_labels = [f"{e[0]+1} - [{z}] : {e[1]}" for e, z in zip(enumerate(files), download_counts)]
        plt.legend(bars, legend_labels, loc='upper left', bbox_to_anchor=(1,1))
        plt.xticks(range(len(files)))

        # Save the plot as an image in memory
        img_buffer = BytesIO()
        plt.savefig(img_buffer, format='png', bbox_inches='tight', transparent=True, pad_inches=0.2)
        img_buffer.seek(0)

        # Return the image as a response
        return Response(img_buffer.getvalue(), mimetype='image/png')

    else:
        # Return an error message if the request was not successful
        return f"Failed to retrieve data. Status code: {response.status_code}"
    
@app.route('/page/<owner>/<repo_name>')
def github_stats_image(owner, repo_name):
    return render_template('github_stats_image.html', repo=f"{owner}/{repo_name}")
    
if __name__ == '__main__':
    app.run(debug=True)
