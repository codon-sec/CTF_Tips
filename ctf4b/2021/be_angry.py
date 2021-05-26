import angr

image_base = 0x400000  # 多分default
p = angr.Project('./chall')

state = p.factory.entry_state()
simgr = p.factory.simulation_manager(state)
simgr.explore(find=image_base+0x00002532).run()
found = simgr.found[0]

print(found.posix.dumps(0))
