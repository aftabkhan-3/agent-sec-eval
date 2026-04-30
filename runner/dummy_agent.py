class DummyAgent:
    async def query(self, input_text):
        return f"Echo: {input_text}"