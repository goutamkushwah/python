import asyncio

async def brew_coffee():
    print("Starting coffee...")
    await asyncio.sleep(2)  # Simulate a network call or task
    print("Coffee is ready!")
    return "Delicious Coffee"

async def toast_bread():
    print("Starting toast...")
    await asyncio.sleep(1)
    print("Toast is ready!")
    return "Crunchy Toast"

async def main():
    # Run both tasks concurrently
    print("--- Breakfast Started ---")
    results = await asyncio.gather(brew_coffee(), toast_bread())
    print(f"Result: {results}")
    print("--- Breakfast Finished ---")

# The entry point to run the async loop
asyncio.run(main())