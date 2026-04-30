import json
import os

class AttackRunner:
    def __init__(self, agent):
        self.agent = agent

    def load_attacks(self, path="attacks"):
        attacks = []

        for root, _, files in os.walk(path):
            for file in files:
                full_path = os.path.join(root, file)

                if file.endswith(".txt"):
                    with open(full_path) as f:
                        attacks.append({
                            "name": file,
                            "payload": f.read(),
                            "source": "static"
                        })

                elif file.endswith(".json"):
                    with open(full_path) as f:
                        attack = json.load(f)
                        attack["source"] = "static"
                        attacks.append(attack)

        return attacks

    async def run(self, attacks):
        results = []

        for attack in attacks:
            response = await self.agent.query(attack["payload"])

            results.append({
                "attack": attack["name"],
                "response": response,
                "source": attack.get("source", "static")
            })

        return results