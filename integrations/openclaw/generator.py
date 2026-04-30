class OpenClawGenerator:
    def generate(self, base_attack, n=2):
        variations = []

        for i in range(n):
            mutated = base_attack["payload"] + "\n[VARIANT ATTEMPT]"

            variations.append({
                "name": f"{base_attack['name']}_variant_{i}",
                "payload": mutated,
                "source": "openclaw"
            })

        return variations