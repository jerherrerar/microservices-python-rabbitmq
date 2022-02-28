# microservices-python-rabbitmq
Microservices Python: architecture based in events with RabbitMQ



guide: https://www.youtube.com/watch?v=0iB5IPoTDts
51:45


cd JERSON/myRepo/microservices-python-rabbitmq/
code .
source python-env/bin/activate
sudo docker-compose up


docker-compose exec backend sh
python manage.py makemigrations
python manage.py migrate


cd main/
sudo docker-compose up

docker-compose exec backend sh
python manager.py db init
python manager.py db migrate
python manager.py db upgrade
