
import os
from minimax_mcp.server import mcp

def main():
    port = int(os.environ.get("PORT", "10000"))
    mcp.run(
        transport="sse",
        host="0.0.0.0",
        port=port,
    )

if __name__ == "__main__":
    main()
