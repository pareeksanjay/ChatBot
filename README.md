Perplexity Chatbot App – README
Welcome to your Perplexity-powered chatbot app! This README helps you set up, customize, and run your project locally with ease.

Features
Modern chat UI with gradient backgrounds and responsive design

Secure backend relay to Perplexity API (keeps your API key safe)

Real-time messaging between user and AI

Easily customizable frontend and backend code

Supports enhancements like conversation history, model switching, and markdown rendering

Directory Structure
text
chatbot-app/
│
├── static/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── app.py
Prerequisites
Python 3.7+

pip (Python package manager)

(Optional) Node.js or Python's http.server, if you want an alternative way to serve static files

Installation & Setup
Clone or Download the Repository

Place all project files in a single directory as shown above.

Install Python Dependencies

Open a terminal in your project directory and run:

text
pip install flask requests flask-cors
Add Your Perplexity API Key

Edit app.py

Set PERPLEXITY_API_KEY = "YOUR_API_KEY" (replace with your actual key)

Never commit your real key to public repositories.

Running the App Locally
Start the Backend

In your terminal, run:

text
python app.py
You should see output indicating the server is running at http://127.0.0.1:5000/.

Access the Chatbot UI

Visit http://127.0.0.1:5000/ in your browser.

If you open index.html directly from your filesystem and run into problems, always prefer using the backend server to serve your app.

Customization
Make the UI your own: Edit style.css for different colors, animations, or layouts.

Modify chatbot behavior: Change the system prompt or model in app.py.

Expand features: Implement message history, markdown rendering, or streaming responses as needed.

Add mobile tweaks: The given CSS is responsive, but you can further adapt it for your devices.

Troubleshooting
No response UI: Make sure your backend is running and accessible. Open browser DevTools (F12) to check for network or JS errors.

CORS issues: The app uses flask-cors to handle Cross-Origin requests. If you get CORS errors, double-check the import and that CORS(app) is in app.py.

API issues: Confirm your Perplexity API key is valid and has access.

404 errors: Confirm your <link> and <script> tags in index.html reference correct filenames and paths.

Example Usage
Type a message in the chat box at the bottom of the UI.

Click "Send".

Wait for the AI's response, which will appear in the chat window.

Security Notes
Never expose your Perplexity API key in frontend code.

Always use a backend relay as shown.

Store sensitive credentials using environment variables for advanced deployments.

Further Extensions
Add authentication for multi-user use.

Enable streaming/token-by-token AI responses.

Deploy on cloud platforms (Heroku, Render, AWS, etc.).

Connect to popular messaging platforms (Slack, WhatsApp, etc.).

License
This starter app is open for educational and non-commercial use.
For production or commercial deployments, review Perplexity’s API Terms of Service.

Happy hacking! Feel free to reach out with issues or improvements.
