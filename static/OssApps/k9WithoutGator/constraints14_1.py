# Entrypoint: com.fsck.k9.activity.MessageList.onResume()V
# Target: invokevirtual < Application, Landroid/content/Context, startActivity(Landroid/content/Intent;)V >@40

IAAv1 = Int('IAAv1')    # Pointer<1278203485>.isAvailable()
IAAv0 = Int('IAAv0')    # Pointer<1278203485>

s.add(And((IAAv0 != 0), (IAAv1 == 0)))

