import os 
from flask import Flask 
import redis 


app = Flask(__name__) 
redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = os.getenv('REDIS_PORT', 6379)
r = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/')
def welcome():
    return '''
    <html>
    <head>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                background-image: url('https://i.postimg.cc/R07ZGvTH/greg-rakozy-o-Mp-Az-DN-9-I-unsplash.jpg');
                color: black;
            }
            .container {
                background-color: rgba(255, 255, 255, 0.8);
                padding: 50px;
                margin-top: 100px;
                border-radius: 15px;
                display: inline-block;
            }
            .btn {
                padding: 10px 20px;
                margin: 10px;
                font-size: 18px;
                color: white;
                background-color: #006400; /* Dark Green */
                text-decoration: none;
                border-radius: 5px;
                border: none;
                cursor: pointer;
            }
            .btn:hover {
                background-color: #008000; /* Green */
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to Osmans live counter!</h1>
            <p>See your visits by clicking the link below</p>
            <a href="/about" class="btn">Go to About Page</a>
            <a href="/count" class="btn">Check counter</a>
        </div>
    </body>
    </html>
    '''

@app.route('/count')
def count():
    count = r.incr('visits')  
    return f'''
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                background-image: url('https://i.postimg.cc/R07ZGvTH/greg-rakozy-o-Mp-Az-DN-9-I-unsplash.jpg');
                background-size: cover;
                color: black;
            }}
            .container {{
                background-color: rgba(255, 255, 255, 0.8);
                padding: 50px;
                margin-top: 100px;
                border-radius: 15px;
                display: inline-block;
                text-align: center;
            }}
            .counter {{
                font-size: 50px;
                color: #000000;
                margin: 20px;
                font-weight: bold;
            }}
            .quote {{
                font-size: 20px;
                font-style: italic;
                margin-top: 20px;
            }}
            .progress-bar {{
                width: 100%;
                background-color: #f3f3f3;
                border-radius: 25px;
                margin: 20px 0;
            }}
            .progress-bar-fill {{
                height: 30px;
                width: {count}% ;
                background-color: #008000;  /* Green progress bar */
                border-radius: 25px;
                transition: width 1s ease-in-out;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Visit Counter</h1>
            <div class="counter" id="visitCount">Visit Count: {count}</div>
            
            <!-- Progress Bar -->
            <div class="progress-bar">
                <div class="progress-bar-fill" style="width: {min(count, 100)}%;"></div>
            </div>

            <!-- Random Quote -->
            <div class="quote">{get_random_quote()}</div>
        </div>

        <script>
            // Animate visit counter (simple animation)
            const visitCountEl = document.getElementById('visitCount');
            let start = 0;
            const end = {count};
            const duration = 2000; // 2 seconds
            const stepTime = Math.abs(Math.floor(duration / end));
            const timer = setInterval(function() {{
                start += 1;
                visitCountEl.textContent = "Visit Count: " + start;
                if (start >= end) {{
                    clearInterval(timer);
                }}
            }}, stepTime);
        </script>
    </body>
    </html>
    '''

# Random Facts about the world
import random

def get_random_quote():
    quotes = [
        "Did you know a cloud weighs around a million tonnes?",
        "Did you know wearing a tie can reduce blood flow to the brain by 7.5 per cent?",
        "Did you know the worlds oldest dog lived to 29.5 years old?",
        "Did you know most maps of the world are wrong?"
    ]
    return random.choice(quotes)

@app.route('/about')
def about():
    return '''
    <html>
    <head>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                background-image: url('https://i.postimg.cc/R07ZGvTH/greg-rakozy-o-Mp-Az-DN-9-I-unsplash.jpg');
                background-size: cover;
                color: black;
            }
            .container {
                background-color: rgba(255, 255, 255, 0.8);
                padding: 50px;
                margin-top: 100px;
                border-radius: 15px;
                display: inline-block;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>About This Application</h1>

            <p>Welcome to my first project! My name is <strong>Osman Albakri</strong>, and I'm excited to present this Flask web app built with Docker, Redis, and Nginx.</p>

            <p>This web app has allowed to test my docker and python skills while also teaching me random facts about the world 😄. Ladies and gentlemen, enjoy.</p>

            <h2>What did I use?</h2>
            <ul>
              <li> <strong>1.Flask</strong> – A lightweight Python web framework powering the app.</li>
              <li> <strong>2.Redis</strong> – A in-memory key-value store (like sql) managing the visit counts.</li>
              <li> <strong>3.Docker</strong> – Containerising the entire environment for consistent development and deployment.</li>
              <li> <strong>4.ginx</strong> – Handling load balancing and ensuring smooth performance.</li>
            </ul>

            <p>In the near future, I am planning to expand this application even more so be sure to stay tuned!.</p>
        </div>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7777)
