# Entrypoint: com.fsck.k9.activity.FolderList.onCreate(Landroid/os/Bundle;)V
# Target: invokevirtual < Application, Landroid/content/Context, startActivity(Landroid/content/Intent;)V >@15

IAAv1 = Int('IAAv1')    # Pointer<180240066>.getAutoExpandFolderName()
IAAv0 = Int('IAAv0')    # Pointer<180240066>
IAAv2 = Int('IAAv2')    # equals23<return>

s.add(And(And((IAAv0 != 0), (7000 != IAAv1)), (IAAv2 == 0)))

