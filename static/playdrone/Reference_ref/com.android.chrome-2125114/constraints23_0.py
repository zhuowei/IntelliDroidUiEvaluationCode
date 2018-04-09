# Entrypoint: com.google.android.gms.internal.f.onClick(Landroid/content/DialogInterface;I)V
# Target: invokevirtual < Application, Landroid/app/Activity, startActivityForResult(Landroid/content/Intent;I)V >@82

IAAv0 = Int('IAAv0')    # Pointer<-187127136>
IAAv1 = Int('IAAv1')    # Pointer<-187120907>

s.add(And((IAAv0 == 0), (IAAv1 != 0)))

