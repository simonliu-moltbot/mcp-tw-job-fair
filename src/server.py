import asyncio
import sys
import os

# Import Hack
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from mcp.server.models import InitializationOptions
from mcp.server import NotificationOptions, Server
from mcp.server.stdio import stdio_server
import mcp.types as types

from logic import fetch_job_fairs, filter_fairs_by_region

server = Server("mcp-tw-job-fair")

@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="get_all_job_fairs",
            description="獲取全台灣最近的徵才活動清單",
            inputSchema={
                "type": "object",
                "properties": {},
            },
        ),
        types.Tool(
            name="search_job_fairs_by_region",
            description="依據縣市或地點關鍵字搜尋徵才活動",
            inputSchema={
                "type": "object",
                "properties": {
                    "region": {"type": "string", "description": "縣市名稱，例如：台北"},
                },
                "required": ["region"],
            },
        ),
    ]

@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict | None
) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    if name == "get_all_job_fairs":
        fairs = fetch_job_fairs()
        return [types.TextContent(type="text", text=str(fairs))]
    elif name == "search_job_fairs_by_region":
        region = arguments.get("region")
        fairs = filter_fairs_by_region(region)
        return [types.TextContent(type="text", text=str(fairs))]
    else:
        raise ValueError(f"Unknown tool: {name}")

async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="mcp-tw-job-fair",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )

if __name__ == "__main__":
    asyncio.run(main())
