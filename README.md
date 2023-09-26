docker-compose up -d
make pull

docker pull vgoroshenko/the-internet-demo
docker run -p 5000:5000 -it vgoroshenko/the-internet-demo

pip install -r .\requirements.txt
pytest -v --tb=line --alluredir=reports -n 3