# Entrypoint: com.fsck.k9.activity.MessageCompose.onCreate(Landroid/os/Bundle;)V
# Target: invokevirtual < Application, Lcom/fsck/k9/activity/MessageCompose, startActivity(Landroid/content/Intent;)V >@358

IAAv1 = Int('IAAv1')    # Pointer<1857968671>
IAAv0 = Int('IAAv0')    # Pointer<785230177>

s.add(And(Or((IAAv0 == 0), (IAAv0 != 0)), (IAAv1 == 0)))

