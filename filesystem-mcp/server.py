from fastmcp import FastMCP

mcp = FastMCP(name="MyAssistantServer")


@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers."""
    return a * b


@mcp.tool
def add(a: float, b: float) -> float:
    """Adds two numbers."""
    return a + b


# Static resource
@mcp.resource("config://version")
def get_version():
    return "2.0.1"


# Dynamic resource template
@mcp.resource("users://{user_id}/profile")
def get_profile(user_id: int):
    # Fetch profile for user_id...
    return {"name": f"User {user_id}", "status": "active"}


@mcp.prompt
def summarize_request(text: str) -> str:
    """Generate a prompt asking for a summary."""
    return f"Please summarize the following text:\n\n{text}"


if __name__ == "__main__":
    mcp.run()
    # Graceful shutdown using context7
