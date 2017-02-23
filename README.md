# Big Knob Application

A simple web app with one big knob that changes the response on /status path from -1 to 0.

# How to run
Start the application:
```bash
docker run -p 80:8000 earthquakesan/oneknob
```

Navigate to http://localhost:80/index/ and press the button.
The container status will change to (healthy) within 30 seconds (adjust the param in Dockerfile if necessary).
