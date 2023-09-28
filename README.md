## Getting Started

Install your dependencies:

    docker-compose up -d
    make pull
    docker pull vgoroshenko/the-internet-demo
    pip install -r .\requirements.txt

Start the server:

    docker run -p 5000:5000 -d -it vgoroshenko/the-internet-demo

Load the page you want to see in your browser:

    http://localhost:5000/

Start tests:

    pytest -v --tb=line --alluredir=reports -n 3


An example application that captures prominent and ugly functionality found on the web. Perfect for writing automated acceptance tests against.

Deployed and available at [http://the-internet.herokuapp.com](http://the-internet.herokuapp.com).