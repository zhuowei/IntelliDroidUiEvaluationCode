# Entrypoint: com.mopub.mobileads.n.onTouch(Landroid/view/View;Landroid/view/MotionEvent;)Z
# Target: invokevirtual < Application, Landroid/content/Context, startActivity(Landroid/content/Intent;)V >@51

IAAv2 = Real('IAAv2')    # Pointer<1319726537>.a().b.h
IAAv1 = Real('IAAv1')    # Pointer<1319726537>.a().c
IAAv0 = Int('IAAv0')    # <ChainedInput2>.getAction()
IAAv3 = Real('IAAv3')    # Pointer<1319726537>.a().c.onUserClick().d

s.add(And(Or(And((IAAv0 == 1), (IAAv1 == 0)), And((IAAv0 == 1), (IAAv1 != 0))), (IAAv2 == IAAv3)))

