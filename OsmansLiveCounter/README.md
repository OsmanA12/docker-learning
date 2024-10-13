# My Personal Project

# My First Personal Project, Osmans Live Counter


### Welcome  
Welcome to my first Flask web application, Osman’s Live Counter! 🎉 This represents my understanding of Docker and how I put all my learning into practice by creating this app.

# My First Personal Project, Osmans Live Counter


### Welcome  
Welcome to my first Flask web application, Osman’s Live Counter! 🎉 This represents my understanding of Docker and how I put all my learning into practice by creating this app.

![alt text](https://file%2B.vscode-resource.vscode-cdn.net/Users/ozzyc/Desktop/Screenshots/Screenshot%202024-10-12%20at%2018.23.31.png?version%3D1728843086962)

---

### What Does Osman’s Live Counter Do?  
Osman’s Live Counter is a straightforward web application built with Flask that tracks and displays real-time site visit counts. It uses a Redis database to store the visit data and visually represents it with a dynamic progress bar. Additionally, each time a user visits the page, the site presents a random world fact along with the current visit count. 🌍

---

### Features  
- **Counter:** Keeps track of the number of visits and stores the count in Redis.  
- **Progress Bar:** A visually appealing progress bar that fills based on the visit count.  
- **Random Facts:** Displays interesting facts about the world every time you visit the counter page.  
- **Docker Application:** Utilises Docker and Docker Compose to create a development environment.  
- **Custom Background:** A unique and attractive background.  
- **Nginx Load Balancing:** Facilitates efficient traffic management and provides a solid foundation for future scalability. ⚖️

---

### Tech Features Used  
- **Backend:** Python (Flask)  
- **Database:** Redis  
- **Frontend:** HTML, CSS (custom styling)  
- **Containerisation:** Docker, Docker Compose  
- **Web Server:** Nginx  
- **Deployment:** Nginx + uWSGI  

---

### Using My Application  

**Requirements:**  
Ensure that the following is installed on your system:  
- Python 3.8  
- Redis  
- Docker  

**Installing My Application:**  
1. **Clone the Repository:**  
   ```bash
   git clone https://github.com/OsmanA12/docker-learning/tree/306534df52a4ae3f250d2413c17e96ea3c61e10d/OsmansLiveCounter
   cd VisitCounterX
   ```
2. **Set Up Virtual Environment (Optional):**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate  # For Windows
   ```
3. **Install Dependencies:**  
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Application Locally:** Start the Flask server using:  
   ```bash
   flask run
   ```
5. **Run via Docker:** If you prefer running the app in a Docker container, use:  
   ```bash
   docker-compose up --build
   ```
6. **Access the App:** Navigate to `http://localhost:7777` in your browser to see the application. 🖥️

---

### Usage  
Once the application is up and running, you can use the following pages:  
- **Home Page (/):** This page welcomes users to Osman’s Live Counter and provides links to the About and Visit Counter pages. 

- **Visit Counter Page (/count):** Displays the current visit count, a progress bar, and a random quote.  

- **About Page (/about):** Explains the purpose of the project and the technologies used.


---

---

### How Did I Make This Happen?  
This project marks the start of my journey into full-stack development and deployment with Osman’s Live Counter, and it’s been a truly rewarding learning experience. 💻

#### Key Milestones:
- **Flask Basics:** Getting to grips with Flask gave me a solid understanding of core web development principles. Creating routes and templates was both challenging and satisfying.  
- **Redis Integration:** Setting up Redis to track visits was a real eye-opener. I learned how essential caching and data storage are for modern web applications.  
- **Containerisation with Docker:** Using Docker to set up a multi-container environment completely transformed how I think about development. It made deploying applications much smoother and more efficient.  
- **Nginx for Load Balancing:** Configuring Nginx to handle load balancing was a key step in ensuring the scalability of the app. Seeing it go live was an exhilarating moment!

This experience has ignited my passion for web development, and I’m excited to keep learning and building on this foundation. 🌱

---

### Application Walkthrough  

#### 1. Home Page  
The home page introduces users to Osman’s Live Counter and features two main buttons:


- **About:** Takes users to the About page.  
- **Check Visit Counter:** Redirects users to the Visit Counter page, where they can view the current visit count.

![alt text](https://file%2B.vscode-resource.vscode-cdn.net/Users/ozzyc/Desktop/Screenshots/Screenshot%202024-10-12%20at%2018.23.31.png?version%3D1728843282951)

---

#### 2. Visit Counter Page  
This is the app’s central feature, showcasing the following:

- **Visit Count:** Updated in real-time using Redis.  
- **Dynamic Progress Bar:** A visual representation of the visit count.  
- **Inspirational Quote:** A random fact about the world is displayed at the bottom of the page.  

The progress bar and background can be customised to match your brand’s style. 🎨

![alt text](<Screenshot 2024-10-12 at 18.23.46.png>)

---

#### 3. About Page  
The About page offers a detailed overview of the project, including:

- The purpose and functionality of the app.  
- The technologies behind it, such as Flask, Redis, Docker, and Nginx.  
- Future plans and potential improvements for the project.

![alt text](<Screenshot 2024-10-12 at 18.23.38.png>)



---

### Contributing  
If you want to contribute to Osman’s Live Counter, feel free to fork the repository and submit pull requests. I welcome all contributions, including new features, bug fixes, and documentation improvements. 🤝

#### Steps to Contribute:
1. Fork the repository.  
2. Create a new branch.  
3. Make your changes.  
4. Commit and push your changes.  
5. Open a pull request.  

For any questions or suggestions, feel free to open an issue.



---

### What Does Osman’s Live Counter Do?  
Osman’s Live Counter is a straightforward web application built with Flask that tracks and displays real-time site visit counts. It uses a Redis database to store the visit data and visually represents it with a dynamic progress bar. Additionally, each time a user visits the page, the site presents a random world fact along with the current visit count. 🌍

---

### Features  
- **Counter:** Keeps track of the number of visits and stores the count in Redis.  
- **Progress Bar:** A visually appealing progress bar that fills based on the visit count.  
- **Random Facts:** Displays interesting facts about the world every time you visit the counter page.  
- **Docker Application:** Utilises Docker and Docker Compose to create a development environment.  
- **Custom Background:** A unique and attractive background.  
- **Nginx Load Balancing:** Facilitates efficient traffic management and provides a solid foundation for future scalability. ⚖️

---

### Tech Features Used  
- **Backend:** Python (Flask)  
- **Database:** Redis  
- **Frontend:** HTML, CSS (custom styling)  
- **Containerisation:** Docker, Docker Compose  
- **Web Server:** Nginx  
- **Deployment:** Nginx + uWSGI  

---

### Using My Application  

**Requirements:**  
Ensure that the following is installed on your system:  
- Python 3.8  
- Redis  
- Docker  

**Installing My Application:**  
1. **Clone the Repository:**  
   ```bash
   git clone https://github.com/OsmanA12/docker-learning/tree/306534df52a4ae3f250d2413c17e96ea3c61e10d/OsmansLiveCounter
   cd VisitCounterX
   ```
2. **Set Up Virtual Environment (Optional):**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate  # For Windows
   ```
3. **Install Dependencies:**  
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Application Locally:** Start the Flask server using:  
   ```bash
   flask run
   ```
5. **Run via Docker:** If you prefer running the app in a Docker container, use:  
   ```bash
   docker-compose up --build
   ```
6. **Access the App:** Navigate to `http://localhost:7777` in your browser to see the application. 🖥️

---

### Usage  
Once the application is up and running, you can use the following pages:  
- **Home Page (/):** This page welcomes users to Osman’s Live Counter and provides links to the About and Visit Counter pages. 

- **Visit Counter Page (/count):** Displays the current visit count, a progress bar, and a random quote.  

- **About Page (/about):** Explains the purpose of the project and the technologies used.


---

---

### How Did I Make This Happen?  
This project marks the start of my journey into full-stack development and deployment with Osman’s Live Counter, and it’s been a truly rewarding learning experience. 💻

#### Key Milestones:
- **Flask Basics:** Getting to grips with Flask gave me a solid understanding of core web development principles. Creating routes and templates was both challenging and satisfying.  
- **Redis Integration:** Setting up Redis to track visits was a real eye-opener. I learned how essential caching and data storage are for modern web applications.  
- **Containerisation with Docker:** Using Docker to set up a multi-container environment completely transformed how I think about development. It made deploying applications much smoother and more efficient.  
- **Nginx for Load Balancing:** Configuring Nginx to handle load balancing was a key step in ensuring the scalability of the app. Seeing it go live was an exhilarating moment!

This experience has ignited my passion for web development, and I’m excited to keep learning and building on this foundation. 🌱

---

### Application Walkthrough  

#### 1. Home Page  
The home page introduces users to Osman’s Live Counter and features two main buttons:


- **About:** Takes users to the About page.  
- **Check Visit Counter:** Redirects users to the Visit Counter page, where they can view the current visit count.

![alt text](https://file%2B.vscode-resource.vscode-cdn.net/Users/ozzyc/Desktop/Screenshots/Screenshot%202024-10-12%20at%2018.23.31.png?version%3D1728843282951)

---

#### 2. Visit Counter Page  
This is the app’s central feature, showcasing the following:

- **Visit Count:** Updated in real-time using Redis.  
- **Dynamic Progress Bar:** A visual representation of the visit count.  
- **Inspirational Quote:** A random fact about the world is displayed at the bottom of the page.  

The progress bar and background can be customised to match your brand’s style. 🎨

![alt text](<Screenshot 2024-10-12 at 18.23.46.png>)

---

#### 3. About Page  
The About page offers a detailed overview of the project, including:

- The purpose and functionality of the app.  
- The technologies behind it, such as Flask, Redis, Docker, and Nginx.  
- Future plans and potential improvements for the project.

![alt text](<Screenshot 2024-10-12 at 18.23.38.png>)



---

### Contributing  
If you want to contribute to Osman’s Live Counter, feel free to fork the repository and submit pull requests. I welcome all contributions, including new features, bug fixes, and documentation improvements. 🤝

#### Steps to Contribute:
1. Fork the repository.  
2. Create a new branch.  
3. Make your changes.  
4. Commit and push your changes.  
5. Open a pull request.  

For any questions or suggestions, feel free to open an issue.

