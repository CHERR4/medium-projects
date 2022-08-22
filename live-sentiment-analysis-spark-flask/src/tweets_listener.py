import socket
from tweepy.streaming import Stream
from config.secrets import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET


class TweetPrinter(Stream):

    def __init__(self, spark_socket, consumer_key, consumer_secret, access_token, access_token_secret, **kwargs):
        super().__init__(consumer_key, consumer_secret, access_token, access_token_secret, **kwargs)
        self.client_socket = spark_socket

    def on_status(self, tweet) -> bool:
        """Every time a status is published
        """
        try:
            print(tweet.text.encode('utf-8'))
            self.client_socket.send(tweet.text.encode('utf-8'))  # Send tweet's text to socket
            return True
        except BaseException as e:
            print('Error on_data: %s' % str(e))
        return True

    def on_error(self, error) -> bool:
        """Every time an error occurs on data stream
        """
        print('Error', error)
        return True


def send_data(client_socket: socket, tracks: list):
    """Create data stream and send statuses via socket

    Args:
        client_socket (socket): spark connection socket
        tracks (list[str]): words we want to track in the stream
    """
    printer = TweetPrinter(client_socket, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
    printer.filter(track=tracks)  # Set this parameter to get tweets with a concrete word or hashtag


if __name__ == "__main__":
    socket = socket.socket()
    host = "127.0.0.1"  # Get local machine name
    port = 5557  # Reserve a port for your service.
    socket.bind((host, port))  # Bind to the port
    print("Listening on port: %s" % str(port))

    socket.listen(5)  # Now wait for client connection.
    spark_socket, address = socket.accept()  # Establish connection with client.


    tracks = ["#NFT"]  # Keywords that we want to track
    print("Received request from: " + str(address))
    send_data(spark_socket, tracks)
