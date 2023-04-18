import subprocess
from pathlib import Path
from random import randint
from typing import Any, Iterable, List, AnyStr

user_agents = Path(__file__).parent.parent.joinpath("useragents")


async def async_for(items: Iterable[Any]) -> Any:
    """Iterate over a iterable asynchronously

    Args:
        items (Iterable[Any]): items to iterate over

    Returns:
        Any: yield items
    """
    for item in items:
        yield item


def get_random_user_agents() -> str:
    """Get random user agents line from useragents.txt"""
    all_user_agents = list()

    with open(user_agents, "r") as file:
        all_user_agents = file.read().splitlines()

    random_index = randint(0, len(all_user_agents) - 1)
    return all_user_agents[random_index]


def run_lsof_command() -> List[AnyStr]:
    """Run lsof command and return output"""
    command = "lsof -iTCP -sTCP:LISTEN | grep Code"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    ports = []
    if process.returncode == 0:
        for line in output.decode().split('\n'):
            if line.strip():
                port = line.split()[8].split(':')[1]
                ports.append(port)
    return [port for port in ports if port.isdigit()]
