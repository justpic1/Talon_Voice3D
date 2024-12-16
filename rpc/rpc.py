from talon import Module, Context, actions
import xmlrpc.client
mod = Module()
ctx = Context()
@mod.action_class
class Actions:
    def send_rpc_message(message: str):
        """Send a message to the RPC server"""
        with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
            proxy.receive_message(message)