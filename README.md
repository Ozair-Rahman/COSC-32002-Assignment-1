# COSC-32002-Assignment-1

# How to Run
- Navigate to git directory
- Build image:
    - docker build -t assignment-1 .  
- Run Container
    - docker run -d -p 8000:8000 assignment-1 
- Use API
    - Go to any browser of choice and in the URL bar type: localhost:8000/docs