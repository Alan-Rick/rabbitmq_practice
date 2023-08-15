#!/usr/bin/env python
import pika

user_info = pika.PlainCredentials('guest', 'guest')  # 用户名和密码
connection = pika.BlockingConnection(
    pika.ConnectionParameters('192.168.244.240', 5672, '/', user_info))  # 连接服务器上的RabbitMQ服务
channel = connection.channel()

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(ch)
    print(f" [x] {body}")


channel.basic_consume(
    queue='routing_info', on_message_callback=callback, auto_ack=True)
channel.basic_consume(
    queue='routing_error', on_message_callback=callback, auto_ack=True)
channel.start_consuming()
