import pika, json

params = pika.URLParameters('amqps://cmxpguvc:CmYk5V42zdLUmHcXiZqGMBL1Vr7v3kPV@sparrow.rmq.cloudamqp.com/cmxpguvc')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(
        exchange='',
        routing_key='main',
        body=json.dumps(body),
        properties=properties,
    )
