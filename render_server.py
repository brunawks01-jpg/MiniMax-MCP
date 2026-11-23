
import os
from minimax_mcp.server import mcp

if __name__ == "__main__":
    mcp.settings.host = "0.0.0.0"
    mcp.settings.port = int(os.environ.get("PORT", "10000"))
    mcp.settings.streamable_http_path = "/mcp"
    mcp.run(transport="streamable-http")
