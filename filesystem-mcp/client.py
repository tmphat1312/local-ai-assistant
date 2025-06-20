from fastmcp import Client


async def main():
    async with Client("./filesystem-mcp/server.py") as client:
        result = await client.call_tool("add", {"a": 5, "b": 3})
        print(f"Result: {result[0].text}")


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
