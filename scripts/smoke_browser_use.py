"""Optional authorized local Chromium smoke test for the upstream baseline."""

from __future__ import annotations

import argparse
import asyncio
import os

from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider

from browserops_core.browser_use_adapter import create_agent


async def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="https://example.com")
    args = parser.parse_args()

    model_name = os.environ.get("BROWSEROPS_MODEL_NAME")
    base_url = os.environ.get("BROWSEROPS_MODEL_BASE_URL")
    api_key = os.environ.get("BROWSEROPS_MODEL_API_KEY")
    if not all((model_name, base_url, api_key)):
        raise SystemExit(
            "Set BROWSEROPS_MODEL_NAME, BROWSEROPS_MODEL_BASE_URL and "
            "BROWSEROPS_MODEL_API_KEY before running this paid smoke test."
        )
    assert model_name is not None
    assert base_url is not None
    assert api_key is not None

    provider = OpenAIProvider(base_url=base_url, api_key=api_key)
    llm = OpenAIChatModel(model_name, provider=provider)
    agent = create_agent(
        task=f"Open {args.url}, read the page title, and return the title only.",
        llm=llm,
    )
    try:
        result = await agent.run()
        print(result.final_result())
    finally:
        await agent.browser.stop()


if __name__ == "__main__":
    asyncio.run(main())
