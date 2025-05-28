from aiogram import Bot, Dispatcher, types

@dp.message_handler(commands='buy')
async def process_buy(message: types.Message):
    await bot.send_invoice(
        chat_id=message.chat.id,
        title="Плюшевий єнот 🦝",
        description="Купи єнота, не будь як всі!",
        payload="enot_payload_001",
        provider_token="ТУТ_ТОКЕН_ОПЛАТИ_ЗАДОНАТ_МЕНІ",
        currency="USD",
        prices=[
            types.LabeledPrice(label="Єнот", amount=5000)  # $50.00
        ],
        start_parameter="buy_enot",
        photo_url="https://placekitten.com/300/300",  # рандомна фотка 😼
        photo_width=300,
        photo_height=300,
        photo_size=512,
        need_name=True,
        need_email=True,
        is_flexible=False  # якщо ціна змінюється — став True
    )
