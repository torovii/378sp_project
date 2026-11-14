
import asyncio
from email import policy
from email.parser import BytesParser


class SMTPServer(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        self.buffer = b""
        self.receiving_data = False
        self.message_data = []

        self.transport.write(
            b"220 localhost SMTP Test Server\r\n"
        )

    def data_received(self, data):
        self.buffer += data

        while b"\r\n" in self.buffer:
            line, self.buffer = self.buffer.split(b"\r\n", 1)

            if self.receiving_data:
                if line == b".":
                    raw_message = b"\r\n".join(
                        self.message_data
                    )

                    message = BytesParser(
                        policy=policy.default
                    ).parsebytes(raw_message)

                    print("\n--- EMAIL RECEIVED ---")
                    print("From:", message["From"])
                    print("To:", message["To"])
                    print("Subject:", message["Subject"])
                    print("----------------------\n")

                    self.receiving_data = False
                    self.message_data = []

                    self.transport.write(
                        b"250 Message accepted\r\n"
                    )
                else:
                    if line.startswith(b".."):
                        line = line[1:]
                    self.message_data.append(line)

                continue

            command = line.decode(
                errors="replace"
            ).upper()

            if command.startswith(("EHLO", "HELO")):
                self.transport.write(b"250 localhost\r\n")

            elif command.startswith("MAIL FROM:"):
                self.transport.write(
                    b"250 Sender accepted\r\n"
                )

            elif command.startswith("RCPT TO:"):
                self.transport.write(
                    b"250 Recipient accepted\r\n"
                )

            elif command == "DATA":
                self.receiving_data = True
                self.transport.write(
                    b"354 End data with <CRLF>.<CRLF>\r\n"
                )

            elif command == "QUIT":
                self.transport.write(b"221 Goodbye\r\n")
                self.transport.close()

            else:
                self.transport.write(b"250 OK\r\n")


async def main():
    loop = asyncio.get_running_loop()

    server = await loop.create_server(
        SMTPServer,
        "127.0.0.1",
        1025
    )

    print("SMTP server running on localhost:1025")
    print("Waiting for emails...")

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
