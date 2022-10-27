import asyncio
import time
from asyncua import Client

node_names = [
    'Timestamp','FIT101.Pv', 'LIT101.Pv', 'MV101.Status', 'P101.Status', 'P102.Status', 'P1_STATE', 'AIT201.Pv', 'AIT202.Pv', 'AIT203.Pv', 'FIT201.Pv', 'LS201.Alarm', 'LS202.Alarm', 'LSL203.Alarm', 'LSLL203.Alarm', 'MV201.Status', 'P201.Status', 'P202.Status', 'P203.Status', 'P204.Status', 'P205.Status', 'P206.Status', 'P207.Status', 'P208.Status', 'P2_STATE', 'AIT301.Pv', 'AIT302.Pv', 'AIT303.Pv', 'DPIT301.Pv', 'DPSH301.Alarm', 'FIT301.Pv', 'LIT301.Pv', 'MV301.Status', 'MV302.Status', 'MV303.Status', 'MV304.Status', 'P301.Status', 'P302.Status', 'PSH301.Alarm', 'P3_STATE', 'AIT401.Pv', 'AIT402.Pv', 'FIT401.Pv', 'LIT401.Pv', 'LS401.Alarm', 'P401.Status', 'P402.Status', 'P403.Status', 'P404.Status', 'UV401.Status', 'P4_STATE', 'AIT501.Pv', 'AIT502.Pv', 'AIT503.Pv', 'AIT504.Pv', 'FIT501.Pv', 'FIT502.Pv', 'FIT503.Pv', 'FIT504.Pv', 'MV501.Status', 'MV502.Status', 'MV503.Status', 'MV504.Status', 'P501.Status', 'P502.Status', 'PIT501.Pv', 'PIT502.Pv', 'PIT503.Pv', 'PSH501.Alarm', 'PSL501.Alarm', 'P5_STATE', 'FIT601.Pv', 'FIT602.Pv', 'LIT601.Pv', 'LIT602.Pv', 'LSH601.Alarm', 'LSH602.Alarm', 'LSH603.Alarm', 'LSL601.Alarm', 'LSL602.Alarm', 'LSL603.Alarm', 'P601.Status', 'P602.Status', 'P603.Status', 'P6_STATE']

async def get_nodes(client, idx, tag, nodes):
    nodes[tag] = await client.nodes.root.get_child(["0:Objects", f"{idx}:HMIObject", f"{idx}:"+tag])

async def main():
    url = "opc.tcp://192.168.1.200:4840/swat-historian/server/"
    async with Client(url=url) as client:
        idx = await client.get_namespace_index(uri="http://swat-historian.testbed.itrust")
        nodes= {}
        tasks = [get_nodes(client, idx, tag, nodes) for tag in node_names]
        await asyncio.gather(*tasks)
        await client.register_nodes(list(nodes.values()))
        starttime = time.time()
        while True:
            val = await client.read_values(list(nodes.values()))
            data = dict(zip(node_names, val))
            print(data["Timestamp"])
            print(data["LIT101.Pv"], data["LIT301.Pv"], data["LIT401.Pv"], data["LIT601.Pv"], data["LIT602.Pv"])
            await asyncio.sleep(1 - ((time.time() - starttime) % 1))


if __name__ == '__main__':
    asyncio.run(main())
