banlist = []

class test:
    def __init__(self, parent):
        self.parent = parent
        self.supporter = parent.supporter

        # If you want to have commands with very specific formatting, use the validate() function.
        self.validate = parent.validate

        # Various ways to send messages
        self.send_packet_unicast = parent.send_packet_unicast
        self.send_packet_multicast = parent.send_packet_multicast
        self.send_packet_multicast_variable = parent.send_packet_multicast_variable
        self.send_code = parent.send_code

    async def foobar(self, client, message, listener):
        print("Foobar!")

        # Reading the IP address of the client is as easy as calling get_client_ip from the server object.
        print(self.parent.get_client_ip(client))

        # In case you need to report a status code, use send_code.
        await self.send_code(
            client=client,
            code="OK",
            listener=listener
        )

    async def kickuser(self, client, message, listener):
        print("Foobar!")

        await self.send_code(
            client=client,
            code="OK",
            listener=listener
        )

    async def banuser(self, client, message, listener):
        print("Foobar!")

        banlist.append(message)

        print(banlist)
      
        await self.send_code(
            client=client,
            code="OK",
            listener=listener
        )