# Entrypoint: com.google.android.gm.AutoSendActivity.onCreate(Landroid/os/Bundle;)V
# Target: invokevirtual < Application, Landroid/widget/Button, setOnClickListener(Landroid/view/View$OnClickListener;)V >@60

IAAv0 = Real('IAAv0')    # <ChainedInput1>
IAAv1 = Int('IAAv1')    # Pointer<504223769>

s.add(And(Or((IAAv0 == 0), Not((IAAv0 == 0))), Or(Not((IAAv1 == 0)), Not((7000 == 0)))))

