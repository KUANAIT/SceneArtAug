In AUG.ipynb: Run This to Serve index.html via Flask + ngrok
1. Install dependencies (if not already)
2. Run Flask + ngrok inline
What Happens
•	The public URL is printed in the notebook
•	You can now use it for API call in a index.html

1. Clone the Project
First, download the project from GitHub:
git clone https://github.com/KUANAIT/SceneArtAug.git
cd SceneArtAug
You can then open the folder in your editor (e.g., VS Code, PyCharm, etc.).

2. Run the Website
If it’s a static HTML site:
python -m http.server
Then open in your browser:
http://localhost:8000
(Or just double-click index.html to open it directly.)

3. Upload a Scene Image
•	Click “Choose File” to upload an image (JPG or PNG).
•	Select the Scene Type — either Messy or Clean.

4. Enhance the Scene
•	Click Enhance Scene.
•	Wait a few seconds for the enhancement to complete.
•	The enhanced image will appear below the form.

5. Notes
•	Make sure your backend (ngrok or local API) is running and matches this endpoint in the script:
•	https://your-ngrok-url.ngrok-free.dev/enhance-image
•	If you see an error, check your connection or restart the server.
