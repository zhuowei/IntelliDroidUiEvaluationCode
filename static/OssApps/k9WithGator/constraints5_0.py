# Entrypoint: com.fsck.k9.activity.Accounts.onCreate(Landroid/os/Bundle;)V
# Target: invokevirtual < Application, Landroid/content/Context, startActivity(Landroid/content/Intent;)V >@12

IAAv2 = Int('IAAv2')    # Pointer<-503858156>.getAutoExpandFolderName()
IAAv3 = Int('IAAv3')    # equals16<return>
IAAv1 = Int('IAAv1')    # Pointer<-503858156>.isAvailable()
IAAv0 = Int('IAAv0')    # Pointer<-503858156>.isEnabled()

s.add(And(And(And((IAAv0 != 0), (IAAv1 != 0)), And((7000 == IAAv2), (IAAv3 == 1))), (IAAv3 != 0)))

