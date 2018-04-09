# Entrypoint: com.sec.spp.push.notisvc.card.CardActionLauncher.onReceive(Landroid/content/Context;Landroid/content/Intent;)V
# Target: invokevirtual < Application, Landroid/content/Context, startActivity(Landroid/content/Intent;)V >@152

IAAv4 = Int('IAAv4')    # equals33<return>
IAAv2 = Int('IAAv2')    # <Input2>.getAction()
IAAv5 = Int('IAAv5')    # equals44<return>
IAAv1 = Real('IAAv1')    # <Input2>
IAAv0 = Real('IAAv0')    # <Input1>
IAAv6 = Int('IAAv6')    # <Input2>.getStringExtra().isEmpty()
IAAv3 = Int('IAAv3')    # <Input2>.getStringExtra()

s.add(And(And(And(And(And(And(And(And((IAAv0 != 0), (IAAv1 != 0)), (IAAv2 != 0)), (IAAv3 != 0)), And((IAAv2 == 7000), (IAAv4 == 1))), (IAAv4 != 0)), And(And(And(And((IAAv0 != 0), (IAAv1 != 0)), (IAAv3 != 0)), And((IAAv3 == 7001), (IAAv5 == 1))), (IAAv5 != 0))), And((IAAv0 != 0), (IAAv6 == 0))), And((IAAv0 != 0), (IAAv6 == 0))))

