"""
Taiwan Job Fair MCP Server using FastMCP.
Supports both STDIO and Streamable HTTP transport modes.
"""
import sys
import os
import argparse
import asyncio

# Add current directory to path so we can import 'logic'
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastmcp import FastMCP
import logic

# Initialize FastMCP
mcp = FastMCP("mcp-tw-job-fair")

@mcp.tool()
async def get_all_job_fairs() -> str:
    """
    獲取全台灣最近的徵才活動清單。
    """
    fairs = logic.fetch_job_fairs()
    return str(fairs)

@mcp.tool()
async def search_job_fairs_by_region(region: str) -> str:
    """
    依據縣市或地點關鍵字搜尋徵才活動。
    Args:
        region: 縣市名稱，例如：台北。
    """
    fairs = logic.filter_fairs_by_region(region)
    return str(fairs)

def main():
    parser = argparse.ArgumentParser(description="Taiwan Job Fair MCP Server")
    parser.add_argument("--mode", choices=["stdio", "http"], default="stdio", help="Transport mode")
    parser.add_argument("--port", type=int, default=8000, help="HTTP port (only for http mode)")
    args = parser.parse_args()

    if args.mode == "stdio":
        mcp.run()
    else:
        print(f"Starting FastMCP in streamable-http mode on port {args.port}...", file=sys.stderr)
        mcp.run(
            transport="streamable-http",
            host="0.0.0.0",
            port=args.port,
            path="/mcp"
        )

if __name__ == "__main__":
    main()
