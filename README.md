## Getting Started Test the internet in chrome



Install your dependencies:

    make pull
    venv/Scripts/activate
    pip install -r requirements.txt

Start selenoid server:

    docker-compose up -d

Load the page you want to see in your browser:

    http://localhost:5000/

Start tests:
 
    pytest -v --tb=line --alluredir=reports -n 3


An example application that captures prominent and ugly functionality found on the web. Perfect for writing automated acceptance tests against.

Deployed and available at [http://the-internet.herokuapp.com](http://the-internet.herokuapp.com).