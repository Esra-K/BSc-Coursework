from src.Peer import Peer

client = Peer("127.0.0.1", 11000, is_root=False,
              root_address=("127.0.0.1", 5000))
client.run()