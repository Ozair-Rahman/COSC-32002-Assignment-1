# COSC-32002-Assignment-1

# How to Run
- Clone repository
    - git clone https://github.com/Ozair-Rahman/COSC-32002-Assignment-1.git
- Navigate to git directory
    - cd COSC-32002-Assignment-1
- Build image:
    - docker build -t assignment-1 .  
- Run Container
    - docker run -d -p 8000:8000 assignment-1 
- Use API
    - Go to any browser of choice and in the URL bar type: localhost:8000/docs