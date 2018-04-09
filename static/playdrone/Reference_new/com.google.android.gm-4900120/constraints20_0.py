# Entrypoint: com.google.android.gm.ui.b.onClick(Landroid/view/View;)V
# Target: invokevirtual < Application, Landroid/content/Context, startActivity(Landroid/content/Intent;)V >@89

IAAv1 = Int('IAAv1')    # Pointer<-1022459783>.getContext().m().isEmpty()
IAAv0 = Real('IAAv0')    # Pointer<-1022459783>.getContext().m()

s.add(And((IAAv0 != 0), (IAAv1 == 0)))

