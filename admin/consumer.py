import pika

params = pika.URLParameters('amqps://cmxpguvc:CmYk5V42zdLUmHcXiZqGMBL1Vr7v3kPV@sparrow.rmq.cloudamqp.com/cmxpguvc')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Received in admin', body)

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started consuming')

channel.start_consuming()

channel.close()
