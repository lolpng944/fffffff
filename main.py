from cloudlink import cloudlink
from custom_commands import test


if __name__ == "__main__":
    # Initialize Cloudlink. You will only need to initialize one instance of the main cloudlink module.
    cl = cloudlink()

    # Create a new server object. This supports initializing many servers at once.
    allowed_website = 'https://turbowarp.org'
    
    server = cl.server(logs=True, allowed_origin=allowed_website)

    # Create examples for various ways to extend the functionality of Cloudlink Server.

    # Set the message-of-the-day.
    server.set_motd("CL4 Optimized! Gotta Go Fast!", True)

    # Here are some extra parameters you can specify to change the functionality of the server.

    # Defaults to empty list. Requires having check_ip_addresses set to True.
    # server.ip_blocklist = ["127.0.0.1"]

    # Defaults to False. If True, the server will refuse all connections until False.
    # server.reject_clients = False

    # Defaults to False. If True, client IP addresses will be resolved and stored until a client disconnects.
    # server.check_ip_addresses = True

    # Defaults to True. If True, the server will support Scratch's cloud variable protocol.
    # server.enable_scratch_support = False

    # Binding callbacks - This example binds the "handshake" command with example callbacks.
    # You can bind as many functions as you want to a callback, but they must use async.
    # To bind callbacks to built-in methods (example: gmsg), see cloudlink.cl_methods.

    # Binding events - This example will print a client connect/disconnect message.
    # You can bind as many functions as you want to an event, but they must use async.
    # To see all possible events for the server, see cloudlink.events.

    # Creating custom commands - This example adds a custom command "foobar" from example_commands
    # and then binds the callback test3 to the new command.
    server.load_custom_methods(test)

    # Run the server.
    server.run(ip="0.0.0.0", port=3000)
