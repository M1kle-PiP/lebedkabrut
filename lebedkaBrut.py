from telethon import TelegramClient, events


api_id = 'api'
api_hash = 'hash'
phone_number = 'mobila'


client = TelegramClient('session_name', api_id, api_hash)


index = [6, 9, 12]
template = list("893827*83*39*6")
variants = []


for i in range(10):
    for j in range(10):
        for k in range(10):
            template[index[0]] = str(i)
            template[index[1]] = str(j)
            template[index[2]] = str(k)
            variants.append(''.join(template))


async def send_and_receive():
    await client.start(phone_number)
    current_index = 0
    @client.on(events.NewMessage)
    async def handler(event):
        nonlocal current_index

        print(f"Received response: {event.message.message}")

        if current_index < len(variants):
            await client.send_message('xrocket', variants[current_index])
            current_index += 1

    if current_index < len(variants):
        await client.send_message('xrocket', variants[current_index])
        current_index += 1

    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(send_and_receive())
