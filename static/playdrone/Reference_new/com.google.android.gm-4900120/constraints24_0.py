# Entrypoint: com.google.android.gm.drive.h.onCreateDialog(Landroid/os/Bundle;)Landroid/app/Dialog;
# Target: invokevirtual < Application, Landroid/view/View, setOnClickListener(Landroid/view/View$OnClickListener;)V >@170

IAAv0 = Real('IAAv0')    # <ChainedInput1>
IAAv1 = Int('IAAv1')    # Pointer<2013367870>

s.add(Or(Or(And((IAAv0 == 0), (IAAv1 == 0)), And((IAAv0 == 0), Not((IAAv1 == 0)))), Not((IAAv0 == 0))))

