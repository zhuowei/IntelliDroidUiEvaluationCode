# Entrypoint: com.google.android.gms.plus.PlusOneButton$DefaultOnPlusOneClickListener.onClick(Landroid/view/View;)V
# Target: invokevirtual < Application, Landroid/app/Activity, startActivityForResult(Landroid/content/Intent;I)V >@42

IAAv0 = Int('IAAv0')    # Pointer<500999472>
IAAv1 = Real('IAAv1')    # Pointer<565945978>.a().getTag()

s.add(And((IAAv0 == 0), (IAAv1 != 0)))

