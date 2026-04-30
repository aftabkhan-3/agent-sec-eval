import asyncio
import json

from runner.runner import AttackRunner
from runner.dummy_agent import DummyAgent
from evaluator.evaluator import Evaluator
from integrations.openclaw.generator import OpenClawGenerator


async def main():
    agent = DummyAgent()
    runner = AttackRunner(agent)
    evaluator = Evaluator()
    generator = OpenClawGenerator()

    base_attacks = runner.load_attacks()

    dynamic_attacks = []
    for attack in base_attacks:
        dynamic_attacks.extend(generator.generate(attack, n=2))

    all_attacks = base_attacks + dynamic_attacks

    results = await runner.run(all_attacks)

    final = [evaluator.evaluate(r) for r in results]

    with open("results/output.json", "w") as f:
        json.dump(final, f, indent=2)

    print("Done. Check results/output.json")


asyncio.run(main())