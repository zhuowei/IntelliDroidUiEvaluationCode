# Entrypoint: com.google.android.gms.plus.PlusOneButton$DefaultOnPlusOneClickListener.onClick(Landroid/view/View;)V
# Target: invokevirtual < Application, Landroid/app/Activity, startActivityForResult(Landroid/content/Intent;I)V >@42

IAAv1 = Real('IAAv1')    # Pointer<436239836>.a().getTag()
IAAv0 = Int('IAAv0')    # Pointer<-186604103>

s.add(And((IAAv0 == 0), (IAAv1 != 0)))

