# Entrypoint: com.fsck.k9.activity.UpgradeDatabases$UpgradeDatabaseBroadcastReceiver.onReceive(Landroid/content/Context;Landroid/content/Intent;)V
# Target: invokevirtual < Application, Lcom/fsck/k9/activity/UpgradeDatabases, startActivity(Landroid/content/Intent;)V >@12

IAAv0 = Int('IAAv0')    # <Input2>.getAction()
IAAv1 = Int('IAAv1')    # equals9<return>
IAAv2 = Int('IAAv2')    # equals13<return>

s.add(And(And(And((7000 != IAAv0), (IAAv1 == 0)), And((7001 == IAAv0), (IAAv2 == 1))), (IAAv2 != 0)))

